#Generate a string with N opening brackets ("[") and N closing brackets ("]"), in some arbitrary order. Determine whether
# the generated string is balanced; that is, whether it consists entirely of pairs of opening/closing brackets (in that order),
# none of which mis-nest. Examples:
#[] OK ] [ NOT OK
#[][] OK ] [] [ NOT OK
#[[][]] OK []] [[] NOT OK

string1 = '[]'
string2 = '[[]]'
string3 = '[[[]]]'
string4 = ']['
string5 = '][]['
string6 = '[]][[]'

def test(string):
    length = len(string)
    if length % 2 == 0:
        half = int(length / 2)
        first = '[' * half
        last = ']' * half
        if string[0:half] == first and string[half:length] == last:
            return 'OK'
        else:
            return 'NOT OK'
    else:
        return 'NOT OK'

print(test(string1))
print(test(string2))
print(test(string3))
print(test(string4))
print(test(string5))
print(test(string6))