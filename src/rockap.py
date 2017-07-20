
def rockap(html):
	topic = html.find("span",{"itemprop":"title"}).text
	title = html.title.text
	article = html.find("section",{"itemprop":"articleBody"}).text
	publish_time = html.find('article').find('time').text
	return { 'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}

