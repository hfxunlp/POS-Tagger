#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def parseline(linin):
	rs=[]
	tmp=linin
	rind=tmp.find(")")
	ewtmp=tmp[:rind]
	lind=ewtmp.rfind("(")
	uniwt=ewtmp[lind+1:rind]
	tag,wd=uniwt.split(" ")
	rs.append((wd,tag))
	tmp=tmp[rind+1:]
	lind=tmp.find("(")
	while lind!=-1:
		tmp=tmp[lind:]
		rind=tmp.find(")")
		ewtmp=tmp[:rind]
		lind=ewtmp.rfind("(")
		uniwt=ewtmp[lind+1:rind]
		tag,wd=uniwt.split(" ")
		rs.append((wd,tag))
		tmp=tmp[rind+1:]
		lind=tmp.find("(")
	return rs

def buildpdformat(lin):
	tmp=[]
	for lu in lin:
		tmp.append("/".join(lu))
	return "  ".join(tmp)

def parsefile(fsrc,frs):
	with open(frs,"w") as fwrt:
		with open(fsrc) as frd:
			for line in frd:
				tmp=line.strip()
				if tmp:
					tmp=tmp.decode("utf-8")
					tmp=buildpdformat(parseline(tmp))+"\n"
					fwrt.write(tmp.encode("utf-8"))

if __name__=="__main__":
	parsefile("src.txt","use.txt")
