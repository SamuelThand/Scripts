'''
A script that takes a list that contains lines with links and sequentially downloads them to a download directory
'''

import urllib.request
import time

#If you get 403: Forbidden errors, try augmenting the urllib.request.urlretrieve with a custom header
#Example:
#header = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }

#Enter name of file with link list
fhand = open('testlist.txt')

for line in fhand :
    time.sleep(1)
    line=line.rstrip()
    if line.startswith('https') :
        print('Downloading: ',line)

        #Names the file with original title
        filename = (line.split('/')[-1])

        #Edit your download directory
        urllib.request.urlretrieve(line, f'C:/YOUR/DOWNLOAD/DIRECTORY/{filename}')

        print('Completed')
    else :
        continue
print('Done')
