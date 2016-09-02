#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def colmap(fsrclp,srcp,rsp):
	wds=1
	tgs=1
	wdm={}
	tgm={}
	for fsrcu in fsrclp:
		maxlen=False
		with open(rsp+fsrcu+"i.txt","w") as fwrtw:
			with open(rsp+fsrcu+"t.txt","w") as fwrtt:
				with open(srcp+fsrcu+".txt") as frd:
					for line in frd:
						tmp=line.strip()
						if tmp:
							tmp=tmp.decode("utf-8")
							tmp=tmp.split("  ")
							if not maxlen:
								maxlen=len(tmp)
							clen=maxlen-len(tmp)
							wdl=[]
							tgl=[]
							for tmpu in tmp:
								wd,tg=tmpu.split("/")
								if not wd in wdm:
									cind=str(wds)
									wdm[wd]=cind
									wdl.append(cind)
									wds+=1
								else:
									wdl.append(wdm[wd])
								if not tg in tgm:
									cind=str(tgs)
									tgm[tg]=cind
									tgl.append(cind)
									tgs+=1
								else:
									tgl.append(tgm[tg])
							for tc in xrange(clen):
								wdl.append("0")
								tgl.append("1")
							tmp=" ".join(wdl)+"\n"
							fwrtw.write(tmp.encode("utf-8"))
							tmp=" ".join(tgl)+"\n"
							fwrtt.write(tmp.encode("utf-8"))
	wdm["UNK"]=str(wds)
	tgm["UNK"]=str(tgs)
	return wdm,tgm

def trainmap(wdm,tgm,srcp,rsp,fsrclp):
	for fsrcu in fsrclp:
		maxlen=False
		with open(rsp+fsrcu+"i.txt","w") as fwrtw:
			with open(rsp+fsrcu+"t.txt","w") as fwrtt:
				with open(srcp+fsrcu+".txt") as frd:
					for line in frd:
						tmp=line.strip()
						if tmp:
							tmp=tmp.decode("utf-8")
							tmp=tmp.split("  ")
							if not maxlen:
								maxlen=len(tmp)
							clen=maxlen-len(tmp)
							wdl=[]
							tgl=[]
							for tmpu in tmp:
								wd,tg=tmpu.split("/")
								if wd in wdm:
									wdl.append(wdm[wd])
								else:
									wdl.append(wdm["UNK"])
								if tg in tgm:
									tgl.append(tgm[tg])
								else:
									tgl.append(tgm["UNK"])
							for tc in xrange(clen):
								wdl.append("0")
								tgl.append("1")
							tmp=" ".join(wdl)+"\n"
							fwrtw.write(tmp.encode("utf-8"))
							tmp=" ".join(tgl)+"\n"
							fwrtt.write(tmp.encode("utf-8"))

def testmap(wdm,testfl,srcp,rsp):
	for srcfu in testfl:
		maxlen=False
		with open(rsp+srcfu+"i.txt","w") as fwrt:
			with open(srcp+srcfu+".txt") as frd:
				for line in frd:
					tmp=line.strip()
					if tmp:
						tmp=tmp.decode("utf-8")
						tmp=tmp.split("  ")
						if not maxlen:
							maxlen=len(tmp)
						clen=maxlen-len(tmp)
						wdl=[]
						for tmpu in tmp:
							if tmpu in wdm:
								wdl.append(wdm[tmpu])
							else:
								wdl.append(wdm["UNK"])
						for tc in xrange(clen):
							wdl.append("0")
						tmp=" ".join(wdl)+"\n"
						fwrt.write(tmp.encode("utf-8"))

def saved(dsave,df):
	with open(df,"w") as fwrt:
		for k,v in dsave.iteritems():
			tmp=k+"	"+v+"\n"
			fwrt.write(tmp.encode("utf-8"))

def ldd(df):
	rsd={}
	with open(df) as frd:
		for line in frd:
			tmp=line.strip()
			if tmp:
				tmp=tmp.decode("utf-8")
				k,v=tmp.split("	")
				rsd[k]=v
	return rsd

def gdata(trainf,srcp,rsp,devfl,testfl,wdmf,tgmf):
	wdm,tgm=colmap(trainf,srcp,rsp)
	saved(wdm,wdmf)
	saved(tgm,tgmf)
	trainmap(wdm,tgm,srcp,rsp,devfl)
	testmap(wdm,testfl,srcp,rsp)

if __name__=="__main__":
	gdata(["train"+str(i+1) for i in xrange(218)],"rs\\","mapd\\",["dev"+str(i+1) for i in xrange(58)]+["test"+str(i+1) for i in xrange(56)],[],"wd.txt","tg.txt")
