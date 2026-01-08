@echo off
if not exist "%1\.build" mkdir "%1\.build"
rustc -g "%2" -o "%1\.build\%3.exe"