from math import log

def viterbi(obs, states, start_p, trans_p, emit_p):
	V = [{}]
	for st in states:
		V[0][st] = {"prob": start_p[st] + emit_p[st][obs[0]], "prev": None}
	# Run Viterbi when t > 0
	for t in range(1, len(obs)):
		V.append({})
		for st in states:
			max_tr_prob = max(V[t-1][prev_st]["prob"]+trans_p[prev_st][st] for prev_st in states)
			for prev_st in states:
				if V[t-1][prev_st]["prob"] + trans_p[prev_st][st] == max_tr_prob:
					max_prob = max_tr_prob + emit_p[st][obs[t]]
					V[t][st] = {"prob": max_prob, "prev": prev_st}
					break
	opt = []
	# The highest probability
	max_prob = max(value["prob"] for value in V[-1].values())
	previous = None
	# Get most probable state and its backtrack
	for st, data in V[-1].items():
		if data["prob"] == max_prob:
			opt.append(st)
			previous = st
			break
	# Follow the backtrack till the first observation
	for t in range(len(V) - 2, -1, -1):
		opt.insert(0, V[t + 1][previous]["prev"])
		previous = V[t + 1][previous]["prev"]

	return max_prob,opt

def splitwdtag(lin):
	wdl=[]
	tagl=[]
	for lu in lin:
		ind=lu.rfind("/")
		wdl.append(lu[:ind])
		tagl.append(lu[ind+1:])
	return wdl,tagl

def countfile(fname):
	states=set([])
	wds=set([])
	start_probability={}
	transition_probability={}
	emission_probability={}
	with open(fname) as frd:
		for line in frd:
			tmp=line.strip()
			if tmp:
				tmp=tmp.decode("utf-8")
				tmp=tmp.split("  ")
				wdl,tagl=splitwdtag(tmp)
				stag=tagl[0]
				if not stag in start_probability:
					start_probability[stag]=1
				else:
					start_probability[stag]+=1
				for i in xrange(len(wdl)-1):
					ctag=tagl[i]
					ntag=tagl[i+1]
					if not ctag in transition_probability:
						transition_probability[ctag]={}
					if not ntag in transition_probability[ctag]:
						transition_probability[ctag][ntag]=1
					else:
						transition_probability[ctag][ntag]+=1
					if not ctag in states:
						states.add(ctag)
					cword=wdl[i]
					if not cword in wds:
						wds.add(cword)
					if not ctag in emission_probability:
						emission_probability[ctag]={}
					if not cword in emission_probability[ctag]:
						emission_probability[ctag][cword]=1
					else:
						emission_probability[ctag][cword]+=1
				ctag=tagl[-1]
				cword=wdl[-1]
				if not cword in wds:
					wds.add(cword)
				if not ctag in states:
					states.add(ctag)
				if not ctag in emission_probability:
					emission_probability[ctag]={}
				if not cword in emission_probability[ctag]:
					emission_probability[ctag][cword]=1
				else:
					emission_probability[ctag][cword]+=1
	states=tuple(states)
	wds=tuple(wds)
	return states,norm(start_probability,states),transnorm(transition_probability,states),emisnorm(emission_probability,states,wds)

def norm(din,av):
	sum=0
	ndic={}
	for au in av:
		if au in din:
			tmp=din[au]+1
			sum+=tmp
			ndic[au]=tmp
		else:
			sum+=1
			ndic[au]=1
	sum=float(sum)
	rs={}
	for k,v in ndic.iteritems():
		rs[k]=log(v/sum)
	return rs

def emisnorm(d2in,sk,wk):
	rs={}
	awk=log(1/float(len(wk)))
	nvd={}
	for wu in wk:
		nvd[wu]=awk
	for au in sk:
		if au in d2in:
			rs[au]=norm(d2in[au],wk)
		else:
			rs[au]=nvd
	return rs

def transnorm(d2in,ak):
	rs={}
	aak=log(1/float(len(ak)))
	nvd={}
	for au in ak:
		nvd[au]=aak
	for au in ak:
		if au in d2in:
			rs[au]=norm(d2in[au],ak)
		else:
			rs[au]=nvd
	return rs

def runhmm(trainf,testfl,rsfl):
	states,start_probability,transition_probability,emission_probability=countfile(trainf)
	for i in xrange(len(testfl)):
		with open(rsfl[i],"w") as fwrt:
			with open(testfl[i]) as frd:
				for line in frd:
					tmp=line.strip()
					if tmp:
						tmp=tmp.decode("utf-8")
						wdl=tmp.split("  ")
						_,tagl=viterbi(tuple(wdl),states,start_probability,transition_probability,emission_probability)
						tmp=[]
						for ll in xrange(len(wdl)):
							tmp.append(wdl[ll]+"/"+tagl[ll])
						tmp="  ".join(tmp)+"\n"
						fwrt.write(tmp.encode("utf-8"))

if __name__=="__main__":
	tl=["dev","test"]
	runhmm("train.txt",[i+"wr.txt" for i in tl],[i+"rs.txt" for i in tl])