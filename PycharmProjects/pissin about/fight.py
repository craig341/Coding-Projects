import initial


def mode():
    if initial.is_developer:
        print('developer mode')
    else:
        print('normal mode')
