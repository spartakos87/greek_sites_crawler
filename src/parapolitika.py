
def parapolitika(html):
	topic = html.find("span",{"class":"sect_text artSectText"}).text
	title = html.title.text
	article = html.find("div",{"class":"articleMainContentInner"}).text
	publish_time = html.find("span",{"class":"pDate"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
