# -*- coding: utf-8 -*-

from utils.db_base.base_mongo import BaseMongo
class BoroughDao(BaseMongo):
    def __init__(self, *args, **kwargs):
        super().__init__(conf_name=kwargs.get("conf_name","mongo_local_borough"),table=kwargs.get("table_name","borough_online"))






if __name__ == '__main__':

    print(BoroughDao().find_mongo(city_jp='ruyang'))
