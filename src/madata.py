
def madata(html):
	topic = html.find('article',{'id':"article-post"}).text.split('\n')[3]
	title = html.title.text
	article = html.find('article',{'id':"article-post"}).text
	publish_time=html.find('article',{'id':"article-post"}).text.split('\n')[4]
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
	
