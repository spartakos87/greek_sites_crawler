
def enikos(html):
	topic=html.title.text.split('-')[-1]
	title=html.title.text
	article = html.find("div",{"id":"articletext"}).text
	publish_time = html.find("div",{"class":"article-time small-6 col"}).text
	return { 'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
	
