import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        # Make a GET request to the website
        response = requests.get(url)
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all the links on the page (from <a> and <button> tags)
        links = [link.get('href') for link in soup.find_all('a')]
        links.extend([button.get('href') for button in soup.find_all('button')])
        
        # Find all the hidden input fields on the page
        hidden_inputs = soup.find_all('input', {'type': 'hidden'})
        hidden_links = [input_field.get('value') for input_field in hidden_inputs]
        
        # Combine all the links
        all_links = links + hidden_links
        
        return all_links
    
    except requests.exceptions.RequestException as e:
        print(f"Error scraping the website: {e}")
        return []   

# Example usage

def check_input_fields(url):
    response = requests.get(url)
    soup =BeautifulSoup(response.content, 'html.parser')
    input_fields = soup.find_all('input')
    input_details = {}
    
    for input_field in input_fields:
        input_type = input_field.get('type', 'text')
        input_name = input_field.get('name', '')
        input_value = input_field.get('value', '')
        
        input_details[input_name] = {
            'type': input_type,
            'value': input_value
        }
    
    return input_details


def main(url):


    all_links = scrape_website(url)
    l=[]
    # print("All Links:")
    for link in all_links:
        
        if link!=None and url+link not in l:
            link=url+link
            l.append(link)
    for i in l:
        for link in scrape_website(i):
            if link!=None and url+link not in l:
                link=url+link
                l.append(link)

    inp=[]
    for url in l:
        for i in dict(check_input_fields(url)).keys():
            if i!="":
                inp.append({"url":url,"input_name":i})
            # print(inp)
    print(l)
    print(inp)
    return l,inp
