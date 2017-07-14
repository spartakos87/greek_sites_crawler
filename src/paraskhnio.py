
def paraskhnio(html):
	topic = html.find('li',{'class':'entry-category'}).text
	title = html.title.text
	article = html.find('div',{'class':'td-post-content'}).text
	publish_time = html.find('time',{'class':"entry-date updated td-module-date"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
