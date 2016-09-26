print("set default tensor type to float")
torch.setdefaulttensortype('torch.FloatTensor')

function gradUpdate(mlpin, x, y, criterionin, learningRate)
	local pred=mlpin:forward(x)
	local err=criterionin:forward(pred, y)
	sumErr=sumErr+err
	local gradCriterion=criterionin:backward(pred, y)
	mlpin:zeroGradParameters()
	mlpin:backward(x, gradCriterion)
	mlpin:updateGradParameters(0.875)
	mlpin:updateParameters(learningRate)
	mlpin:maxParamNorm(-1)
end

function evaDev(mlpin, x, y, criterionin)
	mlpin:evaluate()
	local serr=0
	for curpot=1,ndev do
		serr=serr+criterionin:forward(mlpin:forward(x[curpot]), y[curpot])
	end
	mlpin:training()
	return serr/ndev
end

--[[function inirand(cyc)
	cyc=cyc or 8
	for i=1,cyc do
		local sdata=math.random(nsam)
	end
end]]

function saveObject(fname,objWrt)
	local tmpod=nil
	if not torch.isTensor(objWrt) then
		tmpod=nn.Serial(objWrt)
		tmpod:lightSerial()
	else
		tmpod=objWrt
	end
	local file=torch.DiskFile(fname,'w')
	file:writeObject(tmpod)
	file:close()
end

print("load settings")
require"conf"

print("load data")
require "dloader"

sumErr=0
crithis={}
cridev={}
erate=0
edevrate=0
storemini=1
storedevmini=1
minerrate=starterate
mindeverrate=minerrate

print("load packages")
require "nn"
require "rnn"
require "SeqBGRU"
--require "nngraph"
require "dpnn"
require "vecLookup"
require "maskZerovecLookup"
require "gnuplot"

function train()

	print("design neural networks and criterion")
	require "designn"
	local nnmod=getnn()

	print(nnmod)
	nnmod:training()

	local critmod=getcrit()

	print("init train")
	local epochs=1
	local lr=modlr
	--inirand()
	print("Init model Dev:"..evaDev(nnmod,devin,devt,critmod))
	collectgarbage()

	print("start pre train")
	for tmpi=1,warmcycle do
		for tmpj=1,ieps do
			for curpot=1,nsam do
				gradUpdate(nnmod,mword[curpot],mwordt[curpot],critmod,lr)
			end
		end
		local erate=sumErr/eaddtrain
		table.insert(crithis,erate)
		print("epoch:"..tostring(epochs)..",lr:"..lr..",Tra:"..erate)
		sumErr=0
		epochs=epochs+1
	end

	epochs=1
	icycle=1

	aminerr=0
	lrdecayepochs=1

	while true do
		print("start innercycle:"..icycle)
		for innercycle=1,gtraincycle do
			for tmpi=1,ieps do
				for curpot=1,nsam do
					gradUpdate(nnmod,mword[curpot],mwordt[curpot],critmod,lr)
				end
			end
			local erate=sumErr/eaddtrain
			table.insert(crithis,erate)
			local edevrate=evaDev(nnmod,devin,devt,critmod)
			table.insert(cridev,edevrate)
			print("epoch:"..tostring(epochs)..",lr:"..lr..",Tra:"..erate..",Dev:"..edevrate)
			local modsavd=false
			if edevrate<mindeverrate then
				print("new minimal dev error found,save model")
				mindeverrate=edevrate
				saveObject("modrs/devnnmod"..storedevmini..".asc",nnmod)
				storedevmini=storedevmini+1
				if storedevmini>csave then
					storedevmini=1
				end
				modsavd=true
			end
			if erate<minerrate then
				minerrate=erate
				aminerr=0
				if not modsavd then
					print("new minimal error found,save model")
					saveObject("modrs/nnmod"..storemini..".asc",nnmod)
					storemini=storemini+1
					if storemini>csave then
						storemini=1
					end
				end
			else
				if aminerr>=expdecaycycle then
					aminerr=0
					if lrdecayepochs>lrdecaycycle then
						modlr=lr
						lrdecayepochs=1
					end
					lrdecayepochs=lrdecayepochs+1
					lr=modlr/(lrdecayepochs)
				end
				aminerr=aminerr+1
			end
			sumErr=0
			epochs=epochs+1
		end

		print("save neural network trained")
		saveObject("modrs/nnmod.asc",nnmod)

		print("save criterion history trained")
		local critensor=torch.Tensor(crithis)
		saveObject("modrs/crit.asc",critensor)
		local critdev=torch.Tensor(cridev)
		saveObject("modrs/critdev.asc",critdev)

		print("plot and save criterion")
		gnuplot.plot(critensor)
		gnuplot.figprint("modrs/crit.png")
		gnuplot.figprint("modrs/crit.eps")
		gnuplot.plotflush()
		gnuplot.plot(critdev)
		gnuplot.figprint("modrs/critdev.png")
		gnuplot.figprint("modrs/critdev.eps")
		gnuplot.plotflush()

		critensor=torch.Tensor()
		critdev=torch.Tensor()

		print("task finished!Minimal error rate:"..minerrate.."	"..mindeverrate)

		print("wait for test, neural network saved at nnmod*.asc")

		icycle=icycle+1

		print("collect garbage")
		collectgarbage()

	end
end

train()
