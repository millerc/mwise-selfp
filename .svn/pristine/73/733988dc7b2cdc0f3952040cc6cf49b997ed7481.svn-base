import urllib2

try:
    import json
except ImportError:
    import simplejson as json 

from django.conf import settings
from django.contrib import messages
from django.forms.models import model_to_dict
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from qbms.models import Transaction
from selfpublish.models import Ad, Lead

def result(request):
    t, _ = Transaction.objects.get_or_create(
                                             txn_id=request.GET.get('TxnId',''),
                                             opid = request.GET.get('OpId',''),
                                             user_data = request.GET.get('UserData',''),
                                             comment = request.GET.get('Comment',''),
                                             status = request.GET.get('Status',''),
                                             status_code = request.GET.get('StatusCode',''),
                                             status_message = request.GET.get('StatusMessage',''),
                                             txn_timestamp = request.GET.get('TxnTimestamp',''),
                                             customer_name = request.GET.get('CustomerName',''),
                                             customer_street = request.GET.get('CustomerStreet',''),
                                             customer_postal_code = request.GET.get('CustomerPostalCode',''),
                                             masked_ccn = request.GET.get('MaskedCCN',''),
                                             auth_code = request.GET.get('AuthCode',''),
                                             amount = request.GET.get('Amount','').replace(',','')
                                            )    
    try:
        lead = Lead.objects.get(id=t.user_data.split(';')[0])
    except DoesNotExist:
        messages.error(request, 'Lead error. Transaction_id: %s' % t.txn_id)
    else:
        if t.status == 'Success':
            for ad_id in t.user_data.split(';')[1].split(','):
                ad = Ad.objects.get(id=ad_id)
                ad.paid = True
                ad.save()
            messages.success(request, t.status_message)
        else:
            messages.error(request, t.status_message)
            
        return redirect(lead)
    
    return render_to_response("qbms/result.html", {
        "t": model_to_dict(t),
    }, context_instance=RequestContext(request))


def checkout(amount, order, user_data, customer_name, customer_id, comment, cancel_url):

    txn_ticket_request_url = '%s?AuthModel=desktop&AppLogin=%s&AuthTicket=%s&TxnType=Sale&Amount=%s&CustomerName=%s&CustomerID=%s&Comment=%s&UserData=%s&Order=%s&CancelURL=%s' % (settings.QBMS_TICKET_URL, settings.QBMS_APP_LOGIN, settings.QBMS_AUTH_TICKET, str(amount), urllib2.quote(customer_name), str(customer_id), urllib2.quote(comment), urllib2.quote(user_data), urllib2.quote(order), urllib2.quote(cancel_url))
            
    txn_ticket_response = urllib2.urlopen(txn_ticket_request_url)
    txn_ticket_response_data = txn_ticket_response.read().split('\r\n')
    ticket = txn_ticket_response_data[0][7:]
    opid = txn_ticket_response_data[1][5:]
    
    checkout_url = '%s?Ticket=%s&OpId=%s&action=checkout' % (settings.QBMS_CHECKOUT_URL, urllib2.quote(ticket), urllib2.quote(opid))

    return checkout_url
    
def receipt(request, uuid):
    t = Transaction.objects.get(uuid=uuid)
    