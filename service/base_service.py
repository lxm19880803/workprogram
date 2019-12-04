# -*- coding: utf-8 -*-
from dao.mysql_dao.house_sell_dao import HouseSellDao as HSDao
from rulers.mysql_rulers import house_sell_rulers as HSRulers
from dao.mongo_dao.borough_dao import BoroughDao as BroDao
from rulers.mongo_rulers import borough_rulers as BroRulers
from utils.common_utils.city_utils import CityJob
import pandas as pd


class BaseService(object):

    def __init__(self,*args,**kwargs):
        filter=kwargs.get('filter',{})
        self.all_city_dic=CityJob(filter=filter).filtered_city_dic
        self.all_city_cn_dic=CityJob(filter=filter).filtered_city_cn_dic

    ##某城市小区字段覆盖率统计##
    def find_lv(self,*args,**kwargs):
        city_jp=kwargs.get('city_jp')
        sql=HSRulers.borough_all_house()
        hs_df=HSDao().search_sql(city_jp=city_jp,sql=sql)

        if not hs_df.empty:
            good_borough_list = hs_df.borough_id.tolist()
        else:
            good_borough_list = []
        res = []
        print(good_borough_list)
        find=BroRulers.find_def(find={'_id':{'$in':good_borough_list,'$exists': True}})
        fields=BroRulers.fields_def(fields={'_id':1,'borough_info':1,'borough_name':1})
        bro_df=BroDao().find_mongo(city_jp=city_jp,find=find,fields=fields)

        if good_borough_list:
            for idx, row in bro_df.iterrows():
                dicts = {}
                borough_id = row.get('_id')

                if borough_id not in good_borough_list:
                    continue
                dicts['borough_id'] = borough_id
                borough_info = row.get('borough_info', {})
                if borough_info:
                    borough_address = borough_info.get('borough_address', '')  # 小区地址
                    borough_volume = borough_info.get('borough_volume', '')  # 容积率
                    borough_developer = borough_info.get('borough_developer', '')  # 开发商名称
                    borough_intro = borough_info.get('borough_intro', '')  # 小区说明
                    borough_area = borough_info.get('borough_area', '')  # 建筑面积
                    borough_company = borough_info.get('borough_company', '')  # 物业公司
                    borough_costs = borough_info.get('borough_costs', '')  # 物业费
                    borough_completion = borough_info.get('borough_completion', '')  # 建筑年代
                    borough_green = borough_info.get('borough_green', '')  # 绿化
                    borough_totalbuilding = borough_info.get('borough_totalbuilding', '')  # 楼栋数
                    borough_property_right = borough_info.get('borough_property_right', '')  # 产权年限
                    borough_totalnumber = borough_info.get('borough_totalnumber', '')  # 总户数
                    baidu_address = borough_info.get('baidu_address', '')  # 百度地址
                    geo_address = borough_info.get('geo_address', '')  # 高德地址
                    borough_totalarea = borough_info.get('borough_totalarea', '')  # 占地面积
                    borough_type = borough_info.get('borough_type', '')  # 住宅类型
                    borough_buildingType = borough_info.get('borough_buildingType', '')  # 建筑类别
                    borough_construct = borough_info.get('borough_construct', '')  # 建筑结构
                    architectural = borough_info.get('architectural', '')  # 建筑形式
                    borough_tag = borough_info.get('borough_tag', '')  # 小区特色
                    borough_postcode = borough_info.get('borough_postcode', '')  # 小区邮编
                    property_address = borough_info.get('property_address', '')  # 办公地点
                    property_phone = borough_info.get('property_phone', '')  # 办公电话
                    property_desc = borough_info.get('property_desc', '')  # 物业费描述
                    parking_rate = borough_info.get('parking_rate', '')  # 车位配比
                    parking_up_num = borough_info.get('parking_up_num', '')  # 地上车位数量
                    parking_up_rent = borough_info.get('parking_up_rent', '')  # 地上车位租金
                    parking_up_price = borough_info.get('parking_up_rent', '')  # 地上车位售价
                    parking_under_num = borough_info.get('parking_under_num', '')  # 地下车位数量
                    parking_under_rent = borough_info.get('parking_under_rent', '')  # 地下车位租金
                    parking_under_price = borough_info.get('parking_under_rent', '')  # 地下车位售价
                    parking_under_address = borough_info.get('parking_under_address', '')  # 地下车位位置
                    parking_type = borough_info.get('parking_type', '')  # 车位属性
                    entrance_mode = borough_info.get('entrance_mode', '')  # 小区进入方式
                    door_num = borough_info.get('door_num', '')  # 小区入口数量
                    door_shunt = borough_info.get('door_shunt', '')  # 小区主入口分流
                    door_toward = borough_info.get('door_toward', '')  # 小区主入口朝向
                    door_depth = borough_info.get('door_depth', '')  # 小区主入口进深入
                    provide_water = borough_info.get('provide_water', '')  # 供水
                    provide_heating = borough_info.get('provide_heating', '')  # 供暖
                    provide_electric = borough_info.get('provide_electric', '')  # 供电
                    provide_gas = borough_info.get('provide_gas', '')  # 供气
                    provide_elevator = borough_info.get('provide_elevator', '')  # 电梯
                    provide_network = borough_info.get('provide_network', '')  # 通讯设备
                    rim_info = borough_info.get('rim_info', '')  # 周边介绍
                    hygiene = borough_info.get('hygiene', '')  # 卫生服务
                    rim_kindergarten = borough_info.get('rim_kindergarten', '')  # 幼儿园
                    rim_school = borough_info.get('rim_school', '')  # 中小学
                    rim_university = borough_info.get('rim_university', '')  # 大学
                    rim_market = borough_info.get('rim_market', '')  # 商场
                    rim_hospital = borough_info.get('rim_hospital', '')  # 医院
                    rim_postoffice = borough_info.get('rim_postoffice', '')  # 邮局
                    rim_bank = borough_info.get('rim_bank', '')  # 银行
                    rim_other = borough_info.get('rim_other', '')  # 其他
                    borough_entrance = borough_info.get('borough_entrance', '')  # 小区入口
                    if borough_buildingType not in ['板楼', '塔楼', '板塔结合', '独栋', '叠拼', '联排', '双拼', '独栋']:
                        borough_buildingType = ''
                    if borough_type not in ['普通住宅', '公寓', '别墅', '商铺', '写字楼', '厂房']:
                        borough_type = ''
                    if borough_construct not in ['钢混', '砖混', '钢结构']:
                        borough_construct = ''
                    if architectural not in ['低层', '多层', '小高层', '高层', '超高层', '叠拼']:
                        architectural = ''
                    if borough_property_right not in ['70', '50', '40', '小产权', '永久']:
                        borough_property_right = ''
                else:
                    borough_address = ''
                    borough_volume = ''
                    borough_developer = ''
                    borough_intro = ''
                    borough_area = ''
                    borough_company = ''
                    borough_costs = ''
                    borough_completion = ''
                    borough_green = ''
                    borough_totalbuilding = ''
                    borough_property_right = ''
                    borough_totalnumber = ''
                    baidu_address = ''
                    geo_address = ''
                    borough_totalarea = ''
                    borough_type = ''
                    borough_buildingType = ''
                    borough_construct = ''
                    architectural = ''
                    borough_tag = ''
                    borough_postcode = ''
                    property_address = ''
                    property_phone = ''
                    property_desc = ''
                    parking_rate = ''
                    parking_up_num = ''
                    parking_up_rent = ''
                    parking_up_price = ''
                    parking_under_num = ''
                    parking_under_rent = ''
                    parking_under_price = ''
                    parking_under_address = ''
                    parking_type = ''
                    entrance_mode = ''
                    door_num = ''
                    door_shunt = ''
                    door_toward = ''
                    door_depth = ''
                    provide_water = ''
                    provide_heating = ''
                    provide_electric = ''
                    provide_gas = ''
                    provide_elevator = ''
                    provide_network = ''
                    rim_info = ''
                    hygiene = ''
                    rim_kindergarten = ''
                    rim_school = ''
                    rim_university = ''
                    rim_market = ''
                    rim_hospital = ''
                    rim_postoffice = ''
                    rim_bank = ''
                    rim_other = ''
                    borough_entrance = ''
                dicts['小区地址'] = borough_address
                dicts['容积率'] = borough_volume
                dicts['开发商名称'] = borough_developer
                dicts['小区说明'] = borough_intro
                dicts['建筑面积'] = borough_area
                dicts['物业公司'] = borough_company
                dicts['物业费'] = borough_costs
                dicts['建筑年代'] = borough_completion
                dicts['绿化'] = borough_green
                dicts['楼栋数'] = borough_totalbuilding
                dicts['产权年限'] = borough_property_right
                dicts['总户数'] = borough_totalnumber
                dicts['百度地址'] = baidu_address
                dicts['高德地址'] = geo_address
                dicts['占地面积'] = borough_totalarea
                dicts['物业类型'] = borough_type
                dicts['建筑类别'] = borough_buildingType
                dicts['建筑结构'] = borough_construct
                dicts['建筑形式'] = architectural
                dicts['小区特色'] = borough_tag
                dicts['小区邮编'] = borough_postcode
                dicts['办公地点'] = property_address
                dicts['办公电话'] = property_phone
                dicts['物业费描述'] = property_desc
                dicts['车位配比'] = parking_rate
                dicts['地上车位数量'] = parking_up_num
                dicts['地上车位租金'] = parking_up_rent
                dicts['地上车位售价'] = parking_up_price
                dicts['地下车位数量'] = parking_under_num
                dicts['地下车位租金'] = parking_under_rent
                dicts['地下车位售价'] = parking_under_price
                dicts['地下车位位置'] = parking_under_address
                dicts['车位属性'] = parking_type
                dicts['小区进入方式'] = entrance_mode
                dicts['小区入口数量'] = door_num
                dicts['小区主入口分流'] = door_shunt
                dicts['小区主入口朝向'] = door_toward
                dicts['小区主入口进深入'] = door_depth
                dicts['供水'] = provide_water
                dicts['供暖'] = provide_heating
                dicts['供电'] = provide_electric
                dicts['供气'] = provide_gas
                dicts['电梯'] = provide_elevator
                dicts['通讯设备'] = provide_network
                dicts['周边介绍'] = rim_info
                dicts['卫生服务'] = hygiene
                dicts['幼儿园'] = rim_kindergarten
                dicts['中小学'] = rim_school
                dicts['大学'] = rim_university
                dicts['商场'] = rim_market
                dicts['医院'] = rim_hospital
                dicts['邮局'] = rim_postoffice
                dicts['银行'] = rim_bank
                dicts['其他'] = rim_other
                dicts['小区入口'] = borough_entrance
                res.append(dicts)
        df = pd.DataFrame(res)
        if not df.empty:
            name_list = list(df.keys())
            # 总数
            nums = int(df.borough_id.count())
            lvs = {}
            for i in name_list:
                if i == 'borough_id':
                    continue
                ones = df[~(df[i] == '')]
                if not ones.empty:
                    num = int(ones.borough_id.count())
                    # 缺失率
                    lv = (nums - num) / nums
                    lvs[i] = round(lv, 4) * 100
                else:
                    lvs[i] = 100
            if lvs:
                lvs["城市"] = self.all_city_dic.get(city_jp,{}).get('name',"")
                #print(lvs)
                df = pd.DataFrame([lvs])
        return df


if __name__ == '__main__':



    print(BaseService().find_lv(city_jp='bj'))