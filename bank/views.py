from django.shortcuts import render_to_response, get_object_or_404

from bank.models import Account

def account_view(request, account_number=None):
    account = get_object_or_404(Account, pk=account_number)
    payee = request.GET.get('payee')
    amount = request.GET.get('amount')
    context = {'account': account}
    if payee and amount:
        if account.balance - int(amount) < 0:
            context['message'] = {'title': 'Error', 'text': 'Not enough funds', 'type': 'error'}
            return render_to_response('account.html', context)
        account.balance = account.balance - int(amount)
        account.save()
        p = Account.objects.get(pk=int(payee))
        current_balance = p.balance
        p.balance = current_balance + int(amount)
        p.save()
        context['message'] = {'title': 'Transfer successful', 'text': amount+' credits transferred', 'type': 'confirmation'}
    
    return render_to_response('account.html', context)
