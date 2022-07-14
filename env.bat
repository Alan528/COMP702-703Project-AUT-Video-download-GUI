for /F %%i in ('DIR bin /S /B') do ( set file=%%i)

echo file=%file%

setx PATH "%file%"

