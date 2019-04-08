from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
  """
  Defines the game object
  """
  start_date = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ["-start_date"]

  def __str__(self):
    return self.get_base36_id()

  def get_base36_id(self):
    """
    Returns a n character base 36 encoded string which identifies the game
    :return: str
    """
    result = "000000"
    char_set = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    offset = len(result)
    num = self.pk

    while num > 0:
      num, rem = divmod(num, len(char_set))
      result += char_set[rem]

    return result[-offset:]


class Character(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
  game_id = models.ForeignKey(Game, on_delete=models.CASCADE, null=False)
  name = models.CharField(max_length=200, blank=False)
  race = models.CharField(max_length=60)
  alive = models.BooleanField(default=True)
  martial_stat = models.IntegerField(default=0)
  intrigue_stat = models.IntegerField(default=0)
  control_stat = models.IntegerField(default=0)
  finance_stat = models.IntegerField(default=0)
  charisma_stat = models.IntegerField(default=0)

  class Meta:
    ordering = ["game_id", "alive", "user_id"]

  def __str__(self):
    return self.name