import yaml

from main import config


document = yaml.load(config)


def test_1():
    assert document.get('language') == 'python'


def test_2():
    assert '2.7' in document.get('python')


def test_3():
    assert '3.7' in document.get('python')


def test_4():
    assert 'pypy' in document.get('python')


def test_5():
    assert 'pypy3' in document.get('python')


def test_6():
    assert 'pip install -r requirements.txt' in document.get('install')


def test_7():
    assert document.get('script') == 'pytest'


def test_8():
    assert document.get('language') == 'python'
