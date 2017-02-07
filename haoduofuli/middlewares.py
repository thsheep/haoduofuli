# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import json
import redis
import random
from .useragent import agents
from .cookies import init_cookie, remove_cookie, update_cookie
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from scrapy.downloadermiddlewares.retry import RetryMiddleware
import logging


logger = logging.getLogger(__name__)

class UserAgentmiddleware(UserAgentMiddleware):

    def process_request(self, request, spider):
        agent = random.choice(agents)
        request.headers["User-Agent"] = agent


class CookieMiddleware(RetryMiddleware):

    def __init__(self, settings, crawler):
        RetryMiddleware.__init__(self, settings)
        self.rconn = redis.from_url(settings['REDIS_URL'], db=1, decode_responses=True)##decode_responses设置取出的编码为str
        init_cookie(self.rconn, crawler.spider.name)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings, crawler)

    def process_request(self, request, spider):
        redisKeys = self.rconn.keys()
        while len(redisKeys) > 0:
            elem = random.choice(redisKeys)
            if spider.name + ':Cookies' in elem:
                cookie = json.loads(self.rconn.get(elem))
                request.cookies = cookie
                request.meta["accountText"] = elem.split("Cookies:")[-1]
                break
            #else:
                #redisKeys.remove(elem)

    #def process_response(self, request, response, spider):

         #"""
         #下面的我删了，各位小伙伴可以尝试以下完成后面的工作

         #你需要在这个位置判断cookie是否失效

         #然后进行相应的操作，比如更新cookie  删除不能用的账号

         #写不出也没关系，不影响程序正常使用，

         #"""



