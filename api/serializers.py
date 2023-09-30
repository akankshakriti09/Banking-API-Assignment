from rest_framework import serializers
from .models import Bank,Branch,Banklist

class BankListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banklist
        fields = ['id', 'name']

class BranchSerializer(serializers.HyperlinkedModelSerializer):
    bank = serializers.CharField(source='bank.name')
    class Meta:
        model = Branch
        fields = [ 'url', 'ifsc', 'branch', 'bank_id' , 'bank' , 'address', 'city', 'district', 'state']

class BankSerializer(serializers.ModelSerializer):
    Branch_List = BranchSerializer(many=True, read_only=True)  # Nested Serializer
    class Meta:
        model = Bank
        fields = ['id', 'name', 'Branch_List']
        