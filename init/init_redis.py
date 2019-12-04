# -*- coding: utf-8 -*-
import sys
import importlib
importlib.reload(sys)
from utils.db_factory.db_factory import dbfactory
import requests
import json
import logging

class RedisIt(object):
    def __init__(self, *args, **kwargs):
        self.config = kwargs.get("config", {})

    def createDB(self, db_config):
        return dbfactory.create_db(db_config=db_config)

    def db_redis(self, conf_name):
        return dbfactory.db_redis(conf_name=conf_name)

    def run(self, *args, **kwargs):
        try:
            self.data_redis()
            # self.company_redis()
            # self.boroughinfo_redis()
            # self.borough_pika()
            # self.pic_redis()
            self.data_pika()
            return self.config
        except Exception as e:
            logging.error("RedisIt", e)

    def data_redis(self):
        redis_in = self.db_redis(conf_name="redis_local_0")
        self.config.setdefault("data_redis", redis_in)


    # def company_redis(self):
    #     redis_in = self.db_redis(conf_name="sell_company")
    #     self.config.setdefault("in_redis_n", redis_in)

    # def boroughinfo_redis(self):
    #     redis_in = self.db_redis(conf_name="borough_info")
    #     self.config.setdefault("in_redis_b", redis_in)
    #
    # def borough_pika(self):
    #     redis_in = self.db_redis(conf_name="sell_borough")
    #     self.config.setdefault("borough_pika", redis_in)

    def data_pika(self):
        redis_in = self.db_redis(conf_name="codis_online_0")
        self.config.setdefault("data_pika", redis_in)