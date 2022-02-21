from lib import bonjour, somme, call_TA

def test_bonjour():
    assert len(bonjour()) > 0

def test_somme():
    assert somme([2,3]) == 5

def test_call_TA():
    assert "michel" in call_TA('michel')
