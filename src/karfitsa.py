
def karfitsa(html):
	topic = html.find_all('span',{'itemprop':"name"})[-1].text
	title = html.title.text
	article = html.find('div',{'class':'td-post-content td-pb-padding-side'}).text
	publish_time = html.find('time',{'class':'entry-date updated td-module-date'}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
