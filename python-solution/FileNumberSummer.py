class FileNumberSummer:
	def __init__(self, absFilePath):
		self.fileData = open(absFilePath, "r").read().split("\n")

	def _recursivelySumNumbers(self,listOfNumbers, first, last):
		if first == last:
			return int(listOfNumbers[first])
		else:
			mid = (first + last) // 2
			return (self._recursivelySumNumbers(listOfNumbers, first, mid) + self._recursivelySumNumbers(listOfNumbers, mid + 1, last))

	def _sumNumbers(self,listOfNumbers):
		n = len(listOfNumbers)
		return self._recursivelySumNumbers(listOfNumbers, 0, n - 1)

	def _recursivelyHandleNewLineCaseSummer(self,listOfNumbers, first, last):
		if first == last:
			return self._sumNumbers(listOfNumbers[first].split(","))
		else:
			mid = (first + last) // 2
			return (self._recursivelyHandleNewLineCaseSummer(listOfNumbers, first, mid) + self._recursivelyHandleNewLineCaseSummer(listOfNumbers, mid + 1, last))

	def _handleNewLineCaseSummer(self,listOfNumbers):
		n = len(listOfNumbers)
		return self._recursivelyHandleNewLineCaseSummer(listOfNumbers, 0, n - 1)
	
	def getSum(self):
		return self._handleNewLineCaseSummer(self.fileData)