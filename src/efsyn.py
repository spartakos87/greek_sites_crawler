
def efsyn(html):
	topic = html.find("div",{"class":"field field-name-field-category-ref field-type-entityreference field-label-hidden news_section_link"}).text
	title = html.title.text
	article = html.find("div",{"class":"field field-name-body field-type-text-with-summary field-label-hidden"}).text
	publish_time = html.find("div",{"class":"article_meta"}).text.split('|')[0]
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
