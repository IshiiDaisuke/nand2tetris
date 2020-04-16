import os
import myParser
import myCode
import mySymbolTable
path_w = 'sample.hack'
sample = myParser.Myclass()
sample.CleanLineList()
sampletable = mySymbolTable.Meclass()

# makeSymbolTable
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
            # Dnimo = sample.dest()
            # Cnimo = sample.comp()
            # Jnimo = sample.jump()

            # destnum = myCode.dest(Dnimo)
            # if Jnimo == "null":
            #     compnum = myCode.comp(Cnimo)
            # if Cnimo == "null":
            #     jumpnum = myCode.jump(Jnimo)

            count = count + 1
        else:
            # write
            with open(path_w, mode='a') as f:
                print("Error"+"\n")
        sample.advance()


print(sampletable.Symboldic.values())
print(sampletable.Symboldic.keys())



sample.NowLine = 0
addr = 0
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
            if Anum.isdigit():
                Anum = format(int(Anum),'b')
                # write
                with open(path_w, mode='a') as f:
                    f.write("0"+Anum.zfill(15)+"\n")
            else:
                if sampletable.contains(Anum):
                    addr = sampletable.getAddress(Anum)
                    addr = format(int(addr),'b')
                    with open(path_w, mode='a') as f:
                        f.write("0"+addr.zfill(15)+"\n")
                else:
                    sampletable.addEntry(Anum, Onoaddr)
                    with open(path_w, mode='a') as f:
                        f.write("0"+str(format(int(Onoaddr),'b')).zfill(15)+"\n")
                    Onoaddr = Onoaddr+1
        elif command == "L_COMMAND":
            # write
                print("")
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
# print("\nEnd\n---sample---")
# print(sample.LineList)
# print("\n---sampletable---")
# print(sampletable.Symboldic.values())
# print(sampletable.Symboldic.keys())
