import os
import time
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Replace with your API key and video ID
API_KEY = 'YOUR_API_KEY'
VIDEO_ID = 'P6ZLlJNAmnz'

def get_video_status(youtube, video_id):
    try:
        request = youtube.videos().list(part='status', id=video_id)
        response = request.execute()
        
        if response['items']:
            status = response['items'][0]['status']['uploadStatus']
            return status
        else:
            print(f"No status found for video ID: {video_id}")
            return None
    except HttpError as e:
        print(f"An HTTP error occurred: {e}")
        return None

def monitor_upload(api_key, video_id):
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    print(f"Monitoring video upload for: https://youtu.be/{video_id}")

    while True:
        status = get_video_status(youtube, video_id)
        if status == 'processed':
            print(f"Upload complete for: https://youtu.be/{video_id}")
            shutdown_computer()
            break
        elif status is None:
            print("Failed to retrieve video status. Retrying in 60 seconds...")
        else:
            print(f"Current upload status: {status}. Checking again in 60 seconds...")

        # Wait for 60 seconds before checking again
        time.sleep(60)

def shutdown_computer():
    print("Shutting down the computer...")
    os.system("shutdown /s /t 300")

if __name__ == "__main__":
    monitor_upload(API_KEY, VIDEO_ID)
