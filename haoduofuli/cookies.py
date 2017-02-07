import requests
import json
import redis
import logging
from .settings import REDIS_URL

logger = logging.getLogger(__name__)

reds = redis.Redis.from_url(REDIS_URL, db=2, decode_responses=True)
login_url = 'http://haoduofuli.pw/wp-login.php'

##获取Cookie
def get_cookie(account, password):
    s = requests.Session()
    payload = {
        'log': account,
        'pwd': password,
        'rememberme': "forever",
        'wp-submit': "登录",
        'redirect_to': "http://http://www.haoduofuli.pw/wp-admin/",
        'testcookie': "1"
    }
    response = s.post(login_url, data=payload)
    cookies = response.cookies.get_dict()
    logger.warning("获取Cookie成功！（账号为:%s）" % account)
    return json.dumps(cookies)


def init_cookie(red, spidername):
    redkeys = reds.keys()
    for user in redkeys:
        password = reds.get(user)
        if red.get("%s:Cookies:%s--%s" % (spidername, user, password)) is None:
            cookie = get_cookie(user, password)
            red.set("%s:Cookies:%s--%s"% (spidername, user, password), cookie)


def update_cookie(red, accountText, spidername):
    red = redis.Redis()
    pass

def remove_cookie(red, spidername, accountText):
    #red = redis.Redis()
    red.delete("%s :Cookies: %s" % (spidername, accountText))






    pass

#if __name__ == '__main__':
