import subprocess

def run_wapiti(url):
    try:
        # Run Wapiti scan with desired options
        # '-u' flag specifies the URL to scan
        # '-m' flag specifies the scan module
        # '-n' flag specifies not to save the HTML reports
        # '-o' flag specifies the output format: 'text' for plain text output
        # '-f' flag specifies the output file name
        subprocess.run(['wapiti', '-u', url, '-m', 'redirect,brute_login_form,cookieflags,csp,exec,file,htaccess,http_headers,https_redirect,log4shell,methods,nikto,shellshock,spring4shell,takeover,upload,xxe,xss', '-o', 'txt', '-f', 'txt'], check=True)
        
        print("Wapiti scan completed successfully. Output saved to wapiti_report.txt")
    except subprocess.CalledProcessError as e:
        print("Error running Wapiti:", e)

if __name__ == "__main__":
    url = input("Enter the URL to scan: ")
    run_wapiti(url)
