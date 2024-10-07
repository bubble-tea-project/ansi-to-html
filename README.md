<h1 align="center">AnsiParser</h1>

<div align="center">

A convenient library for converting ANSI escape sequences into text or HTML.


[![PyPI - Stable Version](https://img.shields.io/pypi/v/ansiparser?label=stable)](https://pypi.org/project/ansiparser/#history)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ansiparser)](https://pypi.org/project/ansiparser/)
[![GitHub License](https://img.shields.io/github/license/bubble-tea-project/ansiparser)](https://github.com/bubble-tea-project/ansiparser/blob/main/LICENSE)

</div>

## 📖 Description
Parse ANSI escape sequences into screen outputs. This library implements a parser that processes escape sequences like a terminal, allowing you to convert them into formatted text or HTML.

## ✨ Supported Features
- CSI (Control Sequence Introducer) sequences
    - SGR (Select Graphic Rendition) 
    - CUP (Cursor Position)
    - ED (Erase in Display)
    - EL (Erase in Line)
- Convert
    - formatted text 
    - HTML

## 📦 Installation
AnsiParser is available on [PyPI](https://pypi.org/project/ansiparser/):
```console
python -m pip install ansiparser
```

Or you can use [Poetry](https://github.com/python-poetry/poetry):
```console
poetry add ansiparser
```


## 🎨 Usage
```python
import ansiparser

ansip_screen = ansiparser.new_screen()
ansip_screen.put("\x1b[1;6H-World!\x1b[1;1HHello")

ansip_screen.parse()
converted = ansip_screen.to_formatted_string()

print(converted) # ['Hello-World!']
```


## 📜 License
[![GitHub License](https://img.shields.io/github/license/bubble-tea-project/ansiparser)](https://github.com/bubble-tea-project/ansiparser/blob/main/LICENSE)





