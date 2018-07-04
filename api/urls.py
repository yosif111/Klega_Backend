from django.conf.urls import url, include

from . import views

urlpatterns = [
    # ex: /api/postImage
    url('postImage', views.postImage, name='postImage'),

   # ex: /api/
    url('', views.index, name='index'),

]

