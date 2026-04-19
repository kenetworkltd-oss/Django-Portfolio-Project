from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Hero, About, Experience, ContactMessage, Testimonial, TeamMember, Project, Comment
from django.core.paginator import Paginator
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required

def index(request):
    # --- Part A: Handle Contact Form Submission ---
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Create the message in the database
        ContactMessage.objects.create(
            name=name, 
            email=email, 
            subject=subject, 
            message=message
        )
        # Redirect back to the home page to clear the form
        return redirect('index')

    # --- Part B: Load Data for the Website ---
    hero = Hero.objects.first()
    about = About.objects.first()
    experiences = Experience.objects.all()
    testimonials = Testimonial.objects.all()
    team = TeamMember.objects.all()
    projects = Project.objects.all()

    # --- Pagination Logic for the Homepage ---
    all_posts = Post.objects.all().order_by('-date')
    
    # Show exactly 3 posts on the landing page
    paginator = Paginator(all_posts, 3) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'pages/index.html', {
        'hero': hero, 
        'about': about,
        'experiences': experiences,
        'page_obj': page_obj,
        'testimonials': testimonials,
        'team': team,
        'projects': projects,
    })

# Other page views
def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def experience(request):
    experiences = Experience.objects.all()
    return render(request, 'pages/experience.html', {'experiences': experiences})

# Pagination for dedicated Blog Page (Archive)
def blog(request):
    # 1. Fetch all posts
    all_posts = Post.objects.all().order_by('-date')
    
    # 2. Set pagination to 6 so you see an overview of all posts on one page
    paginator = Paginator(all_posts, 6) 
    
    # 3. Get the page number from the URL
    page_number = request.GET.get('page')
    
    # 4. Get the posts for this specific page
    page_obj = paginator.get_page(page_number)
    
    # Ensure this points to blogpage.html
    return render(request, 'pages/blogpage.html', {'page_obj': page_obj})

# Pagination for Project Page
def project_list(request):
    all_projects = Project.objects.all().order_by('-date_created')
    paginator = Paginator(all_projects, 3) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'portfolio/projects.html', {'page_obj': page_obj})

# Individual Blog Detail and Comment Submission
def blog_detail(request, pk):
    # Use get_object_or_404 for better error handling
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    
    if request.method == "POST":
        name = request.POST.get('name')
        body = request.POST.get('body')
        Comment.objects.create(post=post, name=name, body=body)
        return redirect('blog_detail', pk=post.pk)
    
    # Points to the specific detail template
    return render(request, 'pages/blog_detail.html', {'post': post, 'comments': comments})


# --- Authentication Views ---

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Log them in immediately after signup
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'pages/signup.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'pages/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')


@login_required(login_url='login')
def profile_view(request):
    # This view passes the 'user' object to the template automatically
    return render(request, 'pages/profile.html')
