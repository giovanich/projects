import pymongo
from pymongo import MongoClient
import datetime
client = MongoClient('localhost', 27017)
db = client.shopee_co_id


class MongoDB:
    def insert_Shopee(self,Merchant_html_path, Merchant_name, Merchant_rate, Merchant_product, Merchant_established, Merchant_followers, Merchant_location ):
        detail = {
                    '_id' : Merchant_html_path,
                    'Merchant_name' : Merchant_name,
                    'Merchant_rate' : Merchant_rate,
                    'Merchant_location' : Merchant_location,
                    'Merchant_established' : Merchant_established,
                    'Merchant_product' : Merchant_product,
                    'Merchant_followers' : Merchant_followers,
                    'Merchant_crawlingTime' : datetime.datetime.now(),
                    'status' : 1
                }
        result=db.Merchant.insert_one(detail)
    def checkMerchant(self, Merchant_html_path):
        result= db.Merchant.find({'_id' : Merchant_html_path},{'_id':1})
        for i in result:
            return str(i)

    def updateStatus(self, x):
            db.Merchant.update(
                  {"_id": x},
                  { "$set": {"status": 2} }
                )
    def updateStatusEnd(self, x):
            db.Merchant.update(
                  {"_id": x},
                  { "$set": {"status": 0} }
                )
    def checkMerchantToCrawl(self):
        #print("start")
        a = ''
        check = db.Merchant.find({'status':2},{'_id':1}).limit(1).collation({'locale': "en_US", 'numericOrdering': True}).sort('Merchant_followers', pymongo.DESCENDING)
        count = db.Merchant.find({'status':2},{'_id':1}).limit(1).collation({'locale': "en_US", 'numericOrdering': True}).sort('Merchant_followers', pymongo.DESCENDING).count()
        #print(count);input()
        if count == 1:
            for k in check:
                a = str(k).replace('{\'_id\': \'','').replace('\'}','')
                #print("nilai "+a)
        else:
            result = db.Merchant.find({'status':1},{'_id':1}).limit(1).collation({'locale': "en_US", 'numericOrdering': True}).sort('Merchant_followers', pymongo.DESCENDING)
            for j in result:
                a = str(j).replace('{\'_id\': \'','').replace('\'}','')

        return str(a)

    def insertProduct(self, idProduct, merchant_link, namaProduct, jumlahTerjual, hargaAsli, hargaDiskon, hargaRangeAtas, hargaRangeBawah, hargaDisRangeAtas, hargaDisRangeBawah):
        product_info ={"idProduct":idProduct,
            "namaProduct":namaProduct,
            "jumlahTerjual":jumlahTerjual,
            "hargaAsli":hargaAsli,
            "hargaDiskon":hargaDiskon,
            "hargaRangeAtas":hargaRangeAtas,
            "hargaRangeBawah":hargaRangeBawah,
            "hargaDisRangeAtas":hargaDisRangeAtas,
            "hargaDisRangeBawah":hargaDisRangeBawah}
        db.Merchant.update({'_id': merchant_link }, { "$addToSet": { "ProductInfo": product_info } })

    def setStatus(self,Merchant_link):
        db.Merchant.update({'_id': Merchant_link},{'$set':{'status':2}})

    def checkProduct(self, merchant_link, idProduct):

        result = db.Merchant.find({ "_id" : merchant_link ,'ProductInfo' : {'$elemMatch':{'idProduct':idProduct}}},{'_id':1})
        for i in result:
            return str(i)
    def countMerchant(self):
        return db.Merchant.find({'status':1}).count()

    def writeLog(self,Merchant_link, page_product):
        check = db.Log.find({'_id' : Merchant_link}).count()
        #print(count);input()
        if check == 1:
            db.Log.update({'_id' : Merchant_link},{'$set' : {'Product_page' : page_product}})
        else:
            db.Log.insert({'_id' : Merchant_link,'Product_page' : page_product})


    def checkLastCrawling(self,Merchant_link):
        check = db.Log.find().count()
        if check == 0:
            db.Log.insert({'_id': Merchant_link, 'Product_page':0})
            return None
        else:
            searchPage = db.Log.find({'_id' : Merchant_link},{'_id':0, 'Product_page':1 })
            for i in searchPage:
                b = str(i)
                return int(b.replace('{\'Product_page\': ','').replace('}',''))
    #def parseIntAtt(self):
    #    db.Merchant.find({Merchant_followers :{$exists: true}}).forEach(function(obj){obj.Merchant_followers = new NumberInt(obj.Merchant_followers); db.Merchant.save(obj); } );
    #    db.Merchant.find({Merchant_product :{$exists: true}}).forEach(function(obj){obj.Merchant_product = new NumberInt(obj.Merchant_followers); db.Merchant.save(obj); } );
