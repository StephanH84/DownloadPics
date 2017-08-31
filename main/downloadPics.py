'''

@author: Stephan Hähne
'''

import sys
import os, inspect, urllib3
import unittest

class DownloadPicsTest(unittest.TestCase):
    def testDownload(self):
        savedPictureFile = os.curdir + os.sep + "test" + os.sep + "city-q-c-640-480-3.jpg"
        try:
            os.rmdir(savedPictureFile)
        except:
            pass

        downloadUrl("http://lorempixel.com/output/city-q-c-640-480-3.jpg", os.curdir + os.sep + "test")
        assert os.path.isfile(savedPictureFile)

    def testReadUrlList(self):
        list = readFile(get_curr_path() + os.sep + "urlList.txt")
        assert len(list) > 0

def readFile(urlListFile):
    result = []
    with open(urlListFile) as file:
        for line in file:
            result.append(line.split("\n")[0])
    return result

def downloadUrl(url, saveToPath):
    name = url.split("/")[-1]
    http = urllib3.PoolManager()
    filePath = saveToPath + os.sep + name
    chunk_size = 1024
    r = http.request('GET', url, preload_content=False)
    
    with open(filePath, 'wb') as out:
        while True:
            data = r.read(chunk_size)
            if not data:
                break
            out.write(data)
    
    r.release_conn()

def main():
    curr_path = get_curr_path()
    saveToPath = curr_path + os.sep + "images"
    urlListFile = curr_path + os.sep + "urlList.txt"
    urls = readFile(urlListFile)
    print(urls)
    for url in urls:
        downloadUrl(url, saveToPath)


def get_curr_path():
    return os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))


if __name__ == '__main__':
    main()