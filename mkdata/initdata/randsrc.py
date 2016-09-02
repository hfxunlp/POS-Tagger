#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from random import shuffle

def ldall(fname):
	rs=[]
	with open(fname) as frd:
		for line in frd:
			tmp=line.strip()
			if tmp:
				rs.append(tmp)
	return rs

def randt(lin):
	shuffle(lin)
	return lin

def wrtl(fname,lwt):
	with open(fname,"w") as fwrt:
		fwrt.write("\n".join(lwt))

def main(fsrc,frs):
	wrtl(frs,randt(ldall(fsrc)))

if __name__=="__main__":
	main("full.txt","randfull.txt")
