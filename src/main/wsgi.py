import sentry_sdk

from framework.util.settings import get_setting

sentry_sdk.init(get_setting("SENTRY_DSN"), traces_sample_rate=1.0)


def application(environ, start_response):
    if environ["PATH_INFO"] == "/e/":
        division = 1 / 0

    status = "200 OK"

    headers = {
        "Content-type": "text/html",
    }

    payload = (
        b"<!DOCTYPE html>"
        b"<html>"
        b"<head>"
        b"<title>Master</title>"
        b'<meta charset="utf-8">'
        b"</head>"
        b"<body>"
        b"<h1>My Project</h1>"
        b"<hr>"
        b"<p>This is my first project.</p>"
        b"</body>"
        b"</html>"
    )

    start_response(status, list(headers.items()))

    yield payload
