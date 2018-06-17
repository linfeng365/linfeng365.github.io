
import requests
import json

from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
	return render_template('key.json') # template 目录下的 key.json 或 SpaceFn.json 文件。

if __name__ == '__main__':
    app.run()


