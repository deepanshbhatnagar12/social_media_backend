from django.contrib import admin


class ManyToManyFieldAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("admin/css/manytomanyfieldwidget.css",),
        }
        js = ["admin/js/selectSubjectsOfCourse.js"]