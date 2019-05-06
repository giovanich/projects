import pymongo
from pymongo import MongoClient
import datetime


class MongoDB:
    def insert_Tokopedia(self, Merchant_html_path, Merchant_name,Merchant_rate_point,Merchant_location,Merchant_stat_1_month,Merchant_established,Merchant_sold_product,Merchant_followers,Merchant_active_product,Top_Product):
        client = MongoClient('localhost', 27017)
        db = client.tokopedia
        detail = {
                    '_id' : Merchant_html_path,
                    'Merchant_name' : Merchant_name,
                    'Merchant_rate' : Merchant_rate_point,
                    'Merchant_location' : Merchant_location,
                    'Merchant_transaction_last_30_days' : Merchant_stat_1_month,
                    'Merchant_established' : Merchant_established,
                    'Merchant_sold_product' : Merchant_sold_product,
                    'Merchant_total_product' : Merchant_active_product,
                    'Merchant_followers' : Merchant_followers,
                    'Merchant_Product' : [{'Name_Product1':Top_Product[0],'Name_Product2':Top_Product[1],'Name_Product3':Top_Product[2],'Name_Product4':Top_Product[3],
                                        'Name_Product5':Top_Product[4],'Name_Product6':Top_Product[5],'Name_Product7':Top_Product[6],'Name_Product8':Top_Product[7],
                                        'Name_Product9':Top_Product[8],'Name_Product10':Top_Product[9]}],
                    'Merchant_crawlingTime' : datetime.datetime.now(),
                }
        result=db.Merchant.insert_one(detail)
    def drop_collection(self, collection_name):
        if collection_name is 'MerchantTokopedia':
            db = client.tokopedia
            db.Merchant.drop()
        elif collection_name is 'MerchantShopee':
            db = client.shopee
            db.Merchant.drop()
#db = client.shopee
