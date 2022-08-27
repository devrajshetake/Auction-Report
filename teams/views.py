from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from .players import allplayers
from django.http import HttpResponse

# Create your views here.


def players(request):
    queryset = Player.objects.all()

    context = {
        'players':queryset,
    }

    return render(request, "teams/players.html", context)

def player(request,pk):
    if request.method == "POST":
        instance = get_object_or_404(Player, pk=pk)
        form = PlayerForm(request.POST or None, instance=instance)
        if form.is_valid():
            print("valid")
            form.save()
    form = PlayerForm()
    play = Player.objects.get(pk=pk)
    context = {
        'player':play,
        'form':form
    }
    return render(request, "teams/player.html", context)

def home(request):
    return render(request, "teams/home.html")

def teams(request):
    queryset = Team.objects.all()

    for team in queryset:
        team.save()

    context = {
        'teams':queryset,
    }

    return render(request, "teams/teams.html", context)

def team(request,pk):
    team = Team.objects.get(pk=pk)
    team.save() #Jugaad
    players = team.players.all()
    context = {
        'team':team,
        'players':players
    }

    return render(request, "teams/team.html", context)


def addplayers(request):
    for player in allplayers:
        try:
            Player.objects.create(
                name = player['name'],
                base_price = player['base_price'],
                selling_price = player['selling_price'],
                rating = player['rating'],
                img = player['img']
            )
            print("created",player['name'])
        except:
            print("error occured while creating",player['name'])

    return HttpResponse("players craeted maybe")