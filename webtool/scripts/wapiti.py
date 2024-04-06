import subprocess
import json, random
list_of_urls = []

def get_data_from_file(url, filename):
    global list_of_urls
    with open(filename, 'r') as f:
        data = f.read()
        data = json.loads(data)
        dat = {"url": url, "data": data}
        f.close()
    subprocess.run(["rm", filename])

    print(dat)
    return dat
    

def run_wapiti(url):
    unique_id = random.random()
    subprocess.run(["pwd"])
    filename = f"./scripts/out/{unique_id}.json"
    subprocess.run(["touch", filename])
    subprocess.run(["pwd"])

    try:
        subprocess.run(['wapiti', '-u', url, '-m', 'ssrf,brute_login_form,cookieflags,csp,exec,file,htaccess,http_headers,https_redirect,methods,nikto,shellshock,takeover,upload,xxe,xss,csrf',"-o",filename, "-f", "json",  "--flush-session"], check=True)        
        dat = get_data_from_file(url, f"./scripts/out/{unique_id}.json")
        print("Wapiti scan completed successfully. Output saved to wapiti_report.txt")
        save_results(dat, unique_id)
    except subprocess.CalledProcessError as e:
        print("Error running Wapiti:", e)
def save_results(results, filename):
    with open(f"./scripts/out/{filename}.json", 'w') as f:
        f.write(json.dumps(results, indent=4))
if __name__ == "__main__":
    url = input("Enter the URL to scan: ")
    run_wapiti(url)
