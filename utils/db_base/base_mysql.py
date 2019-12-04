#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.db_factory.db_factory import dbfactory
import pandas as pd


class BaseMysql(object):
    def __init__(self, *args, **kwargs):

        self.conn = dbfactory.create_db(conf_name=kwargs.get("conf_name"), db_type="db_mysql")


    def search_sql(self, *args, **kwargs):
        city_jp = kwargs.get("city_jp")
        sql = kwargs.get("sql")
        print(sql)
        if not sql:
            return None
        with self.conn.get_conn(city_jp=city_jp) as conn:
            try:
                df=pd.read_sql_query(sql=sql,con=conn)
                return df
            except Exception as e:
                print(e)
                print(sql)
                return None




if __name__ == '__main__':
    bm=BaseMysql(conf_name="mysql_online_sell-old").search_sql(city_jp="bj",sql = f"select * from house_sell_gov limit 10")
    print(bm)

