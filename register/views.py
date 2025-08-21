from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("your_email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("comfirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect("register")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return redirect("success")   # after successful registration

    return render(request, "register.html")

def success_view(request):
    return render(request, "success.html")
