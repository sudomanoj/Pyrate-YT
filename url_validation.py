def url_validation(url):
    try:
    	cleaned_url = url.split('&')[0]
    except:
        cleaned_url = url
    return cleaned_url