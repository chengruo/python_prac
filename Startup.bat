@echo off
if "%1" == "h" goto begin
mshta vbscript:createobject("wscript.shell").run("%~nx0 h",0)(window.close)&&exit
:begin
python C:\Users\utsc0990\Desktop\startup_Script\Print_SendMail.py
python C:\Users\utsc0990\Desktop\startup_Script\CMD.py