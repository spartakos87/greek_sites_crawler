def athinorama(html):
	try:
		topic = html.title.text.split('-')[1].strip()
	except:
		topic=''
	title = html.title.text
	article = html.find("div",{"id":"ParagraphsContainer"}).text
	publish_time = html.find("p",{"id":"firma"}).find("time").text.strip()
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
