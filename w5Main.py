userA=raw_input('userA input kawi, bawi, bo : ')
userB=raw_input('userB input kawi, bawi, bo : ')
if userA=='kawi':
    if userB=='bawi':
        print "%s" %"UserB Win"
    elif userB=='bo':
        print "%s" %"UserA Win"
    else:
        print "%s" %"Draw"
elif userA=='bawi':
    if userB=='kawi':
        print "%s" %"UserA Win"
    elif userB=='bo':
        print "%s" %"UserB Win"
    else:
        print "%s" %"Draw"
elif userA=='bo':
    if userB=='kawi':
        print "%s" %"UserB Win"
    elif userB=='bawi':
        print "%s" %"UserA Win"
    else:
        print "%s" %"Draw"