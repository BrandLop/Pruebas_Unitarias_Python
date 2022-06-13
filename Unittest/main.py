# assert

if __name__ == '__main__':
    try:
        assert 10 == 9, '10 != 9'
        print('>>> The program is still running')
    except AssertionError as e:
        print(e)