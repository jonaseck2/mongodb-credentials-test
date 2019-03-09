#!/usr/bin/python -u
# -*- coding: utf-8 -*-
from pymongo import MongoClient, database
import os

config = {
  'mongodb': {
    'host': 'localhost',
    'port': 27017,
    'connect': True,
    'username': 'guest',
    'password': 'guest',
    'replicaSet': 'rs0',
    'uri': 'mongodb://localhost',
  },
  'database': {
    'name': 'test_database',
    }
  }

for section in config:
    for key,value in config[section].items():
        env = os.getenv(section.upper() + '_' + key.upper())
        if env:
            print("%s_%s=\"%s\" as %s" % (section.upper(), key.upper(), env, type(value)))
            config[section][key] = type(value)(env)

config['mongodb']['host'] = config['mongodb']['host'].split(',')
uri = config['mongodb'].pop('uri')

client = MongoClient(uri)
db = client.get_database(**config['database'])
print(" [x] Connected using uri=%s" % uri)
client.close()

client = MongoClient(**config['mongodb'])
print(" [x] Connected using %r" % config['mongodb'])

db = client.get_database(**config['database'])
print(" [x] Connected using uri=%s" % uri)
client.close()