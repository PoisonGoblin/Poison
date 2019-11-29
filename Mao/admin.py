from django.contrib import admin
from Mao.models import User, Class


# Register your models here.


# 注册
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # 列表页属性
    list_display = ['pk', 'name', 'date', 'isDelete', 'user_class']  # 显示字段
    list_filter = ['name']  # 过滤字段
    search_fields = ['name']  # 搜索字段
    list_per_page = 10  # 分页

    # 添加,修改页属性，两个属性不能同时使用
    # fields = []   属性的先后顺序
    fieldsets = [
        ("基础信息", {"fields": ['name', 'date']}),
        ("高级信息", {"fields": ['user_class', 'isDelete']})
    ]  # 给属性分组


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    # 列表页属性
    list_display = ['class_name']  # 显示字段
    list_filter = ['class_name']  # 过滤字段
    search_fields = ['class_name']  # 搜索字段
    list_per_page = 10  # 分页

    # 添加,修改页属性，两个属性不能同时使用
    # fields = []   属性的先后顺序
    # fieldsets = []  给属性分组
