@echo off
cd example
for %%f in (*.py) do (
    echo Running %%f
    python %%f
    echo Finished running %%f
    echo -----------------------------------
)
pause