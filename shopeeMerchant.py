from MongoShopee import MongoDB
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
        while self.product_page == 0 or (self.product_page < self.page_ordinal and self.product_page < self.max_product_page):
            self.Selenium.link = "https://shopee.co.id/Kecantikan-cat.14840?page="+str(self.product_page)
            #"https://shopee.co.id/search?keyword="+Concatenate().InfuseSeparator(main=self.Search, separator=self.word_separator)+"&page="+str(self.product_page)
            self.Selenium.Load(self.Selenium.link)
            time.sleep(4)
            self.page_ordinal = int(self.Selenium.ExtractElementText("//*[@id='main']/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/div[2]/div/span[2]"))
            self.product_page+=1
            item_count = 0
            print('item :'+str(item_count))
            item_ordinal = self.Selenium.ExtractElements("//*[@id='main']/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[2]/div")
            print(len(item_ordinal))
            while item_count <= len(item_ordinal):
                item_count +=1
                if item_count <11:
                    product_link = self.Selenium.ExtractElementAttribute('href',''.join(["//*[@id='main']/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[2]/div["+str(item_count)+"]/div/a"]))
                    self.Merchant_location = self.Selenium.ExtractElementText("//*[@id='main']/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[2]/div["+str(item_count)+"]/div/a/div/div[2]/div[5]")
                elif item_count<21:
                    self.Selenium.scrollDown(3)
                    product_link = self.Selenium.ExtractElementAttribute('href',''.join(["//*[@id='main']/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[2]/div["+str(item_count)+"]/div/a"]))
                    self.Merchant_location = self.Selenium.ExtractElementText("//*[@id='main']/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[2]/div["+str(item_count)+"]/div/a/div/div[2]/div[5]")
                elif item_count<31:
                    self.Selenium.scrollDown(4)
                    product_link = self.Selenium.ExtractElementAttribute('href',''.join(["//*[@id='main']/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[2]/div["+str(item_count)+"]/div/a"]))
                    self.Merchant_location = self.Selenium.ExtractElementText("//*[@id='main']/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[2]/div["+str(item_count)+"]/div/a/div/div[2]/div[5]")
                elif item_count<41:
                    self.Selenium.scrollDown(5)
                    product_link = self.Selenium.ExtractElementAttribute('href',''.join(["//*[@id='main']/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[2]/div["+str(item_count)+"]/div/a"]))
                    self.Merchant_location = self.Selenium.ExtractElementText("//*[@id='main']/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[2]/div["+str(item_count)+"]/div/a/div/div[2]/div[5]")
                elif item_count<51:
                    self.Selenium.scrollDown(6)
                    product_link = self.Selenium.ExtractElementAttribute('href',''.join(["//*[@id='main']/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[2]/div["+str(item_count)+"]/div/a"]))
                    self.Merchant_location = self.Selenium.ExtractElementText("//*[@id='main']/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[2]/div["+str(item_count)+"]/div/a/div/div[2]/div[5]")
                else:
                    self.Selenium.scrollUp(3)
                print('item :'+str(item_count))
                if product_link is not None:
                    #print(2)
                    self.Selenium.Load(product_link)
                    #print(3)
                    time.sleep(3)
                    checkformat = len(self.Selenium.ExtractElements("//*[@id='main']/div/div[2]/div[2]/div[2]/div[3]/div"))
                    if checkformat == 3:
                        self.Merchant_html_path = self.Selenium.ExtractElementAttribute('href',"//*[@id='main']/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div[3]/a")
                        checkformat = 0
                        #print(4)
                    elif checkformat == 2:
                        checkformat = 0
                        self.Merchant_html_path = self.Selenium.ExtractElementAttribute('href',"//*[@id='main']/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[3]/a")
                        #print(5)
                    else :
                        print(product_link)

                    if MongoDB().checkMerchant(self.Merchant_html_path) is None :
                        #print(6)
                        self.Selenium.Load(self.Merchant_html_path)
                        #print(7)
                        time.sleep(3)
                        #print(8)
                        self.Merchant_name = self.Selenium.ExtractElementText("//*[@id='main']/div/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div[3]/div[1]/div/h1")
                        #print(9)
                        self.Merchant_rate = self.Selenium.ExtractElementText("//*[@id='main']/div/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[6]/div[2]/div[2]")
                        #print(10)
                        self.Merchant_product = self.Selenium.ExtractElementText("//*[@id='main']/div/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/div[2]")
                        #print(11)
                        self.Merchant_established = self.Selenium.ExtractElementText("//*[@id='main']/div/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[7]/div[2]/div[2]")
                        #print(12)                                                     //*[@id="main"]/div/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div[3]/div[1]
                        self.Merchant_followers =self.Selenium.ExtractElementText("//*[@id='main']/div/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[5]/div[2]/div[2]")
                        #print(13)
                        self.Selenium.BackPage()
                        #print(14)

                        try:

                            MongoDB().insert_Shopee(self.Merchant_html_path, self.Merchant_name, self.Merchant_rate, self.Merchant_product, self.Merchant_established, self.Merchant_followers, self.Merchant_location)
                            #print(15)
                            self.Merchant_html_path = ''
                            self.Merchant_name = ""
                            self.Merchant_rate = ""
                            self.Merchant_product = 0
                            self.Merchant_established = ""
                            self.Merchant_followers = 0
                            self.Merchant_location = ''
                        except Exception as e:
                            print("skip")
                    #self.Selenium.clear_cache()
                    self.Selenium.BackPage();time.sleep(2)

try:
    Run().Crawling()
except Exception as e:
    print(Run().product_page)
    Run().Crawling()
