from django.db import models

# Create your models here.

TOTAL_BUDGET = 100

class Team(models.Model):
    name = models.CharField(max_length=100, default="")
    owner = models.CharField(max_length=100, default="")
    remaining_budget = models.FloatField(default=TOTAL_BUDGET)
    total_players = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def count_players(self):
        return len(self.players.all().order_by("-rating"))

    def calculate_budget(self):
        count = 0
        for player in self.players.all():
            count += player.selling_price
        print(self.players.all())
        return TOTAL_BUDGET - count

    def save(self, *args, **kwargs):
        self.total_players = self.count_players()
        self.remaining_budget = self.calculate_budget()
        super(Team, self).save(*args, **kwargs)
    

class Player(models.Model):
    name = models.CharField(max_length=100, default="")
    base_price = models.FloatField(default=0)
    selling_price = models.FloatField(default=0)
    rating = models.FloatField(default=0)
    team = models.ForeignKey(Team, on_delete = models.PROTECT, null = True, blank = True, related_name="players")

    def __str__(self):
        return self.name
    
