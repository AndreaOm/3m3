# -*- coding: utf-8 -*-
from flask import Flask,request
import thread,time,itchat
from itchat.content import *

# config start
nickname = 'zzz' #config your master weixin Nickname
PORT = 9880 #flask port
sckey = 'zzz' #secret key can protect you api
# config end

app = Flask(__name__)

itchat.auto_login(hotReload=True, enableCmdQR=2)
#itchat.auto_login(hotReload=True) #if you are run in windows can use this
thread.start_new_thread(itchat.run, ())

@app.route('/'+sckey+'.push')
def push():
	try:
		text = request.args.get('t')
		me = itchat.search_friends(name=nickname)[0]['UserName']
		itchat.send(msg=text, toUserName=me)
		return 'success'
	except:
		return 'error'

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=PORT,threaded=True,debug=False)
	while 1:
		itchat.configured_reply()
		time.sleep(1)