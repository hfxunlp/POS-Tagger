local maskZerovecLookup, parent = torch.class('nn.maskZerovecLookup', 'nn.vecLookup')

function maskZerovecLookup:__init(vecin, paddingValue, maxNorm, normType)
	parent.__init(self, torch.cat(torch.Tensor(1,vecin:size(2)):zero():typeAs(vecin),vecin,1), paddingValue, maxNorm, normType)
end

function maskZerovecLookup:updateOutput(input)
	self.weight[1]:zero()
	if self.__input and (torch.type(self.__input) ~= torch.type(input)) then
			self.__input = nil -- fixes old casting bug
	end
	self.__input = self.__input or input.new()
	self.__input:resizeAs(input):add(input, 1)
	return parent.updateOutput(self, self.__input)
end

function maskZerovecLookup:accGradParameters(input, gradOutput, scale)
	parent.accGradParameters(self, self.__input, gradOutput, scale)
end

function maskZerovecLookup:type(type, cache)
	self.__input = nil
	return parent.type(self, type, cache)
end
