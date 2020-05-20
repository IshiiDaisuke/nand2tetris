import os
import myParser
import myCode
import mySymbolTable
filename = input("plz_input_filename...:>???.vm")
print("outputfile = now directry")
path_w = filename+'.hack'
sample = myParser.Myclass(filename)
sample.CleanLineList()
sampletable = mySymbolTable.Meclass()
