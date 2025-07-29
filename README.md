# Vegetation-Change-Detection-NDVI

A simple, visual, and beginner-friendly project to detect deforestation using NDVI (Normalized Difference Vegetation Index) and Landsat satellite data via Google Earth Engine. This notebook compares vegetation health in Rondônia, Brazil (Amazon Rainforest) between 2014 and 2022.

This project was originally written as a [Medium blog post](https://malinian.medium.com/detecting-deforestation-with-python-using-ndvi-a-satellite-powered-exploration-ba4c65164713) — feel free to read the full explanation there!

---

## Requirements

To run this notebook on Google Colab:
!pip install earthengine-api geemap --quiet

If running locally, install the packages via:
pip install earthengine-api geemap

##  How to Use
Sign up for Google Earth Engine
Link your Google Cloud project to your Earth Engine account
Run the deforestation_ndvi_analysis.ipynb notebook in Colab or Jupyter
Explore the interactive NDVI maps to see vegetation changes over time

## Files Included
deforestation_ndvi_analysis.ipynb – Main Python notebook
README.md – Project overview and setup guide

## What It Does
This notebook:
Pulls Landsat 8 satellite images from 2014 and 2022 using Earth Engine
Calculates NDVI for both years
Computes NDVI difference to identify vegetation loss
Applies a binary threshold to detect likely deforested zones
Visualizes it all on an interactive map with NDVI layers

## Inspiration
This project was built as part of an exploration into using satellite data for environmental analysis. NDVI makes it easy to track green cover over time — with just a few lines of Python.
