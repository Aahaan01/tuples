def palindrome(r):
    e=len(r)-1
    s=0
    while s<e:
        if r[s]!=r[e]:
            return False
        e=e-1
        s=s+1
    return True
r=(1,2,3,2,1)
if palindrome(r):
    print("Its a palindrome!")
else:
    print("Its not a palindrome!")