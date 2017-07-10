
def zougla(html):
	topic = str(html.find("link",{"rel":"canonical"})).split("zougla.gr")[-1].split('/')[1]
	title = html.title.text
	article = html.find("div",{"itemprop":"articleBody"}).text
	publish_time = html.find("div",{"class":"top_date"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
