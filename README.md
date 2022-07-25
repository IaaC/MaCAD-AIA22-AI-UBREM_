# MaCAD-AIA22-AI-UBREM_


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#About-the-project">About The Project</a>
      <ul>
        <li><a href="#credits">Credits</a></li>
      </ul>
    </li>
    <li><a href="#Data-Preparation"> Data Generation</a></li>
    <ul>
        <li><a href="#Energy-Consumption">Energy-Consumption</a></li>
      </ul>
    </li>
  <ul>
        <li><a href="#Solar-Radiation">Solar-Radiation</a></li>
      </ul>
    </li>
    <li><a href="#DNN-ml">Machine Learning-DNN</a></li>
    <ul>
        <li><a href="#DNN-Energy-Consumption">DNN-Energy-Consumption</a></li>
      </ul>
    </li>
  <ul>
        <li><a href="#ML-Solar-Radiation">ML-Solar-Radiation</a></li>
      </ul>
    </li>
    <li><a href="#gh">Grasshopper Analytics and Generation</a></li>
    <li><a href="#web">Web development and Mapbox Integration</a></li>
    <li><a href="#bibliography">Bibliography and Other Resources</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- About the Project -->
## About-the-project

Urban Building Energy modeling (UBEM) demonstrated a reliable tool to visualize city fabric and its complex systems use patterns. This tool enables visualizing and prediction of energy and solar potential of buildings as an AI-based UBREM. U-value is an index that measure building envelop/ structure heat transmittance. The lower the u-value shows better insulation, thus decreases your building energy consumption. Use the sliders to alter u-values for walls, windows, roof and basement. A single good insulation layer adding to your wall can decrease building energy consumption (BEC) by almost 30%. Hence, building energy demand (BED) can be met using PV cells on roof top, the PV potential can even exceed BED and support neighboring units manifesting a Positive Energy District (PED) with renewable energy (RE).

