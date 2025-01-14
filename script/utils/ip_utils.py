import requests
import ipaddress
import logging

def fetch_allowed_ips(aws_ip_ranges_url, region):
    try:
        response = requests.get(aws_ip_ranges_url)
        response.raise_for_status()
        data = response.json()
        allowed_ip_networks = [
            ipaddress.ip_network(prefix['ip_prefix'])
            for prefix in data['prefixes'] if prefix['region'] == region
        ]
        logging.debug(f"Updated allowed IP networks: {allowed_ip_networks}")
        return allowed_ip_networks
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching IP ranges: {e}")
        return []
