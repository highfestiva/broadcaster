from collections import defaultdict
from multiprocessing import Queue
from queue import Empty
from time import time

channels = defaultdict(dict)
timeout = 3*60

def cleanup():
	'''Kills dead listeners.'''
	global channels
	for listeners in channels.values():
		for l,t in list(listeners.items()):
			if time()-t > timeout:
				del listeners[l]

def listen(channel):
	global channels
	listeners = channels[channel]
	q = Queue()
	while True:
		try:
			listeners[q] = time()
			data = q.get(timeout=60)
			yield data
		except Empty:
			pass

def publish(channel, data):
	global channels
	cleanup()
	listeners = channels[channel]
	for q in list(listeners.keys()):
		q.put(data)
