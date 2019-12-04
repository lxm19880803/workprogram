# -*- coding: UTF-8 -*-
import pymysql
import contextlib
import logging
from DBUtils.PooledDB import PooledDB
from configs.read_parser import ParserReader
from configs.const import getConfigType,get_db

class MysqlDB(object):
    def __init__(self, *args, **kwargs):
        self.conf_name = kwargs.get("conf_name")


    __pool = {}
    @contextlib.contextmanager
    def get_conn(self, *args, **kwargs):
        city_jp = kwargs.get("city_jp")
        conf_name=self.conf_name
        type=conf_name.split("_")[2]
        pre_conf=conf_name.replace(f"_{type}","")
        conf_type = getConfigType(city=city_jp, type=type)
        conf_name=f"{pre_conf}_{conf_type}"
        conn_pool = MysqlDB.__pool.get(conf_name)
        db_name = get_db(type=conf_type, city=city_jp)
        if conn_pool:
            pass
        else:
            # 获取主从连接
            #print(conf_name)
            conf = ParserReader(conf_name=conf_name).get_db_config()

            #print(conf)
            host = conf.get("host")
            port = int(conf.get("port"))
            user = conf.get("username")
            passwd = conf.get("password")
            mincached = int(conf.get("mincached",1) or 1)
            maxcached = int(conf.get("maxcached",3) or 3)
            maxconnections = int(conf.get("maxconnections",10) or 10)
            #print(host,port,user,passwd,mincached,maxcached,maxconnections)
            conn_pool = PooledDB(creator=pymysql,blocking=True, host=host, port=port, user=user,mincached=mincached, maxcached=maxcached, maxconnections=maxconnections, password=passwd, charset="utf8")
            MysqlDB.__pool.setdefault(conf_name, conn_pool)
        conn = conn_pool.connection()
        conn._con._con.select_db(db_name)
        try:
            yield conn
            # conn.commit()
        except Exception as e:
            #conn.rollback()
            logging.error(e)
        finally:
            conn.close()



if __name__ == '__main__':
    MysqlDB(conf_name="mysql_online_sell-old").get_mongo_conn(city_jp='bj')


