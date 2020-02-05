poem='''\
	Programming is a fun 
	when the work is done 
	If you waana make your work  also fun:
	Use python
	'''
f=open ('poem.txt' , 'w')
f.write(poem)
f.close()
f=open('poem.txt')
while True:
	line =f.readline()
	if (len(line)== 0):
		break
print (line ,end= '')	
f.close()