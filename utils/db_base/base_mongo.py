#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.db_factory.db_factory import dbfactory
import pandas as pd


class BaseMongo(object):
    def __init__(self, *args, **kwargs):

        self.conn = dbfactory.create_db(conf_name=kwargs.get("conf_name"), db_type="db_mongo")
        self.table=kwargs.get('table')

    def find_mongo(self, *args, **kwargs):
        city_jp = kwargs.get("city_jp")
        find=kwargs.get("find",{})
        fields=kwargs.get("fields",{})
        with self.conn.get_mongo_conn(city_jp=city_jp) as client:
            table=client.get_collection(self.table).find(find,fields)
            df=None
            if table:
                print(table)
                df=pd.DataFrame(list(table))
            return df






if __name__ == '__main__':
    BaseMongo(conf_name="mongo_local_borough",table="borough_online").find_mongo(city_jp="ruyang")
