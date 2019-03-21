# coding=utf-8
from flask import *
from flask_qrcode import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def get_data():
    defcol1 = '0-0-0'
    defcol2 = '255-255-255'
    if request.method == "POST":
        text = request.form["text"]
        #colorv = request.form["color"]
        select = request.form.get('comp_select')
        select2 = request.form.get('comp_select2')
        if(str(select)=='Black'):
           colord = '0-0-0'
           defcol1 = colord
        elif(str(select)=='White'):
            colord = '255-255-255'
            defcol1 = colord
        elif(str(select)=='Red'):
            colord = '255-0-0'
            defcol1 = colord
        elif(str(select)=='Green'):
            colord = '0-255-0'
            defcol1 = colord
        elif(str(select)=='Blue'):
            colord = '0-0-255'
            defcol1 = colord
        if(str(select2)=='White'):
            colord2 = '255-255-255'
            defcol2 = colord2
        elif(str(select2)=='Black'):
            colord2 = '0-0-0'
            defcol2 = colord2
        elif(str(select2)=='Red'):
            colord2 = '255-0-0'
            defcol2 = colord2
        elif(str(select2)=='Green'):
            colord2 = '0-255-0'
            defcol2 = colord2
        elif(str(select)=='Blue'):
            colord2 = '0-0-255'
            defcol2 = colord2
        return render_template('index.html',name = text, colorv = colord, colorb = colord2,data=[{'name':'Black'}, {'name':'Green'}, {'name':'Blue'},{'name':'Red'}],
        data2=[{'name':'White'}, {'name':'Green'}, {'name':'Blue'},{'name':'Black'},{'name':'Red'}])
    else:
        return render_template('index.html', data=[{'name':'Black'}, {'name':'White'}, {'name':'Red'},{'name':'Green'},{'name':'Blue'}],
        data2=[{'name':'White'}, {'name':'Black'}, {'name':'Red'},{'name':'Green'},{'name':'Blue'}])        


