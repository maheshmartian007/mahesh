from django import forms
from .models import *
# from ckeditor.fields import RichTextField 
from ckeditor.widgets import CKEditorWidget	

class EmailSendForm(forms.Form):
	name = forms.CharField()
	email = forms.CharField()
	to = forms.CharField()
	comments = forms.CharField(widget=CKEditorWidget()) 



class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment 
		fields = {'name', 'email', 'body'}