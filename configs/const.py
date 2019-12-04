INI_CONFIG_PATH="/Users/luxiaming/Documents/work_program/config.ini"
D_TYPE_LIST=['redis','codis','mysql','mongo','pika']

def get_db(type, city):

    not_bj = {
        "borough": "spider",
        "plathouse": "spider",
        "new-plathouse": "spider",
        "sell-old": "spider",
        "sell-new" : "spider"
    }
    bj = {
        "brokerhouse": "brokerhouse",
        "complex": "newhouse",
        "building": "building",
        "brokerbd": "brokerswarehouse",
        "broker": "brokers",
        "rent": "rent",
        "analysis": "thor",
        "new-analysis": "thor",
        "sell-analysis": "spider",
        "sell-api": "spider",
        "rent-t": "rent",
        "new-rent": "rent",
        "zhuge-dm": "data"
    }
    mag = {
        "dm": "zhuge_dm",
        "ccmag": "comphousemag",
        "comphousemag": "comphousemag",
        "brokers": "brokers",
        "hidden_etl": "count",
        "hidden_new": "count",
        "rules_template": "spider_rules",
        "avgprice": "statistics",
        "localhost": "test",
        "appraisal": "spider",
        "operation": "operation",
        "newhouse_dock": "newhouse_dock",
        "zhuge_user": "zhuge_user"
    }
    special = {
        "design":"deco"
    }
    if type in bj:
        db = bj.get(type) + "_" + city
        return db
    elif type in not_bj:
        db = not_bj.get(type) if city == "bj" else not_bj.get(type) + "_" + city
        return db
    elif type in mag:
        return mag.get(type)
    elif type in special:
        return special.get(type) if city == "" else special.get(type) + "_" + city





sell_old = ('bj', 'bd', 'cc', 'cd', 'cq', 'cs', 'cz', 'dg', 'dl', 'fz', 'guilin', 'gy', 'gz', 'heb', 'hf', 'hhht', 'hn',
            'huizhou', 'hz', 'jh', 'jm', 'jn', 'km', 'ks', 'lf', 'ly', 'lz', 'nb', 'nc', 'nj', 'nn', 'nt', 'qd', 'qhd',
            'qz', 'sh', 'sjz', 'su', 'sx', 'sy', 'sz', 'taiyuan', 'taizhou', 'tj', 'ts', 'weihai', 'wf', 'wh', 'wx',
            'xa', 'xaxq', 'xm', 'xz', 'yc', 'yinchuan', 'yt', 'yz', 'zh', 'zs', 'zz')

