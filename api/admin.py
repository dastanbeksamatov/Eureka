from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import (POS, Dimension, Family, Feature, Genus, Language, Lemma,
                     TagSet, Word)

# Register your models here.
admin.site.register(Word)
admin.site.register(Feature)
admin.site.register(Dimension)
admin.site.register(Language)
admin.site.register(Lemma)
admin.site.register(Family)
admin.site.register(TagSet)
admin.site.register(POS)
admin.site.register(Genus)
