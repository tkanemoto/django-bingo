from django.utils.translation import ugettext as _
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.sites.shortcuts import get_current_site

static_url = staticfiles_storage.url


DEFAULT_THEMES = ['Light', 'Dark']


def themes(request):

    site_theme = getattr(settings, "BINGO_THEME", "")
    site_theme_url = static_url('bingo/themes/{}.css'.format(site_theme.lower()))

    themes = list(getattr(settings, "BINGO_THEMES", DEFAULT_THEMES))
        # if there is no theme list, the user cannot
        # reset the theme, so we remove it from session
        # and use the default one.

    user_theme = request.session.get('theme', '')
    user_theme_url = static_url('bingo/themes/{}.css'.format(user_theme.lower()))

    return {
        'site_theme': site_theme,
        'site_theme_url': site_theme_url,
        'themes': themes,
        'user_theme': user_theme,
        'user_theme_url': user_theme_url,
    }


def bingo(request):
    sse_url = getattr(settings, "BINGO_SSE_URL", None)
    use_sse = True if hasattr(settings, "BINGO_USE_SSE") and sse_url else False
    polling_interval = getattr(settings, "BINGO_POLLING_INTERVAL", 10)
    polling_interval_sse = getattr(settings, "BINGO_POLLING_INTERVAL", 120)
    absolute_uri = request.build_absolute_uri()
    host = request.get_host()
    scheme = request.scheme
    site_name = getattr(settings, "BINGO_SITE_NAME", "Bingo")
    items = {
        'use_sse': use_sse,
        'sse_url': sse_url,
        'polling_interval': polling_interval,
        'polling_interval_sse': polling_interval_sse,
        'absolute_uri': absolute_uri,
        'http_host': host,
        'http_scheme': scheme,
        'site_title': site_name,
    }
    for key, value in themes(request).items():
        items[key] = value

    return items
