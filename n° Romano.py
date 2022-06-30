# transformar numero romano em inteiro

def roman_to_int(input):
    if not isinstance(input, type("")):
        raise TypeError, "expected string, got %s" % type(input)
    input = input.upper()
    nums = {'M':1000,
            'D':500,
            'C':100,
            'L':50,
            'X':10,
            'V':5,
            'I':1,}
    sum = 0
    for i in range(len(input)):
        try:
            value = nums[input[i]]
            if i + 1 < len(input) and nums[input[i+1]] > value:
                sum -= value
            else: sum += value
        except KeyError:
            raise ValueError, 'input is not a valid Roman numeral: %s' % input

    if int_to_roman(sum) == input return sum
    else:
        raise ValueError, 'input is not a valid Roman numeral: %s' % input
