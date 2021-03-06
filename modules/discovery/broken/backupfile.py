#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt'

import re
import sys

from net import utils
from net import request
from utils import output

class Backupfile:
	def __init__(self,agent,proxy,redirect,timeout,url,cookie):
		self.url = url 
		self.cookie = cookie
		self.check = utils.Checker()
		self.output = output.Output()
		self.request = request.Request(
			agent = agent,
			proxy = proxy,
			redirect = redirect,
			timeout = timeout
			)

	def run(self):
		info = {
		'name'        : 'Backupfile',
		'fullname'    : 'Backup files',
		'author'      : 'Momo Outaadi (M4ll0k)',
		'description' : 'Check backup files'
		}

		db = open('data/backup_file.txt','rb')
		db_files = ([x.split('\n') for x in db])
		dbfile = open('data/common_files.txt','rb')
		dbfiles = ([i.split('\n') for i in dbfile])
		
		if '--verbose' in sys.argv:
			self.output.info('Checking backup files...')	
		
		try:
			for ext in db_files:
				for file in dbfiles:
					b = ext[0].replace('[name]',file[0])
					url = self.check.path(self.url,b)
					resp = self.request.send(url,cookies=self.cookie)
					if resp.content and resp.status_code == 200:
						self.output.plus('Backup file available under: %s'%(url))
		except Exception,e:
			pass