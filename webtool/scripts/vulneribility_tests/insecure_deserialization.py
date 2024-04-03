import subprocess

def run_objectmap(url):
    try:
        subprocess.run(['touch objectmap_output.txt'],check=True, shell=True)
        subprocess.run(['/home/monarch/objectmap/objectmap','-u',url,'--random-agent','>>', 'objectmap-output.txt'], check=True)
        
        print("Objectmap scan completed successfully")
    except subprocess.CalledProcessError as e:
        print("Error running Objectmap:", e)

if __name__ == "__main__":
    url = input("Enter the URL to scan: ")
    run_objectmap(url)