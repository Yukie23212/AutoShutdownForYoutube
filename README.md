# Shutdown PC after a youtube Video uploaded

This script allows you to schedule a shutdown after uploading a video to YouTube using the YouTube Data API v3.

## Prerequisites

- You need a YouTube API Key to use this script.
- Python installed on your system. [Download Python](https://www.python.org/downloads/)

## Step-by-Step Guide

### 1. Enable the YouTube Data API v3

1. Go to the [Google Cloud Console](https://console.cloud.google.com/). Use the same account that you will use for create project and upload a video
2. Create a new project or select an existing project. If it's your first project, it will show "My First Project" at the top left.
3. Navigate to `APIs & Services > Library`. Click on the navigation menu (three lines) on the left side to see "APIs & Services".
4. Search for "YouTube Data API v3" and enable it.

### 2. Create API Credentials

1. Navigate to `APIs & Services > Credentials`.
2. Click on `Create Credentials` and select `API key`.
3. Copy the generated API key and keep it secure.

### 3. Install the Google API Client Library

Use the Command Prompt to install the library:

```bash
pip install google-api-python-client
```

## How to Use

1. Download `ShutdownYT.py` and open it with Notepad.
2. Replace `'YOUR_API_KEY'` with your actual API key in the script.
3. Replace `'P6ZLlJNAmnz'` with your actual video ID. Example: For the URL `https://youtu.be/P6ZLlJNAmnz` or `https://www.youtube.com/watch?v=P6ZLlJNAmnz`, use the ID `P6ZLlJNAmnz`.
4. Save the script to a file.
5. Run the script just before starting your upload process. You can use it even if the video is already uploaded or halfway through (50%).

## Notes

- Set the video's visibility to "Public" or "Unlisted" since "Private" won't work as the script can't check it.
- You can change the shutdown timer at the bottom of the script:
- if it working it will be showing `Current upload status: uploaded. Checking again in 60 seconds...`

```python
os.system("shutdown /s /t 300")
```

Currently, it's set to 300 seconds (5 minutes).

- To cancel the shutdown, use:

```bash
shutdown /a
```
