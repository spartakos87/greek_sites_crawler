
def culturenow(html):
	topic = str(a.find("div",{"class":"filters"})).split()
	topic = [topic[k+2] for k,i in enumerate(t) if 'current-cat' in i][0].split('>')[1].split('<')[0]
	title = html.title.text
	article = html.find("div",{"class":"post-content"}).text
	publish_time = html.find("div",{"class":"post-meta"}).text.split('/')[1].strip()
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
