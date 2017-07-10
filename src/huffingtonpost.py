
def huffingtonpost(html):
	topic = html.find("span",{"class":"entrytag"}).text
	title = html.title.text
	article = html.find("div",class_="content",id="mainentrycontent").text
	publish_time = html.find("div",{"class":"times"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
