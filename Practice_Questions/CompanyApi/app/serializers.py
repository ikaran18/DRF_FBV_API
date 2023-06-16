from .models import Company
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
    
    def update(self, company_detail , validated_data):
        newcompany = Company(**validated_data)
        newcompany.id = company_detail.id
        newcompany.save()
        return newcompany