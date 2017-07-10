
def newsbomb(html):
	topic = html.find('h4',{'class':'story-category'}).text.replace('\n','')
	title = html.title.text
	article = html.find('div',{'class':'story-fulltext'}).text
	publish_time = html.find('span',{'class':'day'}).text.split('\t')[-1]
	return {'topic':topic,
			'title':title,	
				'article':article,
					'publish_time':publish_time
		}
                             
