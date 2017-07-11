
def makeleio(html):
	topic = html.find("ul",{"class":"post-categories"}).text
	title = html.title.text
	article = html.find("div",{"class":"post-content-wrap"}).text
	publish_time = html.find("time",{"itemprop":"dateCreated"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}

