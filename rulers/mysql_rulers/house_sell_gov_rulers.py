# -*- coding: utf-8 -*-


#所有城市房源
def all_count():
    sql="""
    select count(*) cnts from house_sell_gov   
    """
    return sql


def off_type(filter):

    sql=f"""
        select source_url from house_sell_gov where {filter}
"""
    return sql