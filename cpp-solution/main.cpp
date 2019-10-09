#include <stdio.h>
#include <iostream>
#include <fstream>

using namespace std;

ifstream f;

string generateFolderName(int a)
{
	char fn[24];
	if (a % 10 == 0) {
		a -= 1;
	}
	int h = a + (10 - (a % 10));
	int l = h - 9;
	sprintf(fn, "%06d-%06d", l, h);
	return fn;
}

string generateFileName(int a)
{
	char fn[12];
	sprintf(fn, "%06d.csv", a);
	return fn;
}

int sumNumbersInFile(string fileDir)
{
	f.open(fileDir);
	long sum = 0;
	int num = 0;
	char c;
	while (!f.eof() ) {
		f.get(c);
		if (c != ',' && c != '\n') {
			int ic = c - '0';
			if (num == 0) {
				num = ic;
			} else {
				num = (num * 10) + ic;
			}
		} 
		if (c == ',' || c == '\n') {
			sum += num;
			num = 0;
		}
	}
	f.close();
	//last number
	//division is done cause the last digit is repeated
	sum += num /10;
	return sum;
}

int main() 
{
	string rootDir = "<ABSOLUTE-PATH-TO-FILES-FOLDER>";
	string fileDir;
	long sum = 0;
	for (int i = 1; i <= 1000; i++) {
		fileDir = rootDir;
		fileDir.append(generateFolderName(i)).append("/").append(generateFileName(i));
		sum += sumNumbersInFile(fileDir);
	}
	cout << sum << '\n';
	return 1;
}

