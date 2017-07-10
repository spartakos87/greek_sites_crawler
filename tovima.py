
def tovima(html):
	topic = html.title.text.split('-')[1].strip()
	title = html.title.text
	article = html.find("div",{"id":"intext_content_tag"}).text
	publish_time =html.find("div",{"class":"article_info"}).text 
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
