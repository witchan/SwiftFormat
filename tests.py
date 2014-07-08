import unittest
import difflib
import os, pprint

import format


o = []




#unittest.TestCase.assertEqual(testCases[0],testCases[1])




class TestFormatting(unittest.TestCase):
    def stringsAreEqual(self,a,b,fileName):
        try:
            self.assertEqual(a,b)
            print("TEST OK for "  + fileName)
        except AssertionError:
            d = difflib.Differ()
            result = list(d.compare(a, b))
            for char in result:
                char = char + " "
                if "+" in char:
                    print("added " + char)
                elif "-" in char:
                    print("removed " + char)
            print("####### Tried to format the code from " + fileName +  " #########")
            print(a.replace(" ","_"))
            print("####### It did not match what the file said was correct formatting: #########")
            print(b.replace(" ","_"))
            print("#######END")
            #print('{} => {}'.format(a,b))
            #for i,s in enumerate(difflib.ndiff(a, b)):
            #    if s[0]==' ': continue
            #    elif s[0]=='-':
            #        print(u'Delete "{}" from position {}'.format(s[-1],i))
            #    elif s[0]=='+':
            #        print(u'Add "{}" to position {}'.format(s[-1],i))
            #print()
    def pathForInTestCaseSubFolder(self,foldername):
        directoryname = os.path.dirname(os.path.abspath(__file__))
        testCaseDirectoryName = directoryname + "/testCases"
        subfolderName = testCaseDirectoryName + "/" + foldername
        fileAbsolutePaths = []
        for root, dirs, files in os.walk(subfolderName):
            for fileName in files:
                if ".test" in fileName:
                    absoluteFilePath = subfolderName + "/" + fileName
                    fileAbsolutePaths.append(absoluteFilePath)
        return fileAbsolutePaths

    def testIndentation(self):
        for fileName in self.pathForInTestCaseSubFolder("indentation"):
            file =  open(os.path.abspath(fileName), "r")
            fileReader = format.FileReader(file)
            testCases  = fileReader.compareTestCasesInReadFile()
            self.stringsAreEqual(testCases[0],testCases[1],fileName)

    def testSpaces(self):
        for fileName in self.pathForInTestCaseSubFolder("spaces"):
            file =  open(os.path.abspath(fileName), "r")
            fileReader = format.FileReader(file)
            testCases  = fileReader.compareTestCasesInReadFile()
            self.stringsAreEqual(testCases[0],testCases[1],fileName)

    #def testIndentation2(self):
    #    file =  open("SwiftFormatter/indentTest.test", "r")
    #    fileReader = reader.FileReader(file)
    #    testCases  = fileReader.parseTestCaseAtIndex(1)
    #    self.stringsAreEqual(testCases[0],testCases[1])
    #    fileReader.close()
    #
    #def testIndentation3(self):
    #    file =  open("SwiftFormatter/indentTest.test", "r")
    #    fileReader = reader.FileReader(file)
    #    testCases  = fileReader.parseTestCaseAtIndex(2)
    #    self.stringsAreEqual(testCases[0],testCases[1])
    #    fileReader.close()
    #
    #def testIndentation4(self):
    #    file =  open("SwiftFormatter/indentTest.test", "r")
    #    fileReader = reader.FileReader(file)
    #    testCases  = fileReader.parseTestCaseAtIndex(3)
    #    self.stringsAreEqual(testCases[0],testCases[1])
    #    fileReader.close()
    #
    #def testIndentation5(self):
    #    file =  open("SwiftFormatter/indentTest.test", "r")
    #    fileReader = reader.FileReader(file)
    #    testCases  = fileReader.parseTestCaseAtIndex(4)
    #    self.stringsAreEqual(testCases[0],testCases[1])
    #    fileReader.close()
    #
    #def testIndentation6(self):
    #    file =  open("SwiftFormatter/indentTest.test", "r")
    #    fileReader = reader.FileReader(file)
    #    testCases  = fileReader.parseTestCaseAtIndex(4)
    #    self.stringsAreEqual(testCases[0],testCases[1])
    #    fileReader.close()
    #
    #def testSpaces1(self):
    #    d = ""

if __name__ == '__main__':
    unittest.main()

    #testFormatter = TestFormatting()

    #testFormatter.test()