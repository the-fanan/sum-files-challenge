import os

class FileNumberSummer:
	def __init__(self, absFilesPath):
		self.rootDir = absFilesPath

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
	
	def _recSumFiles(self,listOfFileNames, folderDir, first, last):
		if first == last:
			fileContent = open(folderDir + "/" + listOfFileNames[first], "r").read().split("\n")
			return self._handleNewLineCaseSummer(fileContent)
		else:
			mid = (first + last) // 2
			return (self._recSumFiles(listOfFileNames, folderDir, first, mid) + self._recSumFiles(listOfFileNames, folderDir, mid + 1, last))

	def _sumFiles(self,folderDir):
		files = os.listdir(folderDir)
		return self._recSumFiles(files, folderDir, 0, len(files) - 1)

	def _recSumFolders(self,listOfFolderNames, first, last):
		if first == last:
			return self._sumFiles(self.rootDir + "/" + listOfFolderNames[first])
		else:
			mid = (first + last) // 2
			return (self._recSumFolders(listOfFolderNames, first, mid) + self._recSumFolders(listOfFolderNames, mid + 1, last))

	def _sumFolders(self):
		folders = os.listdir(self.rootDir)
		return self._recSumFolders(folders, 0, len(folders) - 1)

	def getSum(self):
		return self._sumFolders()