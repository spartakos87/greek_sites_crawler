
def real(html):
	topic = html.title.text.split('-')[1]
	title = html.title.text.split('-')[-1]
	article = html.find("div",{"class":"article_pure_text"}).text
	publish_time =html.find("div",{"class":"article-date"}).text.split("|")[0]
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}


