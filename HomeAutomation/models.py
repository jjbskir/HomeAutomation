from django.db import models

class Lamp(models.Model):
    '''
    The lamp model that represents which lamp and it's current state.
    id: unique id. Automatically added.
    state: on/off, 1/0.
    name: light, type of application.
    date: last time used.
    
    SQL:
    CREATE TABLE "HomeAutomation_lamp" (
    "id" integer NOT NULL PRIMARY KEY,
    "state" integer NOT NULL,
    "name" varchar(100) NOT NULL,
    "date" date NOT NULL)
    '''
    state = models.IntegerField(default=0)
    name = models.CharField(max_length=100, default='lamp')
    date = models.DateField(auto_now=True)