import subprocess

def run_objectmap(url):
    try:
        subprocess.run(['/home/monarch/objectmap/objectmap','-u',url,'--random-agent'], check=True)
        
        print("Objectmap scan completed successfully")
    except subprocess.CalledProcessError as e:
        print("Error running Objectmap:", e)

if __name__ == "__main__":
    url = input("Enter the URL to scan: ")
    run_objectmap(url)