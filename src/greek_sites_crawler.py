import argparse

from get_html import get_html

from skai import skai
from cnn import cnn
from newsbomb import newsbomb
from newsit import newsit
from newsbeast import newsbeast
from protothema import protothema
from zougla import zougla
from tovima import tovima
from dikaiologitika import dikaiologitika
from avgi import avgi
from capital import capital
from documentonews import documentonews
from efsyn import efsyn
from enikos import enikos
from huffingtonpost import huffingtonpost
from iefimerida import iefimerida
from in_gr import in_gr
from left import left
from liberal import liberal
from naftemporiki import naftemporiki
from news247 import news247
from nooz import nooz
from  protagon import protagon
from tanea import tanea
from thetoc import thetoc
from makeleio import makeleio
from contra import contra
from gazzetta import gazzetta
from alfavita import alfavita
from oneman import oneman
from pathfinder import pathfinder
from kontranews import kontranews
from parapolitika import parapolitika
from lifo import lifo
from kathimerini import kathimerini
from cerebrux import cerebrux
from fimotro import fimotro
from altsantiri import altsantiri
from madata import madata
from karfitsa import karfitsa
from paraskhnio import paraskhnio
from press_gr import press_gr
from neolaia import neolaia
from thestival import thestival
from athensvoice import athensvoice
from rockap import rockap
from avopolis import avopolis
from sinavlia import sinavlia
from musicity import musicity
from athinorama import athinorama
from clickatlife import clickatlife
from culturenow import culturenow
from espressonews import espressonews
from real import real
from trelokouneli import trelokouneli
from crashonline import crashonline
from freepen import freepen

import credits


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
site['dikaiologitika']= dikaiologitika
site['alfavita'] =alfavita
site['oneman']=oneman
site['pathfinder']=pathfinder
site['kontranews'] = kontranews
site['parapolitika']= parapolitika
site['lifo']=lifo
site['kathimerini']=kathimerini
site['cerebrux'] = cerebrux
site['fimotro']=fimotro
site['altsantiri']=altsantiri
site['madata']=madata
site['karfitsa']=karfitsa
site['paraskhnio']= paraskhnio
site['press_gr'] = press_gr
site['neolaia'] = neolaia
site['thestival'] = thestival
site['athensvoice'] = athensvoice
site['rockap']=rockap
site['avopolis']=avopolis
site['sinavlia']=sinavlia
site['musicity']=musicity
site['athinorama']=athinorama
site['clickatlife']=clickatlife
site['culturenow']=culturenow
site['espressonews']=espressonews
site['real'] = real
site['trelokouneli']=trelokouneli
site['crashonline']=crashonline
site['freepen']=freepen

def greek_sites_crawler(url):
	html = get_html(url)
	if 'cerebrux.net' in url:
		url = 'cerebrux'
	elif 'left.gr' in url:
		url='left'
	elif 'press-gr.com' in url:
		url = 'press_gr'
	else:
		url = 	url.split('.')[1]
	if url =='in':
		url = url+'_gr'
	if site.get(url,None)==None:
		print("This site dont provider yet \n")
	else:
		try:
			print( site[url](html))
			return site[url](html)
		except:
			pass

if __name__=='__main__':
	helpString = 'Sites which we can crawl: {}'.format(','.join(site))
	parser = argparse.ArgumentParser()
	parser.add_argument("-url",help=helpString,type=str)
	args = parser.parse_args()
	greek_sites_crawler(args.url)
