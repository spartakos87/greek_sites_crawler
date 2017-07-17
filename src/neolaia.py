
def neolaia(html):
	try:
		topic=html.find("li",{'class':"current"}).text
	except:
		topic=''
	title=html.title.text
	article = html.find("div",{"class":"content"}).text
	publish_time =str(html.find("p",{"class":"blog-author"})).split('</span>')[-1].replace('</p>','').strip()
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}

