from django.shortcuts import render, HttpResponse


# Create your views here.


def index(request):
    # return HttpResponse("hello")
    return render(request, '../templates/index.html')


def showdevice(request):
    from Mao import models
    Info = models.Device.objects.all()
    return render(request, '../templates/show.html', {'Info': Info})


def add_device(request):
    from Mao import models
    if request.method == "POST":
        name = request.POST.get("d_name", None)
        type = request.POST.get("d_type", None)
        date = request.POST.get("d_date", None)
        user_class_id = request.POST.get("user_class_id", None)
        models.Device.objects.create(
            d_name=name,
            d_type=type,
            d_date=date,
            user_class_id=user_class_id
        )
        Device_list = models.Device.objects.all()
        return render(request, '../templates/show.html', {'Info': Device_list})
    return render(request, '../templates/add.html')


def search_device(request):
    from Mao import models
    if request.method == "POST":
        name = request.POST.get("d_name", None)
        type = request.POST.get("d_type", None)
        date = request.POST.get("d_date", None)
        user_class_id = request.POST.get("user_class_id", None)
        search_Info = models.Device.objects.all().filter(d_name=name)
        return render(request, '../templates/show.html', {'Info': search_Info})
    return render(request, '../templates/search.html')
