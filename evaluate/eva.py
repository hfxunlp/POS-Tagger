#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def eva(stdf,rsf):
	rsc={}
	stc={}
	mat={}
	with open(stdf) as fstd:
		with open(rsf) as frs:
			sline=fstd.readline()
			while sline:
				rline=frs.readline()
				sline=sline.strip()
				if sline:
					sline=sline.decode("utf-8")
					rline=rline.strip()
					rline=rline.decode("utf-8")
					sline=sline.split("  ")
					rline=rline.split("  ")
					for i in xrange(len(sline)):
						tmp=sline[i]
						ind=tmp.rfind("/")
						stag=tmp[ind+1:]
						tmp=rline[i]
						ind=tmp.rfind("/")
						rtag=tmp[ind+1:]
						stc[stag]=stc.get(stag,0)+1
						rsc[rtag]=rsc.get(rtag,0)+1
						if stag==rtag:
							mat[rtag]=mat.get(rtag,0)+1
				sline=fstd.readline()
	p={}
	r={}
	macrop=0
	macror=0
	microp=0
	micror=0
	total=0
	for k,v in mat.iteritems():
		ri=float(v)
		wei=stc[k]
		ps=ri/rsc[k]
		p[k]=ps
		macrop+=ps
		microp+=ps*wei
		rs=ri/wei
		r[k]=rs
		macror+=rs
		micror+=v
		total+=wei
		print k,rs,ps
	ntag=len(stc)
	macrop/=ntag
	macror/=ntag
	microp/=total
	micror/=float(total)
	macrof=2*macrop*macror/(macrop+macror)
	microf=2*microp*micror/(microp+micror)
	print macrof,microf

#eva("train.txt","trainrs.txt")
eva("dev.txt","devrs.txt")
eva("test.txt","testrs.txt")