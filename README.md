# Greek sites crawler
---

It's a simple *Python3* script in which the user put the url of the site which want and take as return a *json* in this form,
```python
{'topic':topic,
    'title':title,
        'article':article,
            'publish_time':publish_time
            }
```
The program is already support 60 greek site and I believe in the future this number will increase.
*The list of the sites*,
- alfavita
- altsantiri
- athensvoice
 - athinorama
  - avgi
  - avopolis
  - capital
  - cerebrux
 - clickatlife
 - cnn
 - contra
 - crashonline
 - credits
 - culturenow
 - dikaiologitika
 - documentonews
 - efsyn
 - enikos
 - espressonews
- fimotro
 - flashnews
 - freepen
 - gazzetta
 - huffingtonpost
- iefimerida
- in_gr(in.gr)
 - karfitsa
  - kathimerini
 - kontranews
 - left
  - liberal
  - lifo
  - madata
  - makeleio
  - musicity
   - naftemporiki
  - neolaia
  - newpost
 - news247
 - newsbeast
 - newsbomb
 - newsit
 - nooz
 - oneman
 - parapolitika
 - paraskhnio
 - pathfinder
 - press_gr(press-gr)
 - protagon
 - protothema
 - real
 - rockap
 - sinavlia
 - skai
 - tanea
 - thestival
 - thetoc
 - tovima
 - trelokouneli,etc
 
---
## Dependencies
Only you need to have is [Python3](https://www.python.org/downloads/) and the [BeautfulSoup](https://pypi.python.org/pypi/beautifulsoup4)

---
## How to install it
---
Clone the repo and then run in folder greek_sites_crawler

```bash
python3 setup.py install
```
## How to run it
Go to the folder where the script is and execute the below scrip
```python
from greek_sites_crawler import greek_sites_crawler as gr
data = gr(<url>)
data.get.data()
{'topic':topic,
          'title':title,
                       'article':article,
					'publish_time':publish_time
}
	'
```

 
&copy; Serepas Filippas 20017
<mailto:serepasf@yahoo.gr>


