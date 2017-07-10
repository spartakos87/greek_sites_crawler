
def news247(html):
	topic = html.title.text.split('|')[-2]
	title = html.title.text
	article = html.find("div",{"itemprop":"articleBody"}).text
	publish_time = html.find("div",{"class":"date"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
