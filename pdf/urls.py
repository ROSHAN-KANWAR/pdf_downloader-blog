from django.contrib import admin
from django.urls import path
from pdf import views
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.Home,name="home"),
    path("10th-12th/more_pdf/", views.Morepdfhigh, name="mph"),
    path("state-level/more_pdfs/", views.Morepdfstate, name="mps"),
    path("all-govt/more_pdfg/", views.Morepdfindia, name="mpi"),
    path("quiz_page/", views.Quiz, name="quiz"),
    path("quiz_page/scc_question/", views.Quiz1, name="quiz1"),
    path("blog_post/", views.Blog.as_view(), name="blog"),
    path('blog_post/post_view/<int:pk>', views.PostDetailView.as_view(), name='postview'),
    path("blog_post/signup_page/", views.Signup, name="sign"),
    path('blog_post/login/', views.user_login, name="login"),
    path('blog_post/profile/', views.Profile, name="profile"),
    path('logout/', views.Logout, name='logout'),
    path('blog_post/create_blog/', views.Createblog, name='create'),
    path('time/',views.time),
    url(r'^download/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
