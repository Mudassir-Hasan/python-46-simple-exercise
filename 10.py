# QUESTION :

# 10. Define a function overlapping()that takes two lists and returns True if they have at least one member in
# common, False otherwise. You may use your is_member() function, or the in operator, but for the sake
# of the exercise, you should (also) write it using two nested for­loops.

# Solution :

def overlapping(lst1 , lst2) :

    if ( len(lst1) > len(lst2) ) :
        
        for item2 in lst2 :
        
            for item1 in lst1:
        
                if(item2 == item1):
        
                    return True

    elif ( len(lst2) > len(lst1) ):
        
        for item1 in lst1 :
        
            for item2 in lst2 :
        
                if ( item1 == item2 ) :
        
                    return True

    return False


list1 = [1,2,3,4,5,6]
list2 = [6,7,8,9,10]

# function calling

f = overlapping(list1, list2)

print(f) 
