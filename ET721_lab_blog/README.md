# ET721 Lab Blog by Ravindra

Welcome to my Django-based blog app! This is a simple blog application that I built to practice core Django concepts. It allows users to create, view, and edit blog posts. Through this project, I explored Django's models, views, templates, forms, and URL routing.

## Features

- **Create Blog Posts**: I can add new blog posts to the site.

- **View Blog Posts**: I can see a list of all blog posts and read them in detail.

- **Edit Blog Posts**: I can edit existing blog posts.

- **Responsive Design**: The app includes a clean, responsive design for a better user experience.

## Prerequisites

Before I can run the application, I need to make sure I have the following installed:

- **Python** (3.x)
- **Django** (5.x or compatible version)
- **Git** (for version control)

## Setup and Installation

Here are the steps I followed to set up and run the blog app on my local machine.

### Step 1: Clone the Repository

I first cloned the repository to my local machine using Git:

```bash
git clone https://github.com/rarjune7/ET721_lab_blog.git
```

### Step 2: Set Up the Virtual Environment

After cloning the repository, I navigated into the project directory and set up a Python virtual environment:

```bash
cd ET721_lab_blog
python -m venv venv
```

Then, I activated the virtual environment:

- On Windows:

```bash
venv\Scripts\activate
```

- On macOS/Linux:

```bash
source venv/bin/activate
```

### Step 3: Install Dependencies

To install the required dependencies for the project, I ran the following command:

```bash
pip install -r requirements.txt
```

### Step 4: Set Up the Database

Next, I created the necessary database tables by running:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Run the Development Server

To start the Django development server, I ran:

```bash
python manage.py runserver
```

Now, the app is up and running locally at `http://127.0.0.1:8000/`.

### Step 6: Access the App

Finally, I opened my browser and went to `http://127.0.0.1:8000/` to check out the blog. From there, I could create new posts, view a list of posts, and edit them.

## Project Structure

Here’s a breakdown of the project structure that I used:

- `blogproject/`: The main Django project folder.
  - `blog/`: The app that manages the blog functionality.
    - `models.py`: Contains the model for blog posts (BlogPost).
    - `views.py`: Defines views to display blog posts.
    - `urls.py`: Contains URL routing for the blog views.
    - `templates/blog/`: HTML templates for rendering views.
      - `base.html`: The base template with header and navigation.
      - `post_list.html`: Template for listing all blog posts.
      - `post_detail.html`: Template for displaying individual blog posts.
      - `post_form.html`: Template for creating and editing posts.
    - `forms.py`: The form used for creating and editing blog posts.
  - `static/blog/styles.css`: The CSS file where I added some basic styling for the app.


