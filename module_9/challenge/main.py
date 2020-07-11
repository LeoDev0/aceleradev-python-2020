# .travis.yml
config = """
language: python
python:
    - '2.7'
    - '3.7'
    - 'pypy'
    - 'pypy3'

install:
    - pip install -r requirements.txt

script: pytest
"""
