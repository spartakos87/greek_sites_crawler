
def clickatlife(html):
	topic= html.title.text.split('|')[1].strip()
	title= html.title.text
	article = html.find("article",{"class":"story"}).text
	publish_time = [i for i in html.find("article",{"class":"story"}).text.split('\n') if i !=''][0]
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
