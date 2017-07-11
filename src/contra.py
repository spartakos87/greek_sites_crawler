
def contra(html):
	topic = ''
	title = html.title.text
	article = html.find("div",{"itemprop":"articleBody"}).text
	publish_time = html.find("span",{"class":"byline_date"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
