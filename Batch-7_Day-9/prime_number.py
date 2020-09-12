'''
file for prime
'''
def prime(check_number=5):
    '''
    function to check if prime
    '''
    factors_count = 0
    for num in range(1, check_number+1):
        if check_number % num == 0:
            factors_count = factors_count + 1
    if factors_count == 2:
        return True
prime()
