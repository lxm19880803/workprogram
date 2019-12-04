#!/usr/bin/env python
# -*- coding: utf-8 -*-

# !/usr/bin/env python
# -*- coding: utf-8 -*-

from service.mysql_service.house_sell_gov_service import HouseSellGov as HSG
from service.mysql_service.house_sell_sevice import HouseSell as HS
from service.base_service import BaseService as BS
from utils.common_utils.Io_utils import IoJob
from utils.common_utils.city_utils import CityJob
from utils.common_utils import zhuge_email
import threadpool
import pandas as pd
import time


class Job(object):

    def __init__(self, *args, **kwargs):
        self.city_cn_list = kwargs.get('city_cn_list', [])
        self.filter_city = kwargs.get('filter_city', {})
        self.city_cn_dic = CityJob(filter=self.filter_city).filtered_city_cn_dic
        self.city_dic = CityJob(filter=self.filter_city).filtered_city_dic

        self.df_list = []

    def run_df(self, city_jp):
        print(city_jp)
        df = BS(filter=self.filter_city).find_lv(city_jp=city_jp)
        print(city_jp)
        print(df)
        if not df.empty:
            self.df_list.append(df)


    def run_email(self, *args, **kwargs):
        time_=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        out_file_name = kwargs.get('file_name', f'城市线上小区字段覆盖率{time_}.xlsx')
        df_res = kwargs.get('df_res')
        out_path = f"../output/files/{out_file_name}"
        title = '城市线上小区字段覆盖率'
        htmls = '数字标示缺失率'
        df_res.to_excel(out_path, index=False)
        zhuge_email.sendmail(title, htmls, 'ci@zhuge.com', ['luxiaming@zhuge.com'], [], [out_path])

    def run(self, *args, **kwargs):
        pool_num = int(kwargs.get('pool_num', 1))
        city_cn_list = self.city_cn_list if self.city_cn_list else list(self.city_cn_dic.keys())
        city_jp_list = CityJob(filter=self.filter_city).get_city_jp(city_cn_lst=city_cn_list)
        pool = threadpool.ThreadPool(pool_num)
        requests = threadpool.makeRequests(self.run_df, city_jp_list)
        [pool.putRequest(req) for req in requests]
        pool.wait()
        df_res = pd.concat(self.df_list)
        return df_res


if __name__ == '__main__':
    job = Job(city_cn_list=[], filter_city={'is_sell', 1})
    df_res = job.run(pool_num=5)
    job.run_email(df_res=df_res)



