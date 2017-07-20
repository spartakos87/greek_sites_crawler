def avopolis(html):
	topic = html.find("h1",{"class":"pagetitle"}).text
	title = html.title.text
	article = html.find("div",{'class':"article_text"}).text
	publish_time = html.find("span",{"class":"published"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
