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
import webapp2
import logging
import jinja2
import os
from google.appengine.api import users
import urllib2
import json
from google.appengine.ext import ndb
import datetime

class Temperature(ndb.Model):
    temperature = ndb.IntegerProperty()
    latitude = ndb.FloatProperty()
    longitude = ndb.FloatProperty()
    created = ndb.DateTimeProperty()

class MainHandler(webapp2.RequestHandler):
    def get(self):
        temp = Temperature(temperature = 75, latitude = 47.6, longitude = 127.7,  created = datetime.datetime.now())
        temp.put()
        query = Temperature.query()
        data = query.fetch()
        logging.info(data)

class TempHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/index.html')



        # get lat and lon from javascript
        lat = self.request.get('lat')
        lon = self.request.get('lon')

        # creating the url for teh api request
        url = ("http://api.openweathermap.org/data/2.5/weather?"
                "lat=%s&lon=%s&units=imperial&APPID=(d5931eab91873d300502bf1460fce929)" %(lat, lon))
        #fire a request to teh url, turn respone into a string
        string = urllib2.urlopen(url).read()
        #turn string to dictionary
        dict = json.loads(string)
        #choosing temp info out of dictionary

        ##create dictionary to pass to template
        if lat == "" or lon == "":
            form = True
            temp = "waiting for the temp data"
        else:
            form = False
            temp = dict['main']['temp']
            tempobject = Temperature(temperature = int(temp), latitude = float(lat), longitude = float(lon),
                         created = datetime.datetime.now())
            tempobject.put()
            logging.info(tempobject)

        template_var = {"temp": temp, 'form': form}

        self.response.write(template.render(template_var))



class Post(ndb.Model):
    username = ndb.StringProperty()
    date_created = ndb.DateTimeProperty(auto_now_add = True)
    text = ndb.StringProperty()
    likes = ndb.IntegerProperty()
    dislikes = ndb.IntegerProperty()
    comments = ndb.StringProperty(repeated = True)


class BlogHandler(webapp2.RequestHandler):
    def post(self):
        #update blog
        post = Post(username = "splenda", text = "sugar is sweet", likes= 0, dislikes=1, comments = [] )
        post.put()


    def get(self):
        #display all the posts and a box for new ones (if signed in user)


        post = Post(username = "splenda", text = "sugar is sweet", likes= 0, dislikes=1, comments = [] )
        post.put()


        posts = Post.query().fetch()
        template = jinja_environment.get_template('templates/posts.html')
        self.response.write(template.render({'posts':posts}))









jinja_environment = jinja2.Environment(loader =
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
    ('/', TempHandler),
    ('/main', MainHandler),
    ('/blog', BlogHandler)
], debug=True)
