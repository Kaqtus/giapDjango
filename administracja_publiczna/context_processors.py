import urllib.parse


def url_ending(request):
    url_1 = str(request.build_absolute_uri)
    url_2 = url_1.split("/")
    url_end = url_2[-2]
    return {'url_end': url_end}
