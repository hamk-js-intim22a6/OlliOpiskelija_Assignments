from html.parser import HTMLParser
import urllib.request
import urllib.error

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    # <a href="osoite">...</a>
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    self.links.append(attr[1])

def get_links(url):
    try:
        # Open the URL and read its contents
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            
            # Parse the HTML and extract the links
            parser = LinkParser()
            parser.feed(html)            
            # Return the list of links
            return parser.links
    except urllib.error.URLError as e:
        print(f"Error accessing URL: {e.reason}")
        return []
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []

# Example usage
#url = 'https://yle.fi/uutiset/osasto/news'
url = "https://www.iltalehti.fi/urheilu"
links = get_links(url)
for link in links:
    if link.startswith('http'):
        print(link)
    else:
        print(f"https://www.iltalehti.fi/{link}")
        #print(f"https://yle.fi{link}")

