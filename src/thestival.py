
def thestival(html):
	topic = html.find("span",{"class":"NewsItemCategory"}).text
	title = html.title.text
	article = html.find("div",{"class":"ArticleFullText"}).text
	publish_time = [i for i in html.find("div",{"class":"ArticleInfo"}).text.split('\n') if i !=''][-1]
	return { 'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
