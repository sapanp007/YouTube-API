"""
git hub page- googleapis/google-api-python-client
"""

from googleapiclient.discovery import build
api_key = "AIzaSyCPvVBf9lMKGrFA3OIvmLwAd8nJhnJpPmI"

youtube = build('youtube', 'v3', developerKey=api_key)
request = youtube.channels().list(
        part=["id", "statistics"],
        forUsername="jabykoay"
    )
response = request.execute()
print(response)

"""
use of context manager gives http error during closing service object connection
"""
