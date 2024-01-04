from django.shortcuts import render, redirect
from .models import Member
from .forms import MemberForm
from django.contrib import messages


# Create your views here.
def home(request):
    member = Member.objects.all()
    context = {"member": member}
    return render(request, "home.html", context)


def join(request):
    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            fname = request.POST["fname"]
            lname = request.POST["lname"]
            age = request.POST["age"]
            email = request.POST["email"]
            passwd = request.POST["passwd"]
            messages.error(request, "An error occured, Try again")

            context = {
                "fname": fname,
                "lname": lname,
                "age": age,
                "email": email,
            }
            return render(request, "join.html", context)

        messages.success(request, "User Created succesfully")
        return redirect("home")

    context = {}
    return render(request, "join.html", context)
