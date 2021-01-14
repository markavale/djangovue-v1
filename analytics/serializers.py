from rest_framework import serializers
from .models import PageVisit, TextMessage

class PageVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageVisit
        fields = '__all__'
        extra_kwargs = {
            'ip': {'read_only': True}
            }

class TextMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextMessage
        fields = '__all__'
        extra_kwargs = {
            'ip': {'read_only': True}
            }

    # def save(self, *args, **kwargs):
    #     x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')

    #     if x_forwarded_for:
    #         ipaddress = x_forwarded_for.split(',')[-1].strip()
    #     else:
    #         ipaddress = self.request.META.get('REMOTE_ADDR')

    #     sender= TextMessage() #imported class from model
    #     sender.ip= ipaddress
    #     sender.save()