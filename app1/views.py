from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def homepage(req):
    if req.method == 'POST':
        amount = 50000
        order_currency = 'INR'
        client=razorpay.Client(auth=('rzp_test_4mPo19aF7K67Bz','oblE6ns87ISZPO1Y3cLpgz7u'))
        payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})

    return render(req,'index.html')


