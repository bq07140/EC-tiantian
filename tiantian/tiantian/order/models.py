#coding=utf-8
from django.db import models

#订单模型
class OrderInfo(models.Model):
	user = models.CharField(max_length=20)
	ototal = models.DecimalField(max_digits=10,decimal_places=2)
	state = models.BooleanField(default=False)

class OrderDetailInfo(models.Model):
	order = models.ForeignKey('OrderInfo')
	goods = models.CharField(max_length=20)
	# CommaSeparatedIntegerField逗号分隔的整数，IntegerField 整数
	count = models.IntegerField(max_length=None)
	price = models.DecimalField(max_digits=20,decimal_places=2)

#购物车数据
class CartInfo(models.Model):
	user = models.CharField(max_length=20)
	goods = models.CharField(max_length=20)
	count = models.IntegerField(max_length=None)
	isDelete = models.BooleanField(default=False)

	class Meta():
		db_table = 'cartinfo'
