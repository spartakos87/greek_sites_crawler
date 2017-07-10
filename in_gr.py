
def in_gr(html):
	topic = html.title.text.split('-')[-2]
	title = html.title.text
	article = html.find("div",{"id":"intext_content_tag"}).text
	publish_time = html.find("p",{"class":"article-date-info"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
