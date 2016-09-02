#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def splitf(fsrc,freq,rsp):
	cursave=1
	minib=16
	maxdl=16
	with open(freq) as frd:
		with open(fsrc) as fsrd:
			cache=[]
			for line in frd:
				tmp=line.strip()
				if tmp:
					tmp=tmp.decode("utf-8")
					lgth,freq=tmp.split("	")
					lgth=int(lgth)
					freq=int(freq)
					if freq>minib:
						if cache:
							nstore=0
							for cu in cache:
								nstore+=cu[-1]
							with open(rsp+str(cursave)+".txt","w") as fwrt:
								for i in xrange(nstore):
									lind=fsrd.readline()
									lind=lind.strip()
									lind=lind.decode("utf-8")
									lind+="\n"
									fwrt.write(lind.encode("utf-8"))
							cursave+=1
							cache=[]
						with open(rsp+str(cursave)+".txt","w") as fwrt:
							for i in xrange(freq):
								lind=fsrd.readline()
								lind=lind.strip()
								lind=lind.decode("utf-8")
								lind+="\n"
								fwrt.write(lind.encode("utf-8"))
						cursave+=1
					else:
						if cache:
							if cache[0][0]-lgth<maxdl:
								cache.append([lgth,freq])
								nstore=0
								for cu in cache:
									nstore+=cu[-1]
								if nstore>minib:
									with open(rsp+str(cursave)+".txt","w") as fwrt:
										for i in xrange(nstore):
											lind=fsrd.readline()
											lind=lind.strip()
											lind=lind.decode("utf-8")
											lind+="\n"
											fwrt.write(lind.encode("utf-8"))
									cursave+=1
									cache=[]
							else:
								nstore=0
								for cu in cache:
									nstore+=cu[-1]
								with open(rsp+str(cursave)+".txt","w") as fwrt:
									for i in xrange(nstore):
										lind=fsrd.readline()
										lind=lind.strip()
										lind=lind.decode("utf-8")
										lind+="\n"
										fwrt.write(lind.encode("utf-8"))
								cursave+=1
								cache=[[lgth,freq]]
						else:
							cache=[[lgth,freq]]

def splitfl(srcfl,frqfl,rsflp):
	for i in xrange(len(srcfl)):
		splitf(srcfl[i],frqfl[i],rsflp[i])

if __name__=="__main__":
	fd=["train","test","dev"]
	splitfl([i+"s.txt" for i in fd],[i+"f.txt" for i in fd],["rs\\"+i for i in fd])
