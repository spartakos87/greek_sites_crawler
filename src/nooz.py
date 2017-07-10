
def nooz(html):
	topic = [i for i in html.find("div",{"class":"article_canvas"}).text.split('\n') if i!=''][0]
	title = html.title.text
	article = html.find("div",{"class":"article_body_text"}).text
	publish_time = html.find("h3",{"class":"date"}).text
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
