import glob

import json

import pickle

import gzip

import os

import hashlib

import re
names = set([name.split('/').pop() for name in glob.glob('hrefs/*')])

urls = set()
for name in names:
  print(name)
  try:
    obj = json.loads(open('hrefs/' + name).read())
  except:
    ...
  [urls.add(re.sub(r'\?.*?$', '', url)) for url in obj if hashlib.sha256(bytes(url,'utf8')).hexdigest() not in names]
  if len(urls) >= 10000:
    break
  print(urls)
open('urls.pkl.gz', 'wb').write(gzip.compress(pickle.dumps(urls)))
