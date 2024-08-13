from django.contrib import admin
from .models import AllUser,Karyasamiti,ChetriyaSamiti,ToleSamiti,SallakarSamiti,LekhaSamiti,Notice,Report,News,Gallery,Photo

class AllUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'municipality', 'ward', 'tole','member_number','phone','member_type','approved_by','approved_by_position','date_approved')

    # Optional: Add filtering, searching, and ordering
    list_filter = ('municipality', 'tole')
    search_fields = ('first_name', 'last_name', 'middle_name')
    ordering = ('last_name', 'first_name')

admin.site.register(AllUser, AllUserAdmin)

class KaryaSamitiAdmin(admin.ModelAdmin):
    list_display = ('name','image')
    list_filter = ('name',)
    search_fields = ('name',)

admin.site.register(Karyasamiti, KaryaSamitiAdmin)

admin.site.register([ChetriyaSamiti,ToleSamiti,SallakarSamiti,LekhaSamiti,Notice,Report,News])

class PhotoInline(admin.TabularInline):  # or admin.StackedInline
    model = Photo
    extra = 1
    fields = ['image', 'caption']

class GalleryAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

admin.site.register(Gallery, GalleryAdmin)
