# -*- coding: utf-8 -*-

from flask import Flask, request, Response, send_file
import re
import requests, json, flask, os, datetime
from api.image import save_image

app = Flask(__name__, static_folder='dist', static_url_path='')

proxyHost = ''
# api接口基础路径
apiUri = '/api/v1'
# 静态文件地址基础路径
baseUri = '/'

@app.before_request
def before_request():
  # 设置反向代理
  path = request.full_path
  pattern = re.match(apiUri, path)
  if proxyHost != '' and pattern :
    method = request.method
    data = request.data or request.form or None
    headers = dict()
    for name, value in request.headers:
      if not value or name == 'Cache-Control':
        continue
      headers[name] = value

    r = requests.request(method, proxyHost + path, headers=headers, data=data, stream=True)
    resp_headers = []
    for name, value in r.headers.items():
      if name.lower() in ('content-length', 'connection', 'content-encoding') :
        continue
      resp_headers.append((name, value))
    return Response(r, status=r.status_code, headers=resp_headers)
  elif re.match('/images', path) and os.path.isfile('.' + request.path) :
    # 返回images下的图片
    return send_file('.' + request.path)
    

@app.route(apiUri + "/upload-image", methods=['POST'])
def upload_image () :
  method = request.method
  file = request.files['img']
  if method == 'POST' and file :
    imgUrl = save_image(file.stream)
    return str(imgUrl)
  else :
    return 'other'

@app.route('/download/image')
def down_load () :
  return send_file('./images/584e0d51534b6.jpg', as_attachment=True)

@app.errorhandler(404)
def catch_all(err):
  return app.send_static_file("index.html")

app.run(host='127.0.0.1', port='9000', debug=False)