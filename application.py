def in_autotests_we_trust(a, b):
    if a == b:
        print('user 1')
    else:
        print('user 2')
        print('user 3')
        print('user 4')

in_autotests_we_trust(10, '10')

in_autotests_we_trust(0, False)
