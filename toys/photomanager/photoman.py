# TODO License

class PhotoMan:

    def __init__(self, gdc):
        self.gdc = gdc
        


    #  -------------------------------------------------------------------------
    #  Local helper methods for PHOTOS    
    #  -------------------------------------------------------------------------

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


    def uploadPhotos(self, album, path):
      existingPhotos = []
      
      # Precondition check
      if (self.gdc == None): return
      if album == None or path == None: return

      # get all photo name from album and store it in a map/list
      # If already present then dont upload, else upload
      existingPhotos = getExistingPhotos(album.gphoto_id.text)

      pics = os.listdir(path)

      for pic in pics:
        # FIXME Add recurisve directory support, subdirectories can have duplicate names.
        if pic in existingPhotos:
          print "Duplicate entry:", pic
        else:
          filename = path + '/' + pic
          try:
            photo = self.gdc.InsertPhotoSimple(album_url, pic , '', filename, content_type='image/jpeg')
            if photo == None:
              print "Photo upload failed:", pic
            else:
              print "Photo upload successful:", pic
          except:
            print "Could not upload:", pic

    #  -------------------------------------------------------------------------
    #  Local helper methods for ALBUMS
    #  -------------------------------------------------------------------------
    """
      Method to create an album and it checks for any duplicate before adding.
    """
    def createAlbum(self, name):
      result = None

      # create album
      if isDuplicateAlbum(name) == False:
        result = self.gdc.InsertAlbum(title=name, summary='auto')
        print "Created album successfully: ", name
      else:
        result = album
        print "Album already present:", name
      return result

    def isDuplicateAlbum(newName):
      isDuplicate = False
      albums = self.gdc.GetUserFeed()

      # check for any duplicate
      for album in albums.entry:
        isDuplicate = (album.title.text == newName)
        if isDuplicate == True:
          break
      print isDuplicate
      return isDuplicate


