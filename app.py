from bottle import get,post,route,run,template,TEMPLATE_PATH,request,redirect,static_file
import os
import math
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

TEMPLATE_PATH.insert(0,"./views")
root=os.getcwd()

#------------------------------------------------------------------------------------------------
#                                   DATABASE CONNECTIVITY
#------------------------------------------------------------------------------------------------
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["KerasApp"] #appName
user= db["user"] #collectionName




#------------------------------------------------------------------------------------------------
#                                          ROUTES
#------------------------------------------------------------------------------------------------


@route('/static/<filepath:path>')
def serve_static(filepath):
    myroot=os.path.join(root,"static")
    return static_file(filepath,root=myroot)


@get('/test')
def test():
    user.insert({"name":"deepak","age":22})
    return "Success!!"


@get('/')
@get('/home')
def home():
    return template('home')
    


#--------------------------------------------------------------------------------------------------
#                                          SERVER
#--------------------------------------------------------------------------------------------------	


run(host="localhost",port=8997,debug=True)
#run(host="0.0.0.0",port=int(os.environ.get('PORT',5000)))
