#!/usr/bin/env python3
import pymongo
from pymongo import MongoClient
import datetime
client = MongoClient('localhost', 27017)
db = client.shopee_co_id


a = db.Merchant.find({'Merchant_established' : None},{'_id' : 1,'Merchant_rate' : 1,'Merchant_followers' :1})
for i in a:
    x = str(i).replace("{\'_id\': \'",'').replace("\', \'Merchant_rate\': \'",'#').replace("\', \'Merchant_followers\': \'",'#').replace("\'}",'')

    z = x.split('#')
    db.Merchant.update({'_id' : z[0]},{'$set' :{'Merchant_established' : z[1] , 'Merchant_rate' : z[2], 'Merchant_followers' : 0}})
