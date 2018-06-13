#!/usr/bin/env bash


echo "Initializing database ..."
rm master.db
python3 schema.py
echo "Database and schema initialized ..."
echo "Running run.py ..."
clear
python3 run.py
