import imageio
from google_images_download import google_images_download
import sys, os
import ffmpeg


def main(keyword):
    response = google_images_download.googleimagesdownload()
    response.download({"keywords": keyword, "limit": 5, "size": "large", "prefix": "test-"})


def save(keyword):

    os.system(f"ffmpeg -i /Users/K1NG/Code/codename_yta/downloads/{keyword}/test-*.jpg video.mp4 -vcodec mpeg4")
    # ffmpeg - framerate 1 - pattern_type glob - i '*.jpg' - c: v libx264 - r 30 -pix_fmt yuv420p out.mp4

if __name__ == "__main__":
    keyword = sys.argv[1]
    main(keyword)
    save(keyword)