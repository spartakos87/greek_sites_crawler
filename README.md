# greek_sites_crawler
Programm which can crawl plenty of greek sites
#Sites which can crawl
skai,cnn,newsbomb,newsit,newsbeast,protothema,zougla    ,tovima,avgi,capital,documentonews,efsyn,enikos,huffingtonpost,iefimerida,in_gr,left,liberal,naftemporiki,news247,nooz,protagon,tanea,thetoc

## Run
Only you need to have is Python3 and the [BeautfulSoup](https://www.crummy.com/software/BeautifulSoup/)

### Let see how you can run it

python3 greek_sites_crawler -url "<url>"


#### Return 
That return a json in this formation
{'topic':<topic>,
	'title':<title>,
		'article':<article>
			'publish_time':<publish_time>
}

