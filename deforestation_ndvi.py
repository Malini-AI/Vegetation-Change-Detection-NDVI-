# Make sure to install the required packages before running:
# pip install earthengine-api geemap

import ee
import geemap

def calculate_ndvi(image):
    ndvi = image.normalizedDifference(['SR_B5', 'SR_B4']).rename('NDVI')
    return image.addBands(ndvi)

def get_landsat_ndvi(year, region):
    collection = (
        ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
        .filterBounds(region)
        .filterDate(f'{year}-06-01', f'{year}-10-31')
        .filterMetadata('CLOUD_COVER', 'less_than', 40)
        .map(calculate_ndvi)
    )
    return collection.median().clip(region)

def main():
    # Authenticate and initialize Earth Engine
    ee.Authenticate()
    ee.Initialize(project='Your Project Name')

    # Define region (Amazon, Rondônia)
    amazon_region = ee.Geometry.BBox(-63.0, -9.0, -60.0, -6.0)

    # Get NDVI images for 2014 and 2022
    ndvi_2014 = get_landsat_ndvi(2014, amazon_region).select('NDVI')
    ndvi_2022 = get_landsat_ndvi(2022, amazon_region).select('NDVI')

    # Calculate NDVI difference and mask deforestation
    ndvi_diff = ndvi_2022.subtract(ndvi_2014).rename('NDVI_Diff')
    loss_mask = ndvi_diff.lt(-0.2).rename('Deforestation_Mask')

    # Initialize map
    Map = geemap.Map(center=[-7.5, -61.5], zoom=7)

    # Visualization parameters
    ndvi_params = {'min': 0, 'max': 1, 'palette': ['white', 'green']}
    diff_params = {'min': -0.5, 'max': 0.5, 'palette': ['red', 'white', 'green']}
    mask_params = {'min': 0, 'max': 1, 'palette': ['black', 'yellow']}

    # Add map layers
    Map.addLayer(ndvi_2014, ndvi_params, 'NDVI 2014')
    Map.addLayer(ndvi_2022, ndvi_params, 'NDVI 2022')
    Map.addLayer(ndvi_diff, diff_params, 'NDVI Difference')
    Map.addLayer(loss_mask, mask_params, 'Deforestation Mask')
    Map.addLayerControl()

    # Display map
    Map.show()

if __name__ == "__main__":
    main()
