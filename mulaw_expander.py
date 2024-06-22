#mu-law calculator
from time import time
m=1

def mulaw(step,chord): #7 to 12/15 bit decoding
	output_chord=(((2**chord)*33)-33)*m
	stepsize=(2*m*(2**chord))
	exp_num = output_chord+(step*stepsize) 
	print ("Encoded x= ",x, "binary is :",bin(x),"step= ",step, "chord = ",chord)
	print("Expanded chord  = ", output_chord)
	print("stepsize =", stepsize)
	print ("expanded x is :", exp_num,"  expanded x + half step bias is :", exp_num + (stepsize>>1))
	print("\n")
	
 # Generate the lookup table
t=time()
for chord in range(8): #chord 0 to 7
		for step in range(16): #step 0 to 15
					x=(chord<<4)+step
					mulaw(step,chord)
print ("128 values calculated in ",time()-t, "seconds")

x=""
while x=="":
#Take an input	
	bits=input("enter A for 13 bit conversion, B for 16 bit : ")
	x=int(input("\n enter a number 0 to 255 to convert :"))
	polarity=x&128
	x=x&127
	step=x&15
	chord=(x&120)>>4
	if bits =="b":
		m=4
	else:
		m=1
	mulaw(step, chord)
	x=""
	if polarity ==128:
		print ("Polarity is positive\n")
	else :
		print ("Polarity is negative\n")