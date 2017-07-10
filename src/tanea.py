
def tanea(html):
	topic = html.title.text.split('-')[1]
	title = html.title.text
	article = html.find("div",{'class':'mainarticle__body'  }).text
	publish_time = html.find("span",{'class':"published__time"  }).text
	return { 'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
