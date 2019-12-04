# -*- coding: utf-8 -*-
from dao.mysql_dao.house_sell_dao import HouseSellDao as HSDao
from rulers.mysql_rulers import house_sell_rulers as HSRuler
import sys

class HouseSell(object):

    def __init__(self,*args,**kwargs):
        pass



    #某城市总数
    def all_count(self,*args,**kwargs):
        city_jp=kwargs.get("city_jp")
        sql = HSRuler.all_count()
        df=HSDao().search_sql(sql=sql,city_jp=city_jp)
        return df


    def borough_id_counts(self,*args,**kwargs):
        city_jp = kwargs.get("city_jp")
        sql = HSRuler.borough_all_house()
        df = HSDao().search_sql(sql=sql, city_jp=city_jp)
        return df





if __name__ == '__main__':

    print(HouseSell().borough_id_counts(city_jp='bj'))



