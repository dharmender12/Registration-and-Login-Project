from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # You can add real authentication here
        if username and password:  
            # Pass username to success page
            return redirect("success")  
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})
    
    return render(request, "login.html")


def success_view(request):
    return render(request, "success.html")
