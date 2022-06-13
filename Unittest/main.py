# assert

if __name__ == '__main__':
    try:
        # assert 10 == 9, '10 != 9'
        # This is the same as previous line
        if not 10 == 9:
            raise AssertionError('10 != 9')
        print('>>> The program is still running')
    except AssertionError as e:
        print(e)