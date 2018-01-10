
# 01-09-18
# Check to see if a string has 
# the same amount of 'x's and 'o's. 
# The method must return a boolean 
# and be case insensitive. 
# The string can contain any char.

def xo(s):
    # input is not case sensitive
    str = s.lower()
    # initialize counter variables for x and o
    x_counter = 0
    o_counter = 0
    # Loop thru letters to count x and o
    for letter in str:
        if letter == 'x':
            x_counter += 1
        elif letter == 'o':
            o_counter += 1
    # If x and o counts are equal return true
    if x_counter == o_counter:
        return True
    # If both letter counters = 0 then also return true 
    elif x_counter == 0 & o_counter == 0:
        return True
    else: 
        return False

def test1():
	print(xo(xxoxxxooxCxoxoxxoxoooxxoxAoxxEoxoxbxoxoxoxfoxoxxxooxxooooxdox))
	print(xo(xmxxoGrxdoxxxxoxooooxooxAoSCJooLoxNooxoUfxxpQxtEhkoxooxbx))
	print(xo(obXXCXXooXooXoXooXXooooXXXooXXoXXXoXXooXooXXoooXXXXAooooX))