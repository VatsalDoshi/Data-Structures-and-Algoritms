a= 'spam spam spam'
b= list(a)
c= a.split()
print(b)
print(c)


d= 'spam-spam1-spam2'
delimiter = '-'
e = d.split(delimiter)
print(e)
print(delimiter.join(e))