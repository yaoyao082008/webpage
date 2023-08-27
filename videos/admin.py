from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import *
# Register your models here.

@admin.register(tax_video)
@admin.register(long_term_care_video)
@admin.register(medicare_video)
@admin.register(retirement_video)
@admin.register(college_university_savings_video)
@admin.register(life_insurance_video)
@admin.register(estate_planning_video)
@admin.register(asset_protection_video)
@admin.register(other_video)
@admin.register(exam_video)
@admin.register(Real_Estate_Investment_Video)
@admin.register(Company_Structure_Video)
@admin.register(General_Financial_Planning_Video)

class VideoAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'author', 'my_order']