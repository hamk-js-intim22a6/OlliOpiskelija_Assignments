from html.parser import HTMLParser
import urllib.request
import urllib.error

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

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
            links = parser.links
            
            # Return the list of links
            return links
    except urllib.error.URLError as e:
        print(f"Error accessing URL: {e.reason}")
        return []
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []

# Example usage
url = 'https://yle.fi/uutiset/osasto/news'
links = get_links(url)
for link in links:
    print(link)
