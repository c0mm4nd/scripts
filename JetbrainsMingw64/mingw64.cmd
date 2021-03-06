:: @name         JetbrainsMingw64
:: @namespace    https://c0mm4nd.com/
:: @version      0.1.1
:: @description  A solution to load msys2(mingw64) as the default terminal in jetbrains IDEs
:: @author       Command M
@echo off
setlocal

set MSYS2_PATH_TYPE=inherit

:: change MINGW64 to MINGW32 if you need 32bit toolchain
set MSYSTEM=MINGW64 

:: change C:\msys64 to your msys2 root
"C:\msys64\usr\bin\sh" -login -i -lc 'cd $OLDPWD; bash'
