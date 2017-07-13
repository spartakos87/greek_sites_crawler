
def cnn(html):
	try:
		topic = str(html.find('ul',{ 'class':"nav-child submenu"})).split('href')
		topic = [topic[k+1] for k,i in enumerate(topic) if 'active' in i][0]
		topic = topic.split('>')[1].split('<')[0]
	except:
		topic ='' # There isn't specific topic
	title = html.title.text
	article = html.find('div',{'class':"story-text story-fulltext"}).text
	publish_time = [i for i in html.find('div',{'class':"story-date story-credits icon icon-time"}).text.split('\t') if i!='' and i!='\n'][1]
	return {'topic':topic,
				'title':title,
					'article':article,
						'publish_time':publish_time
			}

