# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import base64
from django.db import models

# Create your models here.

class ImageManager(models.Manager):
    def createxs(self, userUUID, base64):
        image = self.create(userUUID=userUUID, base64=base64)
        return image
        
class Image(models.Model):
    userUUID = models.CharField(max_length=200)
    base64 = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    objects = ImageManager()

    def __str__(self):
        return base64.decodestring(self.base64)
    def getBase64(self):
        return self.base64
