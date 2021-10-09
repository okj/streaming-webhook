# streaming-webhook
 Simple script that scrapes new additions to different streaming sites and sends them as a Discord webhook

## Setup

Create and add your Discord webhook urls to a `.env` file. See an example in [templates](https://github.com/okj/streaming-webhook/tree/main/templates)

    modulename=https://discord.com/api/webhooks/123/ABC
    modulename=https://discord.com/api/webhooks/321/CAB
    ...

Install the requirements with pip

`python3 -m pip install -r requirements.txt`

Remove unwanted modules in `modules/`

Run the script

`python3 main.py [Hours between checks]`

## Result

![preview](https://raw.githubusercontent.com/okj/streaming-webhook/main/images/preview.PNG)


## Contributing

Check out the [templates](https://github.com/okj/streaming-webhook/tree/main/templates) directory for an example of how to create a module for a site of your own.

### Disclaimer
*This project is in no way affiliated with any of the supported streaming websites. Use this script at your own risk.*