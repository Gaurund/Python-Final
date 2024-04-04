from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    template_name = "cookbookapp/index.html"
    # logger.info('Shop page accessed')

    # week_orders = Order.objects.all()
    # order_products = OrderProduct.objects.all()
    # products = Product.objects.all()

    context = {
        'title': "Сайт кулинарных рецептов",
        # 'orders': week_orders,
        # 'products': products,
        # 'order_products': order_products
    }

    return render(
        request,
        template_name,
        context
    )
