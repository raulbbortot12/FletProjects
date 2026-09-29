pytest.ini
[pytest]
testpaths = tests FletProjects/BookApp/tests FletProjects/ParouImparApp/tests FletProjects/PeopleApp/tests FletProjects/TarefaDescricaoApp/tests
markers =
    smoke: mark test as smoke test
    regression: mark test as regression test

FletProjects/PeopleApp/tests/test_hello.py
def test_feature_1():
    assert True

def test_feature_2():
    assert 1 + 1 == 2

def test_feature_3():
    assert 'hello'.upper() == 'HELLO'