from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import json, os, sys, time

# Send the webhook!
def webhookPost(message):
    data = {'content': message}
    requests.post(os.getenv("WEBHOOK_URL"), data=json.dumps(data), headers={'Content-Type': 'application/json'})

# Simple get request with example headers
def getHtml(url):
    try:
        return requests.get(url,headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"})
    except requests.exceptions.ConnectionError as ce:
        webhookPost(f"Error connecting to `{url}` (site down?)\n```{ce.strerror}```")
    except Exception as e:
        webhookPost(f"An unknown error has occurred\n```{str(e)}```")
    sys.exit("Error grabbing HTML")

# Determines if media has been found before
## If it has been found, return True
## If it has NOT been found, add it to found media
def find(media: str):
    with open("found.txt", "r") as f:
        found = f.read().split("\n")
    
    print(media, found)
    if (media in found):
        return True
    print(f"New: {media}")

    count = 0 
    found.insert(0,media)
    with open("found.txt", "w") as f:
        for m in found:
            if (count == 90): break     # Only save 90 at a time; KM only has 45 on their home page so 45*2 in the event that all 45 media have never been found
            f.write(m+"\n")
            count+=1
    return False

# Scrapes KissMovies "Latest update" carousel
def scrape():
    new_media = []

    response = getHtml("https://www.kissmovies.io/")
    if (response.status_code != 200):
        webhookPost(f"Error grabbing HTML!\nStatus code:```{response.status_code}```\n```{response.text}```") 
        return
    
    soup = BeautifulSoup(response.content, 'html.parser')
    carousel = soup.find("ul",attrs={"class":"scroll_popular"})
    found_media = carousel.find_all("a")

    for media in found_media:
        if not find(media["title"]): new_media.append(media["title"])
    
    webhookPost("\n".join(new_media))

if __name__ == "__main__":
    load_dotenv()

    interval = 18000      # Run every 5 hours by default

    if len(sys.argv) > 1: # Get user provided interval (hours)
        interval = int(sys.argv[1])*3600
    
    while True:
        scrape()
        print(f"Sleeping for {interval/3600} hours...")
        time.sleep(interval)