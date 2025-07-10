from django.conf import settings

def analytics_tracking_id(request):
    return {
        'GA_TRACKING_ID': settings.GA_TRACKING_ID
    }
