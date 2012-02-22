import webapp2
import os
import jinja2
from google.appengine.api import urlfetch
import json
import config

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

url = "https://raw.github.com/currencybot/open-exchange-rates/master/latest.json"
class MainPage(webapp2.RequestHandler):
  def get(self):
      resp = urlfetch.fetch(url)
      data = json.loads(resp.content)
      template_values = {
      }
      template = jinja_environment.get_template('index.html')
      self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)
