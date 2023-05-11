from django.db import models
# Create your models here.


class ConferenceRoom(models.Model):
    name_room = models.CharField(max_length=255, unique=True)
    capacity_room = models.IntegerField(null=False)
    projector_available = models.BooleanField()


class ReserveRoom(models.Model):
    date_reservation = models.DateField()
    id_room = models.ForeignKey(ConferenceRoom, on_delete=models.CASCADE)
    comment_reservation = models.CharField()

    class Meta:
        unique_together = ('date_reservation', 'id_room')
