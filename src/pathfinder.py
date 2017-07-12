
def pathfinder(html):
	topic = html.find("div",{"class":"tags"}).text
	title = html.title.text
	article = html.find("div",{"itemprop":"articleBody"}).text
	publish_time = html.find("time",{"itemprop":"datePublished"}).text
	return { 'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
