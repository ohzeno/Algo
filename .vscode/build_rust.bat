@echo off
setlocal
set "workspace=%~1"
set "filepath=%~2"
set "filename=%~3"

if not exist "%workspace%\.build" mkdir "%workspace%\.build"
rustc -g "%filepath%" --crate-name solution -o "%workspace%\.build\%filename%.exe"