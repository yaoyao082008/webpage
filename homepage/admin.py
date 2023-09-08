from django.contrib import admin
from .models import  *
from django.contrib.auth.models import User
# Register your models here.


admin.site.register(verifed_user)
admin.site.register(inner_webinar)
admin.site.register(chinese_webinar)
admin.site.register(english_webinar)
admin.site.register(agent_contact)
admin.site.register(everyone_video_number)