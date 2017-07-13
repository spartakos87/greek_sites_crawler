
def dikaiologitika(html):
	try:
		topic=html.find("div",{"class":"item__category"}).text.split('\n')[-2]
	except:
		topic=''
	title = html.title.text
	article = html.find("div",{"class":"item__fulltext"}).text
	publish_time = html.find("span",{"itemprop":"datePublished"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
