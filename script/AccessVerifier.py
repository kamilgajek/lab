import os
from flask import Flask, request, jsonify
import requests
import logging
import ipaddress
from utils.ip_utils import fetch_allowed_ips
from utils.ip_scheduler import start_ip_scheduler
from utils.logging_utils import configure_logging  # Import the function

# Load configuration from environment variables
aws_ip_ranges_url = os.getenv('AWS_IP_RANGES_URL')
region = os.getenv('REGION')
schedule_interval_days = int(os.getenv('SCHEDULE_INTERVAL_DAYS'))
log_directory = os.getenv('LOG_DIRECTORY', '/app/logs')  # Default to /app/logs

app = Flask(__name__)

# Configure logging
configure_logging(log_directory)

# Global variable to store allowed IP networks
allowed_ip_networks = []

# Start the IP update scheduler
start_ip_scheduler(aws_ip_ranges_url, region, allowed_ip_networks, schedule_interval_days)

@app.route('/verify', methods=['POST'])
@app.route('/verify', methods=['POST'])
def verify():
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    logging.debug(f"Received request from IP: {client_ip}")

    try:
        client_ip_obj = ipaddress.ip_address(client_ip)
        if any(client_ip_obj in network for network in allowed_ip_networks):
            logging.info(f"IP {client_ip} is allowed")
            return '', 200  # Return only the status code 200
        else:
            logging.warning(f"IP {client_ip} is unauthorized")
            return '', 401  # Return only the status code 401
    except ValueError:
        logging.error(f"Invalid IP address format: {client_ip}")
        return jsonify({"status": "error", "message": "Invalid IP address format"}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
