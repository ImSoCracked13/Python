from fraction import Fraction

def test_constructor(capsys):
    f = Fraction(1, 2)
    assert f.numerator == 1
    assert f.denominator == 2
    with capsys.disabled():
        print("Test constructor successful!")

def test_str(capsys):
    f = Fraction(1, 2)
    assert str(f) == '1/2'

    f = Fraction(-1, 2)
    assert str(f) == '-1/2'

    f = Fraction(1, -2)
    assert str(f) == '-1/2'

    f = Fraction(-1, -2)
    assert str(f) == '1/2'
    with capsys.disabled():
        print('Test str successful!')


def test_add(capsys):
    f1 = Fraction(1, 2)
    f2 = Fraction(2, 3)
    f3 = f1.add(f2)

    assert f3.numerator == 7
    assert f3.denominator == 6

    f1 = Fraction(-4, 5)
    f2 = Fraction(6, 7)
    f3 = f1.add(f2)

    assert f3.numerator == 2
    assert f3.denominator == 35