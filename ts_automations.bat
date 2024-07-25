::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAnk
::fBw5plQjdG8=
::YAwzuBVtJxjWCl3EqQJgSA==
::ZR4luwNxJguZRRnk
::Yhs/ulQjdF+5
::cxAkpRVqdFKZSDk=
::cBs/ulQjdF+5
::ZR41oxFsdFKZSDk=
::eBoioBt6dFKZSDk=
::cRo6pxp7LAbNWATEpCI=
::egkzugNsPRvcWATEpCI=
::dAsiuh18IRvcCxnZtBJQ
::cRYluBh/LU+EWAnk
::YxY4rhs+aU+JeA==
::cxY6rQJ7JhzQF1fEqQJQ
::ZQ05rAF9IBncCkqN+0xwdVs0
::ZQ05rAF9IAHYFVzEqQJQ
::eg0/rx1wNQPfEVWB+kM9LVsJDGQ=
::fBEirQZwNQPfEVWB+kM9LVsJDGQ=
::cRolqwZ3JBvQF1fEqQJQ
::dhA7uBVwLU+EWDk=
::YQ03rBFzNR3SWATElA==
::dhAmsQZ3MwfNWATElA==
::ZQ0/vhVqMQ3MEVWAtB9wSA==
::Zg8zqx1/OA3MEVWAtB9wSA==
::dhA7pRFwIByZRRnk
::Zh4grVQjdCyDJGyX8VAjFDxbQACHMiuYD6EgzO3o5P6IsnENRu01fYzPyYuHLt8D+ErjZ5M+xUZ9l8cICRVobB2hawwgulJFuWiBMsmjsQb1dlqM9kQjEnF7lWrVnxcoZd9u18AM3jC38EzrlqoenHf5E6UPAi7nyL5ldc0P/h+5bUfciY9BWcnvfqnmDjfcKmYRnz7Gk4YK
::YB416Ek+ZW8=
::
::
::978f952a14a936cc963da21a135fa983
@echo off
cd /d %~dp0
call venv\Scripts\activate.bat
call python -m streamlit run ts/app.py
pause