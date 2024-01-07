from django.contrib import admin


from checking.models.checking import CheckingDuration, Checking, CheckingTerm

# Register your models here.

admin.site.register(CheckingDuration)
admin.site.register(Checking)
admin.site.register(CheckingTerm)
