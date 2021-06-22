import pymysql
import os

class DataBase():
    def __init__(self):
        self.db = pymysql.connect(host="127.0.0.1", user="fil12385ki",
                                  passwd="peter1421", db="fil12385ki_donate", charset="utf8")
    def show_table(self,table,where):
        print("show_all_data:")
        ID = table+"ID"
        cur = self.db.cursor()
        str = "SELECT * FROM {} ".format(table)
        if(where != None):
            str += "where {}.{}={}".format(table, ID, where)
        cur.execute(str)
        t = [self.lab_name(table)]
        t.append(cur.fetchall())
        for row in t:
            print(row)
        return t

    def join(self,table1,table2,where):
        ID=table2+"ID"
        print("show_all_data:")
        cur = self.db.cursor()
        str = "Select * From {} Inner join {} on  {}.{}={}.{} ".format(
            table1, table2, table1, ID, table2, ID)
        if(where != None):
            str += "where {}.{}={}".format(table1,ID, where)
        print(str)
        cur.execute(str)
        t = [self.lab_name(table1)+self.lab_name(table2)]
        t.append(cur.fetchall())
        for row in t:
            print(row)
        return t
    def lab_name(self,table):
        cur = self.db.cursor()
        cur.execute(
            "SELECT COLUMN_NAME, ORDINAL_POSITION, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{}'".format(table))
        t = cur.fetchall()
        t=[ x[0] for x in t]
        return t
    

    def close(self, do):
        self.db.cursor().execute(do)
        self.db.commit()





table_name = ["提案人資料", "聯絡窗口", "募資方案", "募資方式", "贊助者資料", "已完成訂單"]
# t = DataBase()
# pro_way()
# # pro_data()
# content = t. show_table(table_name[0], where='1')
# t = DataBase()

# b = t.join(table_name[0], table_name[1],where=1)
# print(b)

# t = DataBase()
# # content = t. join(table_name[2], table_name[0], where=name)
# b = t.join(table_name[0], table_name[1],where='"n1"')

# def all_table():
#     t = DataBase()
#     b = t.show_table(table=table_name[0])
#     print(b)


# def show_all_pro():
#     t = DataBase()
#     b = t.show_table(table=table_name[2])
#     return b


# def proname_data():
#     t = DataBase()
#     b = t.join(table_name[0], table_name[1])
#     print(b)


# def pro_data():
#     t = DataBase()
#     b = t.join(table_name[0], table_name[2])
#     print(b)

# def pro_way():
#     t = DataBase()
#     b = t.join(table_name[2], table_name[3])
#     print(b)
#     return b