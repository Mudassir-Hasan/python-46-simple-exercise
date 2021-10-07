import random 

color_l = ["red", "orange", "yellow", "green", "cian", "blue", "violet"]



def color_pick (color_l):
    i = random.randint(0,(len(color_l)-1))
    return color_l[i]

a = color_pick(color_l)

def make_anagram(a):
    anagram = ""
    while len(anagram) != len(a):
        i = random.randint(0,len(a)-1)
        if a[i] not in anagram:
            anagram += a[i]
    return anagram


print(make_anagram(a))