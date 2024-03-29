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
import jinja2
import os

class MainHandler(webapp2.RequestHandler):
    def get(self):
        entry = jinja_environment.get_template('templates/entry.html')
        self.response.write(entry.render({}))

class ResponseHandler(webapp2.RequestHandler):
    def post(self):
        team_members = {
                        'mikaela ':{'college':'Univ AK Fairbanks'},
                    'nisha ':{'college':"UC san diego"},
                        ' gabryelle':{'college':'digy pen'},
                        ' irwin':{'college':"OU"}}

        pluralnoun1 = self.request.get('pluralnoun1')
        place1 = self.request.get('place1')
        response = jinja_environment.get_template('templates/response.html')
        self.response.write(response.render({
            'pluralnoun1':pluralnoun1,
            'place1':place1,
            'team_members': team_members
            }))




jinja_environment = jinja2.Environment(loader =
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/response', ResponseHandler)
], debug=True)
