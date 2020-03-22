#! python3
# threadedDownloadXkcd.py - Downloads XKCD comics using multiple threads.

import requests, os, bs4, threading
os.makedirs('xkcd',exist_ok=True)

def downloadXkcd(startComic, endComic):
  for urlNumber in range(startComic, endComic):
    # Download the page
    print('Downloading page https://xkcd.com/%s...' % (urlNumber))
    res = requests.get('https://xkcd.com/%s' % (urlNumber))
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the commc image
    comicElem = soup.select('#comic img')
    if comicElem == []:
      print('Could not find comic image.')
    else:
      comicUrl = comicElem[0].get('src')
      print('Downloading image%s...' % (comicUrl))
      res = requests.get('https:' + comicUrl)
      res.raise_for_status()

      # Save the image to ./xkcd
      imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')

      for chunk in res.iter_content(100000):
        imageFile.write(chunk)
      imageFile.close()

#  Create and start the Thread objects.
downloadThreads = []
for i in range(0, 140, 10):
  start = i
  end = i + 9
  if start == 0:
    start = 1
  downloadThread = threading.Thread(target=downloadXkcd, args=(start, end))
  downloadThreads.append(downloadThread)
  downloadThread.start()

# Wait for all threads to end.
for downloadThread in downloadThreads:
  downloadThread.join()
print('Done.')