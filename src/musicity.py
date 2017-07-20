def musicity(html):
	# There aren't topic and publish time
	title = html.title.text
	article = html.find("div",{"class":"itemFullText"}).text
	return {'topic':'',
			'title':title,
				'article':article,
					'publish_time':''
		}
