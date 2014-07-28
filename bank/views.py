from django.shortcuts import render_to_response, get_object_or_404

from bank.models import Account

def account_view(request, account_number=None):
    account = get_object_or_404(Account, pk=account_number)
    return render_to_response('account.html', {'account': account})
