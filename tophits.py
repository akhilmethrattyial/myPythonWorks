import collections
import requests
import sys
import os

arguments = sys.argv

if len(arguments) == 3:
  
  LOG_FILE = arguments[1]
  VIEW_NUMBER = arguments[2]
  
  if os.path.exists(LOG_FILE):
    
    EXCLUDES = ['::1','127.0.0.1']
    ipCounter = collections.Counter()

    def getCountryCode(ip):
      reply = requests.get('https://freegeoip.net/json/{}'.format(ip))
      return reply.json()['country_code']

    with open(LOG_FILE) as logs:
      for logLine in logs:
        clientIp = logLine.split()[0]
        if clientIp not in EXCLUDES:
            ipCounter.update((clientIp,))


    for ip,count in ipCounter.most_common(int(VIEW_NUMBER)):
      print('{}'.format(ip)) 
      
  else:
    print('')
    print('Error : Unable to locate {}'.format(LOG_FILE))
    print('Usage : tophists.py  /path/to/access_log  Number')
    print('')    
      
    
else:
  print('')
  print('Usage : tophists.py  /path/to/access_log  Number')
  print('')
