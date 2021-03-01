from bs4 import BeautifulSoup
import requests
from IPython import embed
import time


headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}

time.sleep(2)

BASE_URL = 'https://albertyumol.github.io/'

def extract_html_content(target_url):
    response = requests.get(target_url,headers)
    return response.text



def main():
    # html_content = extract_html_content(target_page)
    # print(html_content)


    # soup = BeautifulSoup(html_content,'html.parser')

    # elements = soup.find_all('h2')

    # for element in elements:
    #     print(element.get_text())

    for i in range(5):
        if i == 1:
            page = BASE_URL + "index.html"
        else:    
            page = BASE_URL + "page" + str(i) 
            
        html_content = extract_html_content(page)
        soup = BeautifulSoup(html_content,'html.parser')

        titles = soup.find_all('h2')

        for element in titles:
            print(element.get_text())

if __name__ == "__main__":
    main()