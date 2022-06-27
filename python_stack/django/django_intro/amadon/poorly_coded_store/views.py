from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    if request.method == "POST":
        print("executed only when POST Method used (when a button or input of submit type, inside a form of post method, is clicked )")
        quantity_from_form = int(request.POST["quantity"])
        # price_from_form = float(request.POST["price"]) could be changed by user
        id = Product.objects.get(id=request.POST["product_id"])
        print(id.price)
        total_charge = quantity_from_form * id.price
        print("Charging credit card...")
        Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
        return redirect('/checkout')
    print("a redirect or GET method")
    print("check if user logged in")
    order = Order.objects.last()
    orders = Order.objects.all()
    quantity = 0
    total_price = 0
    for order in orders:
        quantity = quantity + order.quantity_ordered
        total_price = total_price + order.total_price 
    print("Ordered Items :",quantity)
    print("Total spent :",total_price)

    context = {
        "order":order,
        "quantity":quantity,
        "total_price":total_price,

    }
    return render(request, "store/checkout.html",context)