from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import Signupform,Login,profile_user,profile_admin,Blogcreate
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView
from django.http import Http404
from datetime import date
from django.contrib.auth.decorators import login_required
from .models import Highschool,Statelevel,India,Genquiz,Scc,Blogpost
# Create your views here.
def Home(request):
    fm =Highschool.objects.order_by('id').reverse()[0:3]
    fm1 = Statelevel.objects.order_by('id').reverse()[0:3]
    fm2=India.objects.order_by('id').reverse()[0:3]
    return render(request,'home.html',{'fm':fm,'fm1':fm1,'fm2':fm2})

##more pdf highschool
def Morepdfhigh(request):
    mph =Highschool.objects.order_by('year1')
    return  render(request,'morepdfhigh.html',{'mph':mph})
###morepdfstate
def Morepdfstate(request):
    mps =Statelevel.objects.order_by('year1')
    return  render(request,'morepdfstate.html',{'mps':mps})
###morepdfIndia
def Morepdfindia(request):
    mpi =India.objects.order_by('year1')
    return  render(request,'morepdfind.html',{'mpi':mpi})

###Quiz view
def Quiz(request):
    d = date.today()
    d2 = d.strftime("%B %d, %Y")
    quiz=Genquiz.objects.all()
    return render(request, 'quiz.html',{'quiz':quiz,'d2':d2})
#ssc
def Quiz1(request):
   quiz1 = Scc.objects.all()
   return render(request, 'scc.html',{'quiz1':quiz1})

##blog
class Blog(ListView):
        d = date.today()
        d2 = d.strftime("%B %d, %Y")
        model = Blogpost
        template_name = 'blog.html'
        ordering = ['id']
        paginate_by = '3'
        paginate_orphans = 2

        def get_context_data(self, *args, **kwargs):
            try:
                return super(Blog, self).get_context_data(*args, **kwargs)
            except Http404:
                self.kwargs['page'] = 1
                context = super(Blog, self).get_context_data(*args, **kwargs)
                return context


#signup page
def Signup(request):
        if request.method == 'POST':
            fm = Signupform(request.POST)
            if fm.is_valid():
                fm.save()
                messages.info(request, 'Successfully ! Create an account- Now you can Login the page')
                return HttpResponseRedirect('/blog_post/login/')
        else:
            fm = Signupform()
        return render(request, 'signup.html', {'form': fm})


#login form

def user_login(request):
    if request.method == 'POST':
        fm = Login(request=request, data=request.POST)
        if fm.is_valid():
            uname1 = fm.cleaned_data['username']
            upass1 = fm.cleaned_data['password']
            user = authenticate(username=uname1, password=upass1)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/blog_post/profile/')
    else:
        fm = Login()
    return render(request, 'login.html', {'form': fm})


##profile
#profile
def Profile(request):
        if request.user.is_authenticated:
            if request.method == 'POST':
                if request.user.is_superuser == True:
                    fm = profile_admin(request.POST, instance=request.user)
                    user = User.objects.all()
                else:
                    fm = profile_user(request.POST, instance=request.user)
                    user = None
                if fm.is_valid():
                    fm.save()
                    return HttpResponseRedirect('/blog_post/profile')
            else:
                if request.user.is_superuser == True:
                    fm = profile_admin(instance=request.user)
                    user = User.objects.all()
                else:

                    fm = profile_user(instance=request.user)
                    user = None
            return render(request, 'profile.html', {'name': fm, 'user': user})
        else:
            return HttpResponseRedirect('/blog_post/login')

#logout

def Logout(request):
  logout(request)
  fm= messages.success(request, 'Logout Successfully ! ')
  return HttpResponseRedirect('/blog_post/login',{'fm':fm})


###postview

class PostDetailView(DetailView):
    model = Blogpost
    template_name = "postview.html"


##blogdesign form
@login_required(login_url='/blog_post/login/')
def Createblog(request):
    if request.method=="POST":
       bc=Blogcreate(request.POST,request.FILES)
       if bc.is_valid():
            bc.save()
            return HttpResponseRedirect("/blog_post/")
    else:
       bc=Blogcreate()
    return render(request,'blogcreate.html',{'form':bc})

def time(request):
    d = date.today()
    d2 = d.strftime("%B %d, %Y")
    return render(request,'time.html',{'d2':d2})