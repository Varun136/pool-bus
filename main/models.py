from django.db import models

class Bus(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    register_number = models.CharField(max_length=20, blank=False, null=False)

    class Meta:
        db_table = 'bus'

    def __str__(self):
        return self.name


class Stop(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)

    class Meta:
        db_table = 'stop'

    def __str__(self):
        return self.name

class Route(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    order_number = models.IntegerField()

    class Meta:
        db_table = "route"

    def __str__(self):
        return "{}-{}".format(self.bus.name, self.stop.name)