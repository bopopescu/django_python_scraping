from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import FetchInterestingUrl, FetchNonInterestingUrl, Users


def index(request):
    username = ""
    useremail = ''

    user = ""
    try:
        if(request.session['user'] != 'logout'):
            username = Users.objects.get(email = useremail).username
            user = "logged"
    except:
        user = 'logout'


    return render(request, 'index.html', {'user': user, 'username': username})
    # return HttpResponse("Hello, world. You're at the polls index.")


def user(request):
    useremail = ''
    user = ''
    username = ""
    try:
        if(request.session['user'] != 'logout'):
            useremail = request.session['user']
            username = Users.objects.get(email = useremail).username
            user = "logged"
    except:
        user = 'logout'
    # form = "User Signup"
    return render(request, 'user.html', {'user': user, 'useremail': useremail, 'username': username})


def signup(request):
    username = request.POST.get("username")
    password = request.POST.get("pass")
    email = request.POST.get("email")
    # msg = "gdgbvsdfgd"
    respo = ""
    if(Users.objects.filter(email=email)):
        msg = "User already exist"
    else:
        try:
            Users.objects.create(username=username, email=email, password=password)
            msg = "User added"
            request.session['user'] = email
        except:
            msg = "Error! try again"


    print(msg)
    return redirect("/")

def login(request):
    print("login proccess start")
    email = request.POST.get("username")
    password = request.POST.get("pass")
    if(Users.objects.filter(email=email).filter(password=password)):
        request.session['user'] = email
        redirectUrl = "/"
        print("user exist login")
    else:
        print("somthing wrong in password")
        redirectUrl = "/user?msg=Your Username and Password Not Matching . Retry!"
        
    return redirect(redirectUrl)


def logout(request):
    request.session['user'] = "logout"
    return redirect("/")






def scrapingAdmin(request):
    website = request.GET.get("website")
    # print(website)
    if (website == "eventshigh.com"):
        print("eventshigh.com")
        from .eventshigh_com import main
    elif(website == "insider.in"):
        print("insider.in")
        from .insider_in import main
    elif(website == "naadyogacouncil.com"):
        print("naadyogacouncil.com")
        from .naadyogacouncil_com import main
    else:
        print("No website")
    return render(request, "admin/index.html", {'status': 'ok'})
    # return HttpResponse("Scraping")







def fetchInterestingUrl(request):
    data = FetchInterestingUrl.objects.all()
    website = request.GET.get("website")
    all_data = []
    i = 0
    for urls in data:
        if(urls.website == website):
            all_data.append({"url": urls.url, "website": urls.website, "status": urls.status })
    print(len(data))
    # print(all_data)
    # print(all_data)
    user = ""
    if(request.session['user'] != 'logout'):
        user = "logged"

    return render(request, 'index.html', {'urls': all_data, 'user': user})
    # return HttpResponse(data)


def fetchNonInterestingUrl(request):
    data = FetchNonInterestingUrl.objects.all()
    website = request.GET.get("website")
    all_data = []
    i = 0
    for urls in data:
        if(urls.website == website):
            all_data.append({"url": urls.url, "website": urls.website })
    print(len(data))
    # print(all_data)

    user = ""
    if(request.session['user'] != 'logout'):
        user = "logged"

    return render(request, 'index.html', {'urls': all_data, 'user': user})
    # return HttpResponse(data)


