import csv
import google_auth_oauthlib.flow
import googleapiclient.discovery
from googleapiclient.errors import HttpError

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
client_secrets_file = "client_secret.json"

flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
credentials = flow.run_local_server(port=8080)

youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)


if __name__ == '__main__':
    with open('Subscribers.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            channel_id = row['Kanal-ID']
            try:
                youtube.subscriptions().insert(
                    part='snippet',
                    body={'snippet': {'resourceId': {'channelId': channel_id}}}
                ).execute()
                print(channel_id)
            except HttpError as e:
                print("Error subscribing to channel:", channel_id)
                print("Error details:", e.content)
