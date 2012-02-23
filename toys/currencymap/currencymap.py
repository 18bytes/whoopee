import webapp2
from google.appengine.api import urlfetch
import json, jinja2, os
import config

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

url = "https://raw.github.com/currencybot/open-exchange-rates/master/latest.json"
class MainPage(webapp2.RequestHandler):
  def get(self):
      resp = urlfetch.fetch(url)
      data = json.loads(resp.content)
      base = self.request.get("base")
      base = "INR"
      factor =  1 / (data['rates'][base])
      for code in data['rates']:
        data['rates'][code] = 1 / (data['rates'][code] * factor)

      template_values = {
        'base': base,
        'rates': data['rates'],
        'countries': config.countries,
      }
      template = jinja_environment.get_template('index.html')
      #self.response.out.write(factor)
      self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
