import requests
from bs4 import BeautifulSoup

def get_html(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
	url = requests.get(url,headers=headers).content.decode()
	url = BeautifulSoup(url,'html.parser')
	for script in url(["script", "style"]):
		script.extract()
	return url
