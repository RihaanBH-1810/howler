import markdown

def convert_md_to_html(filename):
    with open(filename, 'r') as f:
        tempMd= f.read()
    tempHtml = markdown.markdown(tempMd)
    with open('./scanner/templates/report.html', 'w') as f:
        f.write(tempHtml)


