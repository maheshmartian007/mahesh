from django.shortcuts import render, get_object_or_404 ,redirect
from blogapp.models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from django.http import HttpResponseRedirect
# from django.template import Context
# from django.template.loader import render_to_string, get_template
# from django.core.mail import EmailMessage
from blogapp.forms import *
from django.core.mail import send_mail
from taggit.models import Tag
 
# Create your views here.

# Function Based View

def post_list_view(request, tag_slug = None):
	
	post_list = Post.objects.all()
	print(post_list, 'This is post_list')
	tag = None
	print(tag_slug, 'This is tag slug')

	if tag_slug:
		tag = get_object_or_404(Tag, slug = tag_slug)
		print(tag, 'this is tag ')
		post_list = post_list.filter(tags__in= [tag])
		print(post_list)

	paginator = Paginator(object_list = post_list, per_page = 2)
	page_number = request.GET.get('page')


	try:
		post_list = paginator.page(page_number)

	except PageNotAnInteger: 
		post_list = paginator.page(1)

	except EmptyPage:
		post_list = Paginator.page(paginator.num_pages)


	my_dict = {'post_list': post_list , 'tag': tag}


	return render(request = request, template_name = 'blogapp/post_list.html', context= my_dict)


# class Based View

# class PostListView(ListView):
# 	model = Post 
# 	paginate_by = 2


def post_detail_view(request, year, month, day, post):

	
	post = get_object_or_404(Post, slug = post, status= 'published', publish__year = year, publish__month=month, publish__day = day)
	print(post, 'this is post')
	comments = post.comments.filter(active = True)
	print(comments,'comments')
	csubmit = False
	
	if request.method == 'POST':
		form = CommentForm(request.POST)
		print(form , 'form')

		if form.is_valid():
			new_comment = form.save(commit = False)
			new_comment.post = post
			new_comment.save()
			csubmit = True

	else:
		form = CommentForm()
		# redirect()
	
	my_dict = {'post': post, 'form': form, 'csubmit': csubmit, 'comments':comments}
	return render(request = request, template_name = 'blogapp/post_detail.html', context= my_dict)


	# else:

	# 	form = CommentForm()
	# 	my_dict = {'post': post, 'form': form, 'csubmit': csubmit, 'comments':comments}
	# 	print(my_dict, 'my_dict')
	# 	return render(request = request, template_name = 'blogapp/post_detail.html', context= my_dict)

	# return redirect('blogapp/post_detail.html')



def mail_send_view(request, id):
	post  = get_object_or_404(Post, id = id, status='published')
	sent = False

	if request.method == 'POST':
		form = EmailSendForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			subject = f"{cd['name']}({cd['email']} recommends you to read {post.title})"

			post_url = request.build_absolute_uri(post.get_absolute_url())

			message = f"Read the Post at :\n {post_url} \n\n {cd['name']} \'s Comments:\n{cd['comments']} "

			# message = f"{post.title} \n\n {post.body} \n{post.author} \n\n\n Read the Original Post at :\n {post_url} \n\n \n\n {cd['name']} \'s Comments:\n{cd['comments']}"

			# send_mail (subject, message, form_email, recipient_list)

			send_mail(subject, message, 'hhramanjinappa@gmail.com', [cd['to']])
			sent = True
	else:

		form = EmailSendForm()


	my_dict = {'form': form, 'post': post, 'sent': sent} 
	return render( request = request, template_name = 'blogapp/sharebymail.html', context = my_dict)



# def sendmail(request):
# 	ctx = {
#         'user': "Ajay"
#     }
#     message = get_template('mail.html').render(ctx)
    
#     msg = EmailMessage(
#         'Subject',
#         message,
#         'from@example.com',
#         ['to@example.com'],
#     )
#     msg.content_subtype = "html"  # Main content is now text/html
#     msg.send()
#     print("Mail successfully sent")

