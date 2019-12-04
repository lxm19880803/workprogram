# -*- coding: utf-8 -*-
from dao.mysql_dao.house_sell_gov_dao import HouseSellGovDao as HSGDao
from rulers.mysql_rulers import house_sell_gov_rulers as HSGRuler
from init.init_redis import RedisIt
import sys

class HouseSellGov(object):

    def __init__(self,*args,**kwargs):
        self.redis_config=RedisIt().run()



    #某城市总数
    def all_count(self,*args,**kwargs):
        city_jp=kwargs.get("city_jp")
        sql = HSGRuler.all_count()
        df=HSGDao().search_sql(sql=sql,city_jp=city_jp)
        return df


    def off_type(self,*args,**kwargs):
        filter=kwargs.get('filter','')
        if filter:
            city_jp = kwargs.get("city_jp")
            sql = HSGRuler.off_type(filter=filter)
            df=HSGDao().search_sql(sql=sql,city_jp=city_jp)
            print(df)
            source_urls=df['source_url'].tolist()
            data_redis=self.redis_config.get('data_redis')
            for source_url in source_urls:
                print(source_url)
                pass
                #data_redis.lpush(f"{city_jp}_delete", source_url)
            print(f"{city_jp}下架总数为{len(source_urls)}")


if __name__ == '__main__':

    #print(HouseSellGov().all_count(city_jp="bj"))

    HouseSellGov().off_type(filter="status=1 and source_name='heyuan/Fang'",city_jp='heyuan')


