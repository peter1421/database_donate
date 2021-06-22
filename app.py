from flask import Flask, request, render_template
import random
app = Flask(__name__, static_folder="static", static_url_path="/")
import try_D


table_name = ["提案人資料", "聯絡窗口", "募資方案", "募資方式", "贊助者資料", "已完成訂單"]



@app.route('/')
def show_index():
    t =try_D.DataBase()
    content = t. base_show(table_name[2])
    return render_template('sql_show.html', labels=content[0], content=content[1])


@app.route('/welcome')
def show_welcome():
    return render_template('index.html')



@app.route('/all_prouser')
def show_all_prouser():
    t = try_D.DataBase()
    content = t. base_show(table_name[0])
    return render_template('sql_show.html', labels=content[0], content=content[1])


@app.route('/all_spouser')
def show_all_spouser():
    t = try_D.DataBase()
    content = t. base_show(table_name[4])
    return render_template('sql_show.html', labels=content[0], content=content[1])

@app.route('/all_pro')
def show_all_pro():
    t = try_D.DataBase()
    content = t. base_show(table_name[2])
    return render_template('sql_show.html', labels=content[0], content=content[1])


@app.route('/prouser')
def show_prouser():
    try:
        name = "'n{}'".format(str(request.args.get("prouser", "")))
    except:
        name=None
    t = try_D.DataBase()
    content = t. base_show(table_name[0], table_name[1], where=name)
    return render_template('sql_show.html', labels=content[0], content=content[1])


@app.route('/spouser')
def show_spouser():
    try:
        name = "'p{}'".format(str(request.args.get("spouser", "")))
    except:
        name = None
    t = try_D.DataBase()
    content = t. base_show(table_name[4], table_name[1], where=name)
    return render_template('sql_show.html', labels=content[0], content=content[1])


@app.route('/pro')
def show_pro():
    try:
        name = "'{}'".format(str(request.args.get("pro", ""))) 
    except:
        name = None
    t = try_D.DataBase()
    content = t. base_show(table_name[2], where=name)
    return render_template('sql_show.html', labels=content[0], content=content[1])



@app.route('/self_search')
def self_search():
    table1 = request.args.get("table1", "")
    table2 = request.args.get("table2", "")
    arr = request.args.get("arr", "")
    val = "'{}'".format(str(request.args.get("val", "")))
    t = try_D.DataBase()
    content = t. base_show(table1, table2,where=val,arr=arr)
    return render_template('sql_show.html', labels=content[0], content=content[1])


@app.route('/search')
def search():
    return render_template('search.html', labels=table_name)


@app.route('/all_order')
def show_all_order():
    t = try_D.DataBase()
    content = t. base_show(table_name[5])
    return render_template('order.html', labels=content[0], content=content[1])


@app.route('/add_order')
def show_add_order():
    spo_id = "{}".format(str(request.args.get("spo_id", "")))
    way_id = "{}".format(str(request.args.get("way_id", "")))
    t = try_D.DataBase()
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


if __name__=="__main__":
    app.run(port=3000)


# @app.route("/cal")
# def index_c():
#     max = int(request.args.get("max", ""))
#     result = 0
#     for x in range(1, max+1):
#         result += x
#     return render_template("result.html", data=result)


# @app.route("/show")
# def index_s():
#     name = request.args.get("n", "")
#     return "歡迎"+name


# @app.route("/page")
# def index_p():
#     return render_template("page.html")


