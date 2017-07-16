import re

def skai(html):
	try:
		topic = str(html.find("h3",{"class":"section-title"})).split('>')[1].split('<')[0]
	except:
		topic=''
	title = str(html.find('title')).replace('<title>','').replace('</title>','')
	article = html.find('article').text
	publish_time = re.findall(r'\d{2}/\d{2}/\d{4}',html.find("meta",{"name":'publish-date'}).text)[0]
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
