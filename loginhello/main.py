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
from google.appengine.api import users


class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
                greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                        (user.nickname(), users.create_logout_url('/bye')))

        else:
            greeting = ('<a href = "%s">Sign in </a>' %
                users.create_login_url('/'))
        self.response.write('<html><body>%s</body></html>' % greeting)

class ByeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<html><body> Bye </body></html>')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/bye', ByeHandler)
], debug=True)
