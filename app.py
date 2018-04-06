import imageio
from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()
response.download({"keywords": "beijing pollution", "limit": 5, "size": "large"})