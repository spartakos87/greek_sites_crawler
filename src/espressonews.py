
def espressonews(html):
	topic = html.find("div",{"class":"field-item even"}).text
	title = html.title.text
	article = html.find("div",{"class":"field field-name-body field-type-text-with-summary field-label-hidden"}).text
	publish_time = html.find("div",{"class":"field field-name-post-date field-type-ds field-label-hidden"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
	
