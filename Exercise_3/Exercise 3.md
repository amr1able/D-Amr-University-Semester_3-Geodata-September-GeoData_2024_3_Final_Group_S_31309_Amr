# Exercise 3: OpenHygrisC Nitrate Data - QGIS Temporal Controller and PostgreSQL/PostGIS

## Overview

This task involved creating a spatio-temporal animation of nitrate concentration data using the **OpenHygrisC** groundwater quality dataset, stored in **PostgreSQL/PostGIS** and visualized in **QGIS**. The goal was to produce a video depicting the nitrate levels over time, leveraging the **QGIS Temporal Controller**.

## Process

### 1. **Data Preparation**
   - **Database Setup**: The **OpenHygrisC** data (station locations, measurement data, catalog of substances) was imported into **PostgreSQL/PostGIS**.
   - I faced an extreme amount of difficulty and challanges with this one:
     - I have faced numerous errors that could range from small ones like changing the encoding = "cp1252" to display the german characters right from the CSV files instead of the UTF-8 default.
    
     - I only kept the notebooks I used from directory. Please refer back to the notebook [OpenHyPE_GW_Stations_and_Data_V007_dev.ipynb](./OpenHyPE-main/python/OpenHyPE_GW_Stations_and_Data_V007_dev.ipynb)
       
![Screenshot](../Screenshots/Screenshot%202024-09-08%20211906.png)

     - The right data was not there on the website which led me to download the equivalent and work with it soon to find much worse situations later when I was working with the chemistry data. When I searched in the older chat of the previous semester I found that Seif has shared it in SQLite format which I then reworked everything with the new (old data) and then worked everything out and refixed the errors.
     
![Screenshot](../Screenshots/Screenshot%202024-09-08%20211114.png)

![Screenshot](../Screenshots/Screenshot%202024-09-20%20154049.png)


     - The worst personal error found was at the beginning of using ipython-sql it kept not wanting to work since the last year's lectures and I tried to fix every single library with pip and conda-forge to find the right combination and it took me days of continous frustrating work to get the right one. I have dedicated a directory with screenshots of that. [Warming_Stripes_images.ipynb](./Python/Warming_Stripes_images.ipynb)
    
[Screenshots/SQL-Parse errors](../Screenshots/SQL-Parse%20errors/)

![Screenshot](../Screenshots/SQL-Parse%20errors/Screenshot%202024-09-08%20212740.png)


   - **Views and Indexes**: The dataset used several pre-defined database views and indexes to enhance data retrieval performance, as indicated in the provided Jupyter Notebooks.
 
     - The was this error worthy of mentioning that the katalog stoff had that for some reason the index was not really having the calculation performed so I had to exclude the index:
![Screenshot](../Screenshots/Screenshot%202024-09-21%20000726.png)

![Screenshot](../Screenshots/Screenshot%202024-09-21%20000703.png)

But without changing the index and leaving it ugly it worked

![Screenshot](../Screenshots/Screenshot%202024-09-21%20000923.png)

![Screenshot](../Screenshots/Screenshot%202024-09-21%20000228.png)

Please refer back to [OpenHyPE_import_katalog_stoff.ipynb](./OpenHyPE-main/python/OpenHyPE_import_katalog_stoff.ipynb)     

### 2. **Temporal Visualization in QGIS**
   - **QGIS Connection**: Established a live connection between **QGIS** and the **PostgreSQL/PostGIS** geodatabase.
     
![Screenshot](../Screenshots/Screenshot%202024-09-21%20135422.png)
     
![Screenshot](../Screenshots/Screenshot%202024-09-21%20144340.png)
     
   - **Data Handling**: Loaded the nitrate concentration data for visualization. Applied database views.
   - **Temporal Controller**: Configured the **QGIS Temporal Controller** to animate the nitrate concentration changes over time, starting from the earliest records (early 1960s) to the most recent data points.

![Screenshot](../Screenshots/Screenshot%202024-09-21%20144400.png)
     

     

### 3. **Video Creation**
   - **Image Export**: Rather than using the temporal controller slider, I exported individual frames (images) representing each time step.
     
![Screenshot](../Screenshots/Screenshot%202024-09-21%20144416.png)
     
   - **Video Assembly**: Compiled the exported images into an **MPEG** video using a Python script.
     
![Screenshot](../Screenshots/Screenshot%202024-09-21%20150126.png)

    - I choose many frames of weekly (biweekly to be exact) steps to make a smoother change than changing them monthly
     
![Screenshot](../Screenshots/Screenshot%202024-09-21%20150126.png)
 
    - I suffered a lot with the enconding but luckily it worked and the videos even are playable over most social media platforms too.

![Screenshot](../Screenshots/Screenshot%202024-09-21%20151256.png)

![Screenshot](../Screenshots/Screenshot%202024-09-21%20152559.png)

    - I ended up going for the recommended MPEG. I used 26 FPS which is equal to 52/2 (biweekly frame) so every second equals 1 year

![Screenshot](../Screenshots/Screenshot%202024-09-21%20165826.png)

Please refer back to [Time_Series_Video_Creator_V01_dev.ipynb](./OpenHyPE-main/python/Time_Series_Video_Creator_V01_dev.ipynb) 

The final video:
[/OpenHyPE-main-Time.Series.Final/video/timeseries_Amrs_version.mp4](./OpenHyPE-main-Time.Series.Final/video/)

[Download the video "timeseries_Amrs_version.mp4"](./OpenHyPE-main-Time.Series.Final/video/timeseries_Amrs_version.mp4)


## Folder Structure
The following folder structure was used for the exercise:

   
   - **OpenHyPE-main-Time.Series.Final**:
       - **images**: Stores the exported images representing each time step and the video. I had to delete the images but left only the last few as per the request of not making the file big... but they can be produced again from the temporal control bar by pressing on the disc button then it saves it:
         
        ![Screenshot](../Screenshots/Screenshot%202024-09-21%20144400.png)

        ![Screenshot](../Screenshots/Screenshot%202024-09-21%20144416.png) 
         
       - **video**: Has the desired output video; each second represents a year.
         
         
   - **OpenHyPE-main**: 
     - **Data**: Contains the original OpenHygrisC datasets, including station locations and nitrate measurements except the chemistry one because it was a large file.
     - **python**: Includes the jupyter notebooks and the Python scripts used to process the images and create the final video.
     - **QGIS**: Has the files with the layers needed. username is : "env_master" and password is : "M123xyz"

