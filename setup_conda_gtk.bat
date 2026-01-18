@echo off
REM setup_conda_gtk.bat - Create conda env with GTK and reportlab (Windows)
where conda >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
  echo Conda not found in PATH. Install Miniconda or Anaconda and re-run this script.
  exit /b 1
)
echo Creating conda env 'gtk'...
conda create -n gtk -c conda-forge python=3.11 pygobject pycairo gtk3 reportlab -y
if %ERRORLEVEL% NEQ 0 exit /b %ERRORLEVEL%
echo Activating environment...
call conda activate gtk
if %ERRORLEVEL% NEQ 0 (
  echo Failed to activate conda environment. You may need to run "conda init" and reopen the shell.
  exit /b %ERRORLEVEL%
)
echo Verifying installation...
python -c "import gi; print('gi', gi.__version__); import reportlab; print('reportlab OK')"
echo Done.
pause
