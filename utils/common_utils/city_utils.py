# -*- coding: UTF-8 -*-
import requests,json


class CityJob:
    def __init__(self,*args,**kwargs):
        filter=kwargs.get('filter',{})
        #print(filter)
        # self.all_city_dic=self.get_all_city_dic()
        # self.all_city_cn_dic=self.get_all_city_cn_dic()
        self.filtered_city_dic=self.get_filtered_city_dic(filter=filter)
        self.filtered_city_cn_dic=self.get_filtered_city_cn_dic(filter=filter)


    def get_all_city_dic(self,*args,**kwargs):



        '''

        :return: 所有的城市字典，key是中文城市，value是
        {"id": i.get("id"), "logogram": i.get("logogram"), "name": i.get("name"),
                   "city_fpy": i.get("city_fpy")}

        '''

        headers = {"Content-Type": "application/json"}
        res = requests.post(
            "http://config.dapi.zhugefang.com/config/getCity",
            data=json.dumps({}),
            headers=headers,
        ).json()
        all_city_dic = {}
        for k, i in list(res["data"].items()):
            #print(i)
            dic = {"id": i.get("id"), "logogram": i.get("logogram"), "name": i.get("name"),
                   "city_fpy": i.get("city_py")}
            all_city_dic[i.get("logogram")]=dic
        return all_city_dic


    def get_all_city_cn_dic(self,*args,**kwargs):
        '''

        :return: 所有的城市字典，key是中文城市，value是
        {"id": i.get("id"), "logogram": i.get("logogram"), "name": i.get("name"),
                   "city_fpy": i.get("city_fpy")}

        '''

        headers = {"Content-Type": "application/json"}
        res = requests.post(
            "http://config.dapi.zhugefang.com/config/getCity",
            data=json.dumps({}),
            headers=headers,
        ).json()
        all_city_cn_dic = {}
        for k, i in list(res["data"].items()):
            #print(i)
            dic = {"id": i.get("id"), "logogram": i.get("logogram"), "name": i.get("name"),
                   "city_fpy": i.get("city_py")}
            if not all_city_cn_dic.get(i.get("name",""),{}):
                all_city_cn_dic[i.get("name","")]=dic
            else:
                all_city_cn_dic[i.get("name","")+"1"]=dic
        return all_city_cn_dic


    def get_city_cn(self,*args,**kwargs):
        city_jp_lst=kwargs.get('city_jp_lst',[])
        city_jp=kwargs.get('city_jp','')
        if city_jp_lst:
            city_cn_lst=[]
            for city_jp in city_jp_lst:
                city_cn=self.filtered_city_dic.get(city_jp,'')
                city_cn_lst.append(city_cn)
            return city_cn_lst
        elif city_jp:
            return self.filtered_city_dic.get(city_jp,'')

    def get_city_jp(self, *args, **kwargs):
        city_cn_lst = kwargs.get('city_cn_lst', [])
        city_cn = kwargs.get('city_cn', '')
        city_jp_lst=[]
        if city_cn_lst:
            for city_cn in city_cn_lst:
                city_jp = self.filtered_city_cn_dic.get(city_cn, {}).get('logogram',"")
                city_jp_lst.append(city_jp)
            return city_jp_lst
        elif city_cn:
            city_jp = self.filtered_city_cn_dic.get(city_cn, {}).get('logogram', "")
            return [city_jp]




    def get_city_info(self, *args,**kwargs):
        filter=kwargs.get('filter','')
        pms = {
            "page": {
                "index": 1,
                "size": 1000
            }
        }
        if filter:
            pms.setdefault('filter', filter)
        res = requests.post(url="http://config.dapi.zhugefang.com/config/getcityinfo", json=pms)
        if res:
            return json.loads(res.content)['data']
        else:
            return []


    def get_filtered_city_dic(self, filter={}):
        data_list = self.get_city_info(filter=filter)
        # print(data_list)
        city_dic = {}
        for i in data_list:
            dic = {"id": i.get("id"), "logogram": i.get("logogram"), "name": i.get("name"),
                   "city_fpy": i.get("city_fpy")}
            city_dic[i.get("logogram")] = dic
        #print(city_dic)
        return city_dic

    def get_filtered_city_cn_dic(self, filter={}):
        data_list = self.get_city_info(filter=filter)
        city_dic = {}
        for i in data_list:
            dic = {"id": i.get("id"), "logogram": i.get("logogram"), "name": i.get("name"),
                   "city_fpy": i.get("city_fpy")}
            city_dic[i.get("name")] = dic
        return city_dic


    def CityApi(self,city="", type=""):
        jsons = dict()
        if city:
            jsons.setdefault("city", city)
        if type:
            jsons.setdefault("type", type)
        data = requests.post(url="http://config.dapi.zhugefang.com/config/getCity", json=jsons)
        result = json.loads(data.content)["data"]
        return result



if __name__ == '__main__':

    pass
    all_city_dic=CityJob().all_city_dic
    print(len(all_city_dic))
    print(all_city_dic.get('jz'))
    # a=job.get_city_py_or_sx_list(isfpy=2,city_cn_list=["桂林","吉林"])
    # print(a)

