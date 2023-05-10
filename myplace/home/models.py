from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.

class Prefectures(models.Model):
    prefecture_code = models.CharField(verbose_name='都道府県コード',null=True,blank=True)
    name = models.CharField(verbose_name='都道府県名',null=True,blank=True)
    name_kana = models.CharField(verbose_name='都道府県カナ名',null=True,blank=True)
    name_eng = models.CharField(verbose_name='都道府県英名',null=True,blank=True)
    prefectural_capital = models.ForeignKey('Municipality',verbose_name='県庁所在地',null=True,blank=True,on_delete=models.SET_NULL)
    history = HistoricalRecords()


class Municipality(models.Model):
    municipality_code = models.CharField(verbose_name='市区町村コード',null=True,blank=True)
    name = models.CharField(verbose_name='市区町村名',null=True,blank=True)
    name_kana = models.CharField(verbose_name='市区町村カナ名',null=True,blank=True)
    name_eng = models.CharField(verbose_name='市区町村英名',null=True,blank=True)
    prefecture = models.ForeignKey(Prefectures,verbose_name='所属都道府県',null=True,blank=True,on_delete=models.SET_NULL)
    history = HistoricalRecords()
