
def newsit(html):
	topic = str(html.title).split('-')[-2].strip()
	title = html.title.text.replace('<title>','').replace('</title>','')
	article = html.find("div",{"id":"intext_content_tag"}).text
	publish_time = html.find("div",{"class":"first_info_00"}).text.split(':')[1].split('|')[0].strip()
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}

