import os
import subprocess
command=f"cd /home/monarch/SSRFmap"
# Step 1: Prompt the user for a URL
url = input("Enter the URL you want to test: ")

# Step 2: Create a data/request.txt file with a basic HTTP GET request for the provided URL
request_content = f"""GET / HTTP/1.1
Host: {url}
"""

# Ensure the data directory exists
os.makedirs("data", exist_ok=True)

# Write the request content to data/request.txt
with open("data/request.txt", "w") as file:
    file.write(request_content)

# Step 3: Run ssrfmap with the generated request file
# Note: Adjust the ssrfmap command according to your needs, e.g., specifying modules, verbosity, etc.
command = f"python3 /home/monarch/SSRFmap/ssrfmap.py -r data/request.txt -p url -v"

# Step 4: Capture the output of ssrfmap and store it in a text file
output_file = "ssrfmap_output.txt"
with open(output_file, "w") as file:
    subprocess.run(command, shell=True, stdout=file, stderr=file)

print(f"Output has been saved to {output_file}")
