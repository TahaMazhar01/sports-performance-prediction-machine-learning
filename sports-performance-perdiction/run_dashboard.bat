@echo off
REM === Activate virtual environment and run Streamlit dashboard ===

REM Navigate to project directory
cd /d "D:\BSCS\4_Spring_2024\MaCHINE LEARNING\python  labs\venv\sports-performance-perdiction"

REM Activate the virtual environment
call ..\Scripts\activate.bat

REM Run the Streamlit dashboard
streamlit run dashboard.py

pause
