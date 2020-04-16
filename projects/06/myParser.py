import os
import myCode
import mySymbolTable

class Myclass:
    def __init__(self):
        # read
        FileName = input("plz_input_filename...:")
        print("outputfile = now directry")
        # ファイルが存在しているかの確認
        if os.path.isfile(FileName):
            Assembler_data = open(FileName, "r")
            self.LineList = Assembler_data.readlines()
            self.NowLine = 0

            Assembler_data.close()
        else:
            print("\n...\n")
            print("...\n")
            print("...\n")
            print("Notfound...\n\n")

# コメントアウト//や改行記号、空白を消している
    def CleanLineList(self):
        for linenum in range(len(self.LineList)):
            self.LineList[linenum] = self.LineList[linenum].rstrip()
            self.LineList[linenum] = self.LineList[linenum].replace(" ","")
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


    def hasMoreCommands(self):
        if len(self.LineList) == self.NowLine:
            return 0
        else:
            return 1


    def advance(self):
        self.NowLine = self.NowLine + 1


    def commandType(self):
        if self.LineList[self.NowLine][0] == "@":
            self.command = "A_COMMAND"
        elif self.LineList[self.NowLine][0] == "(":
            self.command = "L_COMMAND"
        else:
            self.command = "C_COMMAND"
        return self.command


    def symbol(self):
        # replaceは破壊的作業じゃないらしいから代入して壊した
        cmd = self.LineList[self.NowLine]
        if self.command == "A_COMMAND":
            cmd = cmd.replace('@','',1)
        elif self.command == "L_COMMAND":
            cmd = cmd.replace('(','')
            cmd = cmd.replace(')','')
        return cmd


    def dest(self):
        if "=" in self.LineList[self.NowLine]:
            eq = self.LineList[self.NowLine].index("=")
            Dnimo = self.LineList[self.NowLine][:eq]
            return Dnimo
        else:
            return "null"


    def comp(self):
        # 基本的なC命令かな
        if "=" in self.LineList[self.NowLine]:
            eq = self.LineList[self.NowLine].index("=")
            Cnimo = self.LineList[self.NowLine][eq+1:]
            return Cnimo
        # 0;JMTみたいなのに対して、0を取得するため
        elif ";" in self.LineList[self.NowLine]:
            semi = self.LineList[self.NowLine].index(";")
            Cnimo = self.LineList[self.NowLine][:semi]
            return Cnimo
        else:
            return "null"


    def jump(self):
        # C命令のJを取る場合
        if ";" in self.LineList[self.NowLine]:
            semi = self.LineList[self.NowLine].index(";")
            Jnimo = self.LineList[self.NowLine][semi+1:]
            return Jnimo
        else:
            return "null"
