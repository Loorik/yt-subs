# Import youtube subscribers

Use this script to import your exported youtube subcribers. 

# Requirements
Install requirements i.e. using  `pip install -r requirements.txt`.
You need to setup a project in Google Cloud, activate Youtube Data API v3 for the project, set youtube.force-ssl scope, setup OAuth consent screen, create OAuth credentials and download the `client_secrets.json` file to this repository. 
Your subscriptions should be in csv format and it should at least contain the ChannelId. You can also use the ChannelTitle if available, but the script needs to be adopted then. You can download your subscriptions using [Google Takeout Manager](https://takeout.google.com/takeout/custom/youtube)

# Usage
If requirements are installed, `Subscribers.csv` and `client_secrets.json` are in place (same directory as `main.py`), execute `main.py`, follow instructions on your browser and enjoy. 
For each added subscriber, the script prints the ChannelId.
