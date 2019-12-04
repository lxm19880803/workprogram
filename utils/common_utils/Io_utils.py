#!/usr/bin/python
#coding=utf-8

import pandas as pd
import xlrd


class IoJob:

    def __init__(self):
        pass


    def df_write_to_excel(self, path, df, head=[]):
        ws = pd.ExcelWriter(path=path)
        head = head
        print(head)
        df = df[head]
        df.to_excel(ws, f"sheet", index=False)
        ws.save()
        print('数据导出完成')

    def read_excel(self,path,row_names=[],column_names=[]):
        df = pd.read_excel(path,dtype=str,encoding='utf-8-sig')
        if row_names:
            df = df.loc[:, row_names]  # 读所有行的title以及data列的值，这里需要嵌套列表
        #print(df)
        return df

    def read_excel_old(self,path="",sheet_num=1,col_names=[]):
        res=[]
        workbook = xlrd.open_workbook(filename=path)
        booksheet = workbook.sheet_by_index(sheet_num)
        for i in range(booksheet.nrows):
            if i > 0:
                line = booksheet.row_values(i)
                res_dic={}
                for index,name in enumerate(col_names):
                    res_dic[name]=line[index]
                res.append(res_dic)
        df=pd.DataFrame(res)
        print(df)
        return df



    def read_mysql(self, sql,mysqlconn):
        df = pd.read_sql_query(sql,mysqlconn)
        return df

    def write_mysql(self,df,mysqlconn,table_name,head=[]):
        head = head
        print(head)
        df = df[head]
        df.to_sql(name=table_name, con=mysqlconn, index=True,if_exists = 'replace')



if __name__ == '__main__':
    pass

