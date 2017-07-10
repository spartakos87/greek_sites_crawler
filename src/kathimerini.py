
def kathimerini(html):
	topic = .find("span",{"class":"item-category"}).text#html.title.text.split('|')[1].strip()
	title = html.title.text
	article = html.find("div",{"class":"freetext"}).text
	publish_time = html.find("time").text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
