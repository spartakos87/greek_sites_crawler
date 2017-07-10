
def avgi(html):
	topic=html.find("span",{"itemprop":"articleSection"}).text
	title = html.title.text
	article = html.find("div",{"itemprop":"articleBody"}).text
	publish_time = html.find("time",{"class":"time-published"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
