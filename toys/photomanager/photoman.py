# Long live google (and its photo service.)
# I am photoman, My god is Sundar (The creator) and my purpose of existence is to help him maintain his digital photos.

import gdata.photos.service
import gdata.media
import gdata.geo
import os

import settings.*


# TODO: Preprocess and find out what to upload. Update a summary in summary.log
# TODO: Recursive directories
# TODO: Must be able to interrupt

# TODO: Duplicate entries
# TODO: Import from other albums, FlickR, Facebook

# TODO: Configure tempuser and temppass environment variable before running.




# TODO License

class PhotoMan:

    def __init__(self):
        self.gdc = self.initGooglePhotoService()
        

   """
    Method to intialize Google Photo service.
   """
   def initGooglePhotoService():
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

      # get all photo name from album and store it in a map/list
      # If already present then dont upload, else upload
      existingPhotos = getExistingPhotos(album.gphoto_id.text)

      pics = os.listdir(path)
      
      # Try to upload each file.
      for pic in pics:
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
              errFiles.append(pic)

      # Print the summary
      self.printUploadSumnmary(album.gphoto_id.text, pics, successFiles, errFiles, duplicateFiles)



    def printUploadSummary(self, albumid, allPhotos, successPhotos , errPhotos, duplicatePhotos):
      total = len(allphotos)
      errors = len(errPhotos)
      duplicates = len(duplicatePhotos)
      success = len(successPhotos)
      print "------------------------------"
      print "Photo album: " + albumid
      if errors == 0 and duplicates == 0 and total == success:
          print "Hooray, I have uploaded all %r photos for you!! " % (total)
      else if errors > 0 and duplicates == 0:
          print ":( Unfortunately I could not upload %r photos out of %r. Files failed are:" % (errors, total)
          print errPhotos
      else if errors == 0 and duplicates > 0 and success == 0:
          print "Well, I have already uploaded this album and there is nothing new in it. So remove it, your album is in safe hands!."
      else if errors == 0 and duplicates > 0 and success > 0:
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

      check = isDuplicateAlbum(name)
    
      if check[1] == False:
        result = self.gdc.InsertAlbum(title=name, summary='auto')    # create album
        print "Created album successfully: ", name
      else:
        result = check[0] # FIXME: Get the existing album reference
        print "Album already present:", name
      return result

    def isDuplicateAlbum(newName):
      isDuplicate = False
      albums = self.gdc.GetUserFeed()

      # check for any duplicate
      for album in albums.entry:
        isDuplicate = (album.title.text == newName)
        if isDuplicate == True:
            album = None
            break
      return (album, isDuplicate)






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

