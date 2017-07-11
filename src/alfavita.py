
def alfavita(html):
	topic = html.find("div",{"class":"field-item even"}).text
	title = html.title.text
	article = html.find("div",{"class":"field field-name-body field-type-text-with-summary field-label-hidden"}).text
	publish_time = html.find("span",{"class":"uk-text-muted uk-text-small"}).text.split('|')[0]
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
