
import requests
import socket
import ssl
import whois
import dns.resolver
from urllib.parse import urlparse
import os

# Function to check website HTTP status
def check_http_status(url):
    try:
        response = requests.get(url)
        print(f"HTTP Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error with HTTP request: {e}")

# Function to get the website's SSL certificate info
def check_ssl_certificate(url):
    hostname = urlparse(url).hostname
    context = ssl.create_default_context()
    try:
        with context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname) as s:
            s.connect((hostname, 443))
            ssl_info = s.getpeercert()
            print("SSL Certificate Info: ")
            for item in ssl_info:
                print(f"{item}: {ssl_info[item]}")
    except Exception as e:
        print(f"Error fetching SSL certificate: {e}")

# Function to get DNS records of the website
def check_dns_records(url):
    domain = urlparse(url).hostname
    try:
        print(f"DNS Records for {domain}:")
        result = dns.resolver.resolve(domain, 'A')
        for ipval in result:
            print(f"IP Address: {ipval.to_text()}")
    except dns.resolver.NoAnswer:
        print(f"No DNS record found for {domain}")
    except Exception as e:
        print(f"Error fetching DNS records: {e}")

# Function to get whois information of the domain
def check_whois_info(url):
    domain = urlparse(url).hostname
    try:
        whois_info = whois.whois(domain)
        print(f"Whois Information for {domain}:")
        for key, value in whois_info.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"Error fetching Whois information: {e}")

# Function to check if website is reachable via ping
def check_ping(url):
    hostname = urlparse(url).hostname
    response = os.system(f"ping -c 4 {hostname}")
    if response == 0:
        print(f"{hostname} is reachable")
    else:
        print(f"{hostname} is not reachable")

# Main function
def main():
    url = input("Enter the URL of the website to check (e.g., https://example.com): ")

    # Check HTTP status code
    check_http_status(url)

    # Check SSL certificate
    check_ssl_certificate(url)

    # Check DNS records
    check_dns_records(url)

    # Check Whois information
    check_whois_info(url)

    # Check Ping status
    check_ping(url)

if __name__ == "__main__":
    main()
