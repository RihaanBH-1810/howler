import json
import os
import markdown

def generate_md():
    log_dir = "./scripts/out/"
    report_md = "./scripts/out/report.md"

    name_file_dict = {
        "basic_scan_results.json": "Basic Scan Results",
        "csrf_results.json": "CSRF Scan Results",
        "nosql_targets.json": "NoSQL Injection possible Targets",
        "nosql_results.json": "NoSQL Injection Results",
        "ssrf_results.json": "SSRF Results",
        "xss_results.json": "XSS Results",
        "links.json": "All internal links available in the website",
        "fuzzer.json": "Fuzzer Results",
    }

    with open(report_md, 'w') as report_file:
        for filename in os.listdir(log_dir):
            if filename.endswith(".json") and filename not in ["fuzzer.json", "basic_scan_results.json"]:
                with open(os.path.join(log_dir, filename), 'r') as log_file:
                    file_content = log_file.read()
                    if file_content:
                        print(f"Processing {filename}")
                        try:
                            log_data = json.loads(file_content)
                            if log_data:  # Check if log_data is not empty
                                report_file.write(f"## {name_file_dict[filename]}\n")
                                for dict_index, dict_data in enumerate(log_data):
                                    report_file.write(f"### Record {dict_index+1}\n")
                                    for key, value in dict_data.items():
                                        report_file.write(f"* **{key}**: {value}\n")
                                    report_file.write("\n")
                        except json.JSONDecodeError:
                            print(f"Error: Invalid JSON data in {filename}")
def convert_md_to_html(filename):
    with open(filename, 'r') as f:
        tempMd= f.read()
    tempHtml = markdown.markdown(tempMd)
    with open('./scanner/templates/report.html', 'w') as f:
        f.write(tempHtml)
if __name__ == "__main__":
    generate_md()