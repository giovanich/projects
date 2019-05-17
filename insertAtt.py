import pymongo
from pymongo import MongoClient
import datetime
from MongoShopee import MongoDB
from pprint import pprint
client = MongoClient('localhost', 27017)
db = client.shopee_co_id


#product_info ={
#    "namaProduct": 'Terserah apake',
#    "jenisProduct": 'Jenis Terserah apake'}
#
#db.MerchantTokped.update({'Merchant_html_path': 'https://www.tokopedia.com/nurulagency'  }, { "$addToSet": { "ProductInfo3": product_info } })
#i =0
#while i !=18:#
#    db.Merchant.update({'status': 2},{'$set' :{'status': 1}})
#    i+=1
#result = db.Merchant.find({ "_id" : "https://shopee.co.id/fygalery" ,'ProductInfo' : {'$elemMatch':{'hargaAsli':'4444444444444'}}},{'id':0})
#for i in result:
#    print(str(i))
#https://shopee.co.id/herbal_idr

#MongoDB().checkMerchantToCrawl()
#result = db.MerchantTokped.find({'status':1},{'$and' :[{'Merchant_followers' :{'$exists' : True}},{'Merchant_followers' :{'$type' : 2}}]},).collation({'locale': "en_US", 'numericOrdering': True}).sort('Merchant_followers', pymongo.DESCENDING)
#for i in result :
#    print(str(i))

# JANGAN DIHAPUS
# >> for Parse to INT [Use on Mongo Console]
# db.Merchant.find({Merchant_followers :{$exists: true}}).forEach(function(obj){obj.Merchant_followers = new NumberInt(obj.Merchant_followers); db.Merchant.save(obj); } );
# >> for Parse to STRING [Use on Mongo Console]
# db.MerchantTokped.find({Merchant_product :{$exists: true}}).forEach(function(obj){obj.Merchant_product =  "" + obj.Merchant_product; db.Merchant.save(obj); } );

from OmniCrawler import Selenium
from datetime import datetime
from DataStructure.StringManipulator import Concatenate, Enumerate, Manipulate
import traceback
import time
import os
import datetime


class Run:
    Merchant_html_path = ''
    Merchant_name = ""
    Merchant_rate = ""
    Merchant_product = 0
    Merchant_established = ""
    Merchant_followers = 0
    Merchant_location = ''
    product_page = 0
    max_product_page = 100
    number_item = 0
    Date_Crawling = 0
    word_separator = "+"
    link = ""
    Selenium = Selenium()
    Search = "beauty"
    page_ordinal = 100
    def Crawling(self):
            self.link = "https://shopee.co.id/herbal_idr"
            try:
                self.Selenium.Load(self.link)
                time.sleep(4)
                if MongoDB().checkMerchant(self.Selenium.link) is not None :
                    self.Merchant_name = self.Selenium.ExtractElementText("//*[@id='main']/div/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div[3]/div[1]/div/h1")
                    self.Merchant_rate = self.Selenium.ExtractElementText("//*[@id='main']/div/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[6]/div[2]/div[2]")
                    self.Merchant_product = self.Selenium.ExtractElementText("//*[@id='main']/div/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/div[2]")
                    self.Merchant_established = self.Selenium.ExtractElementText("//*[@id='main']/div/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[7]/div[2]/div[2]")
                    self.Merchant_followers =self.Selenium.ExtractElementText("//*[@id='main']/div/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[5]/div[2]/div[2]")
                    self.Merchant_location = self.Selenium.ExtractElementText("//*[@id='main']/div/div[2]/div[2]/div[2]/div/div[3]/div[3]/div[2]/div/div[2]/div/div[1]/div/a/div/div[2]/div[5]")
                    detail = {
                                'Merchant_name' : self.Merchant_name,
                                'Merchant_rate' : self.Merchant_rate,
                                'Merchant_location' : self.Merchant_location,
                                'Merchant_established' : self.Merchant_established,
                                'Merchant_product' : self.Merchant_product,
                                'Merchant_followers' : self.Merchant_followers,
                                'Merchant_crawlingTime' : datetime.datetime.now(),
                                'status' : 1
                            }
                    db.Merchant.update(
                          {"_id": self.link},
                          { "$set": detail }
                        )
            except Exception as e:
                print(e)
                self.Selenium.Refresh()
                self.Crawling()


Run().Crawling()
