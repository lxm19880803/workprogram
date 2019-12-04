# -*- coding: utf-8 -*-
from dao.mongo_dao.borough_dao import BoroughDao as BDao
from rulers.mongo_rulers import borough_rulers as BRuler
import pandas as pd

class BoroughService(object):

    def __init__(self,*args,**kwargs):
        pass


    def innit_rulers(self,find_num=0,fields_num=0):

        find_dic = BRuler.find_dic
        fields_dic = BRuler.fields_dic
        find_type=f"find_{find_num}"
        fields_type=f"fields_{fields_num}"
        find = find_dic.get(find_type,'find_0')
        fields = fields_dic.get(fields_type,'fields_0')
        if not find and  not fields:
            print("未传入规则，小区表触发全表扫描！！")
            return {},{}
        else:
            return find,fields



    # {"小区id": borough_id, "小区名": borough_name, "城市": str(row["城市"]), "城区": cityarea,
    # "商圈": cityarea2_name, "物业类型": borough_type}
    def borough_type(self,*args,**kwargs):
        city_jp=kwargs.get("city_jp")
        #选择规则查询mongo小区表
        find,fields=self.innit_rulers(find_num=0,fields_num=1)
        #返回df格式数据
        borough_df=BDao().find_mongo(find=find,fields=fields,city_jp=city_jp)
        res = []
        heads = borough_df.columns.values.tolist()
        #print(heads)
        if "cityarea" and "borough_name" in heads:
            for idx, row in borough_df.iterrows():
                area = str(row["cityarea"])
                try:
                    borough_info = row["borough_info"]
                    borough_type = borough_info.get("borough_type", "")
                    borough_id = int(row["_id"])
                    borough_name = str(row["borough_name"])
                    cityarea2 = eval(area)["cityarea2"]
                    cityarea2_name = ""
                    if cityarea2:
                        cityarea2_name = cityarea2[0].get("cityarea2_name", "")
                    cityarea = eval(area)["cityarea"].get("cityarea_name", "")
                    res_dic = {"小区id": borough_id, "小区名": borough_name, "城市": city_jp, "城区": cityarea,
                               "商圈": cityarea2_name, "物业类型": borough_type}
                    res.append(res_dic)
                except:
                    print(area)
            df =pd.DataFrame(res)
            return df





if __name__ == '__main__':


    print(BoroughService().borough_type(city_jp='nj'))

