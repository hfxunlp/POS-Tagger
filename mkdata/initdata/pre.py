#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

ls=len("19980131-04-013-023/m  ")
with open("srcr.txt","w") as f:
	with open("src.txt") as frd:
		for line in frd:#按行读
			tmp=line.strip()#读一行后去左右的换行空格制表等符号
			if tmp:#如果tmp不为空
				tmp=tmp.decode("GB2312","ignore")#以utf-8解码
				if tmp.startswith('199801'):
					tmp=tmp[ls:]+"\n"
					f.write(tmp.encode("utf-8"))
