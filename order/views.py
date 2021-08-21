from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from django.utils import timezone

from customer.models import Customer
from order.models import Order, OrderItem
from product.models import Product
from django import views


class Cart(LoginRequiredMixin, views.View):
    permission_required = 'auth.see_profile'

    def get(self, request, *args, **kwargs):
        return render(request, 'order/cart.html')


# def add_to_cart(request, **kwargs):
#     customer = get_object_or_404(Customer, user_ptr_id=request.user.id)
#     product = Product.objects.filter(id=kwargs.get('item_id', "")).first()
#     order_item, status = OrderItem.objects.get_or_create(product=product)
#     customer_order, status = Order.objects.get_or_create(owner=customer, is_ordered=True)
#     customer_order.items.add(order_item)
#     if status:
#         customer_order.ref_code = generate_order_id()
#         customer_order.save()
#
#     messages.info(request, "item added to cart")
#     return redirect(reverse('product:product'))
#
#
# def delete_from_cart(request, item_id):
#     item_to_delete = OrderItem.objects.filter(pk=item_id)
#     if item_to_delete.exists():
#         item_to_delete[0].delete()
#         messages.info(request, "Item has been deleted")
#     return redirect(reverse('order:cart'))
#
#
# def order_details(request, **kwargs):
#     existing_order = get_user_pending_order(request)
#     context = {
#         'order': existing_order
#     }
#     return render(request, 'order/cart.html', context)
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order_item, created = OrderItem.objects.get_or_create(
        product=product,
        is_ordered=False
    )

    order_query_set = Order.objects.filter(owner=request.user, is_ordered=False)

    if order_query_set.exists():
        order = order_query_set[0]

        if Order.items.filter(order__items__product_id=product.id).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Added quantity Item")
            return redirect("product:product_detail", pk=pk)
        else:
            Order.items.add(order_item)
            messages.info(request, "Item added to your cart")
            return redirect("product:product_detail", pk=pk)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(owner_id=request.user.id,
                                     ordered_date=ordered_date,
                                     )
        order.items.add(order_item)
        messages.info(request, "Item added to your cart")
        return redirect('product:product_detail', pk=pk)
#
#
# def remove_from_cart(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     order_qs = Order.objects.filter(
#         user=request.user,
#         ordered=False
#     )
#     if order_qs.exists():
#         order = order_qs[0]
#         if order.items.filter(product__pk=product.pk).exists():
#             order_item = OrderItem.objects.filter(
#                 product=product,
#                 customer=request.user,
#                 ordered=False
#             )[0]
#             order_item.delete()
#             messages.info(request, "Item \"" + order_item.item.item_name + "\" remove from your cart")
#             return redirect("core:product", pk=pk)
#         else:
#             messages.info(request, "This Item not in your cart")
#             return redirect("core:product", pk=pk)
#     else:
#         # add message doesnt have order
#         messages.info(request, "You do not have an Order")
#         return redirect("core:product", pk=pk)
