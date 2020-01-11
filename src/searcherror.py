# -*- coding: utf-8 -*-


class SearchError(Exception):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
