HEADER_SCORES = {
    "Content-Security-Policy": 20,
    "Strict-Transport-Security": 20,
    "X-Frame-Options": 10,
    "X-Content-Type-Options": 10,
    "Referrer-Policy": 10,
    "X-XXS-Protection": 10
    }

HTTPS_SCORE = 20


def get_risk_level(score):
    if score >= 90:
        return "Excellent"
    elif score >= 70:
        return "Good"
    elif score >= 40:
        return "Moderate"
    else:
        return "Poor"


def calculate_score(https_enabled, headers):
    """
    Calculate the security score out of 100.
    """

    score = 0

    if https_enabled:
        score += HTTPS_SCORE

    for header, points in HEADER_SCORES.items():
        if headers.get(header, {}).get("present"):
            score += points

    risk_level = get_risk_level(score)

    return {
        "total": score,
        "risk": risk_level
    }