#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# is appengine a link or a way to control between all the aspects of a web page how do we use those aspects
#


import webapp2
import logging
import jinja2
import os
from google.appengine.api import users
from google.appengine.ext import ndb
import urllib2
import json
import datetime

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/index.html')



        user = users.get_current_user()
        if user:
            greeting =  users.create_logout_url('/')

            url = "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=lego-movie"
            string = urllib2.urlopen(url)
            legogif = json.loads(string.read())
            legogif_url = legogif['data']['image_url']

            self.response.write(template.render({"greeting":greeting,
                                                 "legogif_url":legogif_url
                                                }))


        else:
            greeting = ('<a href = "%s">Sign in </a>' %
                users.create_login_url('/'))
        self.response.write('<html><body>%s</body></html>' % greeting)


class Comment(ndb.Model):
    user = ndb.StringProperty()
    comment_text = ndb.TextProperty()
    created = ndb.DateTimeProperty()

class ArtHandler(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()
        comment = self.request.get('comment')
        template = jinja_environment.get_template('templates/art.html')

        commentobject = Comment(user = user.nickname(), comment_text = comment, created = datetime.datetime.now())
        commentobject.put()

        query = Comment.query()
        data = query.fetch()
        logging.info(data)

        clean_data = []
    



        self.response.write(template.render({'data':data}))




jinja_environment = jinja2.Environment(loader =
    jinja2.FileSystemLoader(os.path.dirname(__file__)))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/ArtHandler',ArtHandler),





], debug=True)
