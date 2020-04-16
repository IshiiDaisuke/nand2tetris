import os
import myCode
import mySymbolTable

class Myclass:
    def __init__(self):
    # def constructor():
        # read
        FileName = input("plz_input_filename...:")
        FileName = "pong/Pong.asm"
        if os.path.isfile(FileName):
            Assembler_data = open(FileName, "r")
            self.LineList = Assembler_data.readlines()
            self.NowLine = 0  # add

            Assembler_data.close()
            # return LineList
        else:
            print("\n...\n")
            print("...\n")
            print("...\n")
            print("Notfound...\n\n")


    # def CleanLineList(self.LineList):
    def CleanLineList(self):
        for linenum in range(len(self.LineList)):
            self.LineList[linenum] = self.LineList[linenum].rstrip()
            self.LineList[linenum] = self.LineList[linenum].replace(" ","")
        self.LineList = [a for a in self.LineList if a != '']
        for linenum in range(len(self.LineList)):
            if (self.LineList[linenum][0] == "/"):
                del self.LineList[linenum]
                if linenum == 0:
                    # return Cleanself.LineList(self.LineList)
                    return self.CleanLineList()
                else:
                    linenum = linenum - 1
                    continue
            else:
                if(0 <= self.LineList[linenum].find("/")):
                    self.LineList[linenum] = self.LineList[linenum][:self.LineList[linenum].find("/")]
                # for strnum in range(len(self.LineList[linenum])):
                #     print(self.LineList[linenum][strnum])
                #     if self.LineList[linenum][strnum] == "/":
                #         # if self.LineList[linenum][strnum+1] == "/":
                #         self.LineList[linenum] = self.LineList[linenum][:strnum]
        # return self.LineList


    # def hasMoreCommands(self.LineList,self.NowLine):
    def hasMoreCommands(self):
        if len(self.LineList) == self.NowLine:
            return 0  # false
        else:
            # advance(self.NowLine)
            return 1  # true


    # def advance(self.NowLine):
    def advance(self):
        self.NowLine = self.NowLine + 1


    # def commandType(self.LineList,self.NowLine):
    def commandType(self):
        if self.LineList[self.NowLine][0] == "@":
            self.command = "A_COMMAND"
            # symbol()
            # symbol(self.LineList,self.NowLine,command)
        elif self.LineList[self.NowLine][0] == "(":
            self.command = "L_COMMAND"
            # symbol()
            # symbol(self.LineList,self.NowLine)
        else:
            self.command = "C_COMMAND"
            # dest()
            # comp()
            # jump()
            # dest(self.LineList,self.NowLine)
            # comp(self.LineList,self.NowLine)
            # jump(self.LineList,self.NowLine)
        return self.command


    def symbol(self):
        cmd = self.LineList[self.NowLine]
        if self.command == "A_COMMAND":
            cmd = cmd.replace('@','',1)
        elif self.command == "L_COMMAND":
            cmd = cmd.replace('(','')
            cmd = cmd.replace(')','')
        return cmd
    # def symbol(self.LineList,self.NowLine,command):
    #     if self.command == "A_COMMAND":
    #         self.LineList[self.NowLine].remove('@')
    #     elif self.command == "L_COMMAND":
    #         self.LineList[self.NowLine].remove('(')
    #         self.LineList[self.NowLine].remove(')')
    #     return self.LineList[self.NowLine]


    # def dest(self.LineList,self.NowLine):
    def dest(self):
        if "=" in self.LineList[self.NowLine]:
            eq = self.LineList[self.NowLine].index("=")
            Dnimo = self.LineList[self.NowLine][:eq]
            return Dnimo
        else:
            return "null"


    # def comp(self.LineList,self.NowLine):
    def comp(self):
        if "=" in self.LineList[self.NowLine]:
            eq = self.LineList[self.NowLine].index("=")
            Cnimo = self.LineList[self.NowLine][eq+1:]
            return Cnimo
        elif ";" in self.LineList[self.NowLine]:
            semi = self.LineList[self.NowLine].index(";")
            Cnimo = self.LineList[self.NowLine][:semi]
            return Cnimo
        else:
            return "null"


    # def jump(self.LineList,self.NowLine):
    def jump(self):
        if ";" in self.LineList[self.NowLine]:
            semi = self.LineList[self.NowLine].index(";")
            Jnimo = self.LineList[self.NowLine][semi+1:]
            return Jnimo
        else:
            return "null"
