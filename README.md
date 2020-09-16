# QRS-extractor

## Project goals:
- [x] visualize MIT signal
- [x] custom QRS detector implementation
- [x] perform QRS detection
- [x] extract QRS to csv
- [x] predict whether QRS is or abnormal
- [x] write API that receives QRS and says whether it's normal

## Introduction
This project is learning project for QRS classification. 

I downloaded MIT BIH Arrhythmia Database, extracted QRSes,  calculated surface feature and based on boxplots I chose threshold for normal and abnormal QRS.

## Running server
To run server that predicts QRS class run:

`python app.py`

Example request:

`curl -H "Content-Type: application/json" -d "{\"samples\":\"[-0.315,-0.315,-0.295,-0.295,-0.3,-0.305,-0.31,-0.32,-0.305,-0.305,-0.3,-0.31,-0.32,-0.325,-0.315,-0.315,-0.315,-0.325,-0.34,-0.35,-0.33,-0.33,-0.33,-0.34,-0.335,-0.345,-0.345,-0.335,-0.33,-0.335,-0.36,-0.37,-0.365,-0.355,-0.38,-0.385,-0.415,-0.44,-0.45,-0.475,-0.505,-0.51,-0.55,-0.625,-0.795,-1.055,-1.35,-1.685,-1.99,-2.215,-2.39,-2.525,-2.62,-2.695,-2.715,-2.69,-2.625,-2.535,-2.42,-2.26,-2.05,-1.805,-1.58,-1.355,-1.15,-0.935,-0.745,-0.58,-0.435,-0.33,-0.27,-0.245,-0.23,-0.205,-0.155,-0.11,-0.065,-0.06,-0.045,-0.035,-0.005,0.02,0.04,0.05,0.065,0.085,0.12,0.14,0.145,0.145,0.13,0.13,0.145,0.165,0.175,0.19,0.2,0.215,0.23,0.25,0.265,0.29,0.29,0.275,0.26,0.265,0.255,0.255]\"}" http://127.0.0.1:5000/predict`

Expected output:

`"QRS label is V"`

