
def oneman(html):
	topic = html.find("a",{"class":"section"}).text
	title = html.title.text
	article = html.find("div",{"class":"body"}).text
	publish_time = html.find("span",{"itemprop":"datePublished"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
