
# Vegetation-Change-Detection-NDVI

A simple, visual, and beginner-friendly project to detect deforestation using NDVI (Normalized Difference Vegetation Index) and Landsat satellite data via Google Earth Engine.  

This script compares vegetation health in Rondônia, Brazil (Amazon Rainforest) between 2014 and 2022.

This project was originally written as a [Medium blog post](https://malinian.medium.com/detecting-deforestation-with-python-using-ndvi-a-satellite-powered-exploration-ba4c65164713) — feel free to read the full explanation there!

## Requirements
To run this script:
````markdown
pip install earthengine-api geemap
````

You'll also need to sign up for Google Earth Engine and authenticate your environment by running:

```bash
earthengine authenticate
```

---

## How to Use

1. Clone the repository
2. Run the script `deforestation_ndvi_analysis.py`
3. Explore the interactive NDVI map displayed in your browser
4. If needed, initialize Earth Engine with your project:

```python
ee.Initialize(project='your-project-name')
```

---

## Files Included

* `deforestation_ndvi_analysis.py` – Main Python script
* `README.md` – Project overview and setup guide

---

## What It Does

This script:
* Fetches Landsat 8 satellite images from 2014 and 2022 using Earth Engine
* Calculates NDVI for each year
* Computes NDVI difference to identify vegetation loss
* Applies a binary threshold mask to detect potential deforested areas
* Visualizes it on an interactive geemap map

---

## Inspiration

This project was built as part of an exploration into using satellite data for environmental analysis.
NDVI makes it easy to track green cover over time — with just a few lines of Python.


