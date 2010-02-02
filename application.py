import string, urllib, re
try:
    import json
except ImportError:
    from django.utils import simplejson as json
    
import web

from urlparse import urlparse
from random import randrange, choice
from google.appengine.ext import db

urls = (
    '/', 'index',
    '/([a-zA-Z0-9]{2,10})', 'redirect',
)

app = web.application(urls, globals())
render = web.template.render('templates', base='layout')

URL_CHARS = "".join(string.digits + string.letters)
ALLOWED_PROTOCOLS = frozenset(['http', 'https', 'ftp', 'ftps'])

class URL(db.Model):
    actual = db.LinkProperty()
    shortened = db.LinkProperty()

class index:
    def GET(self):
        return render.index()

    def POST(self):
        xhr = web.ctx.env.get('HTTP_X_REQUESTED_WITH', None)
        i = web.input()
        self.url_to_shorten = i.url
        if not self.__validate_url():
            error_msg = "The URL specified is invalid"
            if xhr:
                web.ctx.headers.append(('Content-Type', 'application/json'))
                return json.dumps({'error': True, 'msg' : error_msg})
            else:
                return render.index(error_msg)
        else:
            url, short_url = self.__generate_url()
            url = web.websafe(url)
            if xhr:
                web.ctx.headers.append(('Content-Type', 'application/json'))
                return json.dumps({'success' : True, 'url' : url, 'short' : short_url})
            else:
                return render.index(None, url, short_url)

    def __validate_url(self):
        parsed = urlparse(self.url_to_shorten)
        if parsed.scheme is '':
            self.url_to_shorten = "http://" + self.url_to_shorten
            parsed = urlparse(self.url_to_shorten)
        if parsed.path is not None:
            if re.search("([<>])", parsed.path):
                return False
        if parsed.scheme in ALLOWED_PROTOCOLS:
            # http://stackoverflow.com/questions/106179/regular-expression-to-match-hostname-or-ip-address
            validhostregex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z]|[A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9])$"
            if re.match(validhostregex, parsed.netloc) is not None:
                return True
            # this was my previous validation code - hostnames however
            # can not start or end with any punctuation.
            #if re.sub("[-.]", '', parsed.netloc).isalnum()
        return False
        
    def __generate_url(self):
        query = db.GqlQuery("SELECT * FROM URL WHERE actual = :1", self.url_to_shorten)
        entry = query.get()
        if not entry:
            entry = URL()
            entry.actual = self.url_to_shorten
            while True:
                shortened = "".join([choice(URL_CHARS) for i in xrange(randrange(2,11))])
                shortened = web.ctx.homedomain + '/' + shortened
                query = db.GqlQuery("SELECT * FROM URL WHERE shortened = :1", shortened)
                already_exists = query.get()
                if not already_exists:
                    entry.shortened = shortened
                    break
            entry.put()
        return (entry.actual, entry.shortened)
            
class redirect:
    
    def GET(self, url):
        shortened = web.ctx.homedomain + '/' + url
        query = db.GqlQuery("SELECT * FROM URL WHERE shortened = :1", shortened)
        entry = query.get()
        if not entry:
            return render.notfound(web.websafe(url))
        else:
            web.seeother(entry.actual)

def _main():
    app.cgirun()
    
if __name__ == "__main__":
    _main()