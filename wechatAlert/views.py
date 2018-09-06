#coding=utf-8  
from django.http import HttpResponse
from django.shortcuts import render
import itchat
import json
import os

def login(request):
	itchat.auto_login(enableCmdQR=True);
	#uuid = itchat.get_QRuuid(self);
	redict = {};
	redict["status"] = 0;
	redict["info"] = "login success."
	return HttpResponse(json.dumps(redict));
	

def logout(request):
	itchat.logout();
	redict = {};
        redict["status"] = 0;
        redict["info"] = "logout success."
	return HttpResponse(json.dumps(redict));

def sendMsg(request):
	msg = nodename=request.POST['msg'];
	redict = {}
	user = unicode(os.environ["WECHAT_ALERT_USER"],"utf-8");
	users = itchat.search_friends(name=user);
	userName = users[0]['UserName'];
	sendRes = itchat.send(msg, toUserName=userName);
	print sendRes;
	if sendRes[u"BaseResponse"][u'Ret'] == 0:
		redict["status"] = 0;
       		redict["info"] = "send success.";
	else:
		redict["status"] = 400;
                redict["info"] = "send failed.";
	return HttpResponse(json.dumps(redict));
	
