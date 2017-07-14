
def fimotro(html):
	topic=html.find('div',{'class':"menu-section clearfix"}).find('li',{'class':'menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor current-menu-parent current-post-parent menu-item-25457'}).text
	title = html.title.text
	article = html.find('div',{'class':'entry-content'}).text
	publish_time = str( html.find("meta",{"property":"article:published_time"})).split('=')[1].split()[0].replace('"','')
	return {'topic':topic,
			'title':title,
				'article':article,
					'publish_time':publish_time
		}