![image](https://user-images.githubusercontent.com/108461498/180661208-f4f61a7c-6820-4581-91c2-83ab61948f3c.png)

AI-UBREM addresses Energy consumption(EC) mitigation to manifest the concept of postitive Energy District (PED) relying on renewable energy (RE) resources like thermal, Biogas, wind and PV cells. The project utilizes ANN to predict energy consumption of 5 building typologies in Vienna city, residential, detched, apartments, school and office. Shedding light to the fact that vienna city energy conumption of household contributes to almost one third of vienna's total EC.

![image](https://user-images.githubusercontent.com/108461498/180659915-480110e7-adf0-43a9-bdcd-b5ab9dc8df5f.png)



<!-- Credits -->
## Credits

AI-UBREM is a project of IAAC, Institute for Advanced Architecture of Catalonia developed in the Module of Artificial Intellignece in Architecture (AIA) for  MACAD in 2022/23 by Sammar Z. Allam, Naitik Sharma, and Alexander Lopez. Faculty: Angelos Chronis .

<!-- Data-Generation-->
## Data-Preparation

An intensive research process for more than a month to gather energy data about consumption, use, and u-values of buildings in Vienna city to rely on and build a  AI-UBREM dataset to put to test.  Multiple UN-funded projects and reliable governmental city websites, in addition to the AIT of Vienna city along with published data , reports, and simulation results are utilized to build both BEC and PV potential datasets.

Open street maps has been utilized to retrieve Vienna buildings data like geometry, building typology, height, level, long and lat and OSMID which builds our main geojson and geo-referenced files using colab and retrieved libraries like geopanda , networkx and numpy. 
Link:


________________________________________
Mapping APIs
https://www.openstreetmap.org/#map=16/41.3893/2.1725
https://developers.google.com/maps/documentation/maps-static/overview
https://developers.google.com/maps/documentation/streetview/overview
https://docs.mapbox.com/api/overview/


![image](https://user-images.githubusercontent.com/108461498/180660406-dcb0da21-3190-49bb-9c61-49e3fdae42c4.png)



<!-- Energy-Consumption -->
## Energy-Consumption
Building Energy consumption data has been gathered from multiple resources including UN-funded projects and published research conducted by researchers and scholars from the AIT Austrian Institute of Technology. 
 
![image](https://user-images.githubusercontent.com/108461498/180660414-5aa2c8c7-0618-4ea9-a4ae-51e82196ac19.png)

![image](https://user-images.githubusercontent.com/108461498/180660419-f21c2e50-5ad1-4da2-b836-1e5ebb470014.png)

Tabula Project 
![image](https://user-images.githubusercontent.com/108461498/180660421-57acc278-39de-4482-869c-f144564f3bd4.png)

 

Entranze Project:

 ![image](https://user-images.githubusercontent.com/108461498/180660429-4d173dd4-49ef-420e-9c1e-c3d5c22b0449.png)

![image](https://user-images.githubusercontent.com/108461498/180660435-2ec2f7e2-41a3-4633-826c-b3893005ca6f.png)

 ![image](https://user-images.githubusercontent.com/108461498/180660439-ad45c6cd-97fa-4cad-b684-62d8b7e0dd33.png)




 


Links: 
1.	https://www.wien.gv.at/umweltgut/public/grafik.aspx?ThemePage=9
2.	Tabula Project Vienna,  link: https://episcope.eu/fileadmin/tabula/public/docs/scientific/AT_TABULA_ScientificReport_AEA.pdf
3.	Entranze Project by EU and UN Link: https://www.entranze.eu/files/downloads/D2_3/Heating_and_cooling_energy_demand_and_loads_for_building_types_in_different_countries_of_the_EU.pdf



The idea is to retrieve data about buildings energy consumption , u-value of building envelop and link it to a renewable energy resource for future retrofitting and PED plan. 

![image](https://user-images.githubusercontent.com/108461498/180661094-86e841b7-c5ad-4cef-90d1-e0115442c91c.png)


<!-- Solar-Radiation -->
## Solar-Radiation
In order to manifest PED conceptualization, a renewable energy resource quantification is essential not only to meet but exceed the predicted BEC after retrofitting by decreasing the building’s envelope u-value.  Simulation tools have been utilized to simulate solar radiation, hence building a dataset for Vienna building solar radiation and PV potential. 


 
![image](https://user-images.githubusercontent.com/108461498/180660452-8a7e5aee-415e-4b0a-8648-2dbede9947d1.png)

![image](https://user-images.githubusercontent.com/108461498/180660471-a9273ca6-7a2b-412b-a499-5b1b778f9e27.png)




<!-- Machine-Learning (DNN) -->
## DNN-ml
An intesive research process for more than a month to gather energy data about consumption, use, and u-values of buildings in Vienna city to rely on and build AI-UBREM dataset to put to test. 

<!-- DNN-Energy-Consumption -->
## DNN-Energy-Consumption
 Deep neural network regression has been trained through 4 layers with 36 neurons, then 16 , 8, and finally 4 neurons which are the number of output predicted data.  Dataset has 11 features to train DNN model which are ‘area', 'Heating_energy_kWh_per_m2_a', 'Cooling_energy_kWh_per_m2_a', 'DHW_energy_kWh_per_m2_a', 'total_energy_kWh_per_m2_a', 'u_value_walls_W_per_m2K', 'u_value_roof_W_per_m2K', 'u_value_basement_W_per_m2K', 'u_value_glass_W_per_m2K', 'g_value_glass_W_per_m2K', 'bdgcode'.
 
 
 ![image](https://user-images.githubusercontent.com/108461498/180660493-5e81b7b3-becd-4d6c-b5c0-45d57e3f568b.png)

mse_test: 0.001160272629931569
 
<!-- ML-Solar-Radiation -->
## ML-Solar-Radiation

Multiple iteration and approaches are utilized to get the most reliable solar radiation prediction. Linear regression and neural network regressions are put to trial. At the end, DNN models of 5 dense layers is the one with best results for prediction. 

![image](https://user-images.githubusercontent.com/108461498/180662092-10fe4c61-a59a-4634-92f1-dd40d2d97504.png)

4 features are utilized to train a DNN of 5 dense layers , Building height, volume, roof area, and solar radiation. 

![image](https://user-images.githubusercontent.com/108461498/180662107-f552723a-5ac5-44e8-afaa-27f5b9d2bc8a.png)


![image](https://user-images.githubusercontent.com/108461498/180661782-40c3d61f-0459-4e01-bf8e-ffa033e89d5c.png)


![image](https://user-images.githubusercontent.com/108461498/180661725-b7888646-ee0f-487f-ac52-c3a0f9e93d20.png)

![image](https://user-images.githubusercontent.com/108461498/180661731-1a18d801-6747-4b28-8bc8-04aa790c8d3d.png)


<!-- Grasshopper-Scripts -->
## gh

Grasshopper tool is not only used in simulation but it is utilized to test energy and solar radiation prediction from the ANN models generated. It is used to validate the final models and prove their reliability. 


![image](https://user-images.githubusercontent.com/108461498/180660952-342003e2-19a8-485c-b6bd-f89ca1ceda19.png)

<!-- Web-Development -->
## web
Mapbox is the platform used to make AI-UBREM for Vienna available for users and accessible by real estate developers as well.  Files have been prepared for each layer. One main layer with whole Vienna buildings. Then, five layers for each building typology, residential, apartments, detached houses, schools, and office. Finally and the most significant layer for solar radiation prediction and calculating the PV potential for each buildings for roof. 


AI in Architecture (iaac.net)

Link: http://aia22.iaac.net:8080/

![image](https://user-images.githubusercontent.com/108461498/180661124-427a6474-8890-4bc6-8bd2-6b5348714213.png)


![image](https://user-images.githubusercontent.com/108461498/180661135-f4054db3-27fc-402b-8426-3e081bdb8e15.png)

Layer_1
Main layer for the city of Vienna to visulaize buildings, land-use, five- buildings typology energy consumption for heating, cooling , DHW, and total of these. 

Layer_2
The apartment typology layer where you alter the U-value of walls, windows, basement, and roof of a selected apartment building to predict the new BEC after the building retrofitting.
Layer_3
The detached housing typology layer where you alter the U-value of walls, windows, basement, and roof of a selected detached housing building to predict the new BEC after the building retrofitting.

Layer_4
The office typology layer where you alter the U-value of walls, windows, basement, and roof of a selected office building to predict the new BEC after the building retrofitting.

Layer_5
The residential typology layer where you alter the U-value of walls, windows, basement, and roof of a selected residential building to predict the new BEC after the building retrofitting.

Layer_6
The school typology layer where you alter the U-value of walls, windows, basement, and roof of a selected school building to predict the new BEC after the building retrofitting.


Layer_7
This solar radiation prediction of the selected buildings in vienna city . It refelcts the PV otential as renewable energy resource support to the building to meet its BEC. Hence, this contributes to meet PED conceptualization manifestation. 
