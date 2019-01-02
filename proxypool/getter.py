from proxypool.tester import Tester
from proxypool.db import RedisClient
from proxypool.crawler import Crawler
from proxypool.setting import *
import sys
import time
import datetime


class Getter():
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()

    def is_over_threshold(self):
        """
        判断是否达到了代理池限制
        """
        if self.redis.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False

    def run(self):
        print('获取器执行开始')
        if not self.is_over_threshold():
            for callback_label in range(self.crawler.__CrawlFuncCount__):
                callback = self.crawler.__CrawlFunc__[callback_label]
                source_name = str(callback);
                # print(source_name)

                # 开始计时
                start = datetime.datetime.now()
                # 获取代理
                proxies = self.crawler.get_proxies(callback)


                # 结束计时
                end = datetime.datetime.now()

                print(source_name + " 使用代理IP, 耗时 " + str((end - start).seconds) + "秒 " + " 件数:" + str(len(proxies)))

                # 刷新屏幕
                sys.stdout.flush()
                for proxy in proxies:
                    self.redis.add(proxy)
        print('获取器执行结束')
        # 刷新屏幕
        sys.stdout.flush()
