class FileNumberSummer:
	def __init__(self, rootDir, start, end):
		self.rootDir = rootDir
		self.start = start
		self.end = end

	def generateFolderName(self,value):
		if value % 10 == 0:
			value = value - 1
		highest = value + (10 - (value % 10))
		lowest = highest - 9
		return "{0:0=6}".format(lowest) + "-" + "{0:0=6}".format(highest)

	def generateFileName(self,value):
		return "{0:0=6}".format(value) + ".csv"

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
	
	def sumFiles(self,first, last):
		if first == last:
			fileContent = open(self.rootDir + "/" + self.generateFolderName(first) + "/" + self.generateFileName(first), "r").read().split("\n")
			#return self._handleNewLineCaseSummer(fileContent)
			return self._handleNewLineCaseSummer(fileContent)
		else:
			mid = (first + last) // 2
			return (self.sumFiles(first, mid) + self.sumFiles(mid + 1, last))

	def getSum(self):
		return self.sumFiles(self.start, self.end)