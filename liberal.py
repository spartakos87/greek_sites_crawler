
def liberal(html):
	topic = html.find("h3",{"class":"related_header listing_breadcrumb"}).text
	title = html.title.text
	article = html.find("div",{"itemprop":"articleBody"}).text
	publish_time = html.find("div",{"class":"article_date"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
