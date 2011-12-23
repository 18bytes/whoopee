import gdata.photos.service
import gdata.media
import gdata.geo
import os

import photoman.PhotoMan
import settings.*

# Long live google (and its photo service.)
# I am photoman, My god is Sundar (The creator) and my purpose of existence is to help him maintain his digital photos.

# TODO: Preprocess and find out what to upload. Update a summary in summary.log
# TODO: Recursive directories
# TODO: Must be able to interrupt

# TODO: Duplicate entries
# TODO: Import from other albums, FlickR, Facebook

# TODO: Configure tempuser and temppass environment variable before running.




def run():
  print "==========================================="

  # Precondition check.
  if (base == None):
    print "Hey, I cannot run if you don't set the base directory in settings.py. \nGo and set it first before running me!!"

  tempList = os.listdir(base)

  photoman = new PhotoMan()
  dirs = [d for d in os.listdir(base) if os.path.isdir(base + '/' + d)]

  for dir in dirs:
    album = photoman.createAlbum(dir)
    if album != None:
      path = base + '/' + dir
      photoman.uploadPhotos(album, path)
  print "==========================================="




if __name__ == "__main__":
  run() # Let photo man be run.


