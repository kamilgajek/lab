from apscheduler.schedulers.background import BackgroundScheduler
from utils.ip_utils import fetch_allowed_ips

def update_allowed_ips(aws_ip_ranges_url, region, allowed_ip_networks):
    allowed_ip_networks.clear()
    allowed_ip_networks.extend(fetch_allowed_ips(aws_ip_ranges_url, region))

def start_ip_scheduler(aws_ip_ranges_url, region, allowed_ip_networks, schedule_interval_days):
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        func=lambda: update_allowed_ips(aws_ip_ranges_url, region, allowed_ip_networks),
        trigger="interval",
        days=schedule_interval_days
    )
    scheduler.start()
    update_allowed_ips(aws_ip_ranges_url, region, allowed_ip_networks)
