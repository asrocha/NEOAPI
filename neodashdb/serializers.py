from rest_framework import serializers
from .models import Assets, Scans,Vulns


class AssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = '__all__'


class ScansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scans
        asset = serializers.StringRelatedField(many=True)
        fields = ('date', 'success','running')


class VulnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vulns
        fields = '__all__'








#tokens


class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)