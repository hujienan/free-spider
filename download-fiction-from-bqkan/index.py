import requests, sys
from bs4 import BeautifulSoup

class downloader(object):
    def __init__(self):
        self.server = 'https://www.bqkan.com/'
        self.target = 'https://www.bqkan.com/3_3026/'
        self.names = []
        self.urls = []
        self.nums = 0

    def get_download_url(self):
        req = requests.get(url = self.target)
        # print(req.encoding)
        # ISO-8859-1
        html = req.text.encode('iso-8859-1')
        div_bf = BeautifulSoup(html, 'html.parser')
        div = div_bf.find_all('div', class_ = 'listmain')
        a_bf = BeautifulSoup(str(div[0]), 'html.parser')
        a = a_bf.find_all('a')
        self.nums = len(a[12:])
        for item in a[12:]:
            self.names.append(item.string)
            self.urls.append(self.server + item.get('href'))

    def get_contents(self, target):
        req = requests.get(url = target)
        html = req.text
        bf = BeautifulSoup(html, 'html.parser')
        texts = bf.find_all('div', class_ = 'showtxt')
        texts = texts[0].text.replace('\xa0'*8, '\n\n')
        return texts

    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')
    
if __name__ == "__main__":
    dl = downloader()
    dl.get_download_url()
    for i in range(dl.nums):
        dl.writer(dl.names[i], 'download-fiction-from-bqkan/fiction.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write('    Downloading: {:2.2%} \r'.format(i/dl.nums))
        sys.stdout.flush()
    print('\n Done')