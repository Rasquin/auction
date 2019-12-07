from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from artifacts.models import Artifact
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request, pk):
    artifact = get_object_or_404(Artifact, pk=pk)
    print(artifact.pk)
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            
            
            total = artifact.price_to_pay
            order_line_item = OrderLineItem(
                    order=order,
                    artifact=artifact,
                    quantity=1
                   
                )
            order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            
            if customer.paid:
                messages.error(request, "You have successfully paid")
                artifact.paid = True
                artifact.save()
                #return redirect(reverse('view_my_biddings'))
                return redirect(reverse('artifacts'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    
    return render(request, "checkout.html", {"artifact": artifact}, {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})
    
    """
            mybidding = request.session.get('mybidding')
            total = 0
            for id  in mybidding:
                artifact = get_object_or_404(Artifact, pk=id)
                total += artifact.price_to_pay
                order_line_item = OrderLineItem(
                    order=auction_order,
                    artifact=artifact,
                   
                )
                order_line_item.save()
"""