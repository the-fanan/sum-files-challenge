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

	def sumNumbersInFile(self,fileDir):
		fileContent = open(fileDir, "r")
		sums = 0
		try:
			line = fileContent.readline()
			while line:
				line = line.strip()
				line = line.split(",")
				for number in line:
					sums += int(number)
				line = fileContent.readline()
		finally:
			fileContent.close()
		return sums

	def sumFiles(self,first, last):
		sums = 0
		for i in range(first, last + 1):
			fileDir = self.rootDir + "/" + self.generateFolderName(i) + "/" + self.generateFileName(i)
			sums += self.sumNumbersInFile(fileDir)
		return sums

	def getSum(self):
		return self.sumFiles(self.start, self.end)