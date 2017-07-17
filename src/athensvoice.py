
def athensvoice(html):
	topic = html.find('div',{"class":"field-theme"}).text
	title = html.title.text
	article = html.find_all("div",{"class":"field-items"})[2].text
	publish_time = html.find("div",{"class":"post-date"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
