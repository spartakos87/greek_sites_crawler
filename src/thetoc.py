
def thetoc(html):
	topic = html.find("div",{"id":"categoryTitle"}).text
	title = html.title.text
	article = html.find("div",{"class":"articleText col-sm-9 mtd"}).text
	publish_time =  html.find("time").text
	return { 'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
