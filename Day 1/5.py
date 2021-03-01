from bs4 import BeautifulSoup
from IPython import embed

def generate_html():
    return """
        <html>
            <head></head>
            <body>
                <a href="/a.html">A</a>
                <a href="/b.html">B</a>
                <a href="/c.html">C</a>
                <a href="/d.html">D</a>
            </body>
        </html>
    """

def main():
    html_doc = generate_html()
    soup = BeautifulSoup(html_doc,'html.parser')

    div_elements = soup.find_all('a')

    for div_element in div_elements:
        print(div_element.attrs['href'])

if __name__ == "__main__":
    main()