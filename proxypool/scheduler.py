import time
from multiprocessing import Process
from proxypool.api import app
from proxypool.getter import Getter
from proxypool.tester import Tester
from proxypool.db import RedisClient
from proxypool.setting import *

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


class Scheduler():
    def schedule_tester(self, cycle=TESTER_CYCLE):
        """
        定时测试代理
        """
        tester = Tester()
        while True:
            print('[测试]开始运行')
            tester.run()
            print("休眠")
            sys.stdout.flush()
            #休眠(单位秒)
            time.sleep(cycle)
    
    def schedule_getter(self, cycle=GETTER_CYCLE):
        """
        定时获取代理
        """
        getter = Getter()
        while True:
            print('开始抓取代理')
            getter.run()
            print('结束抓取代理')
            sys.stdout.flush()
            time.sleep(cycle)

    def schedule_api(self):
        """
        开启API
        """
        print("开启API")
        sys.stdout.flush()
        app.run(API_HOST, API_PORT)
    
    def run(self):
        print('代理池开始运行')
        
        if TESTER_ENABLED:
            print('计划_测试')
            tester_process = Process(target=self.schedule_tester)
            tester_process.start()
            self.schedule_tester()
        
        if GETTER_ENABLED:
            print('计划_获取')
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()
        
        if API_ENABLED:
            api_process = Process(target=self.schedule_api)
            api_process.start()
        #app.run(API_HOST, API_PORT)