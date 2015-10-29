import ssl
from functools import wraps
def sslwrap(func):
    @wraps(func)
    def bar(*args, **kw):
        kw['ssl_version'] = ssl.PROTOCOL_TLSv1
        return func(*args, **kw)
    return bar

ssl.wrap_socket = sslwrap(ssl.wrap_socket)

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
ckey='rmDTAKK7q8ygXbSiYdT64H2XG'
csecret='MsZnn6e5CQP2UE5cRfv0exXsUmWHyLi0uO6RdfUc3RS4WMcCBD'
atoken='207894538-bV0mBkhIOABlkkayg2W1KllY33qDTzSQi6n9fXBj'
asecret='QwlW7TA18EQr8XYHS2mfASU9OFQ80Y8YSIrAu4VDgfTnB'

class listener(StreamListener):
  def on_data(self,data):
            try:
                #print data
                tweet = data.split ('"text":"') [1].split ('","source')[0]
                print tweet
                saveThis = str(time.time())+ '::'+ tweet
                saveFile = open('streamtweetDB3.csv', 'a')
                saveFile.write(data)
                saveFile.write('\n')
                saveFile.close()
                return True
            except BaseException, e:
                print 'failed ondata', str(e)
                time.sleep(10)
  def on_error(self, status):
    print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream= Stream(auth, listener())
twitterStream.filter(track=["magufuli"])
