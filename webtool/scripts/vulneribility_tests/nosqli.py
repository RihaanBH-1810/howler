import subprocess

def run_brahma(url):
    try:
        subprocess.run(['Brahma', '-a','nosqli','-d',url], check=True)
        
        print("Brahma scan completed successfully")
    except subprocess.CalledProcessError as e:
        print("Error running Brahma:", e)

if __name__ == "__main__":
    url = input("Enter the URL to scan: ")
    run_brahma(url)