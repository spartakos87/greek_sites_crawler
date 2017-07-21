
def newpost(html):
	topic = html.find("button",{"class":"dropdown-toggle"}).text
	title = html.title.text
	article = html.find("div",{"class":"article-body"}).text
	publish_time = html.find("div",{"class":"published"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
