#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional, Iterable
import argh
import moviecastcrew as mcc


@argh.arg('--category', '-c', help='Category of people to return (cast, director, etc.)', nargs='+')
def search(movie_name: str, category: Optional[Iterable[str]] = None):
    mcc.search(movie_name, category)


parser = argh.ArghParser()
parser.add_commands([search])

if __name__ == '__main__':
    parser.dispatch()
