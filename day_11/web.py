# -*- coding: utf-8 -*-
# @date       ：2024年04月02日 17:16:44
# @author     ：李龙威
# @className  ：web.py
# @describe   ：自动化
# @packageName：Django

from flask import Flask,render_template

app = Flask(__name__)


@app.route('/show/info')
def index():
    return render_template('index.html')


@app.route('/show/excel')
def excel():
    return render_template('excel.html')


if __name__ == '__main__':
    app.run()
