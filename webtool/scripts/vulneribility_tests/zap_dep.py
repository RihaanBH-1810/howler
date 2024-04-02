import time
from zapv2 import ZAPv2

# Function to start ZAP proxy and spider the target URL
def start_zap_proxy_and_spider(target_url):
    try:
        # Initialize ZAP API with API key
        zap = ZAPv2(apikey='nq9u20q7t1roa1jin42pjrb35j') # Replace 'your_api_key_here' with your actual API key

        # Start ZAP proxy
        zap.core.new_session()
        zap.core.set_mode("standard")
        print("ZAP Proxy started.")

        print("Spidering the target URL...")
        zap.spider.scan(target_url) # Corrected indentation
        while True:
            status = zap.spider.status()
            if status.isdigit():
                status = int(status)
                if status < 100:
                    print("Spider progress: {}%".format(status))
                    time.sleep(5)
                else:
                    print("Spidering completed.")
                    break
            else:
                print("Unexpected status: {}".format(status))
                break
    except Exception as e:
        print("Error starting ZAP proxy and spider:", e)

# Function to perform active scan for RCE vulnerabilities, clickjacking, and invalid redirects and forwards
def perform_active_scan(target_url):
    try:
        # Initialize ZAP API with API key
        zap = ZAPv2(apikey='nq9u20q7t1roa1jin42pjrb35j') # Replace 'your_api_key_here' with your actual API key

        # Perform active scan
        print("Performing active scan...")
        scan_id = zap.ascan.scan(target_url)
        while (int(zap.ascan.status(scan_id)) < 100):
            print("Active scan progress: {}%".format(zap.ascan.status(scan_id)))
            time.sleep(5)
        print("Active scan completed.")

        # Generate alerts for RCE vulnerabilities, clickjacking, and invalid redirects and forwards
        rce_alerts = zap.core.alerts(baseurl=target_url, alerttype='rce')
        clickjacking_alerts = zap.core.alerts(baseurl=target_url, alerttype='clickjacking')
        redirects_forwards_alerts = zap.core.alerts(baseurl=target_url, alerttype='redirects_forwards')

        # Print alerts
        print("RCE Vulnerabilities:")
        for alert in rce_alerts:
            print(alert)
        print("\nClickjacking Vulnerabilities:")
        for alert in clickjacking_alerts:
            print(alert)
        print("\nInvalid Redirects and Forwards:")
        for alert in redirects_forwards_alerts:
            print(alert)
    except Exception as e:
        print("Error performing active scan:", e)


def main():
    target_url = input("Enter the URL to scan: ")

    start_zap_proxy_and_spider(target_url)
    perform_active_scan(target_url)

if __name__ == "__main__":
    main()
