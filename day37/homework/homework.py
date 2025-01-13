# 1
def array(string):  
    items = string.split(',')  
    if len(items) < 3:  
        return None   
    return ' '.join(items[1:-1])
# 2
def template_strings(obj, feature):  
    return obj + " are " + feature
# 3
def contamination(text, char):  
    if not text or not char:  
        return ""  
    return char * len(text)
# 4
def is_palindrome(s):  
    s = s.lower()  
    return s == s[::-1]
# 5
def obfuscate(email):  
    return email.replace('@', ' [at] ').replace('.', ' [dot] ')