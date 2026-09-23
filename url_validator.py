from urllib.parse import urlparse


def validate_url(url):
    """
    Validate and normalize a website URL.
    """

    if not url:
        return False, None, "Please enter a website URL."

    # Add HTTPS if the user does not provide a scheme
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        parsed = urlparse(url)

        if parsed.scheme not in ("http", "https"):
            return False, None, "Only HTTP and HTTPS URLs are supported."

        if not parsed.netloc:
            return False, None, "Please enter a valid website URL."

        if " " in url:
            return False, None, "The URL cannot contain spaces."

        return True, url, None

    except Exception:
        return False, None, "Invalid URL format."