import urllib2
import json

url = "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=kittens"
result = urllib2.urlopen(url)
kittygif = json.loads(result.read())
print kittygif['data']['image_url']
