#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def dbracket(strin):
	lind=strin.find("[")
	rt=strin
	while lind!=-1:
		rind=rt.find("]")
		tmpl=rt[:lind]
		tmpm=rt[lind+1:rind]
		tmpr=rt[rind+1:]
		rind=tmpr.find("  ")
		if rind==-1:
			tmpr=""
		else:
			tmpr=tmpr[rind:]
		rt=tmpl+tmpm+tmpr
		lind=rt.find("[")
	return rt

with open("full.txt","w") as f:
	with open("srcr.txt") as frd:
		for line in frd:#按行读
			tmp=line.strip()#读一行后去左右的换行空格制表等符号
			if tmp:#如果tmp不为空
				tmp=tmp.decode("utf-8")#以utf-8解码
				tmp=dbracket(tmp)+"\n"
				f.write(tmp.encode("utf-8"))
