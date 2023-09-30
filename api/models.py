from django.db import models

# Create your models here.
class Banklist(models.Model):
    name = models.CharField(max_length=49)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = False
        db_table = 'banks'
        verbose_name_plural = 'Bank'

class Bank(models.Model):
    name = models.CharField(max_length=49)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = False
        db_table = 'banks'
        verbose_name_plural = 'Bank '

class Branch(models.Model):
    ifsc = models.CharField(max_length=11)
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)
    bank_name = models.CharField(max_length=255)
    bank = models.ForeignKey(Bank,on_delete=models.CASCADE,related_name='Branch_List')

    def __str__(self):
        return self.branch
    
    class Meta:
        managed = False
        db_table = 'branches'
        verbose_name_plural = 'Branches'

