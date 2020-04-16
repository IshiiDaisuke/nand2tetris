import os
import myParser
import myCode
import mySymbolTable
path_w = 'sample.hack'
sample = myParser.Myclass()
sample.CleanLineList()
sampletable = mySymbolTable.Meclass()

# makeSymbolTable
# まずは(Xxx)のような疑似コードをテーブルに書く作業
count = 0
for _ in range(len(sample.LineList)):
    if(not sample.hasMoreCommands()):
        break
    else:
        command = sample.commandType()
        if command == "A_COMMAND":
            count = count + 1

        elif command == "L_COMMAND":
            cmd = sample.symbol()
            if(not sampletable.contains(cmd)):
                sampletable.addEntry(cmd,count)
        elif command == "C_COMMAND":
            count = count + 1
        else:
            # write
            with open(path_w, mode='a') as f:
                print("Error"+"\n")
        sample.advance()

# もう１周するため探索用のNowLine等を初期化
sample.NowLine = 0
addr = 0
# 変数を格納するOnotherAddress16番目以降が空いてます
Onoaddr = 0x0010
with open(path_w, mode='w') as f:
    f.write("")
for X in range(len(sample.LineList)):
    if(not sample.hasMoreCommands()):
        break
    else:
        command = sample.commandType()
        if command == "A_COMMAND":
            Anum = sample.LineList[X].replace("@","")
            # Aコマンドのうち、純粋な数字のもの
            if Anum.isdigit():
                # format()を使うと2進数表記しても'b'がでてこない
                Anum = format(int(Anum),'b')
                # write
                with open(path_w, mode='a') as f:
                    f.write("0"+Anum.zfill(15)+"\n")
            # Aコマンドのうち、数字でない＝疑似コードor変数
            else:
                # 疑似コード含め過去に登場しているもの =　変数以外
                if sampletable.contains(Anum):
                    addr = sampletable.getAddress(Anum)
                    addr = format(int(addr),'b')
                    with open(path_w, mode='a') as f:
                        f.write("0"+addr.zfill(15)+"\n")
                # 変数
                else:
                    sampletable.addEntry(Anum, Onoaddr)
                    with open(path_w, mode='a') as f:
                        f.write("0"+str(format(int(Onoaddr),'b')).zfill(15)+"\n")
                    # 空きメモリを更新
                    Onoaddr = Onoaddr+1
        # 疑似コード処理なのでoutputする必要ない
        elif command == "L_COMMAND":
            # write
                print("")
        # Cコマンドをそれぞれ解析
        elif command == "C_COMMAND":
            Dnimo = sample.dest()
            Cnimo = sample.comp()
            Jnimo = sample.jump()

            destnum = myCode.dest(Dnimo)
            compnum = myCode.comp(Cnimo)
            jumpnum = myCode.jump(Jnimo)
            # write
            with open(path_w, mode='a') as f:
                f.write("111"+compnum+destnum+jumpnum+"\n")
        sample.advance()
