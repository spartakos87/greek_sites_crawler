
def protothema(html):
	topic = html.find("h2",{"class":"ArticleCatHeading"}).text
	title = html.title.text
	article = html.find("div",{"class":"article-content"}).text
	pubish_time = html.find("span",{"class":"time"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'pubish_time':pubish_time
		}
