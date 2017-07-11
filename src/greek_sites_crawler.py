import argparse
from avgi import avgi
from capital import capital
from cnn import cnn
from contra import contra
from documentonews import documentonews
from efsyn import efsyn
from enikos import enikos
from gazzetta import gazzetta
from get_html import get_html
from huffingtonpost import huffingtonpost
from iefimerida import iefimerida
from in_gr import in_gr
from left import left
from liberal import liberal
from makeleio import makeleio
from naftemporiki import naftemporiki
from news247 import news247
from newsbeast import newsbeast
from newsbomb import newsbomb
from newsit import newsit
from nooz import nooz
from protagon import protagon
from protothema import protothema
from skai import skai
from tanea import tanea
from thetoc import thetoc
from tovima import tovima
from zougla import zougla

site = {}
site['skai']=skai
site['cnn']=cnn
site['newsbomb']=newsbomb
site['newsit'] = newsit
site['newsbeast'] = newsbeast
site['protothema']=protothema
site['zougla']=zougla
site['tovima']=tovima
site['avgi']= avgi
site['capital']=capital
site['documentonews']=documentonews
site['efsyn']=efsyn
site['enikos']=enikos
site['huffingtonpost']=huffingtonpost
site['iefimerida']=iefimerida
site['in_gr']=in_gr
site['left']=left
site['liberal']=liberal
site['naftemporiki']=naftemporiki
site['news247']=news247
site['nooz']=nooz
site['protagon']=protagon
site['tanea']=tanea
site['thetoc']=thetoc
site['makeleio']=makeleio
site['contra']=contra
site['gazzetta']=gazzetta


def greek_sites_crawler(url):
    html = get_html(url)
    url = url.split('.')[1]
    if url == 'in':
        url = url+'_gr'
    if site.get(url, None) == None:
        print("This site dont provider yet \n")
    else:
        print( site[url](html))
        return site[url](html)


if __name__ == '__main__':
    helpString = 'Sites which we can crawl: {}'.format(','.join(site))
    parser = argparse.ArgumentParser()
    parser.add_argument("-url", help=helpString, type=str)
    args = parser.parse_args()
    greek_sites_crawler(args.url)
