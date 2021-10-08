from sites.utils import Utils

class Scraper(): # Do not change
    def scrape(self, site_name: str): # Do not change

        list_of_embeds = []
        url = "YOUR URL HERE"

        soup = Utils.request(url) # Returns a BeautifulSoup object

        # Scraping code goes here
        ## Read about BeautifulSoup: https://beautiful-soup-4.readthedocs.io/en/latest/
        ## Learn about Discord webhooks and embeds: https://discohook.org/

        # Example for creating embed objects
        for element in elements:
            if not Utils.find(title, site_name): # Need to make sure we haven't seen the media already
                list_of_embeds.append(
                    { # Example embed object
                    "title": title,
                    "color": 15539236, # color in int form
                    "image": {
                        "url": "IMAGE URL"
                        },
                    "url": "URL TO MEDIA"
                    })

        Utils.webhookPost(list_of_embeds)