from django.shortcuts import render_to_response, get_object_or_404

from bank.models import Account

def home(request):
    return render_to_response('home.html')

def account_view(request, account_id=None):
    account = get_object_or_404(Account, account_id=account_id)
    payee = request.GET.get('payee')
    amount = request.GET.get('amount')
    context = {
        'account': account,
        'all_accounts': Account.objects.all()
    }
    if payee and amount:
        if account.balance - int(amount) < 0:
            context['message'] = {'title': 'Error', 'text': 'Not enough funds', 'type': 'error'}
            return render_to_response('account.html', context)
        account.balance = account.balance - int(amount)
        account.save()
        p = Account.objects.get(account_id=payee)
        current_balance = p.balance
        p.balance = current_balance + int(amount)
        p.save()
        context['message'] = {'title': 'Transfer successful', 'text': amount+' credits transferred', 'type': 'confirmation'}
    return render_to_response('account.html', context)
