#Total number of lines starting with 'tempest' in first  file
import re
import sys
class compare:
	def __init__(self):
		file1 = open(sys.argv[1],'rt')
		file2 = open(sys.argv[2],'rt')
#file1=open('/home/anvitha/Downloads/source.txt').readlines()
		count1 = 0 
		count2 = 0
		count3 = 0
		count4 = 0
		dictstr1={}
		liststr1=[]
		dictstr2={}
		liststr2=[]
		for i in file1:
			if i.startswith('tempest'):
				str1=i.split()
				if str1[1] == '...':
					count1 +=1
					dkey1 = str1[0]
					dval1 = str1[2]
					dictstr1[dkey1] = dval1
					a = str(dkey1) + str(dval1)
					liststr1.append(a)
			
#Total number of lines starting with 'tempest' in second  file 
		print "Total number of lines starting with 'tempest' in src  file",count1
#file2=open('/home/anvitha/Downloads/destination.txt').readlines()
		for j in file2:
			if j.startswith('tempest'):
				str2=j.split()
				if str2[1] =='...':
					count2 +=1
					dkey2 = str2[0]
					dval2 = str2[2]
					dictstr2[dkey2] = dval2
					b = str(dkey2) + str(dval2)
					liststr2.append(b)
		print "Total number of lines starting with 'tempest' in dest  file ",count2
		fl3 = open("same",'w+')
		aa = set(liststr1)
		bb = set(liststr2)
		count3=aa.intersection(bb)
		print "The Total number of lines 'tempest' to '...' matching status same ",len(count3)
		fl3.close()
		fl4 = open("diff",'w+')
		for k in dictstr1:
			for l in dictstr2:
				if k == l:
					if dictstr1[k] != dictstr2[l]:
						count4 +=1
		print "Total number of lines 'tempest' to '...' matching status differs",count4
		fl4.close()
		fl5 = open("avlfirst",'w+')
		cc = set(dictstr1)
		dd = set(dictstr2)
		count5=dd.difference(cc)
		print " file which has lines 'tempest' to '...' available in first not in second", len(count5)
		fl5.close()
		fl6 = open("avlsecond",'w+')
		count6 =cc.difference(dd)
		print " file which has lines 'tempest' to '...' available in second not in first",len(count6)
		fl6.close()
		fl7 = open("any",'w+')
		count7 = cc.intersection(dd)
		print "Total number of lines 'tempest' to '...' matching status may be anything ", len(count7)
		fl7.close()
comp=compare()



