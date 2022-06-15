from gc import get_threshold
from random import randint
from time import gmtime, strftime
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


allgold = 0


def process_money(request):
    if request.method == "POST":
        gold = randint(10, 20)
        global allgold

        print("first ", allgold)
        date = strftime("%m-%d-%Y %H:%M %p", gmtime())

        if request.POST['which_form'] == 'farm':
            text = f"You entered a farm and earned {gold} gold. ({date})"
            print(text)
            allgold = allgold + gold
            print("second", allgold)
            context = {
                # "gold":gold,
                "text": text,
                "allgold": allgold,
                "color": "green"

            }
            return render(request, "index.html", context)

        if request.POST['which_form'] == 'cave':
            text = f"You entered a cave and earned {gold} gold. ({date})"
            print(text)
            allgold = allgold + gold
            print("third", allgold)
            context = {
                "text": text,
                "allgold": allgold,
                "color": "green"

            }
            return render(request, "index.html", context)

        if request.POST['which_form'] == 'house':
            text = f"You entered a house and earned {gold} gold. ({date})"
            print(text)
            allgold = allgold + gold
            print("forth", allgold)

            context = {
                # "gold":gold,
                "text": text,
                "allgold": allgold,
                "color": "green"

            }
            return render(request, "index.html", context)

        if request.POST['which_form'] == 'quest':
            gold = randint(0, 50)
            if gold % 2 == 0:
                allgold = allgold + gold
                print("fivth", allgold)
                text1 = f"You entered a house and earned {gold} gold. ({date})"


                context = {
                    "text": text1,
                    "allgold": allgold,
                    "color": "green"
                }
                return render(request, "index.html", context)
            else:
                allgold = allgold - gold
                text1 = f"You failed a quest and lost {gold} gold. ({date})"

                context = {
                    "text": text1,
                    "allgold": allgold,
                    "color": "red"
                }
            return render(request, "index.html", context)

    return render(request, "index.html")
