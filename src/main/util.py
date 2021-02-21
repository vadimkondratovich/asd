from pathlib import Path
from typing import Dict
from typing import Optional
from typing import Union
from string import Template

from framework.dirs import DIR_TEMPLATES


def render_template(
    template_path: Union[str, Path],
    context: Optional[Dict] = None,
    *,
    engine: str = "{",
) -> str:
    template = read_template(template_path)
    context = context or {}

    engines = {
        "{": lambda _ctx: template.format(**_ctx),
        "$": Template(template).safe_substitute,
    }

    renderer = engines[engine]
    document = renderer(context)

    return document


def read_template(template_path: Union[str, Path]) -> str:
    template = DIR_TEMPLATES / template_path

    assert template.is_file(), f"template {template_path!r} is not a file"

    with template.open("r", encoding="utf-8") as fd:
        content = fd.read()

    return content
