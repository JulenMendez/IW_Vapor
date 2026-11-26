from django.contrib import admin

# Register your models here.


from .models import Tag, Dev, Sale_event, Game


admin.site.register(Tag)
admin.site.register(Dev)
admin.site.register(Sale_event)
admin.site.register(Game)