def kawibawibo():
    'kawi'>'bo'
    'bawi'>'kawi'
    'bo'>'bawi'
    userA=raw_input('userA input kawi, bawi, bo : ')
    userB=raw_input('userB input kawi, bawi, bo : ')
    if userA!=userB:
        if userA>userB:
            print 'UserA Win'
        elif userA<userB:
            print 'UserB Win'
    elif userA==userB:
        print 'draw'
kawibawibo()
