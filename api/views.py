from api.serializers import BankSerializer, BranchSerializer, BankListSerializer
from rest_framework import viewsets
from .models import Bank, Branch, Banklist
from api import paginations

# Create your views here.
class BankViewSet(viewsets.ModelViewSet):
    queryset = Banklist.objects.all()
    serializer_class = BankListSerializer
    pagination_class = paginations.BankListPagination

class Bank_with_BranchesViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all() 
    serializer_class = BankSerializer  
    pagination_class = paginations.BankPagination

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    pagination_class = paginations.BranchPagination

    def get_queryset(self):
        branch = self.request.query_params.get('branch')
        bank_name = self.request.query_params.get('bank')
        queryset = Branch.objects.all()
        if branch is not None:
            queryset = queryset.filter(branch=branch.upper())
        if bank_name is not None:
            bank_id = None
            try:
                bank_id = Bank.objects.get(name=bank_name.upper())
            except Bank.DoesNotExist as err:
                pass
            queryset = queryset.filter(bank=bank_id)
        return queryset