
def crashonline(html):
	topic = [i for i in html.find("div",{"class":"info"}).text.split('\n') if i!=''][1].split()[0]
	title = html.title.text
	article = html.find("div",{"class":"main-column-left"}).text.split('\n')
	article = article[:article.index('Περισσότερα Άρθρα:')]
	article = '\n'.join(article)
	publish_time = [i for i in html.find("div",{"class":"info"}).text.split('\n') if i!=''][0]
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
