from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Feedback
from .forms import FeedbackForm

def item_list(request):
    items = Item.objects.all()
    return render(request, 'feedback/item_list.html', {'items': items})


def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    feedbacks = item.feedbacks.all()
    avg_rating = feedbacks.aggregate(models.Avg('rating'))['rating__avg'] or 0

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            new_feedback = form.save(commit=False)
            new_feedback.item = item
            new_feedback.save()
            return redirect('item_detail', item_id=item.id)
    else:
        form = FeedbackForm()

    return render(request, 'feedback/item_detail.html', {
        'item': item,
        'feedbacks': feedbacks,
        'avg_rating': avg_rating,
        'form': form
    })
