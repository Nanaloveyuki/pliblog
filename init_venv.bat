echo Running init for Python Virtual Environment...
:: Removed unnecessary timeout
:: timeout /t 3
:: Check if either venv or .venv exists
if exist "venv" (
    set "VENV_DIR=venv"
) else if exist ".venv" (
    set "VENV_DIR=.venv"
)

:: If virtual environment exists, activate it
if defined VENV_DIR (
    echo Python virtual environment already exists in %VENV_DIR%.
    echo Activating virtual environment...
    call "%VENV_DIR%\Scripts\activate.bat"
    echo Virtual environment activated.
) else (
    :: Create virtual environment with venv
    echo Creating Python virtual environment...
    call python -m venv venv
    if %errorlevel% neq 0 (
        echo Error: Failed to create virtual environment.
        exit /b %errorlevel%
    )
    set "VENV_DIR=venv"
    echo Virtual environment created.
    echo Activating virtual environment...
    call "%VENV_DIR%\Scripts\activate.bat"
    echo Virtual environment activated.
)
