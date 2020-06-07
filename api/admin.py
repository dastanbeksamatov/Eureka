from django.contrib import admin
<<<<<<< HEAD:api/admin.py
from api.models import Genus, Word, Feature, Dimension, Language, Lemma, Family, TagSet, POS

=======
from wordDictionary.models import Genus, Word, Feature, Dimension, Language, Lemma, Family, TagSet, POS
from django.contrib.auth.models import Permission
>>>>>>> Add user model:wordDictionary/admin.py


# Register your models here.
admin.site.register(Word)
admin.site.register(Feature)
admin.site.register(Dimension)
admin.site.register(Language)
admin.site.register(Lemma)
admin.site.register(Family)
admin.site.register(TagSet)
admin.site.register(POS)
<<<<<<< HEAD:api/admin.py
admin.site.register(Genus)
=======
admin.site.register(Genus)
admin.site.register(Permission)
# admin.site.register(LogEntry)
>>>>>>> Add user model:wordDictionary/admin.py
