from django.db import models

# Create your models here.
class Room(models.Model):
  room_name = models.CharField(max_length=50)

  def __str__(self):
    return self.room_name


# Create your models here.
class Message(models.Model):
  room_name = models.ForeignKey(Room, on_delete=models.CASCADE)
  message = models.CharField(max_length=100)
  sender = models.CharField(max_length=50)

  def __str__(self):
    return self.message

