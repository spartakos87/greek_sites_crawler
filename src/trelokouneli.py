
def trelokouneli(html):
	topic = html.find("ul",{"class":"post-categories"}).text
	title = html.title.text
	article = html.find("div",{"class":"post_content"}).text
	publish_time = html.find("time",{"class":"entry-date published updated"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
	
