from django.contrib import admin

from .models import Libro

admin.site.register(Libro)

from .models import Miembro

admin.site.register(Miembro)

from .models import Biblioteca

admin.site.register(Biblioteca)
