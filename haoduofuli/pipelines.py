# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
import datetime

class HaoduofuliPipeline(object):

    def __init__(self):
        Client = MongoClient('mongodb://haoduofuli:haoduofuli123@103.200.97.19:19942/haoduofuli')
        db = Client['haoduofuli']
        self.save = db['haoduofuli']
    def process_item(self, item, spider):
        url = item['url']
        category = item['category']
        title = item['title']
        imgurl = item['imgurl']
        yunlink = item['yunlink']
        password = item['password']
        ip = item['ip']
        post = {
            '_id': title,
            '类型': category,
            '图片地址': imgurl,
            '百度云链接': yunlink,
            '百度云密码': password,
            '执行任务的服务器': ip,
            '网页地址': url,
            '存储时间': datetime.datetime.now()
        }
        self.save.insert_one(post)

        return item
