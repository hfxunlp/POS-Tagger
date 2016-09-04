#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from random import random

def exvec(mpf,vecf,rsf,vecsize):
	wdm={}
	with open(mpf) as frd:
		for line in frd:
			tmp=line.strip()
			if tmp:
				tmp=tmp.decode("utf-8")
				tmp=tmp.split("	")
				wdm[tmp[0]]=int(tmp[-1])
	rsd={}
	with open(vecf) as frd:
		for line in frd:
			tmp=line.strip()
			if tmp:
				tmp=tmp.decode("utf-8")
				ind=tmp.find(" ")
				wd=tmp[:ind]
				if wd in wdm:
					rsd[wdm[wd]]=tmp[ind+1:]
	with open(rsf,"w") as fwrt:
		for i in xrange(wdm["UNK"]-1):
			if i in rsd:
				tmp=rsd[i]+"\n"
			else:
				tmp=" ".join([str(random()*2-1) for i in xrange(vecsize)])+"\n"
			fwrt.write(tmp.encode("utf-8"))
		tmp=" ".join(["0" for i in xrange(vecsize)])
		fwrt.write(tmp.encode("utf-8"))

if __name__=="__main__":
	exvec("wd.txt","vectors64.txt","wvec.txt",64)
