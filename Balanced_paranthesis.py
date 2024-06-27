s="(a+b)*((we+aede+)*f)()))"
l=[]
f=0
for i in s:
    if(i=='('):
        l.append('(')
    try:
        if (i == ')' and len(l) > 0):
            l.remove('(')

    except:
        f=1
        break


if(f==0 and len(l)==0):
    print("Paranthesis are balanced")
if(f==1 and len(l)>0):
    print("Parenthesis are not balanced")

