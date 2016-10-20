from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
import MySQLdb
import time
import struct
import imghdr

def pairing(request):
	E = ['' for x in range(4)]
#	A = ['' for x in range(4)]
	A=[]
	ctr = [0 for x in range(4)]
	
	E[0] = ['X','Y']
	E[1] = ['X','Z']
	E[2] = ['W','X','Z','Y']
	E[3] = ['X','Z','W']
	
	
	ptr = 0
	
	while True:
						
		A.append(E[ptr][ctr[ptr]])

		if len(A) != len (set(A)):
			
			A.pop()
			ctr[ptr] = ctr[ptr] + 1
			if ctr[ptr] > (len(E[ptr])-1):
				
				ctr[ptr] = 0
				ptr = ptr - 1
				ctr[ptr] = ctr[ptr] + 1
				
		else:
			ptr = ptr + 1

		if ptr > 3:
			break
#		E[2].pop() # Delete Last entry
#		E[2].pop()
#		E[2].append('Base')  # Add last entry
	
	
	# Use A as final list and use List operations append and pop
	# to manipulate list for final outcome.
	
#	c = 1
#	for i in range(0,4):
#		A[i] = E[i][1]
		
#		ctr[i] = c
#		c = c + 1
		
#	Y = zip(A,ctr)	
	

			
			
	
	
	
	return render(request,'test_beta.html',{'E':E,'A':A})
