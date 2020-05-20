import os
import myCodeWriter

class Myclass:
    def __init__(self,filename):
        # read
        FileName = Path(filename+".vm")
        Assembler_data = FileName.open('r')
        self.LineList = Assembler_data.readlines()
        self.NowLine = 0
        Assembler_data.close()

# コメントアウト//や改行記号、空白を消している
    def CleanLineList(self):
        self.LineList = [a for a in self.LineList if a != '']
        for linenum in range(len(self.LineList)):
            if (self.LineList[linenum][0] == "/"):
                del self.LineList[linenum]
                # [0]の場合-1するとメモリ外に出るため再帰
                if linenum == 0:
                    return self.CleanLineList()
                else:
                    linenum = linenum - 1
                    continue
            else:
                if(0 <= self.LineList[linenum].find("/")):
                    # ごり押し文字検索->削除
                    self.LineList[linenum] = self.LineList[linenum][:self.LineList[linenum].find("/")]
        for linenum in range(len(self.LineList)):
            self.LineList[linenum] = self.LineList[linenum].split()


    def hasMoreCommands(self):
        if len(self.LineList) == self.NowLine:
            return 0
        else:
            return 1

    def advance(self):
        self.NowLine = self.NowLine + 1


    def commandType(self):
        if "push" in self.LineList[self.NowLine][0]:
            self.command = "C_PUSH"
        elif "pop" in self.LineList[self.NowLine][0]:
            self.command = "C_POP"
        elif "label" in self.LineList[self.NowLine][0]:
            self.command = "C_LABEL"
        elif "goto" in self.LineList[self.NowLine][0]:
            self.command = "C_GOTO"
        elif "if" in self.LineList[self.NowLine][0]:
            self.command = "C_IF"
        elif "function" in self.LineList[self.NowLine][0]:
            self.command = "C_FUNCTION"
        elif "return" in self.LineList[self.NowLine][0]:
            self.command = "C_RETURN"
        elif "call" in self.LineList[self.NowLine][0]:
            self.command = "C_CALL"
        else:
            self.command = "C_ARITHMETIC"
        return self.command


    def arg1(self):
        if self.command == "C_ARITHMETIC":
            Arg1 = self.LineList[self.NowLine][0][0]
        else:
            Arg1 = self.LineList[self.NowLine][0][1]
        return Arg1


    def arg2(self):
        if self.command in ["C_PUSH", "C_POP", "C_FUNCTION", "C_CALL"]:
            Arg2 = self.LineList[self.NowLine][0][2]
            return  Arg2
