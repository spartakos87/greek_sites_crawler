
def gazzetta(html):
	topic = html.find("div",{"class":"breadcrumb"}).text
	title = html.title.text
	article = html.find("div",{"itemprop":"articleBody"}).text
	publish_time = html.find("div",{"class":"article_date"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
