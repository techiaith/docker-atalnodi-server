import cherrypy

from punctuate import Punctuation
from truecaser import Truecaser


class PunctuationRestoreAPI(object):

    def __init__(self):
        self.punctuation = Punctuation()
        self.truecaser = Truecaser()

        cherrypy.log("Loading models completed")
        
    @cherrypy.expose
    def index(self):
        msg = "<h1>Welsh Punctuation and Truecasing Restoration Server</h1>\n"
        return msg 

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def restore(self, text, **kwargs):
        raw_text = text
        text = self.punctuation.punctuate(text)
        text = self.truecaser.truecase(text)
        text = text.rstrip()

        result = {
            'version':1,
            'success': True,
            'original_text': raw_text,
            'restored_text': text
        }
        return result



cherrypy.config.update({
    'environment': 'production',
    'log.screen': False,
    'response.stream': True,
    'log.access_file': '/var/log/app/access.log',
    'log.error_file': '/var/log/app/error.log',
})

cherrypy.tree.mount(PunctuationRestoreAPI(), '/')
application = cherrypy.tree
