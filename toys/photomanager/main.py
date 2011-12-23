import gdata.photos.service
import gdata.media
import gdata.geo
import os

import photoman.PhotoMan
import settings.*

# Long live google (and its photo service.)

# TODO: Preprocess and find out what to upload. Update a summary in summary.log
# TODO: Recursive directories
# TODO: Must be able to interrupt

# TODO: Duplicate entries
# TODO: Import from other albums, FlickR, Facebook

# TODO: Configure tempuser and temppass environment variable before running.




def run():
  print "------>>>"
  tempList = os.listdir(base)
  gdc = initGooglePhotoService()
  photoman = new PhotoMan(gdc)

  dirs = [d for d in os.listdir(base) if os.path.isdir(base + '/' + d)]

  for dir in dirs:
    album = photoman.createAlbum(dir)
    if album != None:
      path = base + '/' + dir
      photoman.uploadPhotos(album, path)

  print "<<<------"

"""
  Method to intialize Google Photo service.
"""
def initGooglePhotoService():
  gdc = gdata.photos.service.PhotosService()
  gdc.email = os.environ['tempuser']
  gdc.password = os.environ['temppass']
  gdc.source = 'iuploader'
  gdc.ProgrammaticLogin()
  return gdc


if __name__ == "__main__":
  run()

#createAlbum('Duplicate Test', gdc)

