#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

flg=set()
with open("use.txt") as frd:
	for line in frd:
		tmp=line.strip()
		if tmp:#
			tmp=tmp.decode("utf-8")
			tmp=tmp.split("  ")
			for tmpu in tmp:
				ind=tmpu.rfind("/")
				fg=tmpu[ind+1:]
				if not fg in flg:
					flg.add(fg)
				if ind<=0:
					print tmpu
					print line.decode("utf-8")
flg=list(flg)
flg.sort()
with open("usetag.txt","w") as f:
	f.write(("\n".join(flg)).encode("utf-8"))
