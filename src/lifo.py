
def lifo(html):
	topic = str(html.find("meta",{"itemprop":"articleSection"})).split('=')[1].split('"')[1]
	title = html.title.text
	article = html.find("div",{"itemprop":"articleBody"}).text
	publish_time =html.find("div",{"itemprop":"datePublished"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
