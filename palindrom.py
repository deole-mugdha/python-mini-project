# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def pallindrom3(n):
    print(reversed(n))
    reverse=''.join(reversed(n))
    if n==reverse:
        print("number is pallindrome")
    else:
        print("number is not pallindrome")
    
pallindrom3("121")    
    