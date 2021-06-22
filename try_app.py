import n_d
from flask import Flask, request, render_template
import random
app = Flask(__name__)
# @app.route("/")
# def index():
#     return render_template("index.html")

table_name = ["提案人資料", "聯絡窗口", "募資方案", "募資方式", "贊助者資料", "已完成訂單"]





@app.route('/')
def show_index():
    t = n_d.DataBase()
    #content = t.join(table_name[2], table_name[0], where=None)
    content = t.base_show(table_name[2])
    return render_template('sql_show.html', labels=content[0], content=content[1])





if __name__ == "__main__":
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
