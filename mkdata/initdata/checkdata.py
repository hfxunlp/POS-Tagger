#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

flg=set()
with open("full.txt") as frd:
	for line in frd:
		tmp=line.strip()
		if tmp:#
			tmp=tmp.decode("utf-8")
			tmp=tmp.split("  ")
			ld=[]
			for tmpu in tmp:
				ind=tmpu.find("/")
				fg=tmpu[ind+1:]
				if not fg in flg:
					flg.add(fg)
				if ind>0:
					ld.append(tmpu)
				else:
					print tmpu
flg=list(flg)
flg.sort()
with open("tag.txt","w") as f:
	f.write(("\n".join(flg)).encode("utf-8"))
