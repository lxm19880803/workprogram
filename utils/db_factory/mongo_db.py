# -*- coding: UTF-8 -*-
from pymongo import MongoClient
import logging
import contextlib
from configs.read_parser import ParserReader
from configs.const import getConfigType,get_db

class MongoDB(object):
    def __init__(self, *args, **kwargs):
        self.conf_name = kwargs.get("conf_name")

    __pool = {}
    @contextlib.contextmanager
    def get_mongo_conn(self, *args, **kwargs):
        city_jp = kwargs.get("city_jp")
        conf_name = self.conf_name
        type = conf_name.split("_")[2]
        pre_conf = conf_name.replace(f"_{type}", "")
        conf_type = getConfigType(city=city_jp, type=type)
        conf_name = f"{pre_conf}_{conf_type}"
        conn_pool = MongoDB.__pool.get(conf_name)
        db_name = get_db(type=conf_type, city=city_jp)
        if not conn_pool:
            # 获取主从连接
            # print(conf_name)
            conf = ParserReader(conf_name=conf_name).get_db_config()
            url = ""
            host = conf.get("host")
            port = int(conf.get("port"))
            user = conf.get("username", "")
            passwd = conf.get("password", "")
            maxPoolSize = conf.get("maxPoolSize", 10) or 10
            maxIdleTimeMS = conf.get("maxIdleTimeMS", 40) or 40
            # print(passwd)
            if not url:
                if user and passwd:
                    url = f"mongodb://{user}:{passwd}@{host}:{port}"
                else:
                    url = f"mongodb://{host}:{port}"

            print(url,maxIdleTimeMS,maxPoolSize)


            conn_pool = MongoClient(url, maxPoolSize=maxPoolSize, maxIdleTimeMS=maxIdleTimeMS)
            MongoDB.__pool.setdefault(conf_name, conn_pool)
        #print(conn_pool)
        try:
            client = conn_pool.get_database(db_name)
            yield client
        except Exception as e:
            logging.error('ERROR', e)
        finally:
            # conn.close()
            # conn.close_cursor()
            pass

    # def getMongoConn(self, *args, **kwargs):
    #     link_type = kwargs.get("link_type", 'default')
    #     conf = self.conf.get(link_type)
    #     connect_name = link_type + self.conf_name
    #     conn = MongoDB.__pool.get(connect_name)
    #
    #     city = kwargs.get("city")
    #     db_name = kwargs.get("db_name")
    #     db_name = db_name if db_name else get_db(type=self.conf_name, city=city)
    #     if not conn:
    #         uri = conf.get("url")
    #         host = conf.get("host")
    #         port = conf.get("port")
    #         user = conf.get("username", "")
    #         passwd = conf.get("password", "")
    #         maxPoolSize = conf.get("maxPoolSize", 50)
    #         maxIdleTimeMS = conf.get("maxIdleTimeMS", 10)
    #         if not uri:
    #             if user and passwd:
    #                 uri = f"mongodb://{user}:{passwd}@{host}:{port}"
    #             else:
    #                 uri = f"mongodb://{host}:{port}"
    #         conn = MongoClient(uri,maxPoolSize=maxPoolSize,maxIdleTimeMS=maxIdleTimeMS)
    #         MongoDB.__pool.setdefault(connect_name, conn)
    #     try:
    #         client = conn.get_database(db_name)
    #         yield client
    #     except Exception as e:
    #         logging.error('ERROR', e)
    #     finally:
    #         # conn.close()
    #         # conn.close_cursor()
    #         pass





if __name__ == '__main__':
    print(MongoDB(conf_name="mongo_online_borough").get_mongo_conn(city_jp='bj'))





