import datetime

from django.http import HttpResponse,Http404


def hello(request):
  return HttpResponse("Hello World!!")

def index(request):
  return HttpResponse("Welcome to Django powered index page")

def current_date_time(request):
  now = datetime.datetime.now()
  html = "<html><body><b>%s<b></body></html>" % now
  return HttpResponse(html)

def hours_ahead(request,offset):
  try:
    offset = int(offset)
  except ValueError:
    raise Http404()
  dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
  html = "<html><body>In %s hour's, it will be %s.</body></html>" % (offset, dt)
  return HttpResponse(html)

