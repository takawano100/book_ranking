from django.contrib import admin
from .models import (
    Publishers, Books, Pictures
)


admin.site.register(
    [Publishers, Books, Pictures]    
)