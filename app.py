from flask import Flask, request, render_template
import random
app = Flask(__name__, static_folder="static", static_url_path="/")
import try_D


table_name = ["提案人資料", "聯絡窗口", "募資方案", "募資方式", "贊助者資料", "已完成訂單"]

@app.route('/')
def show_index():
    return render_template('index.html')


@app.route('/welcome')
def show_welcome():
    return render_template('index.html')



@app.route('/all_prouser')
def show_all_prouser():
    t = try_D.DataBase()
    content = t. base_show(table_name[0])
    return render_template('show_all_prouser.html', labels=content[0], content=content[1])


@app.route('/all_spouser')
def show_all_spouser():
    t = try_D.DataBase()
    content = t. base_show(table_name[4])
    return render_template('show_all_spouser.html', labels=content[0], content=content[1])

@app.route('/all_pro')
def show_all_pro():
    t = try_D.DataBase()
    content = t. base_show(table_name[2])
    return render_template('show_all_pro.html', labels=content[0], content=content[1])


@app.route('/prouser')
def show_prouser():
    try:
        name = "'n{}'".format(str(request.args.get("prouser", "")))
    except:
        name=None
    t = try_D.DataBase()
    content = t. base_show(table_name[0], table_name[1], where=name)
    return render_template('show_all_prouser.html', labels=content[0], content=content[1])


@app.route('/spouser')
def show_spouser():
    try:
        name = "'p{}'".format(str(request.args.get("spouser", "")))
    except:
        name = None
    t = try_D.DataBase()
    content = t. base_show(table_name[4], table_name[1], where=name)
    return render_template('show_all_spouser.html', labels=content[0], content=content[1])


@app.route('/pro')
def show_pro():
    try:
        name = "'{}'".format(str(request.args.get("pro", ""))) 
    except:
        name = None
    t = try_D.DataBase()
    content = t. base_show(table_name[2], table_name[3],where=name)
    return render_template('show_all_pro.html', labels=content[0], content=content[1])




@app.route('/all_order')
def show_all_order():
    t = try_D.DataBase()
    content = t. base_show(table_name[5])
    return render_template('sql_show.html', labels=content[0], content=content[1])


@app.route('/add_order')
def show_add_order():
    spo_id = "{}".format(str(request.args.get("spo_id")))
    way_id = "{}".format(str(request.args.get("way_id")))
    t = try_D.DataBase()
    print("??",spo_id,way_id,"??")
    if('None' in spo_id and 'None' in way_id):
        print("NULL")
    else:
        c= t. insert_Completed_order("已完成訂單", spo_id, way_id)
    content = t. base_show(table_name[5])
    return render_template('order.html', labels=content[0], content=content[1])


@app.route('/insert/sur')
def sur():
    surname = "{}".format(str(request.args.get("surname", "")))
    phone = "{}".format(str(request.args.get("phone", "")))
    site = "{}".format(str(request.args.get("site", "")))
    mail = "{}".format(str(request.args.get("mail", "")))
    t = try_D.DataBase()
    t.insert_sur(surname,phone,site,mail)
    return render_template("insert.html")



@app.route('/insert/surdata')
def sur_data():
    return render_template("insert_sur.html")


@app.route('/insert/pro')
def pro():
    proname = "{}".format(str(request.args.get("proname", "")))
    phone = "{}".format(str(request.args.get("phone", "")))
    arr = "{}".format(str(request.args.get("arr", "")))
    money = "{}".format(str(request.args.get("money", "")))
    site = "{}".format(str(request.args.get("site", "")))
    mail = "{}".format(str(request.args.get("mail", "")))
    t = try_D.DataBase()
    t.insert_pro(proname, arr, money, phone, site, mail)
    return render_template("insert.html")


@app.route('/insert/prodata')
def pro_data():
    return render_template("insert_pro.html")

@app.route('/insert')
def insert():
    return render_template("insert.html")


@app.route('/creat_prodata')
def creat_prodata():
    return render_template("insert_prodata.html")


@app.route('/creat_prodata_w')
def prodata():
    prouserid = "{}".format(str(request.args.get("prouserid", "")))
    name = "{}".format(str(request.args.get("name", "")))
    content = "{}".format(str(request.args.get("content", "")))
    money = "{}".format(str(request.args.get("money", "")))

    t = try_D.DataBase()
    t.insert_pro_content(prouserid, name, content,money)
    return render_template("insert_proway.html")


@app.route('/creat_proway')
def creat():
    return render_template("insert_proway.html")

@app.route('/creat_proway_w')
def creat_proway():
    proid = "{}".format(str(request.args.get("proid", "")))
    money = "{}".format(str(request.args.get("money", "")))
    content = "{}".format(str(request.args.get("content", "")))

    t = try_D.DataBase()
    t.insert_pro_way(proid,money,content)
    return render_template("index.html")



if __name__=="__main__":
    app.run(port=3000)


# @app.route('/self_search')
# def self_search():
#     table1 = request.args.get("table1", "")
#     table2 = request.args.get("table2", "")
#     arr = request.args.get("arr", "")
#     val = "'{}'".format(str(request.args.get("val", "")))
#     t = try_D.DataBase()
#     content = t. base_show(table1, table2,where=val,arr=arr)
#     return render_template('sql_show.html', labels=content[0], content=content[1])


# @app.route('/search')
# def search():
#     return render_template('search.html', labels=table_name)


