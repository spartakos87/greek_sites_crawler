
def flashnews(html):
	topic = html.find('li',{'class':'active'}).text
	title = html.title.text
	article = html.find("div",{"class":"article-text"}).text
	publish_time= html.find("div",{"id":"article-date"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
