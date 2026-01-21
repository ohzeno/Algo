@echo off
chcp 65001 > nul
if not exist "%~1\.build" mkdir "%~1\.build"
rustc "%~2" --edition 2024 --crate-name solution -o "%~1\.build\%~n3.exe"
"%~1\.build\%~n3.exe"