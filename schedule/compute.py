from django.http import JsonResponse
import time

def main(request):
    data = request.POST.get('some_data')
    print(data)
    return JsonResponse({'status': 'success'})