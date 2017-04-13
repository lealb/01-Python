# -*- coding: utf-8 -*-
# Description:
# 17-4-1:上午12:49
class Row(dict):
    """A dict that allows for object-like property access syntax."""
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)