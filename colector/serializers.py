from rest_framework import serializers
from colector.models import Error, Station, OnlineStations, NewConfig, Emails


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['name']


class ErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Error
        fields = ['station', 'msg', 'time', 'is_sent']


class OnlineStationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineStations
        fields = ['pk', 'station', 'last_request', 'new_config', 'info']


class NewConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewConfig
        fields = ['station', 'is_get', 'out1', 'out2', 'out3', 'status']

class EmailsSrializer(serializers.ModelSerializer):
    class Meta:
        model = Emails
        fields = ['station', 'email']

"""
    def update(self, request, *args, **kwargs):
        '''Changes the title or the content'''
        return None

"""

"""
class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'


class ErrorSerializer(serializers.ModelSerializer):
    station = serializers.CharField()
    msg = serializers.CharField()
    time = serializers.DateTimeField(read_only=True)
    is_sent = serializers.BooleanField(read_only=True)
    pk = serializers.IntegerField(read_only=True)

    class Meta:
        model = Error
        fields = '__all__'


    def create(self, validated_data):
        
        return Error.objects.create(**validated_data)

    def update(self, instance, validated_data):
        
        instance.station = validated_data.get('station', instance.station)
        instance.msg = validated_data.get('msg', instance.msg)
        instance.time = validated_data.get('time', instance.time)
        instance.is_sent = validated_data.get('is_sent', instance.is_sent)
        instance.save()
        return instance
        
        class OnlineStationsSerializer(serializers.Serializer):
    station = serializers.CharField()
    last_request = serializers.DateTimeField(read_only=True)
    new_config = serializers.BooleanField(default=False)
    info = serializers.CharField(max_length=128)
    pk = serializers.IntegerField(read_only=True)

    class Meta:
        model = OnlineStations
        fields = '__all__'

    def create(self, validated_data):
        print('======================')
        print(validated_data)
        return OnlineStations.objects.create(**validated_data)


    def update(self, instance, validated_data):
        print('======================')
        print(validated_data)
        instance.station = validated_data.get('station', instance.station)
        instance.last_request = validated_data.get('last_request', instance.last_request)
        instance.new_config = validated_data.get('new_config', instance.new_config)
        instance.info = validated_data.get('info', instance.info)
        instance.save()
        return instance
"""


