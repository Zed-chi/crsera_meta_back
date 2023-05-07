import json
from datetime import datetime
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.decorators.csrf import csrf_exempt
from restaurant.forms import BookingForm
from restaurant.models import Booking, Menu


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


@csrf_exempt
def bookings(request):
    if request.method == "POST":
        data = json.load(request)
        exist = Booking.objects.filter(
            booking_date=data["reservation_date"]
        ).filter()
        if exist:
            return HttpResponse(
                "{'error':1}", content_type="application/json"
            )
        Booking.objects.create(
            first_name=data["first_name"],
            reservation_date=data["reservation_date"],
            reservation_slot=data["reservation_slot"],
        )
        return redirect(reverse("bookings"))

    date = request.GET.get("date", datetime.today().date())
    bookings = Booking.objects.all().filter(booking_date=date)
    booking_json = serializers.serialize("json", bookings)
    return render(
        request, "bookings.html", {"bookings": booking_json}
    )


def book(request):
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            print("=== valid form===")
            form.save()
    context = {"form": form}
    return render(request, "book.html", context)


def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, "menu.html", {"menu": main_data})


def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(
        request, "menu_item.html", {"menu_item": menu_item}
    )
