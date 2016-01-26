import os
import requests
import shutil

zipurl = 'http://stash.compciv.org/scrapespeare/matty.shakespeare.tar.gz'
resp = requests.get(zipurl)

zname = os.path.join('tempdata', "matty.shakespeare.tar.gz")
zfile = open(zname, 'wb')
zfile.write(resp.content)
zfile.close()
shutil.unpack_archive(zname, extract_dir='tempdata')