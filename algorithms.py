
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


# 01-10-18
# Enter an (unsigned) integer
# convert to binary
# and return the number of 1's
# in the binary representation.

def countBits(n):
    binaryRep = ""
    while n > 0:
        newDigit = int(round(n % 2))
        binaryRep += str(newDigit)
        n = n / 2
    actualB = binaryRep
    counter = 0
    for number in actualB:
        if int(number) == 1:
            counter +=1
    return counter

# tests
print(countBits(0)) #0
print(countBits(4)) # 1
print(countBits(9)) #2
print(countBits(10)) #2
print(countBits(1234)) # 3