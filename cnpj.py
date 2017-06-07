#lfa

from pprint import pprint 
import requests
import json


class Cnpj(object):

	def __init__(self):
		pass

	def headers(self):
		return {
			'Content-Type': 'application/json',
			'Accept': 'application/json'
		}

	def send(self, cnpj):
		try:
			cnpj = cnpj.replace( "-", "" ).replace( ".", "" ).replace( "/", "" )
			url = 'http://receitaws.com.br/v1/cnpj/%s' %(cnpj)
			response = requests.get(url, headers=self.headers())
			return json.loads(response.content.decode('utf-8'))
		except Exception as error:
			raise
    

cnpj = Cnpj().send('27.865.757/0001-02')
pprint (cnpj)