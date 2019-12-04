# -*- coding: utf-8 -*-
from utils.db_base.base_mysql import BaseMysql
from utils.db_base.base_mongo import BaseMongo
class BaseDao(BaseMysql):
    def __init__(self, *args, **kwargs):

        super().__init__(conf_name=kwargs.get("conf_name","mysql_online_sell-old"))





if __name__ == '__main__':
    pass