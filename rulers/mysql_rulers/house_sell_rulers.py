# -*- coding: utf-8 -*-


#所有城市房源
def all_count():
    sql="""
    select count(*) cnts from house_sell   
    """
    #print(sql)
    return sql

#所有发布房源有小区id的个数
def borough_all_house():
    sql = f"""select count(id),borough_id from house_sell where `status`=1 group by borough_id"""
    return sql