from django.http import HttpRequest, HttpResponse

from main.util import render_template

TEMPLATE = "tasks/lesson03/task301.html"


def handler(request: HttpRequest) -> HttpResponse:
    name = request.GET.get("name")

    context = {
        "input_name": name,
        "greeting_name": name or "anonymous",
    }

    document = render_template(TEMPLATE, context)

    response = HttpResponse(content=document)

    return response


if __name__ == '__main__':
    x = render_template(TEMPLATE, {'input_name': 1, 'greeting_name': 2})
    print(x)
