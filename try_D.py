from datetime import datetime
import pymysql
import os


class DataBase():
    def __init__(self):
        self.db = pymysql.connect(host="127.0.0.1", user="fil12385ki",passwd="peter1421", db="fil12385ki_donate", charset="utf8")
    def now_time(self):
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    def select(self,name="*"):
        if(name is None):
            return " "
        str = "select "+name
        return str
    def froms(self,name):
        if(name is None):
            return " "
        str = "from "+name
        return str

    def where(self, name=None, j=None,_id='ID'):
        if(j is None):
            return ''
        else:
            if(_id is "ID"):
                arr=name+_id
                str= "where {}.{}={}".format(name,arr,j)
            else:
                str="where {}={}".format(name,j)
        return str

    def join(self,table1,table2,arr,way="inner"):
        if(table2 is None):
            return ''
        str="{} join {} on {}.{}={}.{}".format(way,table2,table1,arr,table2,arr)
        return str

    def get_auto(self,table_name):
        str="""
        SELECT  AUTO_INCREMENT FROM 
        information_schema.TABLES 
        WHERE(TABLE_NAME='{}')""".format(table_name)
        print("\n-----------------\n使用指令:\n{}\n-----------------\n".format(str))

        cur = self.db.cursor()
        cur.execute(str)
        a=cur.fetchall()
        print(a[0][0])
        return a[0][0]

    def base_show(self, table1, table2=None,where=None,arr='ID',select="*"):
        ID1 = table1+arr
        cur = self.db.cursor()
        if(table2):
            ID2=table2+arr
            t = [self.lab_name(table1)+self.lab_name(table2)]
        else:
            t = [self.lab_name(table1)]
        
        try:    
            str = "{}\n{} {}\n{}".format(self.select(select),self.froms(table1),self.join(table1,table2,ID1),self.where(table1,where))
            cur.execute(str)
        except:
            str = "{}\n{} {}\n{}".format(self.select(select), self.froms(
                table1), self.join(table1, table2, ID2), self.where(table2, where))
            cur.execute(str)

        t.append(cur.fetchall())
        for row in t:
            print(row)
        return t








    def insert_Completed_order(self,table_name,sp_id,way_id):
        cur = self.db.cursor()
        str = "INSERT INTO {}(create_time,贊助人ID,方式ID) VALUES('{}','{}','{}')".format(table_name,self.now_time(),sp_id,way_id)
        print("\n-----------------\n使用指令:\n{}\n-----------------\n".format(str))
        cur.execute(str)
        self.db.commit()    
    def insert_pro_data(self,proname,arr,money,winid):
        str = """INSERT INTO 提案人資料(提案人名, 成立時間, 產業屬性, 資本額, 聯絡窗口ID) 
        VALUES('{}', '{}', '{}', {}, '{}')""".format(proname,self.now_time(),arr,money,winid)
        print("\n-----------------\n使用指令:\n{}\n-----------------\n".format(str))
        cur = self.db.cursor()
        cur.execute(str)
        self.db.commit()    
    def insert_win(self,winid,phone,site,mail):
        str = """ INSERT INTO 聯絡窗口(聯絡窗口ID,電話,聯絡地址,電子信箱) VALUES('{}','{}',"{}",'{}')""".format(winid,phone,site,mail)
        print("\n-----------------\n使用指令:\n{}\n-----------------\n".format(str))
        cur = self.db.cursor()
        cur.execute(str)
        self.db.commit()
    def insert_pro(self,proname,arr,money,phone,site,mail):
        winid = "n"+str(self.get_auto("提案人資料"))
        self.insert_pro_data(proname,arr,money,winid)
        self.insert_win(winid,phone,site,mail)
        print("新增完成")
    def insert_sur_data(self, proname, winid):
        str = """INSERT INTO 贊助者資料(贊助人名, 成立時間, 聯絡窗口ID) 
        VALUES('{}', '{}','{}')""".format(proname, self.now_time(), winid)
        print("\n-----------------\n使用指令:\n{}\n-----------------\n".format(str))
        cur = self.db.cursor()
        cur.execute(str)
        self.db.commit()
    def insert_sur(self,surname,phone,site,mail):
        winid = "p"+str(self.get_auto("贊助者資料"))
        self.insert_sur_data(surname,winid)
        self.insert_win(winid, phone, site, mail)
        print("新增完成")



    def lab_name(self, table):
        cur = self.db.cursor()
        cur.execute(
            """SELECT COLUMN_NAME, ORDINAL_POSITION, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH 
            FROM INFORMATION_SCHEMA.COLUMNS 
            WHERE TABLE_NAME = '{}'""".format(table))
        t = cur.fetchall()
        t = [x[0] for x in t]
        return t
    
    def close(self, do):
        self.db.cursor().execute(do)
        self.db.commit()




table_name = ["提案人資料", "聯絡窗口", "募資方案", "募資方式", "贊助者資料", "已完成訂單"]
# t = DataBase()
# a=t.base_show(table_name[2],table_name[3])
# print(a)
# t.insert_sur("surname","3333333","site","mail")
# t.insert_pro_data("賴清德2.0","行政類","999")
# t.get_auto(table_name[0])
# content = t. base_show(table_name[0], table_name[1], where='"n1"')
# t.insert_Completed_order("已完成訂單","2","1-1",)
# t.show_table(table_name[0])
# t.n_show(table_name[0])
# pro_way()
# # pro_data()
# t = DataBase()
