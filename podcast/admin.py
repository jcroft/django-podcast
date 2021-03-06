from podcast.models import ParentCategory, ChildCategory, MediaCategory, Show, Enclosure, Episode
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


class CategoryInline(admin.StackedInline):
    model = ChildCategory
    extra = 3


class ParentCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [CategoryInline,]


class ChildCategoryAdmin(admin.ModelAdmin):
    list_display = ('parent', 'name')


class MediaCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ShowAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("title",)}
    list_display = ('title', 'organization')
    list_filter = ('title', 'organization')
    fieldsets = (
        (None, {
            'fields': ('organization', 'author', 'webmaster', 'title', 'slug', 'link', 'description', 'image', 'category_show', 'domain', 'language', 'ttl', 'copyright', 'copyright_url', 'feedburner')
        }),
        ('iTunes', {
            'fields': ('subtitle', 'summary', 'category', 'keywords', ('explicit', 'block'), 'redirect', 'itunes')
        }),
    )
    raw_id_fields = ('author','webmaster',)


class EnclosureInline(admin.StackedInline):
    model = Enclosure
    extra = 1
    fieldsets = (
        (None, {
            'fields': ('file','mime',)
        }),
        ('Extras', {
            'classes': ('collapse',),
            'fields': ('title','medium','expression','frame','bitrate','sample','channel','algo','hash','player','embed','width','height')
        }),
    )


class EnclosureAdmin(admin.ModelAdmin):
    list_display = ('title', 'file', 'player', 'mime')
    list_filter = ('mime',)


class EpisodeAdmin(admin.ModelAdmin):
    inlines = [EnclosureInline,]
    prepopulated_fields = {'slug': ("title",)}
    list_display = ('title', 'update', 'show', 'status', 'date',)
    list_editable = ('status', 'date',)
    list_filter = ('show', 'update')
    radio_fields = {'title_type': admin.HORIZONTAL, 'description_type': admin.HORIZONTAL, 'status': admin.HORIZONTAL}
    fieldsets = (
        (None, {
            'fields': ('show', 'author', 'title_type', 'title', 'slug', 'description_type', 'description', 'notes', 'captions', 'category', 'domain', 'frequency', 'priority', 'status', 'date')
        }),
        ('iTunes', {
            'fields': ('subtitle', 'summary', ('minutes', 'seconds'), 'keywords', ('explicit', 'block'))
        }),
        ('Media RSS', {
            'classes': ('collapse',),
            'fields': ('role', 'media_category', ('standard', 'rating'), 'image', 'text', ('deny', 'restriction'))
        }),
        ('Dublin Core', {
            'classes': ('collapse',),
            'fields': (('start', 'end'), 'scheme', 'name')
        }),
        ('Google Media', {
            'classes': ('collapse',),
            'fields': ('preview', ('preview_start_mins', 'preview_start_secs'), ('preview_end_mins', 'preview_end_secs'), 'host')
        }),
    )
    raw_id_fields = ('author',)


admin.site.register(ParentCategory, ParentCategoryAdmin)
admin.site.register(ChildCategory, ChildCategoryAdmin)
admin.site.register(MediaCategory, MediaCategoryAdmin)
admin.site.register(Show, ShowAdmin)
# admin.site.register(Enclosure, EnclosureAdmin)
admin.site.register(Episode, EpisodeAdmin)
