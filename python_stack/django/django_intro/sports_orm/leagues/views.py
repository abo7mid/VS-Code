from unicodedata import name
from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q
from . import team_maker
#make this comment in order to push to github
def index(request):
	context = {
		# "leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"baseball":League.objects.filter(sport="Baseball"),
		"women":League.objects.filter(name__contains="Women"),
		"name": League.objects.filter(name__contains="Hockey"),
		"sport": League.objects.filter(sport__contains="Hockey"),
		"conference": League.objects.filter(name__contains="conference"),
		"atlantic": League.objects.filter(name__contains="Atlantic"),
		"notfootball": League.objects.exclude(sport="Football"),
		"dallas": Team.objects.filter(location="Dallas"),
		"raptors": Team.objects.filter(team_name="Raptors"),
		"city": Team.objects.filter(location__contains="City"),
		"t": Team.objects.filter(team_name__startswith="T"),
		"orderByLocation": Team.objects.order_by("location"),
		"orderByLocationR": Team.objects.order_by("-team_name"),
		"joshua":Player.objects.filter(first_name="Joshua"),
		"cooper":Player.objects.filter(Q(last_name="Cooper") & ~Q(first_name="Joshua")),
		# "cooper":Player.objects.filter(Q(last_name__contains="C") & ~Q(first_name="Olivia")),
		"Alex_Wya": Player.objects.filter(first_name="Alexander") | Player.objects.filter(first_name="Wyatt"),


	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")