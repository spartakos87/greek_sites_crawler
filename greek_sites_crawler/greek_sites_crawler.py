import requests
from bs4 import BeautifulSoup
import re

class greek_sites_crawler:
    """
    Greek sites crawler created by Serepas Filippas aka spartakos87
    email:serepasf@yahoo.gr
    How to run:
        from greek_sites_crawler import greek_sites_crawler
        data = greek_sites_crawler(<your url>)
        data.get_data()
    Which return a dictionary:
    '{topic':topic,
                 'title':title,
                             'article':article,
                                             'publish_time':publish_time
    }
    """
    def __init__(self, url):
        self.url = url

    def get_html(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        url = requests.get(self.url, headers=headers).content.decode()
        url = BeautifulSoup(url, 'lxml')
        for script in url(["script", "style"]):
            script.extract()
        return url

    def get_data(self):
        self.html = self.get_html()
        return self.pick_site()

    def pick_site(self):
        site = {
		"ert":self.ert, 
		"in_gr": self.in_gr,
                  "liberal": self.liberal,
                   "protagon": self.protagon,
                    "kathimerini": self.kathimerini,
    "huffingtonpost": self.huffingtonpost,
    "parapolitika": self.parapolitika,
    "avgi": self.avgi,
    "fimotro": self.fimotro,
    "pathfinder": self.pathfinder,
    "crashonline": self.crashonline,
    "rockap": self.rockap,
    "capital": self.capital,
    "tanea": self.tanea,
    "flashnews": self.flashnews,
    "newpost": self.newpost,
    "lifo": self.lifo,
    "clickatlife": self.clickatlife,
    "makeleio": self.makeleio,
    "athinorama": self.athinorama,
    "paraskhnio": self.paraskhnio,
    "madata": self.madata,
    "neolaia": self.neolaia,
    "skai": self.skai,
    "oneman": self.oneman,
    "karfitsa": self.karfitsa,
    "enikos": self.enikos,
    "naftemporiki": self.naftemporiki,
    "altsantiri": self.altsantiri,
    "news247": self.news247,
    "cerebrux": self.cerebrux,
    "real": self.real,
    "avopolis": self.avopolis,
    "tovima": self.tovima,
    "dikaiologitika": self.dikaiologitika,
    "documentonews": self.documentonews,
    "thetoc": self.thetoc,
    "press_gr": self.press_gr,
    "contra": self.contra,
    "protothema": self.protothema,
    "cnn": self.cnn,
    "thestival": self.thestival,
    "efsyn": self.efsyn,
    "athensvoice": self.athensvoice,
    "newsbeast": self.newsbeast,
    "trelokouneli": self.trelokouneli,
    "newsbomb": self.newsbomb,
    "musicity": self.musicity,
    "alfavita": self.alfavita,
    "freepen": self.freepen,
    "culturenow": self.culturenow,
    "sinavlia": self.sinavlia,
    "kontranews": self.kontranews,
    "nooz": self.nooz,
    "gazzetta": self.gazzetta,
    "left": self.left,
    "zougla": self.zougla,
    "iefimerida": self.iefimerida,
    "espressonews": self.espressonews,	
    "newsit": self.newsit}
        if 'cerebrux.net' in self.url:
            self.url = 'cerebrux'
        elif 'left.gr' in self.url:
            self.url = 'left'
        elif 'press-gr.com' in self.url:
            self.url = 'press_gr'
        elif 'flashnews.gr' in self.url:
            self.url = 'flashnews'
        elif 'newpost.gr' in self.url:
            self.url = 'newpost'
        elif 'fimotro.gr' in self.url:
              self.url = 'fimotro'
        elif 'news247.gr' in self.url:
              self.url = 'news247'
        elif 'sinavlia.gr' in self.url:
              self.url = 'sinavlia'
        else:
            self.url = self.url.split('.')[1]
        if self.url == 'in':
            self.url = self.url + '_gr'
        if site.get(self.url, None) == None:
            print("This site dont provider yet \n")
        else:
            try:
                data =  self.clean_data(site[self.url]())
                return data
            except Exception as ex:
                print(ex)
                pass

    def clean_data(self,data):
        data={'topic':
	       data['topic'].replace('\n',' ').replace('\t',' '),
               'title':data['title'].replace('\n',' ').replace('\t',' '),
                'article':data['article'].replace('\n',' ').replace('\t',' '),
                 'publish_time':data['publish_time'].replace('\n',' ').replace('\t',' ')
             }
        return data

    def skai(self):
        try:
            topic = str(self.html.find("h3", {"class": "section-title"})).split('>')[1].split('<')[0]
        except:
            topic = ' '
        title = str(self.html.find('title')).replace('<title>', '').replace('</title>', '')
        article = self.html.find('article').text
        try:
            publish_time = re.findall(r'\d{2}/\d{2}/\d{4}', self.html.find("meta", {"name": 'publish-date'}).text)[0]
        except:
            publish_time=''
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def alfavita(self):
        topic = self.html.find("div", {"class": "field-item even"}).text
        title = self.html.title.text
        article = self.html.find("div",
                            {"class": "field field-name-body field-type-text-with-summary field-label-hidden"}).text
        publish_time = self.html.find("span", {"class": "uk-text-muted uk-text-small"}).text.split('|')[0]
        return dict(topic=topic, title=title, article=article, publish_time=publish_time)

    def altsantiri(self):
        topic = self.html.find('li', {'class': 'entry-category'}).text
        title = self.html.title.text
        article = self.html.find('div', {'class': 'td-pb-span8 td-main-content'}).text
        publish_time = self.html.find('time', {'class': 'entry-date updated td-module-date'}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def athensvoice(self):
        topic = self.html.find('div', {"class": "field-theme"}).text
        title = self.html.title.text
        article = self.html.find_all("div", {"class": "field-items"})[2].text
        publish_time = self.html.find("div", {"class": "post-date"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def athinorama(self):
        try:
            topic = self.html.title.text.split('-')[1].strip()
        except:
            topic = ''
        title = self.html.title.text
        article = self.html.find("div", {"id": "ParagraphsContainer"}).text
        publish_time = self.html.find("p", {"id": "firma"}).find("time").text.strip()
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def avgi(self):
        topic = self.html.find("span", {"itemprop": "articleSection"}).text
        title = self.html.title.text
        article = self.html.find("div", {"itemprop": "articleBody"}).text
        publish_time = self.html.find("time", {"class": "time-published"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def avopolis(self):
        topic = self.html.find("h1", {"class": "pagetitle"}).text
        title = self.html.title.text
        article = self.html.find("div", {'class': "article_text"}).text
        publish_time = self.html.find("span", {"class": "published"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def capital(self):
        topic = self.html.find("div", {"class": "headingS5"}).text
        title = self.html.title.text
        article = self.html.find("div", {"class": "article__content"}).text
        publish_time = self.html.find("h5", {"class": "category"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def cerebrux(self):
        try:
            topic = self.html.find('span', {'class': 'cat-links'}).text
        except:
            topic = ''
        title = self.html.title.text
        article = self.html.find('div', {'class': 'entry-content'}).text
        publish_time = self.html.find('time', {'class': 'entry-date published'}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def clickatlife(self):
        topic = self.html.title.text.split('|')[1].strip()
        title = self.html.title.text
        article = self.html.find("article", {"class": "story"}).text
        publish_time = [i for i in self.html.find("article", {"class": "story"}).text.split('\n') if i != ''][0]
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def cnn(self):
        try:
            topic = str(self.html.find('ul', {'class': "nav-child submenu"})).split('href')
            topic = [topic[k + 1] for k, i in enumerate(topic) if 'active' in i][0]
            topic = topic.split('>')[1].split('<')[0]
        except:
            topic = ''  # There isn't specific topic
        title = self.html.title.text
        article = self.html.find('div', {'class': "story-text story-fulltext"}).text
        publish_time = \
            [i for i in self.html.find('div', {'class': "story-date story-credits icon icon-time"}).text.split('\t') if
             i != '' and i != '\n'][1]
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def contra(self):
        topic = ''
        title = self.html.title.text
        article = self.html.find("div", {"itemprop": "articleBody"}).text
        publish_time = self.html.find("span", {"class": "byline_date"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def crashonline(self):
        topic = [i for i in self.html.find("div", {"class": "info"}).text.split('\n') if i != ''][1].split()[0]
        title = self.html.title.text
        article = self.html.find("div", {"class": "main-column-left"}).text.split('\n')
        article = article[:article.index('Περισσότερα Άρθρα:')]
        article = '\n'.join(article)
        publish_time = [i for i in self.html.find("div", {"class": "info"}).text.split('\n') if i != ''][0]
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def culturenow(self):
        topic = str(self.html.find("div", {"class": "filters"})).split()
        topic = [topic[k + 2] for k, i in enumerate(topic) if 'current-cat' in i][0]
        if '=' in topic:
                 topic=topic.split('=')[-1]
                 title = self.html.title.text
                 article = self.html.find("div", {"class": "post-content"}).text
                 publish_time = self.html.find("div", {"class": "post-meta"}).text.split('/')[1].strip()
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def dikaiologitika(self):
        try:
            topic = self.html.find("div", {"class": "item__category"}).text.split('\n')[-2]
        except:
            topic = ''
        title = self.html.title.text
        article = self.html.find("div", {"class": "item__fulltext"}).text
        publish_time = self.html.find("span", {"itemprop": "datePublished"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def documentonews(self):
        topic = self.html.find('div', {'class': 'row single-article-head'}).text.split('\n')[5]
        title = self.html.title.text
        article = self.html.find("article").text
        publish_time = self.html.find('p', {'class': 'date'}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def efsyn(self):
        topic = self.html.find("div", {
            "class": "field field-name-field-category-ref field-type-entityreference field-label-hidden news_section_link"}).text
        title = self.html.title.text
        article = self.html.find("div",
                            {"class": "field field-name-body field-type-text-with-summary field-label-hidden"}).text
        publish_time = self.html.find("div", {"class": "article_meta"}).text.split('|')[0]
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def enikos(self):
        topic = self.html.title.text.split('-')[-1]
        title = self.html.title.text
        article = self.html.find("div", {"id": "articletext"}).text
        publish_time = self.html.find("div", {"class": "article-time small-6 col"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def espressonews(self):
        topic = self.html.find("div", {"class": "field-item even"}).text
        title = self.html.title.text
        article = self.html.find("div",
                            {"class": "field field-name-body field-type-text-with-summary field-label-hidden"}).text
        publish_time = self.html.find("div", {"class": "field field-name-post-date field-type-ds field-label-hidden"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def fimotro(self):
        topic = self.html.find('div', {'class': "menu-section clearfix"}).find('li', {
            'class': 'menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor current-menu-parent current-post-parent menu-item-25457'}).text
        title = self.html.title.text
        article = self.html.find('div', {'class': 'entry-content'}).text
        publish_time = str(self.html.find("meta", {"property": "article:published_time"})).split('=')[1].split()[0].replace(
            '"', '')
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def flashnews(self):
        topic = self.html.find('li', {'class': 'active'}).text
        title = self.html.title.text
        article = self.html.find("div", {"class": "article-text"}).text
        publish_time = self.html.find("div", {"id": "article-date"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def freepen(self):
        topic = self.html.find("span", {"class": "label-info"}).text
        title = self.html.title.text
        article = self.html.find("div", {"itemprop": "description articleBody"}).text
        publish_time = self.html.find("span", {"class": "time-info"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def gazzetta(self):
        topic = self.html.find("div", {"class": "breadcrumb"}).text
        title = self.html.title.text
        article = self.html.find("div", {"itemprop": "articleBody"}).text
        publish_time = self.html.find("div", {"class": "article_date"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def huffingtonpost(self):
        topic = self.html.find("span", {"class": "entrytag"}).text
        title = self.html.title.text
        article = self.html.find("div", class_="content", id="mainentrycontent").text
        publish_time = self.html.find("div", {"class": "times"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def iefimerida(self):
        topic = self.html.find("div", {"class": "info"}).text.split()[0]
        title = self.html.title.text
        article = self.html.find("div", {"class": "news-articleBody"}).text
        publish_time = self.html.find("div", {"class": "info"}).text.split()[-1]
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def in_gr(self):
        topic = self.html.title.text.split('-')[-2]
        title = self.html.title.text
        article = self.html.find("div", {"id": "intext_content_tag"}).text
        publish_time = self.html.find("p", {"class": "article-date-info"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def karfitsa(self):
        topic = self.html.find_all('span', {'itemprop': "name"})[-1].text
        title = self.html.title.text
        article = self.html.find('div', {'class': 'td-post-content td-pb-padding-side'}).text
        publish_time = self.html.find('time', {'class': 'entry-date updated td-module-date'}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def kathimerini(self):
        topic = self.html.find("span", {"class": "item-category"}).text  # self.html.title.text.split('|')[1].strip()
        title = self.html.title.text
        article = self.html.find("div", {"class": "freetext"}).text
        publish_time = self.html.find("article", {"id": "item-article"}).find("time").text.split()[0]
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def kontranews(self):
        topic = self.html.find("div", {
            "class": "field field--name-field-category field--type-entity-reference field--label-above"}).text.split(
            '\n')[-2]
        title = self.html.title.text
        article = self.html.find("div", {"property": "schema:text"}).text
        publish_time = self.html.find("span", {"property": "schema:dateCreated"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def left(self):
        topic = self.html.find("div", {"class": "view-content"}).text.split()[3]
        title = self.html.title.text
        article = self.html.find("div", {"class": "views-field-body"}).text
        publish_time = self.html.find("div", {"class": "view-content"}).text.split()[2]
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def liberal(self):
        topic = self.html.find("h3", {"class": "related_header listing_breadcrumb"}).text
        title = self.html.title.text
        article = self.html.find("div", {"itemprop": "articleBody"}).text
        publish_time = self.html.find("div", {"class": "article_date"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def lifo(self):
        topic = str(self.html.find("meta", {"itemprop": "articleSection"})).split('=')[1].split('"')[1]
        title = self.html.title.text
        article = self.html.find("div", {"itemprop": "articleBody"}).text
        publish_time = self.html.find("div", {"itemprop": "datePublished"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def madata(self):
        topic = self.html.find('article', {'id': "article-post"}).text.split('\n')[3]
        title = self.html.title.text
        article = self.html.find('article', {'id': "article-post"}).text
        publish_time = self.html.find('article', {'id': "article-post"}).text.split('\n')[4]
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def makeleio(self):
        topic = self.html.find("ul", {"class": "post-categories"}).text
        title = self.html.title.text
        article = self.html.find("div", {"class": "post-content-wrap"}).text
        publish_time = self.html.find("time", {"itemprop": "dateCreated"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def musicity(self):
        # There aren't topic and publish time
        title = self.html.title.text
        article = self.html.find("div", {"class": "itemFullText"}).text
        return {'topic': '',
                'title': title,
                'article': article,
                'publish_time': ''
                }

    def naftemporiki(self):
        try:
           topic = self.html.find("div",{"class":"Breadcrumb"}).text
        except:
              topic = ''
        title = self.html.title.text
        article = self.html.find("span", {"id": "spBody"}).text
        publish_time = self.html.find("div", {"class": "Date"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time}

    def neolaia(self):
        try:
            topic = self.html.find("li", {'class': "current"}).text
        except:
            topic = ''
        title = self.html.title.text
        article = self.html.find("div", {"class": "content"}).text
        publish_time = str(self.html.find("p", {"class": "blog-author"})).split('</span>')[-1].replace('</p>', '').strip()
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def newpost(self):
        topic = self.html.find("button", {"class": "dropdown-toggle"}).text
        title = self.html.title.text
        article = self.html.find("div", {"class": "article-body"}).text
        publish_time = self.html.find("div", {"class": "published"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def news247(self):
        topic = self.html.title.text.split('|')[-2]
        title = self.html.title.text
        article = self.html.find("div", {"itemprop": "articleBody"}).text
        publish_time = self.html.find("div", {"class": "date"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def newsbeast(self):
        topic = self.html.find("div", {"class": "article-top-meta-categories category-crumb"}).text
        title = self.html.title.text
        article = self.html.find("div", {"class": "article-content"}).text
        publish_time = self.html.find("div", {"class": "article-top-meta-date"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def newsbomb(self):
        topic = self.html.find('h4', {'class': 'story-category'}).text.replace('\n', '')
        title = self.html.title.text
        article = self.html.find('div', {'class': 'story-fulltext'}).text
        publish_time = self.html.find('span', {'class': 'day'}).text.split('\t')[-1]
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def newsit(self):
        topic = str(self.html.title).split('-')[-2].strip()
        title = self.html.title.text.replace('<title>', '').replace('</title>', '')
        article = self.html.find("div", {"id": "intext_content_tag"}).text
        publish_time = self.html.find("div", {"class": "first_info_00"}).text.split(':')[1].split('|')[0].strip()
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def nooz(self):
        topic = [i for i in self.html.find("div", {"class": "article_canvas"}).text.split('\n') if i != ''][0]
        title = self.html.title.text
        article = self.html.find("div", {"class": "article_body_text"}).text
        publish_time = self.html.find("h3", {"class": "date"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def oneman(self):
        topic = self.html.find("a", {"class": "section"}).text
        title = self.html.title.text
        article = self.html.find("div", {"class": "body"}).text
        publish_time = self.html.find("span", {"itemprop": "datePublished"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def parapolitika(self):
        topic = self.html.find("span", {"class": "sect_text artSectText"}).text
        title = self.html.title.text
        article = self.html.find("div", {"class": "articleMainContentInner"}).text
        publish_time = self.html.find("div", {"class": "articleHeader"}).find("span", {"class": "pDate"}).text.replace('\n',
                                                                                                                  '').strip().rstrip()
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def paraskhnio(self):
        topic = self.html.find('li', {'class': 'entry-category'}).text
        title = self.html.title.text
        article = self.html.find('div', {'class': 'td-post-content'}).text
        publish_time = self.html.find('time', {'class': "entry-date updated td-module-date"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def pathfinder(self):
        topic = self.html.find("div", {"class": "tags"}).text
        title = self.html.title.text
        article = self.html.find("div", {"itemprop": "articleBody"}).text
        publish_time = self.html.find("time", {"itemprop": "datePublished"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def press_gr(self):
        topic = [i for i in self.html.find('span', {'class': 'crumbs'}).text.split('\n') if i != ''][2]
        title = self.html.title.text
        article = self.html.find('div', {"itemprop": "articleBody"}).text
        publish_time = self.html.find('span', {'class': 'meta_date'}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def protagon(self):
        try:
            topic = self.html.find("a", {"class": "caeee"}).text
        except:
            try:
                topic = self.html.find("div", {"class": "get-category"}).text
            except:
                topic = ''
        title = self.html.title.text
        article = self.html.find("div", {"class": "content_space"}).text
        publish_time = self.html.find("span", {"class": "generalight uppercase"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time}

    def protothema(self):
        topic = self.html.find("h2", {"class": "ArticleCatHeading"}).text
        title = self.html.title.text
        article = self.html.find("div", {"class": "article-content"}).text
        publish_time = self.html.find("span", {"class": "time"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def real(self):
        topic = self.html.title.text.split('-')[1]
        title = self.html.title.text.split('-')[-1]
        article = self.html.find("div", {"class": "article_pure_text"}).text
        publish_time = self.html.find("div", {"class": "article-date"}).text.split("|")[0]
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def rockap(self):
        topic = self.html.find("span", {"itemprop": "title"}).text
        title = self.html.title.text
        article = self.html.find("section", {"itemprop": "articleBody"}).text
        publish_time = self.html.find('article').find('time').text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def sinavlia(self):
        topic = self.html.find("span", {"class": "entry-category"}).text
        title = self.html.title.text
        article = self.html.find("article", {"class": "entry-content"}).text
        publish_time = self.html.find("time", {"class": "entry-date published"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def tanea(self):
        topic = self.html.title.text.split('-')[1]
        title = self.html.title.text
        article = self.html.find("div", {'class': 'mainarticle__body'}).text
        publish_time = self.html.find("span", {'class': "published__time"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def thestival(self):
        topic = self.html.find("span", {"class": "NewsItemCategory"}).text
        title = self.html.title.text
        article = self.html.find("div", {"class": "ArticleFullText"}).text
        publish_time = [i for i in self.html.find("div", {"class": "ArticleInfo"}).text.split('\n') if i != ''][-1]
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def thetoc(self):
        topic = self.html.find("div", {"id": "categoryTitle"}).text
        title = self.html.title.text
        article = self.html.find("div", {"class": "articleText col-sm-9 mtd"}).text
        publish_time = self.html.find("time").text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def tovima(self):
        topic = self.html.title.text.split('-')[1].strip()
        title = self.html.title.text
        article = self.html.find("div", {"id": "intext_content_tag"}).text
        publish_time = self.html.find("div", {"class": "article_info"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def trelokouneli(self):
        topic = self.html.find("ul", {"class": "post-categories"}).text
        title = self.html.title.text
        article = self.html.find("div", {"class": "post_content"}).text
        publish_time = self.html.find("time", {"class": "entry-date published updated"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

    def zougla(self):
        topic = str(self.html.find("link", {"rel": "canonical"})).split("zougla.gr")[-1].split('/')[1]
        title = self.html.title.text
        article = self.html.find("div", {"itemprop": "articleBody"}).text
        publish_time = self.html.find("div", {"class": "top_date"}).text
        return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }
    def ert(self):
       topic='' # It's not exist,maybe in futer be replaced with tags ,which are provided
       title=self.html.title.text
       article=self.html.find("div",{"class":"td-ss-main-content"}).text
       publish_time=self.html.find("time",{"class":"entry-date updated td-module-date"}).text
       return {'topic': topic,
                'title': title,
                'article': article,
                'publish_time': publish_time
                }

       publish_time=self.html.find("time",{"class":"entry-date updated td-module-date"}).text
	
