#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import os
import utils
from time import time
from pytube import YouTube

def run(string, entities):
	"""Call a url to activate a bot in github"""

	# db = utils.db()['db']
	# query = utils.db()['query']
	# operations = utils.db()['operations']
	# apikey = utils.config('api_key')
	# playlistid = utils.config('playlist_id')
	# https://developers.google.com/youtube/v3/docs/playlistItems/list
	# url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId=' + playlistid + '&key=' + apikey
	nombrebot = ''
	
	for item in entities:
		if item['entity'] == 'nuevobot':
			nombrebot = item['sourceText'].lower()
			
	# url = 'https://youtochipizarron.herokuapp.com/entrenar' + nombrebot
	
	url = 'https://youtochibotas.herokuapp.com/v1/api/redisroomallcards/miembrosfamiliaveracruz-cards' 
	
	utils.output('inter', 'checking', utils.translate('checking',{
		'website_name': url
	}))
	# call the url to create a github bot branch/repository
	try:
		r = utils.http('GET', url)

		# In case there is a problem like wrong settings
		if 'error' in r.json():
			error = r.json()['error']['errors'][0]
			return utils.output('settings_error', 'settings_error', utils.translate('settings_errors', {
				'reason': error['reason'],
				'message': error['message']
			}))


		items = r.json()['rooms']


	except requests.exceptions.RequestException as e:
		return utils.output('request_error', 'request_error', utils.translate('request_errors'))


	# Will synchronize the content (because "end" type) if synchronization enabled
	return utils.output('end', 'success', utils.translate('success', {
	  'nuevobot': nombrebot
	}))
