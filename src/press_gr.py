
def press_gr(html):
	topic = [i for i in html.find('span',{'class':'crumbs'}).text.split('\n') if i!=''][2]
	title = html.title.text
	article = html.find('div',{"itemprop":"articleBody"}).text
	publish_time = html.find('span',{'class':'meta_date'}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
	
