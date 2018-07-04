# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Image
from django.shortcuts import render
from django.http import HttpResponse
from time import gmtime, strftime
import random
import json
import base64
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def postImage(request):
        if request.method != 'POST':
            return HttpResponse("please send a post request")

        # get the userUUID and the base64 string from the post request as a json object
        jsonObj = json.loads(request.body)
        userUUID = jsonObj['userUUID']
        base64String = jsonObj['base64']

        #insert at the database
        Image.objects.create(userUUID=userUUID, base64=base64String)

        #create a unique filename for storage which consists of: userUUID__< current time > 
        fileName = userUUID + "__" +  strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ".jpg"

        #store the image as a file in the file system
        with open(fileName, "wb") as fh:
            fh.write(base64.b64decode(base64String))


        #now pass the file to the model????????

        #here we should return the result of the model.
        return HttpResponse("Done")



