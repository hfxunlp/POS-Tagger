#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import os

def transfile(srcf,rsf):
	rsd=[]
	lines=0
	with open(srcf) as frd:
		for line in frd:
			tmp=line.strip()
			if tmp:
				tmp=tmp.decode("utf-8")
				tmp=tmp.split(" ")
				rsd.append(tmp)
				lines+=1
	rsd=zip(*rsd)
	with open(rsf,"w") as fwrt:
		tmp=str(lines)+"\n"
		fwrt.write(tmp.encode("utf-8"))
		for rsu in rsd:
			tmp=" ".join(rsu)+"\n"
			fwrt.write(tmp.encode("utf-8"))

def transpath(srcpath,rspath):
	for root,dirs,files in os.walk(srcpath):
		for file in files:
			transfile(srcpath+file,rspath+file)

if __name__=="__main__":
	transpath("mapd\\","duse\\")