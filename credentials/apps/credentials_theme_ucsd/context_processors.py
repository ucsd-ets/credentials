""" Marketing URLS context processors. """
from django.conf import settings


def marketing_urls(request):

    return {
        'MARKETING_URLS': getattr(settings, 'MARKETING_URLS', {})
    }