#     sx_lst=[sx for sx in sx_city.split("\n") if sx!=""]
#     for i in job.get_city_cn_list(logogram_list=sx_lst):
#         print(i)

    # #需求给的中文城市字符串,转为city_cn_list
    # splits=job.get_city_cn_list(split=" ",source_str=str_city)
    # city_cn_list=[city_cn.strip() for city_cn in splits]
    # print(city_cn_list,len(city_cn_list))
    #
    # #获得服务器中的城市列表信息
    # city_dic=job.get_filtered_city_dic(filter={})
    # print(city_dic,len(city_dic))
    # #
    # # #获得全拼列表或是缩写列表
    # city_list=job.get_city_py_or_sx_list(isfpy=0,city_cn_list=job.get_filtered_city_dic(filter={"is_rent":1}).keys(),city_dic=city_dic)
    # print(city_list,len(city_list))


    #获得所有的城市信息
    # all_dic=job.get_all_city_dic()
    # print(len(all_dic))

#dic ={'上蔡': "{'py': 'shangcai', 'super_city': '驻马店', 'super_py': 'zhumadian'}", '云阳': "{'py': 'yunyang', 'super_city': '重庆', 'super_py': 'cq'}", '六盘水': "{'py': 'panxian', 'super_city': '盘县', 'super_py': 'liupanshui'}", '卫辉': "{'py': 'weihui', 'super_city': '新乡', 'super_py': 'xx'}", '原阳': "{'py': 'yuanyang', 'super_city': '新乡', 'super_py': 'xx'}", '含山': "{'py': 'hanshan', 'super_city': '马鞍山', 'super_py': 'mas'}", '垫江': "{'py': 'dianjiang', 'super_city': '重庆', 'super_py': 'cq'}", '城口': "{'py': 'chengkou', 'super_city': '重庆', 'super_py': 'cq'}", '奇台': "{'py': 'qitai', 'super_city': '昌吉', 'super_py': 'changji'}", '奉节': "{'py': 'fengjie', 'super_city': '重庆', 'super_py': 'cq'}", '封丘': "{'py': 'fengqiu', 'super_city': '新乡', 'super_py': 'xx'}", '嵩县': "{'py': 'song', 'super_city': '洛阳', 'super_py': 'ly'}", '巫山': "{'py': 'wushan', 'super_city': '重庆', 'super_py': 'cq'}", '巫溪': "{'py': 'wuxi', 'super_city': '重庆', 'super_py': 'cq'}", '常山': "{'py': 'changshan', 'super_city': '衢州', 'super_py': 'quzhou'}", '平舆': "{'py': 'pingyu', 'super_city': '驻马店', 'super_py': 'zhumadian'}", '延津': "{'py': 'yanjin', 'super_city': '新乡', 'super_py': 'xx'}", '开化': "{'py': 'kaihua', 'super_city': '衢州', 'super_py': 'quzhou'}", '彭水': "{'py': 'pengshui', 'super_city': '重庆', 'super_py': 'cq'}", '忠县': "{'py': 'zhong', 'super_city': '重庆', 'super_py': 'cq'}", '新蔡': "{'py': 'xincai', 'super_city': '驻马店', 'super_py': 'zhumadian'}", '枞阳': "{'py': 'zongyang', 'super_city': '铜陵', 'super_py': 'tongling'}", '正阳': "{'py': 'zhengyang', 'super_city': '驻马店', 'super_py': 'zhumadian'}", '汝南': "{'py': 'runan', 'super_city': '驻马店', 'super_py': 'zhumadian'}", '泌阳': "{'py': 'biyang', 'super_city': '驻马店', 'super_py': 'zhumadian'}", '石柱': "{'py': 'shizhu', 'super_city': '重庆', 'super_py': 'cq'}", '确山': "{'py': 'queshan', 'super_city': '驻马店', 'super_py': 'zhumadian'}", '秀山': "{'py': 'xiushan', 'super_city': '重庆', 'super_py': 'cq'}", '获嘉': "{'py': 'huojia', 'super_city': '新乡', 'super_py': 'xx'}", '西平': "{'py': 'xiping', 'super_city': '驻马店', 'super_py': 'zhumadian'}", '辉县': "{'py': 'huixian', 'super_city': '新乡', 'super_py': 'xx'}", '遂平': "{'py': 'suiping', 'super_city': '驻马店', 'super_py': 'zhumadian'}", '郯城': "{'py': 'tancheng', 'super_city': '临沂', 'super_py': 'linyi'}", '酉阳': "{'py': 'youyang', 'super_city': '重庆', 'super_py': 'cq'}", '金门': "{'py': 'jinmen', 'super_city': '泉州', 'super_py': 'qz'}", '长垣': "{'py': 'changyuan', 'super_city': '新乡', 'super_py': 'xx'}", '龙游': "{'py': 'longyou', 'super_city': '衢州', 'super_py': 'quzhou'}"}



