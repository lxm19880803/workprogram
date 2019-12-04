
import requests
import json

class ReqJob:
    def __init__(self):


        self.baidu_api_key="zH6uL46rEug6Fs7NXi4IMPoILHrRnGi7"
        #self.baidu_api_key="th2iOTIzwjZixNS6PsRYwxUkGo9ONGbM"

        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "useragent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        self.login_url = "http://dm.1024.zhugefang.com/user/user/login"  # 获取cookie_url
        self.dm_manage_url = "http://dm.1024.zhugefang.com/spider/CanalManage/list"  # 查询url
        self.nominate_url = "http://dm.1024.zhugefang.com/spider/CanalManage/binduserinfo"  # 绑定请求url
        self.login_data = {
            "password": "wow1988",
            "username": "luxiaming@zhuge.com"
        }
        self.service_type = {
            "sell": 1,
            "complex": 2,
            "rent": 3,
            "apt": 4
        }
        cookie = self.get_cookie()
        self.headers.update({"cookie": cookie})

    def get_cookie(self):  # 获取cookie值

        response = requests.post(self.login_url, headers=self.headers, data=json.dumps(self.login_data))
        cookie_list = dict(response.cookies)
        cookie = f"{cookie_list}".replace("': '", "=").replace("', '", ";").replace("{'", "").replace("'}", "")
        return cookie

    def run_distance(self,start_loc={},end_loc={}):
        if start_loc and end_loc:
            s_loc = str(start_loc['lat']) + "," + str(start_loc['lng'])
            e_loc = str(end_loc['lat']) + "," + str(end_loc['lng'])
            r_info=self.riding_info(loction=s_loc,finsh_loc=e_loc)
            w_info=self.walking_info(loction=s_loc, finsh_loc=e_loc)
            if r_info and w_info:
                r_info_lst=r_info.get("result",{}).get('routes',[])
                w_info_lst=w_info.get("result",{}).get('routes',[])
                if r_info_lst and w_info_lst:
                    r_dis=r_info_lst[0].get("distance",0)
                    w_dis=w_info_lst[0].get("distance",0)
                    r_dur=r_info_lst[0].get("duration",0)
                    w_dur=w_info_lst[0].get("duration",0)
                    if r_dis and w_dis and r_dur and w_dur:
                        distance={"ride":{"dis": r_dis,"time": r_dur},"walk":{"dis": w_dis,"time": w_dur}}
                        print("========")
                        print(distance)
                        return distance
        else:
            return {}



    def riding_info(self, loction, finsh_loc):
        """
        百度骑行返回方案
        :param loction: 起点坐标
        :param finsh_loc: 终点坐标
        :return:
        """
        if loction and finsh_loc:
            url = f'http://api.map.baidu.com/directionlite/v1/riding?origin={loction}&destination={finsh_loc}&ak={self.baidu_api_key}'
            res = requests.get(url).json()
            code = res.get('status', 1)
            msg = res.get('message', '')
            print(res)
            print(code)
            if code == 0:
                return res
            elif code == 302 and msg == "天配额超限，限制访问":
                exit()
            else:
                return {}

    def walking_info(self, loction, finsh_loc):
        if loction and finsh_loc:
            """
            百度步行返回方案
            :param loction: 起点坐标
            :param finsh_loc: 终点坐标
            :return:
            """
            url = f'http://api.map.baidu.com/directionlite/v1/walking?origin={loction}&destination={finsh_loc}&ak={self.baidu_api_key}'
            res = requests.get(url).json()
            code=res.get('status',1)
            msg=res.get('message','')
            print(res)
            if code==0:
                return res
            elif code==302 and msg=="天配额超限，限制访问":
                exit()
            else:
                return {}

    def del_borough_cache(self,borough_id_list,city):
        cookie=self.get_cookie()
        headers=self.headers
        url="http://dm.1024.zhugefang.com/borough/binlog/delcache"
        erro_ids=[]
        for id in borough_id_list:
            data={
                'city': city, 'borough_id':id
            }
            data=json.dumps(data)
            res = eval(requests.post(url=url,data=data,headers=headers).content.decode())
            msg=res.get("message", "")
            if msg!="操作成功":
                print(msg)
                erro_ids.append(id)
        print(erro_ids)



if __name__ == '__main__':
    rj=ReqJob()
    # start_loc= {
    #     "lat" : 38.6575,
    #     "lng" : 116.3567
    # }
    # end_loc={
    #                 "lat" : 39.9237,
    #                 "lng" : 116.356
    #             }
    #
    # rj.run_distance(start_loc,end_loc)

    #rj.del_borough_cache(borough_id_list=[1002216],city='dl')

