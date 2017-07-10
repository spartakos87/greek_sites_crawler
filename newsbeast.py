
def newsbeast(html):
	topic = html.find("div",{"class":"article-top-meta-categories category-crumb"}).text
	title = html.title.text
	article = html.find("div",{"class":"article-content"}).text
	publish_time = html.find("div",{"class":"article-top-meta-date"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
