# Cloudflare DDNS Updater

A simple Python script to automatically update your Cloudflare DNS record with your current public IP address.  
Designed to be run via `crontab` on Linux, so your domain always points to your latest IP.  

## Features
- Updates your Cloudflare DNS record automatically  
- Works with both IPv4 and IPv6  
- Lightweight and easy to configure  
- Perfect for home servers with dynamic IPs  

## Requirements
- Python 3.x  
- A Cloudflare account  
- Your domain added to Cloudflare  

## Configuration
Edit the script and set the following variables:  

```python
zone_identifier = "your_zone_id"
record_name = "sub.domain.com"
X_Auth_Email = "your_cloudflare_email"
X_Auth_Key = "your_cloudflare_api_key"

```

You can find your Zone ID and API Key in your Cloudflare dashboard.

Usage

Run the script manually:
```
python3 cloudflare_ddns.py
```

Or set up a cron job to run it automatically (example: every 5 minutes):
```
*/5 * * * * /usr/bin/python3 /path/to/cloudflare_ddns.py
```
Example Output
[INFO] Current IP: 203.0.113.25
[INFO] DNS record updated successfully!
