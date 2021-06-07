from django.db import models

ACTIONS = (
	('1', 'first'),
	('2', 'second'),
)

DESTIONATIONS = (
	('prm', 'Первичное'),
	('sec', 'Вторичное')
)

# class EntryModel(models.Model):
# 	name = models.CharField(max_length = 100)
# 	age = models.IntegerField()
# 	destination = models.ChoiceField(choices=ACTIONS)
# 	phone = models.CharField(max_length="11")
# 	action = models.ChoiceField(choices=DESTIONATIONS)