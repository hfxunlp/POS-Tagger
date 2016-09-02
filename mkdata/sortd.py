#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def sortf(fsrc,frs,freqf):
	l=[]
	storage={}
	with open(fsrc) as frd:
		for line in frd:
			tmp=line.strip()
			if tmp:
				tmp=tmp.decode("utf-8")
				lgth=len(tmp.split("  "))
				if lgth in storage:
					storage[lgth].append(tmp)
				else:
					l.append(lgth)
					storage[lgth]=[tmp]
	l.sort(reverse=True)
	with open(frs,"w") as fwrtd:
		with open(freqf,"w") as fwrtf:
			for lu in l:
				cwrtl=storage[lu]
				tmp="\n".join(cwrtl)+"\n"
				fwrtd.write(tmp.encode("utf-8"))
				tmp=str(lu)+"	"+str(len(cwrtl))+"\n"
				fwrtf.write(tmp.encode("utf-8"))

def sortfl(srcfl,rsfl,frqfl):
	for i in xrange(len(srcfl)):
		sortf(srcfl[i],rsfl[i],frqfl[i])

if __name__=="__main__":
	fd=["train","test","dev"]
	sortfl([i+".txt" for i in fd],[i+"s.txt" for i in fd],[i+"f.txt" for i in fd])
