# py-aharef

Graph web page structure with a Python-Tkinter application.

This is inspired by htmlgraph from aharef.info.

## Usage

`python3 src/pyaharef/pyaharef.pyw`

## Output

This program produces a 2-dimensional image of a coloured tree of nodes.

Each node is a part of the structure of the HTML file.

## Requirements

Install required modules in the standard way:

`pip3 -r requirements.txt`

The only packages a normal Python 3 install may be missing are nose-cov, the
nose test coverage module, and pymunk, a Python physics library.  A minimal
installation will also install BeautifulSoup4 and nosetests.

## Development

Use a virtual environment such as with `virtualenv`.

```bash
virtualenv ./.venv
source ./.venv/bin/activate
```

Bugs are tracked on the [GitHub Issue tracker](https://github.com/waveclaw/py-aharef/issues).
