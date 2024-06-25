# # Bonus
# ## write a function that takes a string as a parameter
# - first check that the type of the parameter is of type str
# - then, it should separates the word at any capital letter and replace it with a small letter 
# - and  should return the new modified string !

# Example: `helloWorldThere` should return :
# ```hello world there```




def separate_and_lower(string):
    if not isinstance(string, str):
        raise ValueError("Input must be a string")
    
    result = ""
    
    for char in string:
        if char.isupper():
            result += " " + char.lower()
        else:
            result += char
    
    return result.strip()



print(separate_and_lower("HelloWorldThere"))

