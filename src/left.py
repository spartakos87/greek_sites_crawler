
def left(html):
	topic = html.find("div",{"class":"view-content"}).text.split()[3]
	title = html.title.text
	article = html.find("div",{"class":"views-field-body"}).text
	publish_time = html.find("div",{"class":"view-content"}).text.split()[2]
	return {'topic':topic,
			'title':title,	
				'article':article,
					'publish_time':publish_time
		}
