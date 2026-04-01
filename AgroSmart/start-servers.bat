@echo off
cd /d "%~dp0"
echo Starting Flask App...
start "Flask API" cmd /k "python app\app.py"

echo Starting Streamlit App...
start "Streamlit UI" cmd /k "streamlit run app\ui.py"
