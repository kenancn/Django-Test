from django.contrib import admin
from election.profile.models import UserProfile,City,Town
import openpyxl
from openpyxl.utils.cell import col

def get_cities_and_towns():
    print("Dosya import edeceğim")
    path = "/home/dream/Downloads/c.xlsx"
    wb = openpyxl.load_workbook(path, data_only=True)
    sheet = wb.active
    for row in sheet.iter_rows(row_offset=1):
        code = str(row[0].value).strip()
        city_name = str(row[1].value).strip()
        town_name = str(row[2].value).strip()


        try:
            city = City.objects.get(Code=code)
            town = Town(Name=town_name, City=city)
            town.save()

        except:
            city = City(Name=city_name, Code=code)
            city.save()
            town = Town(Name=town_name, City=city)
            town.save()
        print(code, city_name, town_name)

class CityAdmin(admin.ModelAdmin):
    list_display=('Name','Code')

    def import_cities_and_towns(modeladmin,request,queryset):
        get_cities_and_towns()

    actions = [import_cities_and_towns, ]

    import_cities_and_towns.short_description = "İl ve ilçeleri yükle"

class TownAdmin(admin.ModelAdmin):
    list_display=('Name','City')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('email','name','is_active','is_superuser','created_at','city_name',)

    def city_name(self, obj):
        if obj.town.City.Name is not None:
            return obj.town.City.Name
        else:
            "Boş"



admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(City,CityAdmin)
admin.site.register(Town,TownAdmin)
