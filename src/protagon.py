
def protagon(html):
	try:
		topic = html.find("a",{"class":"caeee"}).text
	except:
		try:
			topic =html.find("div",{"class":"get-category"}).text
		except:
			topic =''
	title = html.title.text
	article = html.find("div",{"class":"content_space"}).text
	publish_time = html.find("span",{"class":"generalight uppercase"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time}
