# -*- coding: utf-8 -*-



#{"小区id": borough_id, "小区名": borough_name, "城市": str(row["城市"]), "城区": cityarea,
#"商圈": cityarea2_name, "物业类型": borough_type}
#

find_dic={

    ###全表扫描
    'find_0':{},



}

fields_dic={
    'fields_0':{},
    ###小区名，城区，商圈，物业类型
    'fields_1':{"borough_name":1,"cityarea.cityarea2.cityarea2_name":1,"cityarea.cityarea.cityarea_name":1,"borough_info.borough_type":1},

}


def find_def(*args,**kwargs):
    find=kwargs.get('find')
    return find

def fields_def(*args,**kwargs):
    fields=kwargs.get('fields')
    return fields