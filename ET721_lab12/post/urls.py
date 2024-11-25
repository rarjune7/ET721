from .views import HomePageVIew, CreatePostView

urlpatterns = [
    path('', HomePageView(), name = 'home'),
    path('post', CreatePostView(), name = 'add_post'),
    
]