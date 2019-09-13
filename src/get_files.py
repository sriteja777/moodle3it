import requests
import bs4
import re
from download_utils import get_filename_from_cd, is_downloadable
from humanize import naturalsize
from utils import color_text
from urllib.parse import urlparse
session = requests.session()
url = "https://www.online-convert.com/file-format/pages"
purl = urlparse(url)
# print(purl.scheme, purl.netloc)
pg = session.get(url)
# print(pg.headers)
# exit(1)
sp = bs4.BeautifulSoup(pg.text, 'lxml')
links = []
for link in sp.findAll('a'):
    if link.has_attr('href'):
        refer = link.get('href')
        if refer.startswith('/'):
            links.append(purl.scheme + '://' + purl.netloc + refer)
        elif refer.startswith('#'):
            links.append(url + refer)
        else:
            p = urlparse(refer)
            if p.netloc and p.scheme:
                links.append(refer)


links = list(set(links))
# print(links)
# exit(1)
spaces = '{: <100} {:>20} {:>40}'
print(spaces.format(color_text('link', 'cyan'), color_text('filesize', 'cyan'),color_text('filename', 'cyan')))
for link in links:
    try:
        head = session.head(link, allow_redirects=True,timeout=10).headers
    except requests.ConnectionError as e:
        print('There is a connection error with link',link,'and the error is \n',str(e))
        continue
    if is_downloadable(head.get('content-type')):
        # print(head)
        filename = get_filename_from_cd(head.get('content-disposition'))
        if not filename:
            filename = link.split('/')[-1]

        file_size = int(head['content-length'])
        # print(len(link))
        print('{: <100} {:>20} {:>40}'.format(color_text(link,'blue'), color_text(naturalsize(file_size), 'yellow'), color_text(filename, 'brown')))
        # print('{: >25} {: >20} {: >20}'.format(color_text(link, 'blue'),filename, str(file_size)))