#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

frs=[]
fr=[]
count=0
with open("devrs.txt") as fs:
	for line in fs:
		tmp=line.strip()
		if tmp:
			tmp=tmp.decode("utf-8")
			tmp=tmp.split("  ")
			for i in xrange(len(tmp)):
				frs.append(tmp[i])
with open("dev.txt") as f:
	for line in f:
		tmp=line.strip()
		if tmp:
			tmp=tmp.decode("utf-8")
			tmp=tmp.split("  ")
			for i in xrange(len(tmp)):
				fr.append(tmp[i])
for i in xrange(len(frs)):
	s=frs[i]
	r=fr[i]
	los=s.find("/")
	lor=r.find("/")
	s=s[:los]
	r=r[:lor]
	if s!=r:
		count=i
		break
print count
print frs[count]
print fr[count-1]	
	