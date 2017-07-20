
def sinavlia(html):
	topic = html.find("span",{"class":"entry-category"}).text
	title = html.title.text
	article = html.find("article",{"class":"entry-content"}).text
	publish_time = html.find("time",{"class":"entry-date published"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
	
