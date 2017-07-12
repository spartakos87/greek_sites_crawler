
def kontranews(html):
	topic = html.find("div",{"class":"field field--name-field-category field--type-entity-reference field--label-above"}).text.split('\n')[-2]
	title = html.title.text
	article = html.find("div",{"property":"schema:text"}).text
	publish_time = html.find("span",{"property":"schema:dateCreated"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
