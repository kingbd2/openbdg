from django.contrib import admin

from .models import Glossary, Domain, Raci, User
admin.site.register(Glossary)
admin.site.register(Domain)
admin.site.register(Raci)
admin.site.register(User)
