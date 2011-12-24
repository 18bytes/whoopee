# Long live google (and its photo service.)
# I am photoman, my purpose of existence is to help him maintain digital photos.

import gdata.photos.service
import gdata.media
import gdata.geo
import os
import urllib
import sys

import settings


## Priority Zero items
# TODO: Recursive directories
# TODO: Must be able to interrupt
# TODO: Import from other albums = Facebook, Google+, Flickr
# TODO: Meta data in each album
# TODO: Duplicate entries
# TODO: Configure tempuser and temppass environment variable before running.

## Nice to have
# TODO: Preprocess and find out what to upload. Update a summary in summary.log
# TODO: Once uploaded successfully, create a compressed archive and store it in another location/upload to webservice (Yahoo mail as attachment where unlimited storage?)







# TODO License

class PhotoMan:

  def __init__(self):
    self.gdc = self.initGooglePhotoService()
        
  """
    Method to intialize Google Photo service.
  """ 
  def initGooglePhotoService(self):
    gdc = gdata.photos.service.PhotosService()
    gdc.email = os.environ['tempuser']
    gdc.password = os.environ['temppass']
    gdc.source = 'photoman'
    gdc.ProgrammaticLogin()
    return gdc

  #  -------------------------------------------------------------------------
  #  Local helper methods for PHOTOS    
  #  -------------------------------------------------------------------------
  def uploadPhotos(self, album, path):
    existingPhotos = []
    errFiles = [] # Files which were not uploaded.
    successFiles = [] # Files which were successfully uploaded.
    duplicateFiles = [] # Files already in the server.

    # Precondition check
    if (self.gdc == None): return
    if album == None or path == None: return

    album_url = '/data/feed/api/user/%s/albumid/%s' % (os.environ['tempuser'], album.gphoto_id.text)
    # get all photo name from album and store it in a map/list
    # If already present then dont upload, else upload
    existingPhotos = self.getExistingPhotos(album.gphoto_id.text)
    
    pics = os.listdir(path)
    
    # Try to upload each file.
    for pic in pics:
      if os.path.isdir(pic) == True:
        self.uploadPhotos(self, album, settings.base + '/' + pic)
      else:
        # FIXME Add recurisve directory support, subdirectories can have duplicate names.
        if pic in existingPhotos:
          duplicateFiles.append(pic)
        else:
          filename = path + '/' + pic
          try:
            photo = self.gdc.InsertPhotoSimple(album_url, pic , '', filename, content_type='image/jpeg')
            if photo == None:
              errFiles.append(pic)
            else:
              successFiles.append(pic)
          except:
            print "Unable to upload."
            errFiles.append(pic)
            
            # Print the summary
    self.printUploadSummary(album.gphoto_id.text, pics, successFiles, errFiles, duplicateFiles)



  def printUploadSummary(self, albumid, allPhotos, successPhotos , errPhotos, duplicatePhotos):
    total = len(allPhotos)
    errors = len(errPhotos)
    duplicates = len(duplicatePhotos)
    success = len(successPhotos)
    print "------------------------------"
    print "Photo album: " + albumid
    if errors == 0 and duplicates == 0 and total == success:
      print "Hooray, I have uploaded all %r photos for you!! " % (total)
    elif errors > 0 and duplicates == 0:
      print ":( Unfortunately I could not upload %r photos out of %r. Files failed are:" % (errors, total)
      print errPhotos
    elif errors == 0 and duplicates > 0 and success == 0:
      print "Well, I have already uploaded this album and there is nothing new in it. So remove it, your album is in safe hands!."
    elif errors == 0 and duplicates > 0 and success > 0:
      print "I have uploaded %r photos, and ignored %r photos which are already there." % (success, duplicates)

    if total != (errors + duplicates + success):
      print "Hey, something fishy here. I did not upload all photos available in the Album."
    print "------------------------------"

        

  """
  Method gets the available photo names for the given albumid
  """
  def getExistingPhotos(self, albumid):
    existingPhotos = []
    album_url = '/data/feed/api/user/%s/albumid/%s' % (os.environ['tempuser'], albumid)
    photos = self.gdc.GetFeed(album_url + '?kind=photo')
    for photo in photos.entry:
      existingPhotos.append(photo.title.text)
    return existingPhotos

    
  def downloadPhoto(self, url, albumName):
    if (url == None or albumName == None): return None
    photoName = url[url.rindex('/')+1:] 
    url = url.replace(photoName, "d/" + photoName)
    urllib.retrieve(url, work + '/' + albumName + '/' + photoName)

  # -------------------------------------------------------------------------
  # Import helper methods
  # -------------------------------------------------------------------------
  

        


  #  -------------------------------------------------------------------------
  #  Local helper methods for ALBUMS
  #  -------------------------------------------------------------------------

  """
    Method to create an album and it checks for any duplicate before adding.
  """
  def createAlbum(self, name):
    result = None
    
    # Precondition check.
    if name == None: return None

    check = self.isDuplicateAlbum(name)
    
    if check[1] == False:
      result = self.gdc.InsertAlbum(title=name, summary='auto')    # create album
      print "Created album successfully: ", name
    else:
      result = check[0] # FIXME: Get the existing album reference
      print "Album already present:", name
    return result

  def isDuplicateAlbum(self, newName):
    isDuplicate = False
    album = None
    albums = self.gdc.GetUserFeed()
    
    # check for any duplicate
    for album in albums.entry:
      isDuplicate = (album.title.text == newName)
      if isDuplicate == True:
        break
    return (album, isDuplicate)

  def deleteAllAlbums(self):
    albums = self.gdc.GetUserFeed()
    confirm = raw_input("WARNING: DO YOU WANT TO DELETE ALL ALBUMS?, SAY YES: ")
    if confirm == "YES":
      for album in albums.entry:
        self.gdc.Delete(album)
        print album.title.text + "detelted!!"
    else:
      print "Okay, I do not delete it!"


def run(args):
  print "==========================================="
  action = args[1] if len(args) == 2 else None
  # Precondition check.
  if (settings.base == None):
    print "Hey, I cannot run if you don't set the base directory in settings.py. \nGo and set it first before running me!!"

  tempList = os.listdir(settings.base)

  photoman = PhotoMan()

  if action == "purgeall":
    photoman.deleteAllAlbums()
  elif action == "upload":
    dirs = [d for d in os.listdir(settings.base) if os.path.isdir(settings.base + '/' + d)]
  
    for dir in dirs:
      album = photoman.createAlbum(dir)
      if album != None:
        path = settings.base + '/' + dir
        photoman.uploadPhotos(album, path)
  elif action == "import":
    pass
  else:
    print "[Usage] Allowed actions are: upload, import, prugeall"
    print "upload     Uploads the photos to the album. Creates new album if not existing."
    print "import     imports the album from another service to Google+. photoman looks for import.cfg"
    print "purgeall   DELETES ALL ALBUMS. Use with CAUTION!!"
  print "==========================================="


if __name__ == "__main__":
  run(sys.argv) # Let photo man be run.

