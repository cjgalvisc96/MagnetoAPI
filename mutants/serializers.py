from rest_framework import serializers


class DNAInputSerializer(serializers.Serializer):
    dna = serializers.ListSerializer(child=serializers.CharField())


class StatsOutputSerializer(serializers.Serializer):
    count_mutant_dna = serializers.IntegerField()
    count_human_dna = serializers.IntegerField()
    ratio = serializers.FloatField()
