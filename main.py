from dotenv import load_dotenv
import sys, time, os
import sites

if __name__ == "__main__":
    load_dotenv()

    ### Checks
    if (os.getenv("WEBHOOK_URL") is None): exit("No webhook url defined!")
    if not os.path.exists("db.json"): 
        with open('db.json', 'w') as f:
            f.write("{}")
    ###

    interval = 18000      # Run every 5 hours by default
    if len(sys.argv) > 1: # Get user provided interval (hours)
        interval = int(sys.argv[1])*3600
    
    while True:
        # Run every module in modules/
        for site_name, module in sites.modules.items():
            site = module()
            print(f"Running module {site_name}...")
            site.scrape(site_name)

        print(f"Sleeping for {interval/3600} hours...")
        time.sleep(interval)