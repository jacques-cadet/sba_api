from .models import EtranLoan, Demographics, Race, LookupDisbursedPPPLoan, ForgivenessDocs
from rest_framework import serializers


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = "__all__"


class DemographicsSerializer(serializers.ModelSerializer):
    race = RaceSerializer()

    class Meta:
        model = Demographics
        fields = [f.name for f in Demographics._meta.fields] + ['race']


class EtranLoanSerializer(serializers.ModelSerializer):
    demographics = DemographicsSerializer()

    class Meta:
        model = EtranLoan
        fields = ['url'] + \
            [f.name for f in EtranLoan._meta.fields] + ['demographics']


class LookupDisbursedPPPLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = LookupDisbursedPPPLoan
        fields = "__all__"


class ForgivenessDocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForgivenessDocs
        fields = "__all__"
