from flask import Flask, request, make_response, redirect, render_template

from repositories.mysql.mysql_db import MySqldb
import re

app = Flask(__name__)

cn = MySqldb()


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == 'POST':

        db_config = {
            "host":request.form["host"],
            "user":request.form["user"],
            "password":request.form["password"],
            #"database": request.form["database"] if request.form["database"] else 'mysql',
            "database": request.form["database"] if request.form["database"] else '',
            "port":request.form["port"]
        }

        context = {
            "error":""
        }

        try:
            cn.connect(True, db_config)
            return redirect("/editor")
        except Exception as err:
            context["error"] = f"{err}"
            return render_template("index.html",**context)

    if request.method == 'GET':
        if cn.connection:
            return redirect("/editor")
        
        return render_template("index.html")


def getType(command:str):
    command = command.lower()
    if command in ["select","show","desc", "describe"]:
        return 1
    elif command in ["update","insert","delete","create","drop","alter","grant","revoke"]:
        return 0
    elif command in ["use"]:
        return 2
    else:
        return -1
    
def searchParams(query:str):
    params = re.findall(r"'(.*?)'", query)
    paramsNew = []
    count = 0
    for parm in params:
        count+=1
        paramsNew.append({"nombre":f"parm{count}","valor":parm})
        query = query.replace(f"'{parm}'",f"%s")

    return query, paramsNew

@app.route("/editor", methods=["GET","POST"])
def editor():
    
    if cn.connection is None:
        return redirect("/")
    
    context = {
        "query":"",
        "data":[],
        "message":"",
        "warning":"",
        "error":"",
        "database":"",
        "access_db":[],
        "user":""
    }

    try:
        database = cn.execute_insert("select database() as dbname",[])
        context["database"] = database[0]["dbname"]
    except:
        pass

    try:
        user = cn.execute_insert("select user() as dbuser",[])
        context["user"] = user[0]["dbuser"]
        databases = cn.execute_insert("show databases",[])
        context["access_db"] = databases
    except:
        pass

    if request.method == 'POST':
        action = request.form["inpMethod"].strip()
        query = request.form["Textarea"].strip()
        context["query"] = query

        if action == 'command':
            type = getType(query.split(" ")[0])

            if type == -1:
                context["error"] = f"Comando no soportado"
                return render_template("editor.html", **context)

            query2, params = searchParams(query)
            ret = cn.execute_insert(query2,params)

            try:
                error = ret['OOPS']
                if error == "ERROR MySQL Connection not available.":
                    cn.close_connection()
                    return redirect("/")
                else:
                    context["error"] = error

            except:
                if type == 0:
                    context["message"] = f"Query Ok, {ret} row affected"  
                elif type == 1:
                    context["data"] = ret
                    if len(ret) == 0:
                        context["warning"] = f"Empty"
                elif type == 2:
                    database = cn.execute_insert("select database() as dbname",[])
                    context["database"] = database[0]["dbname"]
                    context["message"] = f"Database changed"
 
        
        if action == 'commit':
            cn.commit_transaction()
            context["message"] = f"Query Ok"
        
        if action == 'rollback':
            cn.rollback()
            context["message"] = f"Query Ok"
        
        if action == 'exit':
            cn.close_connection()
            return redirect("/")
        
        return render_template("editor.html", **context)


    if request.method == "GET":
        return render_template("editor.html", **context)
    

@app.route("/changedb/<dbname>", methods=["GET","POST"])
def changedb(dbname):
    cn.execute_insert(f"use {dbname}",[])
    return redirect("/editor")


app.run(host='0.0.0.0', port=8095, debug=True)