// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed.
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

(INIT)
    @SCREEN
    D=A      // D <- SCREEN
    @addr    // 塗りつぶしたいSCREEN上のワード
    M=D      // SCREEN

    // if(KBD > 0...pressed) goto PRESS
    @KBD
    D=M
    @PRESS
    D;JGT
    @ELSE
    0;JMP
(PRESS) //color select
    @color
    M=-1     // color=-1 black
    @ENDIF
    0;JMP
(ELSE) //color select
    @color
    M=0      // color=0 白
(ENDIF)

(LOOP)      
    @color
    D=M      // D <- color
    @addr
    A=M
    M=D      // *addr <- color
    @addr
    M=M+1

    @8192
    D=A
    @SCREEN
    D=D+A
    @addr
    D=D-M  // D= 8192 + SCREEN - addr
    // 塗り残しがあれば塗りつぶすまで続ける
    @LOOP
    D;JGT

    // 全部塗り終わったら、最初に戻る
    @INIT
    0;JMP

// このプログラムは永久に終了しない
