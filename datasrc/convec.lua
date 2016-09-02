torch.setdefaulttensortype('torch.FloatTensor')

function convec(fsrc,frs,lsize)
	local file=io.open(fsrc)
	local num=file:read("*n")
	local rs={}
	while num do
		table.insert(rs,num)
		num=file:read("*n")
	end
	file:close()
	ts=torch.Tensor(rs)
	ts:resize(#rs/lsize,lsize)
	file=torch.DiskFile(frs,'w')
	file:writeObject(ts)
	file:close()
end

function convfile(fsrc,frs,useint)
	local file=io.open(fsrc)
	local lind=file:read("*n")
	local num=file:read("*n")
	local rs={}
	while num do
		local tmpt={}
		for i=1,lind do
			table.insert(tmpt,num)
			num=file:read("*n")
		end
		table.insert(rs,tmpt)
	end
	file:close()
	if useint then
		ts=torch.IntTensor(rs)
	else
		ts=torch.Tensor(rs)
	end
	file=torch.DiskFile(frs,'w')
	file:writeObject(ts)
	file:close()
end

function gvec(nvec,vecsize,frs)
	local file=torch.DiskFile(frs,"w")
	file:writeObject(torch.randn(nvec,vecsize))
	file:close()
end

convec("wvec.txt","wvec.asc",64)

--[[for nf=1,58 do
	convfile("duse/dev"..nf.."i.txt","thd/dev"..nf.."i.asc",true)
end
for nf=1,56 do
	convfile("duse/test"..nf.."i.txt","thd/test"..nf.."i.asc",true)
end
for nf=1,218 do
	convfile("duse/train"..nf.."i.txt","thd/train"..nf.."i.asc",true)
end]]

--convfile("trainer.txt","traineg.asc",3,true)
--convfile("tester.txt","testeg.asc",3,true)
--convfile("dever.txt","deveg.asc",3,true)
--do not forget unk
--gvec(4772,128,"vrvec.asc")
--gvec(44778,128,"nrvec.asc")
