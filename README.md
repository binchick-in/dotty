# Dotty

A tiny wrapper offering dot notation for dicts and nested dicts.

```
>>> from dotty import Dotty
>>> data = {
...     "foo": "bar",
...     "bin": {
...         "baz": True
...     }
... }
>>> d = Dotty(data)
>>> d.foo
'bar'
>>> d.bin.baz
True
```
