function loadObject(fname)
	local file=torch.DiskFile(fname)
	local objRd=file:readObject()
	file:close()
	return objRd
end

--[[function loadseq(fname)
	local file=io.open(fname)
	local num=file:read("*n")
	local rs={}
	while num do
		local tmpt={}
		for i=1,num do
			local vi=file:read("*n")
			table.insert(tmpt,vi)
		end
		table.insert(rs,tmpt)
		num=file:read("*n")
	end
	file:close()
	return rs
end]]

function loadSeqTensor(fname)
	local file=io.open(fname)
	local lind=file:read("*n")
	local rs={}
	local num=file:read("*n")
	while num do
		local tmpt={}
		for i=1,lind do
			table.insert(tmpt,num)
			num=file:read("*n")
		end
		table.insert(rs,torch.Tensor(tmpt))
	end
	file:close()
	return rs
end

function loadTrain(iprefix,tprefix,ifafix,tfafix,nfile)
	local id={}
	local td={}
	for i=1,nfile do
		table.insert(id,loadObject(iprefix..i..ifafix))
		table.insert(td,loadSeqTensor(tprefix..i..tfafix))
	end
	return id,td
end

wvec=loadObject('datasrc/wvec.asc')
sizvec=wvec:size(2)

mword,mwordt=loadTrain('datasrc/thd/train','datasrc/duse/train','i.asc','t.txt',218)

devin,devt=loadTrain('datasrc/thd/dev','datasrc/duse/dev','i.asc','t.txt',58)

nsam=#mword
ndev=#devin

eaddtrain=ieps*nsam
