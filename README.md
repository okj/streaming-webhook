# streaming-webhook
 Simple script that scrapes new additions to different streaming sites and sends them as a Discord webhook

## Setup

Create and add your Discord webhook url to a **.env** file

    WEBHOOK_URL=https://discord.com/api/webhooks/123/ABC

Install the requirements with pip

`python3 -m pip install -r requirements.txt`

Remove unwanted modules in `modules/`

Run the script

`python3 main.py [Hours between checks]`

## Result

![preview](https://i.imgur.com/i6BF5Mt.png)


## Contributing

Check out the `templates/` directory for an example of how to create a module for a site of your own