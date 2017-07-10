
def capital(html):
	topic = html.find("div",{"class":"headingS5"}).text
	title = html.title.text
	article = html.find("div",{"class":"article__content"}).text
	publish_time = html.find("h5",{"class":"category"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
