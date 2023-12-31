from .models import Client1
def client_id(request):
    client_id = request.session.get('client_id')
    context = {}
    if client_id:
        try:
            client = Client1.objects.get(id=client_id)
            context['client'] = client
        except Client1.DoesNotExist:
            pass
    return context