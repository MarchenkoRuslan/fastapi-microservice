@echo off

echo Checking with black...
black ./app --check
if %errorlevel% neq 0 (
    echo Black found formatting issues
    set /p answer="Do you want to format with black? (y/n) "
    if /i "%answer%"=="y" black ./app
)

echo Checking with isort...
isort ./app --check-only
if %errorlevel% neq 0 (
    echo Isort found import ordering issues
    set /p answer="Do you want to reorder imports? (y/n) "
    if /i "%answer%"=="y" isort ./app
)

echo Checking with autoflake...
autoflake --check --remove-all-unused-imports --remove-unused-variables --expand-star-imports -r ./app
if %errorlevel% neq 0 (
    echo Autoflake found unused imports/variables
    set /p answer="Do you want to remove unused imports/variables? (y/n) "
    if /i "%answer%"=="y" autoflake --in-place --remove-all-unused-imports --remove-unused-variables --expand-star-imports -r ./app
)

echo Checking with flake8...
flake8 ./app 