from django.contrib import admin
from .models import Post, Experience, Hero, About, ContactMessage, Testimonial, TeamMember, Project,Comment


# Register your models here.
#Register model here and step 2
admin.site.register(Post)
admin.site.register(Experience) 
admin.site.register(Hero)
admin.site.register(About)
admin.site.register(ContactMessage)
admin.site.register(Testimonial)
admin.site.register(TeamMember)
admin.site.register(Project)
admin.site.register(Comment)


