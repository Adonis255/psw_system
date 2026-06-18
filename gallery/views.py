from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PhotoItem, PurchaseLog
import json

def home(request):
    items = PhotoItem.objects.filter(is_active=True)
    
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key
    
    purchased_photo_ids = PurchaseLog.objects.filter(
        session_key=session_key, 
        purchased_photo=True
    ).values_list('item_id', flat=True)
    
    purchased_number_ids = PurchaseLog.objects.filter(
        session_key=session_key, 
        purchased_number=True
    ).values_list('item_id', flat=True)
    
    return render(request, 'home.html', {
        'items': items,
        'unlocked_photos': list(purchased_photo_ids),
        'unlocked_numbers': list(purchased_number_ids),
    })

@csrf_exempt
def fake_pay(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_id = data.get('item_id')
        purchase_type = data.get('type')
        
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        
        item = get_object_or_404(PhotoItem, id=item_id)
        
        log, created = PurchaseLog.objects.get_or_create(
            session_key=session_key,
            item=item,
            defaults={'purchased_photo': False, 'purchased_number': False}
        )
        
        if purchase_type == 'photo':
            log.purchased_photo = True
        elif purchase_type == 'number':
            log.purchased_number = True
        
        log.save()
        return JsonResponse({'success': True, 'type': purchase_type})
    
    return JsonResponse({'success': False}, status=400)

def download_image(request, item_id):
    item = get_object_or_404(PhotoItem, id=item_id)
    session_key = request.session.session_key
    
    has_access = PurchaseLog.objects.filter(
        session_key=session_key,
        item=item,
        purchased_photo=True
    ).exists()
    
    if not has_access:
        return JsonResponse({'error': 'Pay first!'}, status=403)
    
    return JsonResponse({'image_url': item.image.url})