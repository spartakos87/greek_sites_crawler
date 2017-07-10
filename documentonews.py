
def documentonews(html):
	topic =html.find('div',{'class':'row single-article-head'}).text.split('\n')[5]
	title = html.title.text
	article = html.find("article").text
	publish_time = html.find('p',{'class':'date'}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
