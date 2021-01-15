from rest_framework import serializers
from . models import Mail, Rating, Skipper


class MailSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class SkipperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skipper
        fields = '__all__'