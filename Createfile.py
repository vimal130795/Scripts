import os,json
files = ['Text_Document.txt','New_Text_Document.txt','New Text Document.txt','New.Text_Document.txt','New Text Document.txt','New.Text_Document.txt']
for a in files:
    temp = a
    i=1
    while 1:
        if os.path.exists(temp):
            b = a.split('.')
            b[-2] = b[-2]+' ('+str(i)+')'
            temp ='.'.join(b)
            i+=1
        else:
            a = temp
            break
    print (a)
    with open(a,'w') as f:
        f.write('hello')

