# Blog by Ravindra

### Project Summary: Django Blog Application

In this project, I built a basic blog application using Django, which involved a step-by-step process of setting up the project, defining models, creating views, handling URL routing, designing templates, and implementing forms for user interaction. Here’s a summary of everything I did:

---

#### **Part 1: Setting up the Project and App**

1. **GitHub Repository**: I created a GitHub repository called `ET721_lab_blog` and opened it in Codespace to work on the project.

2. **Virtual Environment**: I installed and activated a Python virtual environment to manage all the necessary dependencies for the project.

3. **Django Project Setup**: I created a new Django project named `blogproject` and within it, I initialized a Django app called `blog`.

4. **Configuration**: I added the `blog` app to the `INSTALLED_APPS` list in the `settings.py` file, ensuring it was part of the Django project.

#### **Part 2: Define the Model**

1. **BlogPost Model**: In `blog/models.py`, I created a `BlogPost` model to represent blog posts with the following fields:
   - `title`: A `CharField` with a max length of 200 characters.
   - `content`: A `TextField` to store the content of the blog post.
   - `created_at`: A `DateTimeField` with `auto_now_add=True` to automatically record when the post was created.
   - `updated_at`: A `DateTimeField` with `auto_now=True` to automatically update the timestamp whenever the post is modified.

2. **Database Setup**: I ran `makemigrations` and `migrate` to create the necessary database table for the `BlogPost` model.

#### **Part 3: Create Views and URL Patterns**

1. **Views**: I created several views in `blog/views.py` to handle the following:
   - **List View**: Display a list of all blog posts.
   - **Detail View**: Display a single blog post in detail.
   - **Create View**: Allow users to create new blog posts.
   - **Update View**: Allow users to edit existing blog posts.

2. **URL Patterns**: In `blog/urls.py`, I defined the URL patterns to route requests to the appropriate views:
   - `/` for the list view (`post_list`).
   - `/post/<id>/` for the detail view (`post_detail`).
   - `/post/new/` for the create post view (`post_create`).
   - `/post/<id>/edit/` for the edit post view (`post_edit`).
   - I then included `blog/urls.py` in the main `urls.py` of the project.

#### **Part 4: Create Templates**

1. **Templates for Each View**: I created HTML templates in the `templates/blog` directory to render each view:
   - **`post_list.html`**: Displays a list of blog posts with links to their detail pages.
   - **`post_detail.html`**: Displays the full content of a blog post, including its title, content, and creation date, along with an "Edit" link to modify the post.
   - **`post_form.html`**: Displays a form for creating or editing a blog post with fields for the title and content.

2. **Base Template**: I created a `base.html` template that provides a basic structure for all pages, including a header with navigation links to "Home" and "New Post".

#### **Part 5: Create Forms**

1. **BlogPostForm**: I created a `ModelForm` for the `BlogPost` model in `blog/forms.py`. This form handles the creation and editing of blog posts, allowing users to submit data for the `title` and `content` fields.

#### **Part 6: Add Basic Styling**

1. **CSS Styling**: I added basic styling to improve the look and feel of the blog application. The CSS was placed in a `styles.css` file under `static/blog/`, and I linked it to `base.html` to apply the styles across all pages.

#### **Part 7: Testing Your App**

1. **Run the Server**: Finally, I started the Django development server using `python manage.py runserver` to test the app. I verified that all features—viewing, creating, editing blog posts—were functioning as expected.

---

### **Final Outcome**

By following these steps, I successfully built a fully functional Django blog application. The app includes:
- A `BlogPost` model with the necessary fields.
- Views for listing, viewing, creating, and editing posts.
- URL routing to connect the views to specific URLs.
- Templates for rendering the content and handling user input.
- Basic CSS styling to enhance the user interface.

This project demonstrates the essential features of a Django application, including working with models, views, templates, forms, and static files.