es_new = ('changle', 'dangtu', 'haimen', 'haicheng', 'jingjiang', 'laizhou', 'lianjiang', 'leiyang', 'sdpy', 'qianan',
          'shangyu', 'sg', 'tianmen', 'wuzhishan', 'xinji', 'yizheng', 'fjax', 'alaer', 'anning', 'anqiu', 'baoying',
          'gxby', 'boluo', 'hbbz', 'changshu', 'cqchangshou', 'changxing', 'cixi', 'changyi', 'chunan', 'ahcf', 'sdcl',
          'chongzhou', 'cn', 'deqing', 'dongtai', 'donggang', 'dangyang', 'dengfeng', 'dehui', 'dingzhou', 'dayi',
          'dongfang', 'dujiangyan', 'dengzhou', 'donghai', 'enping', 'emeishan', 'fq', 'fengdu', 'fuling', 'feicheng',
          'fengcheng', 'feixi', 'feidong', 'jsfx', 'fuan', 'jxfc', 'gaomi', 'gongyi', 'gaoyou', 'guangrao',
          'gaobeidian', 'huian', 'hechuan', 'haining', 'haian', 'huidong', 'huxian', 'hengxian', 'heshan', 'haiyang',
          'hailin', 'huadian', 'jiangyin', 'jiangdu', 'cqjiangjin', 'jiyuan', 'jintan', 'jiande', 'jinxian', 'jr',
          'scjt', 'sdjy', 'jianyang', 'kaiping', 'kuitun', 'longhai', 'longkou', 'sxly', 'linhai', 'liyang', 'lujiang',
          'laiyang', 'lantian', 'liaozhong', 'liuyang', 'luanxian', 'luannan', 'hblt', 'gdlm', 'linqing', 'liling',
          'lhk', 'mengjin', 'cqnanchuan', 'ninghai', 'nanan', 'nongan', 'ningxiang', 'pingtan', 'pizhou', 'pulandian',
          'pinghu', 'peixian', 'pengzhou', 'puning', 'qijiang', 'qidong', 'qingzhou', 'qionglai', 'qianxi', 'qingxu',
          'qixia', 'qingzhen', 'ruzhou', 'rugao', 'ruijin', 'rudong', 'ruyang', 'renqiu', 'shunde', 'shennongjia',
          'shuyang', 'shihezi', 'shishi', 'jssn', 'sdsh', 'shangzhi', 'hbsz', 'hbsh', 'cqtongliang', 'taixing',
          'tengzhou', 'tongxiang', 'zjtl', 'taishan', 'wanzhou', 'wujiaqu', 'wenling', 'wafangdian', 'hbwj', 'wuchang',
          'wenan', 'wanning', 'wuan', 'wg', 'xinzheng', 'zjxs', 'xingyang', 'xinjian', 'xinmin', 'yongchuan', 'yixing',
          'yiwu', 'yanling', 'yangchun', 'hnyz', 'yuyao', 'yichuan', 'yanshi', 'yidu', 'yongdeng', 'yuzhong',
          'yongchun', 'hnyy', 'yutian', 'jlys', 'hbys', 'yongcheng', 'ya', 'hbyc', 'zhangjiagang', 'zhuozhou',
          'zhangqiu', 'zhucheng', 'zy', 'zhuji', 'zoucheng', 'zouping', 'zunhua', 'zhaodong', 'zhongmou', 'lnzh',
          'zhouzhi', 'zhongxiang', 'hbzy', 'anlu', 'beipiao', 'beiliu', 'chibi', 'cenxi', 'dafeng', 'danyang', 'dengta',
          'dunhuang', 'dongyang', 'fuding', 'guangshui', 'geermu', 'guanghan', 'guiping', 'gaoan', 'huanghua', 'hejian',
          'hancheng', 'hanchuan', 'jinjiang', 'jiangshan', 'kaiyuan', 'linzhou', 'lingbao', 'lengshuijiang', 'lianyuan',
          'lufeng', 'leping', 'laoling', 'meihekou', 'mengzhou', 'ningguo', 'penglai', 'qinyang', 'rushan', 'renhuai',
          'shengzhou', 'songzi', 'shahe', 'tianchang', 'wuyishan', 'wuxue', 'yangzhong', 'yucheng', 'yuanjiang',
          'zixing', 'zhangshu', 'zjfy', 'linan', 'jimo', 'jiaonan', 'jiashan', 'baisha', 'danzhou', 'chengmai',
          'dingan', 'qiongzhong', 'tunchang', 'wenchang', 'lingshui', 'baoting', 'jinan', 'jianhu', 'gaoling', 'hbjz',
          'ynyl', 'yongtai', 'hbzx', 'anda', 'aj', 'binxian', 'chaohu', 'changge', 'changli', 'jncq', 'dh', 'dingxing',
          'faku', 'funing', 'guan', 'guzhen', 'njgc', 'gongzhuling', 'huoqiu', 'hailaer', 'huaiyuan', 'whhn', 'huairen',
          'haiyan', 'jiangyan', 'jizhou', 'hbjs', 'jinhu', 'kangping', 'kaiyang', 'kuerle', 'linqu', 'luoning',
          'lankao', 'luoyuan', 'luanchuan', 'minqing', 'hbps', 'qianjiang', 'qj', 'qionghai', 'hbql', 'quangang',
          'ruian', 'taicang', 'tongcheng', 'wujiang', 'wuhe', 'xinyi', 'xianghe', 'xiantao', 'xinghua', 'xintai',
          'xinmi', 'hnxa', 'xiuwen', 'xinle', 'youxian', 'xiangxiang', 'xinjin', 'xilinhaote', 'yanjiao', 'yueqing',
          'yongkang', 'yuhuan', 'yongning', 'ksys', 'zhaozhou', 'zhaoyuan', 'zhijiang', 'benxi', 'sanmenxia', 'dxal',
          'diqing', 'rikaze', 'gannan', 'ali', 'guantao', 'hexian', 'kenli', 'minggang', 'yongxin', 'zhengding',
          'zhangbei')




def getConfigType(city, type):
    # sell_old = []
    # result = CityConfig.CityConfigService().get_cityinfo(city="bj", where='{"sell_db": 1}')
    # for i in result:
    #     sell_old.append(i.get("logogram"))

    if "sell" in type:
        if city in sell_old:
            return "sell-old"
        else:
            return "sell-new"
    if "broker" in type:
        if city in sell_old:
            return "broker-old"
        else:
            return "broker-new"
    elif "plathouse" in type:
        if city in sell_old:
            return "plathouse-old"
        else:
            return "plathouse-new"
    return type


# 获取es配置名称
def getEsConfigName(city,service_type):
    if "sell" == service_type:
        if city in es_new:
            return "new_es"
        else:
            return "sell"
    return service_type


if __name__ == '__main__':
    pass
    # a = getConfigName("jx", "sell")
    # print(a)
