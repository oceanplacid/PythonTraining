# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


first_string = str(input("Enter A String: "))
second_string = str(input("Enter A String: "))

def find_anagrams(string1, string2):
    
    string1 = first_string.casefold()
    string2 = second_string.casefold()
    
        
    sort_string1 = sorted(string1)
    sort_string2 = sorted(string2)
    
    if sort_string1 == sort_string2:
        return True
    else:
        return False

print (find_anagrams(first_string, second_string))