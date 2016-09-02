#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def dealfile(fsrc,frs):
	with open(frs,"w") as f:
		with open(fsrc) as frd:
			for line in frd:
				tmp=line.strip()
				if tmp:#
					tmp=tmp.decode("utf-8")
					tmp=tmp.split("  ")
					ld=[]
					for tmpu in tmp:
						ind=tmpu.rfind("/")
						if ind!=-1:
							ld.append(tmpu[:ind])
						else:
							ld.append(tmpu)
						tmp="  ".join(ld)+"\n"
					f.write(tmp.encode("utf-8"))

fd=["test","dev"]
#fd=["train"]
for fu in fd:
	dealfile(fu+".txt",fu+"wr.txt")
