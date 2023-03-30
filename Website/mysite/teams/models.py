from django.db import models

# Create your models here.
class Team(models.Model):
    team_name = models.CharField(max_length=100)
    team_record = models.CharField(max_length=10)
    team_id = models.IntegerField()
    
    def __str__(self):
        for item in (self.team_name, self.team_record):
            return item