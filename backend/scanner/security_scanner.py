import requests


SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "X-XSS-Protection"
]


def scan_website(url):
    """
    Perform a safe, non-intrusive HTTP security configuration check.
    """

    try:
        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True,
            headers={
                "User-Agent": "ShieldCheck-Security-Scanner/1.0"
            }
        )

        headers = {}

        for header in SECURITY_HEADERS:
            value = response.headers.get(header)

            headers[header] = {
                "present": bool(value),
                "value": value if value else None
            }

        final_url = response.url

        https_enabled = final_url.lower().startswith("https://")

        return {
            "success": True,
            "https": https_enabled,
            "status_code": response.status_code,
            "final_url": final_url,
            "headers": headers
        }

    except requests.exceptions.Timeout:
        return {
            "success": False,
            "error": "Connection timed out. The website took too long to respond."
        }

    except requests.exceptions.ConnectionError:
        return {
            "success": False,
            "error": "Unable to connect to the website. Please check the URL."
        }

    except requests.exceptions.RequestException as error:
        return {
            "success": False,
            "error": f"Request failed: {str(error)}"
        }

    except Exception:
        return {
            "success": False,
            "error": "An unexpected error occurred while scanning the website."
        }