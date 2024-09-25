# Exercise 2: Digitization: Burial Mounds in Uedemer Hochwald

**Location and Historical Context:**
Southwest of the village of Marienbaum (part of the Xanten municipality) lies the Uedemer Hochwald forest. This area is known for containing numerous burial mounds dating back to the Hallstatt period. The burial mounds are represented as grey dots on the map, as shown in the accompanying image.

## Task 2.1: Georeferencing the Map in QGIS

In this task, I started with the provided QGIS project file `gdms0000_Burial_Mounds_Uedem_V001.qgz`. Using the QGIS Georeferencer tool, I georeferenced the map section that displays the burial mounds. 

- **Layer Used**: DTK10, the NRW topographic map at 1:10,000 scale, imported from the NRW WMS server.
- **Landmarks/Ground Control Points (GCPs)**: I identified and used features such as crossing forest trails, crossroads, and road junctions with known coordinates from the DTK10 layer.
 ![Screenshot](../Screenshots/Screenshot%202024-09-02%20005626.png)

- **Coordinate System**: EPSG:25832.
- **Result**: The georeferenced map was successfully added to the QGIS project, aligned with the DTK10 layer for further analysis.
 ![Screenshot](../Screenshots/Screenshot%202024-09-02%20010103.png)

[Burial_Mounds_Final.tif](./data/Burial_Mounds_Final.tif)

[Burial_Mounds_Final.tif.aux.xml](./data/Burial_Mounds_Final.tif.aux.xml)

## Task 2.2: Creating a Hillshade Model and Overlaying the Georeferenced Map

I generated a **hillshade model** from the **Digital Terrain Model (DTM)** layer to enhance terrain visualization. 
![Screenshot](../Screenshots/Screenshot%202024-09-02%20012206.png)
The georeferenced map was overlaid partially transparent on top of the hillshade model for comparison. 

![Screenshot](../Screenshots/Screenshot%202024-09-02%20012652.png)


- **Georeferenced Map Accuracy**: The burial mounds do align often but **not very well** at all with the topographic variations indicated by the hillshade model.
![Screenshot](../Screenshots/Screenshot%202024-09-02%20012708.png)
  

## Task 2.3: Measuring Mound Heights Using DTM

Using the DTM, I measured the **typical mound heights** relative to their immediate surroundings (not the absolute height above sea level). 

I clipped (cut) the area of study only around the very few selected points from that raster layer.

Due to area of the study being so small and the Max and Minimum being so little apart; a range of around 5 meters. I decided to use the mean height of the area for comparison to avoid any exaggeration by my human error where I select the points for comparison.
![Screenshot](../Screenshots/Screenshot%202024-09-03%20022643.png)

![Screenshot](../Screenshots/Screenshot%202024-09-03%20022657.png)


- **Results**: The burial mounds showed typical relative elevations mean equal to **58.7 cm**, highlighting that they are in slightly elevated positions compared to their immediate environment. These mounds are relatively subtle in the landscape but consistently higher than the adjacent ground level.
  
![Screenshot](../Screenshots/Screenshot%202024-09-03%20022546.png)

I had to learn a lot for this step about clipping and referencing and most especially about Raster Layer Statisics. I repeated these steps several times to make it better.

## Task 2.4: Investigating Rectangular Structures in the Hillshade Model

Upon studying the hillshade model in the **East-North-East direction** of the burial mounds area, I identified **faint rectangular patterns** that are not pathways. 
- **Observation**: These structures are weakly visible but suggest possible anthropogenic and human origins.
- **Hypothesis**: Given their shape, they may represent ancient settlement boundaries, possibly related to agricultural or habitation zones.

![Screenshot](../Screenshots/Screenshot%202024-09-03%20041727.png)
![Screenshot](../Screenshots/Screenshot%202024-09-03%20041840.png)
![Screenshot](../Screenshots/Screenshot%202024-09-03%20041917.png)
- **Digitization**: I selected few of these structures and digitized it. The digitized structure was saved as a **geopackage**.
  
[Rectangular_Historical_Shapes.gpkg](./data/DTM/Rectangular_Historical_Shapes.gpkg)

---
## Folder Structure
The following folder structure was used for the exercise:

- **data**: Contains the georeferenced data, DTM, and hillshade model.
- **Images**: Contains the georeferenced map and points.

