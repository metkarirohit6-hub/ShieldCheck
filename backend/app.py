from flask import Flask, render_template, request
from scanner.url_validator import validate_url
from scanner.security_scanner import scan_website
from scanner.score_calculator import calculate_score

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/scan", methods=["POST"])
def scan():
    url = request.form.get("url", "").strip()

    # Validate URL
    is_valid, validated_url, error = validate_url(url)

    if not is_valid:
        return render_template(
            "index.html",
            error=error,
            entered_url=url
        )

    # Perform safe security scan
    scan_result = scan_website(validated_url)

    if not scan_result["success"]:
        return render_template(
            "index.html",
            error=scan_result["error"],
            entered_url=url
        )

    # Calculate score
    score_data = calculate_score(
        scan_result["https"],
        scan_result["headers"]
    )

    return render_template(
        "results.html",
        url=validated_url,
        scan=scan_result,
        score=score_data
    )


if __name__ == "__main__":
    app.run(debug=True)