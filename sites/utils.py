import requests
from bs4 import BeautifulSoup
import json, os, sys, numpy, math

class Utils():
    # Send the webhook!
    def webhookPost(embeds,site):
        try:
            array = numpy.array(embeds)
            embeds = numpy.array_split(array,math.ceil(len(embeds)/10))
        except ValueError:
            embeds = [embeds]# embeds <=10
        
        for embed_array in embeds:
            data = {
                "embeds": list(embed_array)
                }
            r = requests.post(os.getenv(site), data=json.dumps(data), headers={"Content-Type": "application/json"})

    # Simple get request with example headers, returns soup
    def request(url,site):
        error=""
        try:
            r = requests.get(url,headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0 okj/streaming-webhook","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"})
            if (r.status_code != 200):
                raise requests.exceptions.HTTPError
            return BeautifulSoup(r.content, 'html.parser')
        except requests.exceptions.HTTPError as e:
            requests.post(os.getenv(site), data=json.dumps({"content":f"Unexpected status_code grabbing HTML on `{url}`\n```{e.strerror}```"}), headers={"Content-Type": "application/json"})
        except requests.exceptions.ConnectionError as e:
            requests.post(os.getenv(site), data=json.dumps({"content":f"Error connecting to `{url}` (site down?)\n```{e.strerror}```"}), headers={"Content-Type": "application/json"})
        except Exception as e:
            print("Error sending webhooks")
        return None
    
    # Returns the data in db
    def getDB():
        with open('db.json', 'r') as f:
            data=f.read()
        return json.loads(data)

    # Writes the data to the db
    def setDB(j):
        data = json.dumps(j,indent=4)
        with open('db.json', 'w') as f:
            f.write(data)

    # Determines if media has been found before
    ## If it has been found, return True
    ## If it has NOT been found, add it to found media
    def find(media: str, id: str):
        
        db = Utils.getDB() # json object
        
        if id not in db: # Module not ran yet
            print(f"New: {media}")
            db[id] = [media]
            Utils.setDB(db)
            return False

        if media in db[id]:
            return True

        print(f"New: {media}")
        db[id].insert(0,media)

        if (len(db[id]) >= 90):
            db[id] = db[id][:90]

        Utils.setDB(db)
        return False