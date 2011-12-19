import gdata.photos.service
import gdata.media
import gdata.geo
import os


# FIXME: Duplicate entries
# FIXME: Import from other albums, FlickR, Facebook

# TODO: Configure tempuser and temppass environment variable before running.

# Initialize google photo service.
gd_client = gdata.photos.service.PhotosService()
gd_client.email = os.environ['tempuser']
gd_client.password = os.environ['temppass']
gd_client.source = 'iuploader'
gd_client.ProgrammaticLogin()

# base path
base = '~/Pictures'

# Directories names to upload.
dirs = ['testalbum']


# Print the current albums  
albums = gd_client.GetUserFeed()
for album in albums.entry:
  print 'title: %s, number of photos: %s, id: %s' % (album.title.text, album.numphotos.text, album.gphoto_id.text)

"""
  Method to create an album and it checks for any duplicate before adding.
"""
def createAlbum(name):
  result = None
  isDuplicate = False
  albums = gdc.GetUserFeed()

  # check for any duplicate
  for album in albums.entry:
    isDuplicate = (album.title.text == name)
    if isDuplicate == True:
      break
  # create album
  if isDuplicate == False:
    result = gdc.InsertAlbum(title=name, summary='auto')
    print "Created album successfully: ", name
  else:
    result = album
    print "Album already present:", name
  return result 

def uploadPhotos(album, path):
  # get all photo name from album and store it in a map/list
  # If already present then dont upload, else upload
  existingPhotos = []
  album_url = '/data/feed/api/user/%s/albumid/%s' % (os.environ['tempuser'], album.gphoto_id.text)
  photos = gdc.GetFeed(album_url + '?kind=photo')
  for photo in photos.entry:
    existingPhotos.append(photo.title.text)
  
  pics = os.listdir(path)

  for pic in pics:
    # FIXME Add recurisve directory support, subdirectories can have duplicate names.
    if pic in existingPhotos:
      print "Duplicate entry:", pic
    else:
      filename = path + '/' + pic
      try:
        photo = gdc.InsertPhotoSimple(album_url, pic , '', filename, content_type='image/jpeg')  
        if photo == None:
          print "Photo upload failed:", pic
        else:
          print "Photo upload successful:", pic
      except: 
        print "Could not upload:", pic

  print "TODO: upload photo"

def run():
  print "------>>>"
  for dir in dirs:
    album = createAlbum(dir)
    if album != None:
      path = base + '/' + dir
      uploadPhotos(album, path)
    
  print "<<<------"

gdc = gd_client
run()

#createAlbum('Duplicate Test', gd_client)

