import configparser
from configs import const
from configs.const import getConfigType,get_db

class ParserReader(object):

    def __init__(self,*args,**kwargs):
        self.conf_name=kwargs.get('conf_name') or ""

        self.options=kwargs.get('option') or []
        self.cf = configparser.RawConfigParser()
        self.cf.read(const.INI_CONFIG_PATH)


    def read(self):

        items=[]
        if self.conf_name and not self.options:
            try:
                items=self.cf.items(section=self.conf_name)
                items=[{i[0]:i[1]} for i in items]
            except Exception as e:
                print(e)

        elif self.options and self.conf_name and isinstance(self.options,list):
            try:
                ops = self.cf.items(section=self.conf_name)
                ops = [{i[0]: i[1]} for i in ops]
                items=[]
                for info in ops:
                    if list(info.keys())[0] in self.options:
                        items.append(info)
            except Exception as e:
                print(e)
        elif not isinstance(self.options,list):
            print("传入options格式应为列表形式")
        else:
            print("未传入conf_name,列表如下请重新传入")
            print(self.cf.sections())

        return items


    def get_db_config(self) -> dict:
        items=self.read()
        conf_name=self.conf_name
        db_config={}
        if "_" in conf_name:
            d_type=conf_name.split("_")[0]
            if d_type in const.D_TYPE_LIST:
                for info in items:
                    db_config.update(info)
        #print(db_config)
        return db_config



if __name__ == '__main__':

    res=ParserReader(conf_name="mysql_online_sell_old").read()
    ParserReader(conf_name="mysql_online_sell_old").get_db_config()