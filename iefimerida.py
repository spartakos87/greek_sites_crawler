
def iefimerida(html):
	topic =html.find("div",{"class":"info"}).text.split()[0]
	title = html.title.text
	article = html.find("div",{"class":"news-articleBody"}).text 
	publish_time = html.find("div",{"class":"info"}).text.split()[-1]
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
