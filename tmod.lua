print("set default tensor type to float")
torch.setdefaulttensortype('torch.FloatTensor')

function loadObject(fname)
	local file=torch.DiskFile(fname)
	local objRd=file:readObject()
	file:close()
	return objRd
end

function loadTrain(fprefix,ifafix,tfafix,nfile)
	local id={}
	local td={}
	for i=1,nfile do
		table.insert(id,loadObject(fprefix..i..ifafix))
		table.insert(td,loadObject(fprefix..i..tfafix))
	end
	return id,td
end

require "conf"
require "dloader"
require "nn"
require "rnn"
require "SeqBGRU"
require "vecLookup"
require "maskZerovecLookup"
require "designn"

tmod=getnn()

crit=getcrit()

inp=devin[1]
tar=devt[1]

rs=tmod:forward(inp)

crit:forward(rs,tar)
