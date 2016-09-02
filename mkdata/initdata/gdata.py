#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from random import randint

def gdata(fname_randall,trainf,devf,testf):
	word=set()
	td=[]
	seld=[]
	total=0
	with open(fname_randall) as frd:
		for line in frd:
			tmp=line.strip()
			if tmp:
				tmp=tmp.decode("utf-8")
				wl=tmp.split("  ")
				at=False
				for wu in wl:
					if not wu in word:
						if not at:
							at=True
						word.add(wu)
				if at:
					td.append(tmp)
				else:
					seld.append(tmp)
				total+=1
	ts=int(total*0.1)
	ds=int(total*0.1)
	tl=[]
	while len(tl)<ts:
		ind=randint(0,len(seld)-1)
		tl.append(seld[ind])
		del seld[ind]
	dd=[]
	while len(dd)<ds:
		ind=randint(0,len(seld)-1)
		dd.append(seld[ind])
		del seld[ind]
	td.extend(seld)
	wrtl(trainf,td)
	wrtl(devf,dd)
	wrtl(testf,tl)

def wrtl(fname,lwt):
	with open(fname,"w") as fwrt:
		fwrt.write("\n".join(lwt))

def d2l(dicin):
	rs=[]
	for k,v in dicin.iteritems():
		rs.append(k+"	"+str(v))
	return rs

def main():
	gdata("full.txt","train.txt","dev.txt","test.txt")

if __name__=="__main__":
	main()
