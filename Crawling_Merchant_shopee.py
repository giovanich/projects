from SQLite import DB
from OmniCrawler import Selenium
from datetime import datetime
from DataStructure.StringManipulator import Concatenate, Enumerate, Manipulate
import traceback
import time
import os
import datetime
class Run:
    Product_name = ""
    Product_price = 0
    Product_price_dis = 0
    Product_location = ""
    Product_sold = 0
    product_page = 0
    max_product_page = 84
    number_item = 0
    Date_Crawling = 0
    word_separator = "+"
    link = ""
    Selenium = Selenium()
    Search = "beauty"

    def Crawling(self):
        self.Selenium.link = "https://shopee.co.id/search?keyword="+Concatenate().InfuseSeparator(main=self.Search, separator=self.word_separator)+"&page="+str(self.product_page)
        self.Selenium.Load(self.Selenium.link)
        print(self.Selenium.link);input()
        while self.product_page < self.max_product_page:
            item_count = 1
            item_ordinal = self.Selenium.ExtractElements("//*[@id='main']/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div")
            print(len(item_ordinal));input()
            self.product_page += 1
            while item_count <= len(item_ordinal):
                sub_root = "//*[@id='main']/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[",str(item_count),"]"
                self.Product_location = self.Selenium.ExtractElementText("".join(["//*[@id='main']/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[",str(item_count),"]/div/a/div/div[2]/div[5]"]))
                print(self.Product_location)
                self.Product_price = int(self.Selenium.ExtractElementText("".join(["//*[@id='main']/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[",str(item_count),"]/div/a/div/div[2]/div[2]/div[1]/span[2]"])))
                print(self.Product_price)
                self.Product_price_dis = int(self.Selenium.ExtractElementText("".join([sub_root,'/div/a/div/div[2]/div[2]/div[2]/span[2]'])))
                print(self.Product_price_dis)
                self.Product_name = self.Selenium.ExtractElementText("".join(["//*[@id='main']/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[",str(item_count),"]/div/a/div/div[2]/div[1]/div"]))
                print(self.Product_name)
                check_area = self.Selenium.ExtractElements("".join([sub_root,'/div/a/div/div[2]/div[4]/div']))
                print(check_area);input()
                if check_area is 0 or check_area is None:
                    self.Product_sold = 0
                    print(self.Product_sold)
                else:
                    self.Product_sold = int(self.Selenium.ExtractElementText("".join([sub_root,'/div/a/div/div[2]/div[4]/div[3]'])).replace(' Terjual/ Bulan','').replace('.',''))
                    print(self.Product_sold)
                input()

            self.Selenium.link = "https://shopee.co.id/search?keyword="+Concatenate().InfuseSeparator(main=self.Search, separator=self.word_separator)+"&page="+str(self.product_page)
            self.Selenium.Load(self.Selenium.link)

Run().Crawling()
