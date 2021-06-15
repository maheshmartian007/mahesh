from django.contrib import admin
from blogapp.models import *
from django.utils.html import format_html
# from import_export.admin import ImportExportModelAdmin
# Register your models here.


class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug', 'author', 'less_content', 'publish', 'created', 'updated', 'status', 'post_image']
	list_filter = ('status', 'author',)
	search_fields = ('title', 'body', 'author')
	raw_id_fields = 'author',
	prepopulated_fields = {'slug': ('title',)}
	ordering = ['status', 'publish']
	# exclude  = ('id', 'less_content','created', 'updated', )


	def less_content(self, obj):
		# This function will extract the first 30 charactracters
		# return obj.content[:30]
		return format_html(f'<span style = "color:#03A9F4">{obj.body[:32]}</span>')

class CommentAdmin(admin.ModelAdmin):
	list_display = ('name','email','post','body','created','updated','active')
	list_filter = ('active','created','updated')
	search_fields = ('name','email','body')


# admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)