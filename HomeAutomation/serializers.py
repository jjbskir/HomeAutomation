from rest_framework import serializers
from HomeAutomation.models import Lamp

class LampSerializer(serializers.ModelSerializer):
    '''
    Lamp object serializer.
    '''
    class Meta:
        model = Lamp
        fields = ('id', 'state', 'name', 'date')
