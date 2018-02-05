# markdown\_jinja

This extension to [Python-Markdown][python_markdown] enables to use [Jinja2][jinja2] markup in markdown documents.

## Installation

This module can installed using ``pip``:

```sh
$ pip install markdown-jinja
```

## Usage

JinjaMarkdown can be passed as a standard extension to Python-Markdown:

```python
import markdown
from markdown_jinja import JinjaMarkdown
html = markdown.markdown(text, extensions=[JinjaMarkdown(context_file='path/to/context.json')])
```

[python_markdown]: https://pythonhosted.org/Markdown/
[jinja2]: http://jinja.pocoo.org/
