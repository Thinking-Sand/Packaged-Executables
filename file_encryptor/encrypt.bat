@echo off
echo File/Folder Encryption Tool
echo ------------------------
echo WARNING: This will encrypt your files in place. Make sure you remember the password!
echo If you lose the password, you won't be able to recover the files.
echo.
echo You can enter either:
echo  - A path to a single file (e.g., C:\Users\YourName\Desktop\secret.txt)
echo  - A path to a folder to encrypt all files inside it (e.g., C:\Users\YourName\Folder)
echo.
set /p FILE_PATH="Enter the path of the file or folder to encrypt: "
set /p PASSWORD="Enter the password: "

cd /d "%~dp0"
python file_encryptor.py encrypt "%FILE_PATH%" --password "%PASSWORD%"
if %ERRORLEVEL% EQU 0 (
    echo.
    echo Encryption completed! Your files have been encrypted in place.
    echo IMPORTANT: Keep your password safe - you'll need it to decrypt the files!
)
pause
