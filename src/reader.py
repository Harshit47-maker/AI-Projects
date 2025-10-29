import pypdf
import arxiv
import requests
from io import BytesIO
client = arxiv.Client()
def rpdf():
    text = ''
    print('Please note that currently we can work with text pdfs only.')
    print('Other forms of pdf support will be added soon')
    print('Thanks for using')
    a = input('Do you have pdf installed on your computer ........(y/n) : ')
    if a == 'y':
        b = input('Enter pdf full name or Path : ')
        r = pypdf.PdfReader(b)
        for page in r.pages :
            text = page.extract_text()
    else :
        c = input('Want to provide a url to fetch pdfs from ArXiv .......(y/n) : ')
        if c == 'y':
            url = input('Please enter ArXiv url : ')
            res = requests.get(url)
            if res.status_code != 200 :    
             raise Exception(f"Failed to fetch PDF : {res.status_code}")
            else: 
                stream = BytesIO(res.content)
                re = pypdf.PdfReader(stream)
                for page in re.pages:
                    text = page.extract_text()
        else :
            print('We are soory for not being able to fulfill your requests.')
            print('Other ways will be added soon.')
    if text != '' :
        return text
    else:
        print('No text to perform further operations. ')
        