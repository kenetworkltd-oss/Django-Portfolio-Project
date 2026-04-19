from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('experience/', views.experience, name='experience'),
    path('blog/', views.blog, name='blog'),  # This powers the blogpage.html
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'), # For the comments page later
    
    # --- Authentication Routes ---
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
]