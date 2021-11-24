from utils import add

def tests():
    res = add(1,2)
    expected = 3
    assert res == expected

if __name__ == "__main__":
    try:
        tests()
    except Exception as e:
        print('Errors')
        print(str(e))
