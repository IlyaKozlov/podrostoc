sleep 5
python3.8 -m unittest -v -f /podrostoc/tests/test_style.py /podrostoc/tests/api/test* /podrostoc/tests/api/test*
test_exit_code=$?
if [ $test_exit_code -eq 0 ]
  then python -c "import cowsay; cowsay.cow('All right')"
  else python -c "import cowsay; cowsay.dragon('Tests failed')"
fi
exit "$test_exit_code"
