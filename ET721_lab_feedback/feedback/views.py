from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg  # Use Avg directly from models
from .models import Item, Feedback
from .forms import FeedbackForm


def home(request):
    """
    View to display the home page.
    """
    return render(request, 'feedback/home.html')

def item_list(request):
    """
    View to display a list of items.
    """
    items = Item.objects.all()
    return render(request, 'feedback/item_list.html', {'items': items})

def item_list(request):
    """
    View to display a list of items.
    """
    items = Item.objects.all()
    return render(request, 'feedback/item_list.html', {'items': items})


def item_detail(request, item_id):
    """
    View to display the details of a single item, including feedback and the ability to add feedback.
    """
    # Fetch the item or return 404 if not found
    item = get_object_or_404(Item, id=item_id)
    
    # Retrieve all feedback for the item
    feedbacks = Feedback.objects.filter(item=item)
    
    # Calculate the average rating, defaulting to 0 if there are no ratings
    avg_rating = feedbacks.aggregate(avg_rating=Avg('rating'))['avg_rating'] or 0

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Save the new feedback, linking it to the item
            new_feedback = form.save(commit=False)
            new_feedback.item = item
            new_feedback.save()
            return redirect('item_detail', item_id=item.id)
    else:
        form = FeedbackForm()

    # Render the template with item details, feedbacks, average rating, and the feedback form
    return render(request, 'feedback/item_detail.html', {
        'item': item,
        'feedbacks': feedbacks,
        'avg_rating': round(avg_rating, 2),  # Round to 2 decimal places for better display
        'form': form
    })
