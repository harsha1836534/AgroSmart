@echo off
echo Using python interpreter...
python src\train_nlp_model.py
python src\train_crop_model.py
echo Training complete.
pause
