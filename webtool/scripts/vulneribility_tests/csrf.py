import subprocess

def run_xsrfprobe(url, options):
    try:
        command = ['xsrfprobe', '-u', url] + options.split()
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("Error running XSRFProbe:", e)
        return None

def main():
    url = input("Enter the URL to test for CSRF vulnerabilities: ")
    options = input("Enter additional options for XSRFProbe (if any): ")
    print("Running XSRFProbe on", url)
    output = run_xsrfprobe(url, options)
    if output:
        print("XSRFProbe output:")
        print(output)

if __name__ == "__main__":
    main()
