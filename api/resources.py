from tastypie.resources import ModelResource
from api.models import Image
from tastypie.authorization import Authorization

class ImageResource(ModelResource):
    class Meta:
        queryset = Image.objects.all()
        resource_name = 'image'
        authorization = Authorization()
        fields = ['userUUID', 'base64'] #Limiting Fields, will only return this


