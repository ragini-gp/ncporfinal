from django.contrib import admin
from nsidc_app.models import about

# from nsidc_app.models import research_drop

from nsidc_app.models import informationResearch
from nsidc_app.models import researchScientist
from nsidc_app.models import researchGrant, myclass, archiveclass
from nsidc_app.models import scientificPublication, research_example_down_sp
from nsidc_app.models import scientificExpedition,research_example_down_scientists, research_example_down_resgran


# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    class Media:
        css={
            "all":("css/main.css",)
        }

        js=("js/blog.js",)

admin.site.register(about, BlogAdmin)


# admin.site.register(research_drop,BlogAdmin)(drop-dowm-->dropdowm through cms / made by priyanshi)

admin.site.register(informationResearch, BlogAdmin)
admin.site.register(researchScientist, BlogAdmin)
admin.site.register(researchGrant, BlogAdmin)
admin.site.register(scientificPublication, BlogAdmin)
admin.site.register(scientificExpedition, BlogAdmin)
admin.site.register(research_example_down_scientists,BlogAdmin)
admin.site.register(research_example_down_resgran,BlogAdmin)
admin.site.register(research_example_down_sp,BlogAdmin)
admin.site.register(myclass)
admin.site.register(archiveclass)



# admin.site.register(research_drop,BlogAdmin)(drop-dowm-->dropdowm through cms / made by priyanshi)
