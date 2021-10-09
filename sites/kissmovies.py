import re
from sites.utils import Utils

class Scraper():

    # Scrapes KissMovies "Latest update" carousel
    def scrape(self, site_name: str):
        new_media = []
        url = "https://www.kissmovies.io"

        soup = Utils.request(url)

        ### Scraping code
        carousel = soup.find("ul",attrs={"class":"scroll_popular"})
        found_media = carousel.find_all("a")
        ###

        for a in found_media:
            title = re.sub(' +', ' ',a.find("div",attrs={"class":"name"}).text).strip()
            if not Utils.find(title, site_name): 
                new_media.append({
                    "title": title,
                    "color": 15539236,
                    "image": {
                        "url": "https:"+a.find("div",attrs={"class":"thumb_anime"})["style"].split("'")[1]
                    },
                    "url": url+a["href"]
                    })
        
        Utils.webhookPost(new_media,site_name) # A list of embeds