from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Product, Order

def product_list(request):
    all_products_available = Product.objects.all()
    return JsonResponse([{'id': product.id, 'name': product.name, 'price': product.price} for product in products], safe=False)

def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=orderId)

    return JsonResponse({
        'id': order.id,
        'customer_name': order.customer_name,
        'products': [{'name': product.name, 'price': product.price} for product in order.products.all()],
        'total_price': order.total_price
    })

def create_order(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        product_ids = request.POST.getlist('products')
        order = Order.objects.create(customer_name=customer_name)

        for product_id in product_ids:
            product = Product.objects.get(id=product_id)
            order.products.add(product)

        order.calculate_total_price()
        
        return JsonResponse({'id': order.id, 'customer_name': order.customer_name, 'total_price': order.total_price})
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)
