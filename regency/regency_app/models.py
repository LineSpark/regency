from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
  """
  Defines the game object
  """
  start_date = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=60, null=True, blank=True)

  class Meta:
    ordering = ["-start_date"]

  def __str__(self):
    return self.get_base36_id() + "{}".format(" - {}".format(self.name.capitalize()) if self.name.strip() else "")

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

  get_base36_id.short_description = 'Game Id'


class Player(models.Model):
  name = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
  game = models.ForeignKey(Game, on_delete=models.CASCADE, null=False)

  class Meta:
    unique_together = (("name", "game"),)

  def __str__(self):
    return "{}".format(self.name)


class Character(models.Model):
  player = models.ForeignKey(Player, on_delete=models.CASCADE, null=False)
  name = models.CharField(max_length=200, blank=False)
  race = models.CharField(max_length=60)
  alive = models.BooleanField(default=True)
  martial_stat = models.IntegerField(default=0, verbose_name="Martial")
  intrigue_stat = models.IntegerField(default=0, verbose_name="Intrigue")
  control_stat = models.IntegerField(default=0, verbose_name="Control")
  finance_stat = models.IntegerField(default=0, verbose_name="Finance")
  charisma_stat = models.IntegerField(default=0, verbose_name="Charisma")

  class Meta:
    ordering = ["alive", "player_id"]

  def __str__(self):
    return self.name


class Turn(models.Model):
  game = models.ForeignKey(Game, on_delete=models.DO_NOTHING, null=False)
  current_turn = models.BooleanField(default=True)
  turn = models.IntegerField(verbose_name="Turn Number")

  class Meta:
    ordering = ["game_id", "-turn"]

  def __str__(self):
    return "Turn {}: {}".format("(current)" if self.current_turn else "", self.turn)


class Region(models.Model):
  REGIONS = (
    ("ZUL", "Zulia"),
    ("ULE", "Ule"),
    ("DAX", "Daxia"),
    ("WI", "Western Isles"),
    ("CHE", "Cherobek"),
    ("SAY", "Sayenne"),
  )

  name = models.CharField(max_length=30, choices=REGIONS)

  def __str__(self):
    return self.name


class Orders(models.Model):
  character = models.ForeignKey(Character, on_delete=models.DO_NOTHING, null=False, limit_choices_to={"alive": True})
  turn = models.ForeignKey(Turn, on_delete=models.DO_NOTHING, null=False)

  COMMAND_TYPES = (
    ("Tax", "Tax"),
    ("Trade", "Trade"),
    ("Income", "Income"),
    ("Move", "Move"),
    ("Train", "Train"),
    ("Disband", "Disband"),
    ("Scheme", "Scheme"),
    ("Bribe", "Bribe"),
    ("Assas", "Assassinate"),
    ("Theft", "Theft"),
    ("Skill", "Advance Skill"),
    ("Hide", "Hide"),
    ("Contest", "Contest"),
    ("Spawn", "Insight Rebellion"),
    ("Petition", "Petition the Gods"),
  )

  command_1_type = models.CharField(max_length=10, choices=COMMAND_TYPES, blank=False, null=True, verbose_name="Command")
  command_1_player_target = models.ForeignKey(Player, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='player_target_1', verbose_name="Player")
  command_1_region_source = models.ForeignKey(Region, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='region_source_1', verbose_name="From Region")
  command_1_region_target = models.ForeignKey(Region, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='region_target_1', verbose_name="To Region")
  command_2_type = models.CharField(max_length=10, choices=COMMAND_TYPES, blank=False, null=True, verbose_name="Command 2")
  command_2_player_target = models.ForeignKey(Player, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='player_target_2', verbose_name="Player")
  command_2_region_source = models.ForeignKey(Region, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='region_source_2', verbose_name="From Region")
  command_2_region_target = models.ForeignKey(Region, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='region_target_2', verbose_name="To Region")
  command_3_type = models.CharField(max_length=10, choices=COMMAND_TYPES, blank=False, null=True, verbose_name="Command 3")
  command_3_player_target = models.ForeignKey(Player, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='player_target_3', verbose_name="Player")
  command_3_region_source = models.ForeignKey(Region, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='region_source_3', verbose_name="From Region")
  command_3_region_target = models.ForeignKey(Region, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='region_target_3', verbose_name="To Region")
  command_4_type = models.CharField(max_length=10, choices=COMMAND_TYPES, blank=True, null=True, verbose_name="Command 4")
  command_4_player_target = models.ForeignKey(Player, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='player_target_4', verbose_name="Player")
  command_4_region_source = models.ForeignKey(Region, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='region_source_4', verbose_name="From Region")
  command_4_region_target = models.ForeignKey(Region, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='region_target_4', verbose_name="To Region")
  command_5_type = models.CharField(max_length=10, choices=COMMAND_TYPES, blank=True, null=True, verbose_name="Command 5")
  command_5_player_target = models.ForeignKey(Player, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='player_target_5', verbose_name="Player")
  command_5_region_source = models.ForeignKey(Region, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='region_source_5', verbose_name="From Region")
  command_5_region_target = models.ForeignKey(Region, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='region_target_5', verbose_name="To Region")

  def __str__(self):
    return "Turn: {} - Player: {}".format(self.turn, self.character)