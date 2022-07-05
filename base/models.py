from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=200) 
    def __str__(self): 
        return self.name

# a room can have only one topic 
# where as a topic can have multiple rooms
class Room(models.Model):
    host =  models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    topic =  models.ForeignKey(Topic, on_delete=models.SET_NULL, null = True)
    name = models.CharField(max_length=200) # textfield
    description = models.TextField(null=True , blank=True) # by default it false ie if true it cannot be blank 
    # participants =
    updated = models.DateTimeField(auto_now=True)
    # everytime the save method triggered then take a snap shot of the time
    created = models.DateTimeField(auto_now_add=True) 
    # initial time stamp
    def __str__(self):
        return self.name 

# one to many relationship
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # when the user is deleted then what should happen to the messages 
    # if set_null then they will stay 
    # if cascade then messages also deleted
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField() 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.body[0:50]

