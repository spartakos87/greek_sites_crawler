
def cerebrux(html):
	try:
		topic = html.find('span',{'class':'cat-links'}).text
	except:
		topic = ''
	title = html.title.text
	article = html.find('div',{'class':'entry-content'}).text
	publish_time = html.find('time',{'class':'entry-date published'}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
			
