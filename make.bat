@ECHO OFF
SET SPHINXBUILD=sphinx-build
SET SOURCEDIR=source
SET BUILDDIR=build
SET SPHINXOPTS=
SET SPHINXPROJ=sample_userguide
SET MAKE=make

if "%1" == "" goto help
if "%1" == "help" goto help
if "%1" == "clean" goto clean
if "%1" == "html" goto html

:help
ECHO.
ECHO Usage:
ECHO.
ECHO   make.bat clean    to remove all files
ECHO   make.bat html     to make HTML documents
ECHO.
goto end

:clean
rmdir /s /q %BUILDDIR%
goto end

:html
%SPHINXBUILD% -b html %SOURCEDIR% %BUILDDIR% %SPHINXOPTS%
goto end

:end


