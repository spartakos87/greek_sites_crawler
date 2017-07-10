
def naftemporiki(html):
	topic = html.find("span",{"itemprop":"articleSection"}).text
	title = html.title.text
	article = html.find("span",{"id":"spBody"}).text
	publish_time =html.find("div",{"class":"Date"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time}
