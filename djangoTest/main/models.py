from django.db import models
import sqlite3
from djangoTest import settings

class DB():
    dbName = ''

    def __init__(self, dbName):
        self.dbName = dbName

    connect = sqlite3.connect(dbName)
    cursor = sqlite3.Cursor(connect)

countTown = 0
countCountry = 0

class Town(models.Model):
    id = models.CharField(primary_key=True, max_length=200)#models.ForeignKey (settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    id_country = models.CharField(max_length=200)#models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING())

    def publish(self):
        global countTown
        self.id = countTown + 1
        self.save()

    def __str__(self):
        return (self.id, self.name, self.id_country)

    def create(self, name, id_country):
        self.name = name
        self.id_country = id_country

    def getID(self):
        return self.id

    def update(self, id, name, id_country):
        self.name = name
        self.id_country = id_country

    def delete(self, id):
        self.id = id


class Country(models.Model):
    id = models.CharField(primary_key=True, max_length=200)#models.ForeignKey (settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    picture = models.CharField(max_length=200)
    flag = models.CharField(max_length=200)
    vize = models.BooleanField()
    price = models.FloatField()

    def publish(self):
        self.id = countCountry + 1
        self.save()

    def __str__(self):
        return (self.id, self.name, self.picture, self.flag, self.vize, self.price)

    def create(self, name, picture, flag, vize, price):
        self.name = name
        self.picture = picture
        self.vize = vize
        self.price = price
        self.flag = flag

    def update(self, id, name, picture, flag, vize, price):
        self.name = name
        self.picture = picture
        self.vize = vize
        self.price = price
        self.flag = flag

    def delete(self, id):
        self.id = id