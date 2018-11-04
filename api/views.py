# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Image
from django.shortcuts import render
from django.http import HttpResponse
from time import gmtime, strftime
import random
import json
import base64
import cv2
import keras
import tensorflow 
import numpy as np



# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def postImage(request):
        if request.method != 'POST':
            return HttpResponse("please send a post request")

        # get the userUUID and the base64 string from the post request as a json object
        jsonObj = json.loads(request.body.decode('utf-8'))
        userUUID = jsonObj['userUUID']
        base64String = jsonObj['base64']
      
      
        #insert at the database
        Image.objects.create(userUUID=userUUID, base64=base64String)


        # # #create a unique filename for storage which consists of: userUUID__< current time > 
        # fileName = userUUID + "__" +  strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ".jpg"

        # # #store the image as a file in the file system
        # with open(fileName, "wb") as fh:
        #     fh.write(base64.b64decode(base64String))

        # convert the base64 string to an image object
        img = base64.b64decode(base64String); 
        npimg = np.fromstring(img, dtype=np.uint8); 

        #pass the image to open cv
        im = cv2.imdecode(npimg, 1)

        #resize the image
        # im = cv2.imread(fileName)
        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        im = np.array(im).astype('float32')
        im = im / 255.0
        im = cv2.resize(im, (256,256), interpolation=cv2.INTER_CUBIC)
        im = np.expand_dims(im, axis=0)
        # import the model and graph session from settings
        from django.conf import settings
        model=settings.MODEL
        graph=settings.GRAPH


        #predict
        with graph.as_default():
            result = model.predict(im)
            print("model1 = ")
            print(result[0])


        if(result[0] > 0.75):
            HttpResponse([1])
        else:
            HttpResponse([0])

        return HttpResponse(result)



