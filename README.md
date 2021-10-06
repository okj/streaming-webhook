# kissmovies-webhook
 Simple script that scrapes new additions to kissmovies and sends them as a Discord webhook them as a webhook over Discord

## Setup

Create and add your Discord webhook url to a **.env** file

    WEBHOOK_URL=https://discord.com/api/webhooks/123/ABC

Install the requirements with pip

`python3 -m pip install -r requirements.txt`

Run the script

`python3 main.py [Hours between checks]`

## Result

![preview](https://i.imgur.com/i6BF5Mt.png)