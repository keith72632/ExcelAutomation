@echo off
if exist Build echo "Folder already exists"
if not exist Build mkdir Build && echo "Folder built"
