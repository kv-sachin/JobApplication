from rest_framework.serializers import ModelSerializer
from testapp.models import hydjobs, punejobs, blorejobs, chennaijobs, noidajobs, indorejobs


class HydJobsSerializer(ModelSerializer):
    class Meta:
        model = hydjobs
        fields = '__all__'


class PuneJobsSerializer(ModelSerializer):
    class Meta:
        model = punejobs
        fields = '__all__'


class BloreJobsSerializer(ModelSerializer):
    class Meta:
        model = blorejobs
        fields = '__all__'


class ChennaiJobsSerializer(ModelSerializer):
    class Meta:
        model = chennaijobs
        fields = '__all__'


class NoidaJobSerializer(ModelSerializer):
    class Meta:
        model = noidajobs
        fields = '__all__'

class IndoreJobSerializer(ModelSerializer):
    class Meta:
        model = indorejobs
        fields = '__all__'