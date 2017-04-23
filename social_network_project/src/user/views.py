from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template.loader import  get_template
from django.template import  Context
from django.shortcuts import  render_to_response, redirect
from user.models import  User, Comments
from django.core.exceptions import ObjectDoesNotExist
from user.forms import CommentForm
from django.core.context_processors import csrf
from django.contrib import auth

# Create your views here.

def basic_one(request):
    view = "basic_one"
    html = "<html><body>This is %s view</html></body>" % view
    return HttpResponse(html)

def template_two(request):
    view = "template_two"
    t = get_template('myview.html')
    html = t.render(Context({'name': view}))
    return HttpResponse(html)

def template_simple(request):
    view = "template_simple"
    return render_to_response('myview.html', {'name':view})

def template_three_simple(request):
    view = "template_three"
    return render_to_response('myview.html', {'name': view})

def users(request):
    return render_to_response('users.html', {'users': User.objects.all(), 'username': auth.get_user(request)})

#def user(request, article_id=1):
   #return render_to_response('user.html',{'user': Article.objects.get(id=article_id),'comments': Comments.objects.filter(comments_art_id= article_id)})
def user(request, article_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['user'] = User.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_art_id=article_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('user.html', args)



def addlike(request, article_id):
    try:
        user = User.objects.get(id=article_id)
        user.user_likes += 1
        user.save()
        response = redirect('/')
        response.set_cookie(article_id, "test")
        return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')

def addcomment(request, article_id):
    if request.POST and ("pause" not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = User.objects.get(id=article_id)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/users/get/%s/' % article_id)