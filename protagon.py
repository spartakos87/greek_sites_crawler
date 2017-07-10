
def protagon(html):
	topic = html.find("a",{"class":"caeee"}).text
	title = html.title.text
	article = html.find("div",{"class":"content_space"}).text
	publish_time = html.find("span",{"class":"generalight uppercase"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time}
