#Megan Kenworthy
#HW1-Sort of Sorting
#Dr. Lall
#February 2, 2018

import sys

#Description: Modified bucket sort is a stable version of the bucket
#			  sorting algorithm, modified to be used in radix sort 
#			  by sortinng beginning at the least significant digit 
#	   		  in each input and sorting "up" to the most significant digit		  
#Pre: A list len(L) of each of the characters in position "k"
#Post: A list, newOrder, of length = len(L) containing the "ord" values
# 	   of the input characters in ascending order 
def Modified_Bucket_Sort(L):

	#setting up the buckets for all possible chars
	buckets = [ [] for b in range(256)]
	
	#list used to maintain overall list order 
	newOrder = []

	for name_char in range(0,len(L)): 			#iterate through chars
		theletter = L[name_char]
		thebucket = ord(theletter)
		buckets[thebucket].append(name_char)	#place char in appropriate bucket

	for bucket in buckets:						#iterate through all non-empty buckets
		if len(bucket)!=0:
			for each_char in bucket: 			#append each item to the new order list
				newOrder.append(each_char)		#(will be sorted for all chars at this index)
	return newOrder

#Description: The Radix sorting algorithm executes "k" bucket sorts on characters 
#			  starting with the least significant digit. In Radix we find the list
#			  of characters to be sorted and then determie the new ordering for the 
# 			  list to be sorted in the next iteration. 
# Pre: Unsorted input list, L.
# Post: List L sorted correctly according to the number of pre-defined 'k' places 
def Radix(L):

	#iterate through the least significant chars, 1-0
	for lsc in reversed(range(0,2)):
		charlist=[] 									#character list, used in bucket sort
		sortedlist = []									#used for next iteration of sort
		for inputnames in L:
			charlist.append(inputnames[lsc])    
		Bsorted = Modified_Bucket_Sort(charlist)		#calling bucket sort on the charlist

		for nameindex in range(0, len(Bsorted)):		#getting the new order of the input list
			sortedlist.append(L[Bsorted[nameindex]])    #finds/orders the names correctly
		L = sortedlist 									#according to the past iteration 
		
	return L


def main():
    inputLine=1
    inputFile=[]
    while inputLine!='0': 
            inputLine=sys.stdin.readline() #reads in inputs and puts each line into a list fileList
            inputLine=inputLine.strip('\n')
            inputFile.append(inputLine) 
    
    #for formatting (newline between sets)
    newset=True

    for n in range(0,len(inputFile)):
        currentinput=inputFile[n]

        #isdigit() - python builtin method for string handeling, returns "TRUE" if all vals
        #			 in string are digits (used bec readline reads in as string)
        if currentinput.isdigit() and currentinput!='0': 
            if newset!=True:
                print   
            newset=False
            
            #Iterates through the current set that is meant to be sorted 
            #Appends the value at lengthoftest(current set)+position in that set
            #    to get the correct inputs 
            lengthoftest=int(currentinput)
            List_to_Sort=[]
            for i in range(1,lengthoftest+1):
                List_to_Sort.append(inputFile[n+i]) 
            
            SortedList = Radix(List_to_Sort) 
            for name in SortedList:
            	print(name)
        
main()
	
	
