from rest_framework import serializers
from .models import Tone, Summary

class ToneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tone
        fields = ['id', 'name']


class SummarySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    tone_name = serializers.ReadOnlyField(source='tone.name')

    class Meta:
        model = Summary
        fields = [
            'id',
            'text',
            'summary_text',
            'tone',
            'tone_name',
            'created_at',
            'user'
        ]