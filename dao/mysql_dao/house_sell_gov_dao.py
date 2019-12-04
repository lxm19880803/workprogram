# -*- coding: utf-8 -*-
from utils.db_base.base_mysql import BaseMysql
class HouseSellGovDao(BaseMysql):
    def __init__(self, *args, **kwargs):
        super().__init__(conf_name=kwargs.get("conf_name","mysql_online_sell-old"))





if __name__ == '__main__':

    sql = f"select * from house_sell_gov limit 10"
    HouseSellGovDao().search_sql(sql=sql,city_jp='bj')




