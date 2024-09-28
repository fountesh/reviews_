from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Product, Reviews
from .forms import ReviewForm

# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'C:/Users/User/.vscode/project_/reviews_/reviews_proj/reviews_app/templates/products/product_list.html'
    context_object_name = 'products'

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            return redirect('product_detail', pk=pk)
    else:
        form = ReviewForm()

    return render(request, 'C:/Users/User/.vscode/project_/reviews_/reviews_proj/reviews_app/templates/products/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'form': form
    })