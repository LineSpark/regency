from django.contrib import admin

from .models import Character, Game, Region, Turn, Player, Orders


# Register your models here.
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
  list_display = ("get_base36_id", "name", "start_date",)
  # list_editable = ("name",)
  list_filter = ("start_date",)
  search_fields = ("name",)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
  pass


@admin.register(Turn)
class TurnAdmin(admin.ModelAdmin):
  pass


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
  list_display = ("name", "game",)


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):

  def player(self, obj):
    return obj.character.player.__str__()

  list_display = ("turn", "character", "player",)
  fieldsets = (
    (None, {
      "fields": (("character", "turn"),)
    }),
    ("Command 1", {
      "fields": (("command_1_type", "command_1_player_target"), ("command_1_region_source", "command_1_region_target"),)
    }),
    ("Command 2", {
      "fields": (("command_2_type", "command_2_player_target"), ("command_2_region_source", "command_2_region_target"),)
    }),
    ("Command 3", {
      "fields": (("command_3_type", "command_3_player_target"), ("command_3_region_source", "command_3_region_target"),)
    }),
    ("Command 4", {
      "fields": (("command_4_type", "command_4_player_target"), ("command_4_region_source", "command_4_region_target"),)
    }),
    ("Command 5", {
      "fields": (("command_5_type", "command_5_player_target"), ("command_5_region_source", "command_5_region_target"),)
    }),
  )


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
  def age(self, obj):
    return obj.orders_set.count()

  list_display = ("name", "age", "alive", "player",)
  ordering = ("-alive", "-player",)

  fieldsets = (
    (None, {
      "fields": (("name", "alive"), "player")
    }),
    ("Talents", {
      "fields": ("martial_stat",
                 "intrigue_stat",
                 "control_stat",
                 "finance_stat",
                 "charisma_stat",
                 )})
  )
