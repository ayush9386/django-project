from rest_framework import serializers
from restapi.models import student

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = student
        fields = ['id' , 'name', 'score' ]
    

