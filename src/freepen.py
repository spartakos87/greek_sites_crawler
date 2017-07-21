
def freepen(html):
	topic = html.find("span",{"class":"label-info"}).text
	title = html.title.text
	article = html.find("div",{"itemprop":"description articleBody"}).text
	publish_time = html.find("span",{"class":"time-info"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
