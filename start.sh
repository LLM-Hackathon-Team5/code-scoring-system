#!/bin/bash
python /app/CodeAnalyzer/python_analyzer.py &
python /app/CodeAutoFixer/python_fixer.py &
python /app/Review_Commenter/python_comment_generator.py &
wait