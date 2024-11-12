# Blog by Ravindra

# Step 1: Clone the repository
git clone https://github.com/rarjune7/ET721.git
cd blog-project

# Step 2: Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate 

# Step 3: Install Django and other dependencies
pip install django

# Step 4: Create a new Django project
django-admin startproject ET721_lab_blog.
cd ET721_lab_blog

# Step 5: Create a new Django app called 'blog'
python manage.py startapp blog

# Step 6: Migrate the database (set up initial schema)
python manage.py migrate

# Step 7: Create a superuser (optional, for admin access but i didn't do)
python manage.py createsuperuser

# Step 8: Add the blog app to the INSTALLED_APPS in settings.py
# Open blogproject/settings.py and add 'blog' to the INSTALLED_APPS list
sed -i '/INSTALLED_APPS = \[/a\ \ \ \ "blog",' blogproject/settings.py

# Step 9: Set up URLs for the blog app in blogproject/urls.py
echo "from django.contrib import admin" >> blogproject/urls.py
echo "from django.urls import path, include" >> blogproject/urls.py
echo "" >> blogproject/urls.py
echo "urlpatterns = [" >> blogproject/urls.py
echo "    path('admin/', admin.site.urls)," >> blogproject/urls.py
echo "    path('', include('blog.urls'))," >> blogproject/urls.py
echo "]" >> blogproject/urls.py

# Step 10: Create blog/urls.py to handle blog URLs
echo "from django.urls import path" > blog/urls.py
echo "from . import views" >> blog/urls.py
echo "" >> blog/urls.py
echo "urlpatterns = [" >> blog/urls.py
echo "    path('', views.post_list, name='post_list')," >> blog/urls.py
echo "    path('new/', views.post_create, name='post_create')," >> blog/urls.py
echo "]" >> blog/urls.py

# Step 11: Create basic views for the blog app in blog/views.py
echo "from django.shortcuts import render" > blog/views.py
echo "from .models import Post" >> blog/views.py
echo "" >> blog/views.py
echo "def post_list(request):" >> blog/views.py
echo "    posts = Post.objects.all()" >> blog/views.py
echo "    return render(request, 'blog/post_list.html', {'posts': posts})" >> blog/views.py
echo "" >> blog/views.py
echo "def post_create(request):" >> blog/views.py
echo "    return render(request, 'blog/post_create.html')" >> blog/views.py

# Step 12: Create templates directory for post_list and post_create HTML files
mkdir -p blog/templates/blog
echo "<html>" > blog/templates/blog/post_list.html
echo "<body>" >> blog/templates/blog/post_list.html
echo "<h1>Blog Posts</h1>" >> blog/templates/blog/post_list.html
echo "<ul>" >> blog/templates/blog/post_list.html
echo "  {% for post in posts %}" >> blog/templates/blog/post_list.html
echo "    <li>{{ post.title }}</li>" >> blog/templates/blog/post_list.html
echo "  {% endfor %}" >> blog/templates/blog/post_list.html
echo "</ul>" >> blog/templates/blog/post_list.html
echo "</body>" >> blog/templates/blog/post_list.html
echo "</html>" >> blog/templates/blog/post_list.html

echo "<html>" > blog/templates/blog/post_create.html
echo "<body>" >> blog/templates/blog/post_create.html
echo "<h1>Create a New Post</h1>" >> blog/templates/blog/post_create.html
echo "</body>" >> blog/templates/blog/post_create.html
echo "</html>" >> blog/templates/blog/post_create.html

# Step 13: Create a static directory to hold your CSS file
mkdir -p blog/static/blog
echo "body {" > blog/static/blog/styles.css
echo "    background-color: #e0f7fa;" >> blog/static/blog/styles.css
echo "    font-family: 'Arial', sans-serif;" >> blog/static/blog/styles.css
echo "}" >> blog/static/blog/styles.css
echo "a {" >> blog/static/blog/styles.css
echo "    color: #00796b;" >> blog/static/blog/styles.css
echo "}" >> blog/static/blog/styles.css
echo "a:hover {" >> blog/static/blog/styles.css
echo "    color: #004d40;" >> blog/static/blog/styles.css
echo "}" >> blog/static/blog/styles.css

# Step 14: Link CSS file in the templates (post_list.html and post_create.html)
sed -i 's|</head>|    <link rel="stylesheet" type="text/css" href="{% static 'blog/styles.css' %}">\n</head>|' blog/templates/blog/post_list.html
sed -i 's|</head>|    <link rel="stylesheet" type="text/css" href="{% static 'blog/styles.css' %}">\n</head>|' blog/templates/blog/post_create.html

# Step 15: Run the development server
python manage.py runserver
