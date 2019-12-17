from django.shortcuts import render, HttpResponse


# Create your views here.


def index(request):
    # return HttpResponse("hello")
    return render(request, '../templates/index.html')


def showdevice(request):
    from Mao import models
    Info = models.Device.objects.all()
    Info_model = models.Class.objects.all()
    if request.method == "POST":
        name = request.POST.get("d_name", None)
        type = request.GET.get("type", None)
        # 搜索框、方案为空
        if name == '' and type == '':
            return render(request, '../templates/show.html', {'Info': Info, 'Info_model': Info_model})
        # 搜索框为空，方案不为空
        # if name == '' and type != '':
        #     search_Info = models.Device.objects.all().filter(user_class_id=type)
        #     return render(request, '../templates/show.html', {'Info': search_Info, 'Info_model': Info_model})
        # 搜索框不为空，方案为空
        if name != '' and type == '':
            search_Info_name = models.Device.objects.all().filter(d_name=name)
            return render(request, '../templates/show.html', {'Info': search_Info_name, 'Info_model': Info_model})
        if type == '':
            return HttpResponse(type)
        # 搜索框、方案均不为空
        else:
            search_Info_name = models.Device.objects.all().filter(d_name=name)
            search_Info_type = models.Device.objects.all().filter(d_type=name)
            search_Info = search_Info_name | search_Info_type
            return render(request, '../templates/show.html', {'Info': search_Info, 'Info_model': Info_model})
    return render(request, '../templates/show.html', {'Info': Info, 'Info_model': Info_model})


def add_device(request):
    from Mao import models
    if request.method == "POST":
        name = request.POST.get("d_name", None)
        type = request.POST.get("d_type", None)
        date = request.POST.get("d_date", None)
        describe = request.POST.get("d_describe", None)
        user_class_id = request.POST.get("user_class_id", None)
        models.Device.objects.create(
            d_name=name,
            d_type=type,
            d_date=date,
            d_describe=describe,
            user_class_id=user_class_id
        )
        Device_list = models.Device.objects.all()
        return render(request, '../templates/show.html', {'Info': Device_list})
    return render(request, '../templates/add.html')


def search_device(request):
    from Mao import models
    search_Info_model = models.Class.objects.all()
    if request.method == "POST":
        name = request.POST.get("d_name", None)
        search_Info = models.Device.objects.all().filter(d_name=name)
        return render(request, '../templates/show.html', {'Info': search_Info})
    if request.method == "GET":
        type = request.GET.get("type", None)
        search_Info = models.Class.objects.all().filter(class_name=type)
        return render(request, '../templates/show.html', {'Info_model': search_Info})
    return render(request, '../templates/search.html', {'Info_model': search_Info_model})
