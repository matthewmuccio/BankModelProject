#!/usr/bin/env bash


clear
echo "Initializing database ..."
rm master.db
python3 schema.py
sleep 0.5
echo "Database and schema initialized ..."
sleep 0.5
echo "Running run.py ..."
sleep 0.5
clear
python3 run.py
