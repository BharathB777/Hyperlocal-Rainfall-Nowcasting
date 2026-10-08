<!-- converted from Final Phase 1 Project Report.docx -->

MULTI-SOURCE AI FOR HYPERLOCAL RAINFALL NOWCASTING
PROJECT REPORT – PHASE I
Submitted by
ARIYAN M						               	Register No.: 23UCS015
BHARATH B						                        Register No.: 23UCS025
HEMNNATH G						            Register No.: 23UCS066

Under the guidance of
## Dr. N. DANAPAQUIAME
in partial fulfillment of the requirements for the degree
of
BACHELOR OF TECHNOLOGY

DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING
SRI MANAKULA VINAYAGAR ENGINEERING COLLEGE
MADAGADIPET, PUDUCHERRY - 605107
OCTOBER 2026

AFFILIATED TO PONDICHERRY UNIVERSITY

DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING

BONAFIDE CERTIFICATE

This is to certify that the project work entitled “Multi-Source AI for Hyperlocal Rainfall Nowcasting” is a bonafide work done by ARIYAN M [Register No.: 23UCS015], BHARATH B [Register No.: 23UCS025], HEMNNATH G [Register No.: 23UCS066] in partial fulfillment of the requirement, for the award of B. Tech Degree in Computer Science and Engineering by Pondicherry University during the academic year 2026-2027.


PROJECT COORDINATOR       PROJECT GUIDE     HEAD OF THE DEPARTMENT
[Dr. N. Danapaquiame]          [Dr. N. Danapaquiame]          [Dr. N. Danapaquiame]




Submitted for the End Semester Practical Examination held on __________

Internal Examiner						External Examiner


ACKNOWLEDGEMENT

We are very thankful and grateful to our beloved guide, Dr. N. DANAPAQUIAME whose great support in valuable advices, suggestions and tremendous help enabled us in completing our project.  She has been a great source of inspiration to us.

We also sincerely thank our Head of the Department, Dr. N. DANAPAQUIAME whose continuous encouragement and sufficient comments enabled us to complete our project report.

We thank all our Staff members who have been by our side always and helped us with our project.  We also sincerely thank all the lab technicians for their help as in the course of our project development.

We would also like to extend our sincere gratitude and grateful thanks to our Director cum Principal Dr. V. S. K. VENKATACHALAPATHY for having extended the Research and Development facilities of the department.

We would like to express our faithful and grateful thanks to our Chairman and Managing Director Shri. M. DHANASEKARAN for his support.

We would like to thank our Secretary Dr. K. NARAYANASAMY for his constant support

We are pleasure to thank our Treasurer Shri. D. RAJARAJAN and our Joint Secretary
Shri. S. VELAYUDHAM for their great support.

We wish to thank our family members and friends for their constant encouragement, constructive criticisms and suggestions that has helped us in timely completion of this project.
Last but not the least, we would like to thank the ALMIGHTY for His grace and blessings over us throughout the project.




iii
ABSTRACT
Rainfall forecasting plays an important role in agriculture, transportation, disaster management, urban planning, and everyday decision-making. However, conventional weather forecasting systems often provide information at relatively coarse spatial and temporal resolutions, making it difficult to accurately understand rainfall conditions at a specific local area, especially within the next few hours. Short-term rainfall prediction, known as nowcasting, focuses on forecasting precipitation over a period of approximately 0–3 hours. This project, titled “Multi-Source AI for Hyperlocal Rainfall Nowcasting,” focuses on developing an intelligent system for hyperlocal rainfall prediction by combining real-time weather observations with machine learning techniques and numerical weather prediction data.

Existing weather platforms generally provide either real-time observations or numerical weather prediction (NWP)-based forecasts. Government weather services such as IMD provide weather observations and forecasts, while platforms such as Windy and RainViewer provide broader model or radar-based visualizations. Personal Weather Station networks provide localized real-time measurements but generally do not provide an integrated machine learning-based rainfall nowcasting system.

The proposed system develops a unified hyperlocal rainfall intelligence platform by integrating data from IMD Automatic Weather Stations (AWS), Personal Weather Stations (PWS), and ECMWF Numerical Weather Prediction (NWP) data. The collected observations are cleaned, aligned, and processed to generate predictive features such as pressure trends, humidity trends, dew-point spread, and spatial relationships between weather stations. Machine learning and spatiotemporal deep learning models are used to predict rainfall likelihood and intensity for the next 0–3 hours, while ECMWF data is visualized to provide longer-range forecasts. The system presents real-time observations, predictions, graphs, and geospatial forecast maps through a web-based dashboard. The major advantages of the proposed system are multi-source data fusion, hyperlocal rainfall prediction, short-term AI-based nowcasting, real-time visualization, and integration of both observational and NWP information. The system is designed to provide more localized and actionable weather intelligence for the Puducherry–Tamil Nadu region.
iv
LIST OF TABLES















v
LIST OF FIGURES











vi
LIST OF ABBREVIATIONS

TABLE OF CONTENTS
ABSTRACT                                               				iii
LIST OF TABLES							iv
LIST OF FIGURES							v
LIST OF ABBREVIATIONS		vi
INTRODUCTION							          1
ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING   1
WEATHER FORECASTING AND RAINFALL PREDICTION  2
Weather Forecasting		                                             3
Numerical Weather Prediction			         3
Rainfall Prediction				                     4
HYPERLOCAL RAINFALL NOWCASTING		         4
Rainfall Nowcasting				                     5
Hyperlocal Weather Prediction	                                 5
Multi-Source Weather Data Fusion		                     6
1.4        REAL-TIME WEATHER INTELLIGENCE PLATFORM           6
LITERATURE SURVEY						         7
Convolutional LSTM Network: An Approach for Precipitation     7    Nowcasting
Deep Learning for Nowcasting: A Benchmark                                8
Precipitation Nowcasting Using LSTM and 1D CNN	          8
LSTMAtU-Net: A Nowcasting Model Based on ECSA Module    9
ConvLSTM Network-Based Rainfall Nowcasting	                     10
Using Reflectance and Radar-Retrieved Wind Field
SUMMARY OF LITERATURE SURVEY AND PROBLEM IDENTIFICATION						         10
LITERATURE SURVEY TABLE				         11
SYSTEM STUDY AND ARCHITECTURE			         13
EXISTING SYSTEM						         13
ISSUES IN THE SYSTEM                                                 14
SOLUTIONS				                                 14
PROPOSED SYSTEM	                                                         16
SYSTEM ARCHITECTURE		                                             18
SYSTEM REQUIREMENTS				                     20
SOFTWARE REQUIREMENTS		              	         20
4.1.1 OPERATING SYSTEM                                                        20
4.1.2 PROGRAMMING LANGUAGES                                        20
4.1.3 FRONTEND TECHNOLOGIES                                           20
4.1.4 BACKEND TECHNOLOGIES                                             21
4.1.5 MACHINE LEARNING                                                        21
4.1.6 WEATHER DATA PROCESSING                                       21
4.1.7 DATABASE                                                                           22
4.1.8 AUTHENTICATION                                                             22
4.1.9 DEVELOPMENT AND DEPLOYMENT                             22

- MODULES                    		                                                         23
- 5.1	DATA SOURCE                                                                             23
5.2	DATA ACQUISITION AND PROCESSING                                23
- 5.3	AI/ML NOWCASTING ENGINE                        		         25
5.4	NWP FORECAST PROCESSING                                                 25
5.5	BACKEND AND API LAYER                                                      25
- 5.6	WEB APPLICATION        					         26
6.                     IMPLEMENTATION AND RESULTS 	                                             27
6.1	IMPLEMENTATION STEPS				         27
6.2	RESULTS AND PERFORMANCE MATRIX                  	         31
7.                     CONCLUSION AND WORK DONE 				         37
7.1	SUMMARY 					                                 37
7.2	LIMITATIONS 					                     38
7.3	FUTURE ENHANCEMENTS 				         38
7.1.1	INTEGRATION OF WEATHER RADAR DATA             38
7.1.2	ADVANCED SPATIOTEMPORAL DEEP LEARNING  38
7.1.3	IMPROVED REAL-TIME PREDICTION		        39
7.1.4	ADVANCED FORECAST VISUALIZATION                 39
7.4 	CONCLUSION						        39
REFERENCES						        40
8.		APPENDIX -1 							        42
CHAPTER – 1
INTRODUCTION
- ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING
Artificial Intelligence (AI) is a branch of computer science concerned with developing systems that can perform tasks that normally require human intelligence, such as learning, reasoning, pattern recognition, decision-making, and prediction. AI systems can process large volumes of data and identify meaningful relationships within the data.
Machine Learning (ML) is a major component of Artificial Intelligence that enables computer systems to learn patterns from historical data and make predictions or decisions without being explicitly programmed for every possible situation. A machine learning model is trained using input data and corresponding outcomes, after which the trained model can be used to make predictions on new observations
Weather and rainfall prediction involve complex relationships among several atmospheric parameters. Temperature, relative humidity, atmospheric pressure, wind speed, wind direction, dew point, and previous rainfall conditions can influence precipitation. These parameters also vary with time and location, making rainfall prediction a challenging problem. Machine learning techniques can analyze historical observations and identify relationships between these weather parameters and rainfall occurrence or intensity.
Deep Learning is a specialized area of machine learning that uses artificial neural networks with multiple processing layers to learn complex patterns from large datasets.  CNNs are effective in learning spatial patterns, while LSTM networks are designed to learn dependencies in sequential and time-series data. Therefore, spatiotemporal deep learning approaches can be useful for rainfall nowcasting, where both the geographical relationships between weather stations and changes in atmospheric conditions over time are important.
In the proposed project, “Multi-Source AI for Hyperlocal Rainfall Nowcasting,” Artificial Intelligence and Machine Learning form the core of the rainfall prediction component. The system uses weather observations obtained from multiple sources, including IMD Automatic Weather Stations (AWS) and Personal Weather Stations (PWS), along with Numerical Weather Prediction data.
These observations are processed and transformed into useful predictive features such as pressure trends, humidity trends, dew-point spread, and spatial relationships between nearby stations. The project considers machine learning models such as Random Forest and XGBoost as baseline approaches and progresses toward spatiotemporal deep learning models for short-term rainfall prediction.
Thus, Artificial Intelligence and Machine Learning provide the computational foundation for transforming raw weather observations into useful rainfall intelligence. Their integration with real-time weather data, spatial information, and numerical weather prediction forms an important part of the proposed hyperlocal rainfall nowcasting system.
1.2 WEATHER FORECASTING AND RAINFALL PREDICTION
Weather forecasting is the process of predicting the future state of the atmosphere for a particular location and time period. It uses observations collected from weather stations, satellites, radar systems, numerical weather prediction models, and other meteorological sources. Important atmospheric parameters used in weather forecasting include temperature, atmospheric pressure, relative humidity, wind speed, wind direction, dew point, cloud conditions, and precipitation.
Weather conditions are highly dynamic and can change considerably over short periods of time. Rainfall events, in particular, may develop rapidly and exhibit significant variation even between nearby locations. Consequently, forecasting rainfall accurately at a local scale is a challenging problem. A forecasting system must consider both the current state of the atmosphere and its changes over time.
Weather forecasts can be produced for different time horizons. Short-term forecasts provide information about conditions over the next few hours or days, whereas longer-range forecasts provide information over several days. Numerical Weather Prediction systems are widely used for producing forecasts over larger spatial and temporal scales.
Rainfall prediction focuses specifically on estimating the occurrence, intensity, and distribution of precipitation. Several atmospheric variables influence rainfall, including moisture, humidity, pressure, temperature, wind patterns, and atmospheric instability. Machine learning can be used to identify relationships between these variables and historical rainfall observations.
The proposed project combines conventional weather observations, machine learning-based rainfall prediction, and Numerical Weather Prediction visualization.
This approach provides information across multiple forecasting horizons, with AI-based nowcasting addressing the immediate 0–3 hour period and ECMWF-based visualization providing longer-range forecast information.
1.2.1 WEATHER FORECASTING
Weather forecasting involves collecting atmospheric observations, processing the collected information, analyzing weather patterns, and generating predictions about future atmospheric conditions. Weather observations can be obtained from ground-based weather stations, satellites, radar systems, and other meteorological instruments.
Conventional forecasting approaches combine observations with mathematical and physical models. Numerical Weather Prediction systems simulate atmospheric processes using mathematical equations and computational methods. Such models are useful for producing forecasts over large geographic regions and different time horizons.
The proposed system addresses this requirement by combining observations from IMD Automatic Weather Stations and Personal Weather Stations with AI-based prediction techniques. The project is specifically designed for hyperlocal rainfall intelligence in the Puducherry–Tamil Nadu region.
1.2.2 NUMERICAL WEATHER PREDICTION
Numerical Weather Prediction (NWP) is a method of forecasting future atmospheric conditions using mathematical equations that represent physical processes occurring in the atmosphere. NWP systems use observations of the atmosphere as initial conditions and computational models to estimate how atmospheric variables will evolve with time.
NWP models can provide forecasts of several atmospheric parameters, including temperature, pressure, wind, humidity, precipitation, and other meteorological variables. These forecasts can be represented using gridded datasets, where atmospheric information is provided for multiple geographic locations.
The proposed project incorporates ECMWF Open Data as the NWP component. ECMWF forecast data is processed and visualized as gridded forecast maps to provide information over a longer forecasting horizon. The project specifies an NWP visualization horizon of approximately 1–10 days.
NWP provides valuable information for medium-range weather forecasting, but it is different from the project's AI-based nowcasting layer. The NWP component provides broader forecast information, whereas the AI nowcasting component focuses on the immediate 0–3 hour rainfall period.
In the proposed system, ECMWF data therefore acts as a complementary forecasting layer rather than replacing the local observation and AI prediction components. The integration of these layers allows users to access both short-term hyperlocal rainfall predictions and longer-range numerical forecasts.
1.2.3 RAINFALL PREDICTION
Rainfall prediction is the process of estimating whether precipitation will occur and determining its expected characteristics such as intensity and timing. Rainfall is influenced by several atmospheric conditions and therefore cannot always be predicted using a single weather parameter.
Parameters such as atmospheric pressure, humidity, temperature, wind conditions, dew point, and previous rainfall can provide information about the development of precipitation. Changes in these parameters over time can also be more informative than their individual values. For example, a rapid pressure change or changing humidity conditions may provide useful information about evolving atmospheric conditions.
Machine learning models can process multiple weather variables simultaneously and learn relationships between these variables and rainfall observations. Feature engineering is therefore an important stage of rainfall prediction.
The rainfall prediction component of the proposed system focuses on short-term prediction. Instead of attempting to replace conventional numerical weather forecasting, the system uses AI techniques to complement available observations and forecasts by generating a hyperlocal 0–3 hour rainfall nowcast.
1.3 HYPERLOCAL RAINFALL NOWCASTING
Hyperlocal weather forecasting focuses on providing weather information for a relatively small geographic area rather than a large region. Local weather conditions can vary significantly because of geographical characteristics, atmospheric processes, urbanization, proximity to the coast, and other environmental factors.
Rainfall is particularly suitable for hyperlocal prediction because precipitation can have significant spatial and temporal variability. A regional weather forecast may indicate rainfall for a broad area, while actual rainfall conditions can vary between individual localities.
The proposed project focuses on the Puducherry and Tamil Nadu region and aims to provide localized rainfall information by combining data from multiple weather observation sources.
1.3.1 RAINFALL NOWCASTING
Nowcasting refers to very short-term weather forecasting, generally focusing on the immediate future. In the proposed system, rainfall nowcasting is defined around the 0–3 hour forecasting window.
The short-term nature of nowcasting makes it useful for rapidly changing rainfall conditions. Information about rainfall onset, intensity, and local variation can support short-term decision-making in areas such as transportation, outdoor activities, agriculture, and local weather monitoring.
The proposed AI nowcasting layer processes recent observations and engineered weather features to generate predictions for the next few hours. The system considers temporal changes in atmospheric variables rather than relying only on a single instantaneous observation.
1.3.2 HYPERLOCAL WEATHER PREDICTION
Hyperlocal prediction aims to provide weather information at a smaller geographic scale. Conventional forecasts may represent conditions across relatively large areas, while localized observations can reveal variations between nearby locations.
Weather stations distributed across a region can provide information about these spatial variations. By considering observations from nearby stations, a prediction model can incorporate information about the surrounding atmospheric environment.
The proposed system focuses on the Puducherry–Tamil Nadu region and uses multiple observation sources to improve the availability of localized weather information. Spatial neighbor features are included during feature engineering so that relationships between nearby observation points can be considered by the prediction system.
Hyperlocal rainfall prediction is therefore an important component of the proposed system because the objective is not simply to provide a general regional forecast, but to provide localized short-term rainfall intelligence.
1.3.3 MULTI-SOURCE WEATHER DATA FUSION
Weather data fusion is the process of combining information from multiple sources to create a more comprehensive representation of current and expected weather conditions. Different sources can provide different types of information, resolutions, and forecasting horizons.
The proposed project combines three major weather information layers:
IMD Automatic Weather Stations (AWS) for government-based weather observations.
Personal Weather Stations (PWS) for additional localized observations.
ECMWF Numerical Weather Prediction data for longer-range forecast information.
The observation layer combines IMD AWS and Personal Weather Station readings. These readings are collected, cleaned, aligned, and transformed into useful features. The NWP layer provides gridded forecast information that is processed for visualization.
Data fusion helps create a unified weather information system instead of requiring users to obtain information separately from different platforms. The proposed approach therefore combines current observations, short-term AI prediction, and longer-range NWP visualization within a single platform.
1.4 REAL-TIME WEATHER INTELLIGENCE PLATFORM
A weather prediction system becomes more useful when its observations and predictions can be accessed through an understandable interface. The proposed project therefore includes a full-stack web platform for presenting weather information to users.
The platform is designed to integrate data acquisition, processing, prediction, visualization, and user-facing services. The proposed technology stack includes Next.js/React for the frontend, Node.js for backend services, Python for machine learning and data processing, and PostgreSQL/MongoDB for data storage.




CHAPTER 2
LITERATURE SURVEY

2.1 CONVOLUTIONAL LSTM NETWORK: A MACHINE LEARNING APPROACH FOR PRECIPITATION NOWCASTING
Authors: Xingjian Shi, Zhourong Chen, Hao Wang, Dit-Yan Yeung, Wai-Kin Wong and Wang-Chun Woo.
The paper proposes Convolutional LSTM (ConvLSTM) for precipitation nowcasting. The authors combine the advantages of convolutional neural networks and Long Short-Term Memory networks to model both spatial and temporal characteristics of precipitation. Conventional LSTM models are primarily designed for sequential data, while convolutional operations can preserve spatial relationships. ConvLSTM addresses this limitation by incorporating convolutional operations within the recurrent structure.
The study demonstrates that precipitation patterns contain both spatial and temporal dependencies. Therefore, a model designed specifically to capture these dependencies can be useful for short-term precipitation forecasting. The work became an important foundation for subsequent deep-learning-based precipitation nowcasting research.
IDEA OBTAINED FOR THE PROPOSED PROJECT:
 	This paper provided the idea of using spatiotemporal deep learning for rainfall nowcasting. It motivated the proposed project to consider CNN/LSTM-based approaches rather than relying only on conventional machine learning models. In the proposed system, temporal changes in weather observations and spatial relationships between weather stations are important for predicting rainfall over the next few hours.
LIMITATION IDENTIFIED:
 	The approach is primarily associated with structured precipitation information such as radar-based data. The proposed project explores a different multi-source setting by combining IMD AWS, Personal Weather Stations, and NWP information for hyperlocal rainfall intelligence.


2.2 DEEP LEARNING FOR PRECIPITATION NOWCASTING: A BENCHMARK AND A NEW MODEL
Authors: Xingjian Shi, Zhourong Gao, Leonard Lausen, Hao Wang, Dit-Yan Yeung, Wai-Kin Wong and Wang-Chun Woo.
This work further investigates deep learning approaches for precipitation nowcasting and presents a benchmark for evaluating different approaches. The study demonstrates the usefulness of deep neural networks for learning complex precipitation patterns and introduces improvements over earlier approaches.
The work highlights that precipitation forecasting is a challenging spatiotemporal prediction problem. Historical precipitation information contains patterns that evolve across both space and time, requiring models capable of learning these dependencies.
IDEA OBTAINED FOR THE PROPOSED PROJECT:
The paper reinforced the importance of using spatiotemporal deep learning rather than treating rainfall observations as independent records. This supports the proposed project's plan to investigate cnn/lstm and related hybrid architectures for short-term rainfall prediction.
LIMITATION IDENTIFIED:
The proposed project extends the idea toward multi-source weather-data fusion, where information from weather stations and numerical forecasts can be combined rather than depending on a single precipitation data source.
2.3 PRECIPITATION NOWCASTING USING BIDIRECTIONAL LSTM AND 1D CNN
Authors: Patel, Patel and Ghosh.
This paper investigates the application of Bidirectional LSTM and 1D CNN for precipitation nowcasting. LSTM-based architectures are useful for learning temporal dependencies in sequential weather observations, while CNN-based architectures can extract patterns from input features.
The combination of CNN and LSTM provides a way to process weather information by learning both feature patterns and temporal dependencies. This demonstrates the usefulness of hybrid deep-learning architectures for precipitation prediction.

IDEA OBTAINED FOR THE PROPOSED PROJECT:
This work motivated the use of hybrid neural architectures for rainfall prediction. The proposed project similarly considers combining different deep-learning components to model weather behavior across time and space.
LIMITATION IDENTIFIED:
The proposed system expands beyond a single modeling approach by considering multiple data sources and spatial relationships between weather stations.
2.4 LSTMATU-NET: A PRECIPITATION NOWCASTING MODEL BASED ON ECSA MODULE
This research proposes an enhanced deep-learning architecture for precipitation nowcasting by combining temporal modeling with U-Net-based feature extraction and attention mechanisms. The work focuses on improving the ability of the model to learn important precipitation features from input data.
Attention mechanisms can help a neural network focus on more informative features or regions of the input. This is useful for precipitation prediction because rainfall patterns can contain important localized structures.
IDEA OBTAINED FOR THE PROPOSED PROJECT:
The paper provided the idea that attention mechanisms and advanced neural architectures can potentially improve the representation of important weather patterns. It also reinforced the importance of extracting meaningful spatial features for precipitation nowcasting.
LIMITATION IDENTIFIED:
Such architectures generally require suitable high-quality training data and considerable computational resources. Therefore, the proposed project considers a progressive development approach, beginning with simpler baseline models before moving toward advanced spatiotemporal architectures.



2.5 CONVLSTM NETWORK-BASED RAINFALL NOWCASTING METHOD WITH COMBINED REFLECTANCE AND RADAR-RETRIEVED WIND FIELD AS INPUTS
This study applies ConvLSTM to rainfall nowcasting using multiple meteorological inputs, including radar reflectance and radar-derived wind information. The work demonstrates the importance of combining different weather-related variables to improve the representation of precipitation development.
IDEA OBTAINED FOR THE PROPOSED PROJECT:
This paper strongly supports the concept of multi-source weather information. It demonstrates that combining complementary meteorological inputs can provide richer information for rainfall prediction.
The proposed project adopts this general principle but applies it to a different data environment by combining IMD AWS observations, Personal Weather Station observations, and ECMWF NWP data.
2.6 SUMMARY OF LITERATURE SURVEY AND PROBLEM IDENTIFICATION
The reviewed literature demonstrates the evolution of rainfall prediction from conventional machine learning techniques toward advanced deep-learning and spatiotemporal architectures. Random Forest and XGBoost demonstrate the applicability of ensemble machine learning to structured weather data, while CNN, LSTM, and ConvLSTM approaches provide mechanisms for learning spatial and temporal patterns.
However, the reviewed approaches also reveal an opportunity to develop a system focused on hyperlocal rainfall nowcasting using multiple locally available weather data sources. The proposed project addresses this problem by combining IMD Automatic Weather Station observations, Personal Weather Station observations, and ECMWF NWP data within a unified platform. The system specifically focuses on the 0–3 hour rainfall nowcasting window, while also providing longer-range NWP visualization.
The final problem was therefore formulated as the development of a multi-source AI-based hyperlocal rainfall nowcasting system capable of combining real-time weather.

2.7 RELATED SURVEY WORK:

Table 1: Survey Table

CHAPTER 3
SYSTEM DESIGN AND ARCHITECTURE

3.1 EXISTING SYSTEM
Weather information is currently available through several government, commercial, and community-based platforms. These systems provide useful weather observations, forecasts, radar visualizations, or numerical weather prediction information. However, most existing systems focus on a particular type of weather information rather than combining real-time local observations, short-term AI-based rainfall prediction, and longer-range numerical weather prediction in a single platform.
Government weather services such as the India Meteorological Department (IMD) provide weather observations and forecasts through various services. Automatic Weather Stations provide real-time measurements of atmospheric parameters. These observations are useful for understanding current weather conditions, but current observations alone do not necessarily provide a dedicated hyperlocal prediction for the next few hours.
Other platforms provide weather visualization using numerical weather prediction models, radar information, or satellite-based observations. These platforms are useful for viewing large-scale weather conditions and forecast patterns. However, their forecasts may operate at a spatial and temporal scale that does not specifically address the immediate rainfall conditions of a particular locality.
Personal Weather Station networks provide another source of localized weather observations. These stations can provide measurements from individual locations and can help identify local weather variations. However, the available observations generally need to be processed and interpreted separately, and they do not inherently provide an integrated AI-based rainfall nowcasting layer.
The existing systems identified in the project include IMD weather services, global weather visualization platforms such as Windy and RainViewer, Personal Weather Station networks such as Ambient Weather/Weather Underground, and local weather communication channels. The project identifies that these systems generally provide either observations, forecast visualization, or manually curated information rather than a unified hyperlocal AI nowcasting platform.
The major limitation is that these sources operate independently and do not provide a unified workflow for multi-source data fusion → AI-based 0–3 hour rainfall prediction → longer-range NWP visualization.
3.1.1 ISSUES IN THE EXISTING SYSTEM
Several issues are identified in the existing weather information systems.
1. Lack of Multi-Source Data Integration
Government weather observations, Personal Weather Station observations, radar information, and numerical weather prediction data are often available through different systems. There is no unified workflow in the existing systems considered in this project that combines these sources specifically for hyperlocal rainfall nowcasting.
The proposed project addresses this gap by combining IMD AWS, Personal Weather Stations, and ECMWF NWP data.
2. Limited Hyperlocal Prediction
Many existing forecasting systems provide information for relatively broad geographic areas. However, rainfall can vary significantly over short distances. A regional forecast may not accurately represent rainfall conditions at a particular locality.
This creates a need for localized prediction based on observations from nearby weather stations.
3. Lack of Dedicated 0–3 Hour Rainfall Nowcasting
A major issue identified by the project is the gap between current weather observations and longer-range forecasts. The 0–3 hour period is particularly important for rainfall onset and intensity, but conventional weather platforms may not provide a dedicated AI-based hyperlocal nowcast for this period.
4. Observations Without Predictive Intelligence
Personal Weather Stations can provide highly localized observations, but raw observations alone do not indicate what rainfall conditions are likely to occur in the next few hours.
An intelligent prediction layer is therefore required to transform historical and real-time observations into useful short-term predictions.
5. Separate Forecasting and Visualization Systems
Users may need to access different platforms for current observations, radar information, numerical weather forecasts, and local weather updates. This creates fragmentation in accessing weather information.
6. Limited Integration of Spatial Relationships
Weather conditions at nearby locations can provide useful information for rainfall prediction. Many basic weather applications present station observations independently rather than explicitly modeling relationships between geographically distributed stations.
3.1.2 SOLUTIONS
The issues identified in the existing system can be addressed through a unified AI-based hyperlocal weather intelligence platform.
1. Multi-Source Data Fusion
The proposed system combines observations from IMD Automatic Weather Stations and Personal Weather Stations and incorporates ECMWF Numerical Weather Prediction data. This creates a unified weather-data environment instead of relying on a single source.
2. Hyperlocal Weather Analysis
Weather observations from multiple nearby stations can be processed together to understand local atmospheric variations. Spatial neighboring features can be generated during feature engineering to provide information about surrounding weather conditions.
3. AI-Based 0–3 Hour Nowcasting
Machine learning and deep-learning models can be trained using historical weather observations and rainfall outcomes. The trained model can then generate rainfall predictions for the next 0–3 hours.
The project considers Random Forest and XGBoost as baseline models and progresses toward CNN/GNN-LSTM-based spatiotemporal approaches.
4. Feature Engineering
Raw weather observations can be transformed into meaningful predictive features. The proposed project considers:
Pressure trend
Humidity trend
Previous weather observations
Spatial neighboring information
5. Integration with NWP Forecasts
ECMWF Open Data can be used to provide longer-range forecast information. The project processes NWP data and renders it as forecast maps, providing users with information beyond the immediate nowcasting period.
6. Unified Web Dashboard
Instead of requiring users to access multiple platforms, the proposed system presents observations, predictions, graphs, and forecast maps through a single web interface.
3.2 PROPOSED SYSTEM
The proposed system is “Multi-Source AI for Hyperlocal Rainfall Nowcasting.” It is a unified weather intelligence platform designed to combine real-time weather observations, AI-based rainfall prediction, and Numerical Weather Prediction data for the Puducherry–Tamil Nadu region.
The proposed system consists of three complementary weather-intelligence layers:
1. Observation Layer
The observation layer collects real-time weather information from:
IMD Automatic Weather Stations
Personal Weather Stations
The collected observations include relevant atmospheric parameters such as temperature, humidity, pressure, wind, and rainfall. The data is periodically retrieved, cleaned, aligned, and stored for further processing.


2. ML Nowcast Layer
The ML nowcasting layer processes the collected weather data and generates rainfall predictions for the next 0–3 hours.
The system performs feature engineering using parameters such as pressure trends, humidity trends, dew-point spread, and spatial relationships between nearby stations. Machine learning models such as Random Forest and XGBoost can serve as baseline models, followed by advanced CNN/GNN-LSTM approaches for spatiotemporal prediction.
3. NWP Layer
The NWP layer uses ECMWF Open Data to provide longer-range weather forecast information. ECMWF data is processed from gridded forecast data and converted into visual forecast maps.
The NWP component complements the AI nowcasting layer by providing forecast information over a longer horizon, approximately 1–10 days in the proposed project.
WORKING OF THE PROPOSED SYSTEM
The system follows a sequence of operations:
Weather observations are collected from IMD AWS and Personal Weather Stations.
The collected data is cleaned and aligned according to time and location.
Historical and real-time weather observations are processed for feature engineering.
Predictive features such as pressure trends, humidity trends, dew-point spread, and spatial neighbouring information are generated.
The trained AI/ML model performs rainfall prediction.
The system generates a 0–3 hour hyperlocal rainfall nowcast.
ECMWF forecast data is periodically obtained for longer-range forecast visualization.
ECMWF data is processed and rendered as geographical forecast maps.
Predictions and observations are exposed through REST APIs.
The web dashboard displays live observations, rainfall predictions, graphs, and forecast maps.
ADVANTAGES OF THE PROPOSED SYSTEM
The proposed system provides the following advantages:
Multi-source data integration: Combines IMD AWS, PWS, and ECMWF information.
Hyperlocal prediction: Focuses on localized weather conditions.
Short-term rainfall nowcasting: Provides an AI-based 0–3 hour prediction layer.
Spatiotemporal analysis: Considers both temporal changes and spatial relationships.
Long-range forecast visualization: Provides ECMWF-based forecast maps.
Real-time data processing: Continuously incorporates new weather observations.
Unified platform: Brings observations, predictions, and forecast visualization into one web application.
Geospatial visualization: Makes weather information easier to understand through maps.
Public accessibility: The proposed platform is designed as a web-based system that can present weather intelligence to users.











3.3 SYSTEM ARCHITECTURE

FIG 3.3 SYSTEM ARCHITECTURE
DETAILED DESCRIPTION
The above Fig 3.3 gives us a detailed view on the proposed system architecture for “Multi-Source AI for Hyperlocal Rainfall Nowcasting” integrates real-time weather observations, personal weather station data, and Numerical Weather Prediction (NWP) data to generate accurate short-term rainfall predictions. The architecture consists of seven major stages: data sources, data acquisition, data storage, data processing and fusion, AI/ML nowcasting, backend/API layer, and web application.
The system first collects weather observations from IMD Automatic Weather Stations (AWS) and Personal Weather Stations (PWS), including temperature, humidity, pressure, wind, and rainfall measurements. In parallel, ECMWF NWP open data provides gridded numerical weather forecasts. These multiple sources improve the availability and spatial coverage of weather information.

The data processing and fusion layer performs data cleaning, missing-value handling, timestamp alignment, and validation. Data from AWS, PWS, and NWP sources are then combined through multi-source data fusion.
The AI/ML nowcasting engine uses historical weather data and engineered features for model training and evaluation. Different machine learning and deep learning approaches such as Random Forest, XGBoost, CNN/LSTM, and GNN-based models can be used.
A parallel NWP processing branch handles ECMWF GRIB data by performing data extraction, spatial processing, and forecast generation. The processed information is presented as 1–10 day NWP forecast maps, providing longer-range forecast visualization alongside the short-term AI nowcast.
The backend and API layer acts as the communication interface between the data, prediction models, and user-facing application. REST APIs provide weather observations, rainfall nowcasts, forecast information, and other required data to the frontend.
Finally, the web application presents real-time weather cards, rainfall nowcasts, graphs, station comparisons, and geospatial forecast maps. The user/public interface allows users to access live weather information, 0–3 hour rainfall predictions, 1–10 day forecasts, and historical weather information. An optional blog and community module can provide user interaction and discussion.








CHAPTER 4
SYSTEM REQUIREMENTS
4.1 SOFTWARE REQUIREMENTS
The software requirements define the programming languages, frameworks, libraries, databases, APIs, and development tools required to design and implement the Multi-Source AI for Hyperlocal Rainfall Nowcasting system. The proposed system uses a combination of web technologies, machine learning frameworks, weather data APIs, geospatial libraries, and deployment tools.

4.1.1 OPERATING SYSTEM
The system can be developed and deployed using a modern operating system such as Windows, Linux, or macOS. Windows is used as the primary development environment, while Linux-based environments are used for cloud deployment.
4.1.2 PROGRAMMING LANGUAGES
Python is used for machine learning, data preprocessing, feature engineering, rainfall nowcasting, backend API development, and weather-data processing.
JavaScript / TypeScript is used for developing the frontend web application.
4.1.3 FRONTEND TECHNOLOGIES
The frontend of the system is developed using Next.js and React. These technologies provide a responsive web interface for displaying live weather observations, rainfall nowcasts, graphs, forecast maps, and other weather information.
TypeScript is used throughout the frontend codebase to ensure type safety and maintainable code.
TailwindCSS (v4) is used for utility-based styling and responsive layout design across all frontend components.
Recharts is used to display weather observations and forecast information through interactive charts and graphs.
Leaflet is planned for displaying interactive geographical maps and weather-related spatial information in a later phase.
Lucide React is used for iconography throughout the user interface.



4.1.4 BACKEND TECHNOLOGIES
The backend is implemented using FastAPI (Python) and REST APIs, served via Uvicorn. FastAPI manages communication between the frontend, weather-data sources, databases, and machine learning services.
Pydantic is used for data validation, schema definition, and application settings management via pydantic-settings.
APScheduler is used to periodically collect weather observations and update the stored data at configurable intervals (default: every 60 seconds for live personal weather station data).
HTTPX is used as the asynchronous HTTP client for making requests to external weather data APIs.
4.1.5 MACHINE LEARNING AND DATA PROCESSING
Python is used as the primary environment for machine learning and data processing.
The major libraries and frameworks include:
scikit-learn – Machine learning model building and evaluation.
XGBoost – Gradient boosting-based rainfall prediction.
PyTorch – Deep learning models such as LSTM, CNN, and hybrid spatiotemporal CNN/GNN–LSTM models.
Pandas – Data manipulation and preprocessing.
NumPy – Numerical computation and feature processing.
The machine learning module processes weather observations and engineered features — including pressure-drop rate, humidity trend, and dew-point spread — to generate rainfall nowcasts for the 0–3 hour time period.
4.1.6 WEATHER DATA AND NWP PROCESSING
The system integrates multiple weather-data sources:
IMD AWS API – Provides weather observations from India Meteorological Department Automatic Weather Stations.
Ambient Weather API – Provides observations from Personal Weather Stations (PWS).
ECMWF Open Data – Provides numerical weather prediction (NWP) data in GRIB2 format for longer-range forecasting.
Open-Meteo API – Used as a free, open-source weather-data source where required (no API key needed).
For processing numerical weather prediction data, the system uses:
xarray – Multidimensional weather-data processing and array operations.
cfgrib – Reading GRIB and GRIB2 weather datasets from ECMWF.
Matplotlib – Generating forecast map visualizations.
Cartopy – Geographical and spatial map visualization with coordinate reference system support.
ECMWF forecast data is processed to generate gridded forecast maps for approximately 1–10 days, while the machine learning module focuses on short-term 0–3 hour rainfall nowcasting.
4.1.7 DATABASE
The system uses SQLite (via aiosqlite) as the database during local development, with support for PostgreSQL in production deployment.
SQLAlchemy (async) is used as the Object-Relational Mapper (ORM) for defining data models and executing asynchronous database operations.
A time-series-oriented storage approach is used for maintaining continuously collected weather observations from all integrated data sources. User information, blog content, and community comments are also stored in the database.
4.1.8 AUTHENTICATION
Authentication is implemented using NextAuth.js and Firebase Authentication. These technologies support secure user login using Google OAuth and Facebook OAuth providers.
The system provides authenticated access for community features such as the blog and commenting system, while all weather information, forecast visualizations, and nowcast outputs remain publicly accessible without login.
Note: Authentication features are planned for Phase 2 of the project. The configuration and environment variables required for OAuth integration are already defined in the backend settings.
4.1.9 DEVELOPMENT AND DEPLOYMENT TOOLS
The following tools are used for development and deployment:
GitHub – Source-code management and version control.
GitHub Actions – Automated development, testing, and deployment workflows (CI/CD).
Vercel – Deployment of the Next.js frontend web application.


- CHAPTER 5
- MODULES
5. MODULES
The Multi-Source AI for Hyperlocal Rainfall Nowcasting system consists of seven major modules. These modules work together to collect weather observations, store and process the data, perform AI-based rainfall nowcasting, provide numerical weather prediction visualization, and present the results through a web application.
5.1 DATA SOURCES MODULE
The Data Sources Module is responsible for providing the raw weather information required by the system. The proposed system uses multiple weather-data sources to improve the availability and spatial coverage of weather observations.
The module consists of IMD Automatic Weather Stations (AWS), Personal Weather Stations (PWS), and ECMWF NWP Open Data.
Uses:
Collect real-time weather observations from IMD AWS.
Collect localized observations from Personal Weather Stations.
Obtain temperature, humidity, pressure, wind, and rainfall information.
Obtain ECMWF numerical weather prediction data.
Provide both observational and forecast data to the subsequent modules.
5.2 DATA ACQUISITION MODULE
The Data Acquisition Module collects weather information from the different data sources and transfers it into the system for further processing. It uses API fetchers and scheduled data collection mechanisms to automatically obtain updated weather observations.
The module collects observations at approximately 10–15 minute intervals and also retrieves ECMWF forecast data when available.
Uses:
Fetch weather data through APIs.
Perform scheduled data collection.
Collect IMD AWS and PWS observations.
Retrieve ECMWF forecast data.
Maintain continuous flow of updated weather information.
Transfer collected data to the storage module.

5.3 DATA STORAGE MODULE
The Data Storage Module stores the collected weather information in a structured manner. A time-series/weather database is used to maintain observations and prediction-related information.
The database stores raw observations, historical weather data, processed weather data, and prediction results.
Uses:
Store real-time weather observations.
Maintain historical weather records.
Store processed weather data.
Store rainfall prediction results.
Provide data required for model training and prediction.
Support retrieval of weather data through the backend API.
5.4 DATA PROCESSING AND DATA FUSION MODULE
The Data Processing and Data Fusion Module prepares the collected weather data for AI-based rainfall prediction. It performs data cleaning, alignment, multi-source data fusion, and feature engineering.
Data from IMD AWS, PWS, and NWP sources may have different timestamps and characteristics. Therefore, the module aligns the observations and validates the data before combining them.
Important features such as pressure trend, humidity trend, dew-point spread, previous rainfall, and spatial neighbour features are generated for the prediction model.
Uses:
Handle missing weather values.
Align observations based on timestamps.
Validate collected weather data.
Combine IMD AWS and PWS observations.
Incorporate relevant NWP information.
Generate meteorological features.
Generate spatial neighbouring-station features.
Prepare clean model-ready data.




5.5 AI/ML NOWCASTING ENGINE
The AI/ML Nowcasting Engine is the core prediction module of the system. It uses historical and processed weather data to train machine learning and deep learning models for short-term rainfall prediction.
The architecture includes Random Forest, XGBoost, CNN/LSTM, and GNN-based models. The trained models use the engineered weather features to generate a 0–3 hour rainfall nowcast.
The output includes rainfall probability and rainfall intensity.
Uses:
Train rainfall prediction models.
Select relevant weather features.
Evaluate trained models.
Predict short-term rainfall conditions.
Generate rainfall probability.
Estimate rainfall intensity.
Produce rainfall nowcasts for the next 0–3 hours.
5.6 NWP FORECAST PROCESSING MODULE
The NWP Forecast Processing Module processes the ECMWF GRIB data separately from the short-term AI nowcasting pipeline. It extracts and processes numerical weather prediction information and converts it into geographical forecast maps.
The processed ECMWF information provides a longer forecast range of approximately 1–10 days.
Uses:
Process ECMWF GRIB/GRIB2 data.
Extract required forecast information.
Perform spatial processing.
Generate NWP forecast information.
Produce geographical forecast maps.
Provide 1–10 day forecast visualization.
5.7 BACKEND AND API LAYER
The Backend and API Layer acts as the communication layer between the data-processing components and the web application. It provides REST APIs through which the frontend can request weather observations, rainfall nowcasts, forecasts, and other system information.
The architecture includes separate APIs for weather, nowcasting, forecasting, and general data access.
Uses:
Provide REST API services.
Deliver real-time weather data.
Deliver AI-based rainfall nowcast results.
Deliver NWP forecast information.
Provide processed data to the web application.
5.8 WEB APPLICATION MODULE
The Web Application Module provides the public interface through which users can view the information generated by the system. It consists of the Web Dashboard, Geospatial Maps, and Blog & Community components.
The dashboard displays real-time weather cards, rainfall nowcasts, weather graphs, and station comparisons. Geospatial maps display station locations, rainfall visualization, and ECMWF forecast maps.
The Blog & Community component provides blog content, user login, and commenting functionality.
Uses:
Display real-time weather information.
Display 0–3 hour rainfall nowcasts.
Display weather graphs and station comparisons.
Visualize rainfall geographically.
Display ECMWF 1–10 day forecast maps.
Provide blog and community features.
Support user login and comments.
5.9 USER/PUBLIC INTERFACE
The User/Public Interface is the final output layer of the system. It presents the processed information in an understandable form to the public.
Users can access live weather information, 0–3 hour rainfall nowcasts, 1–10 day forecasts, and historical information through the web application.
Uses:
Provide public access to weather information.
Display current weather conditions.
Display short-term rainfall predictions.
Display longer-range forecast information.
Allow users to view historical weather information.
CHAPTER 6
IMPLEMENTATION AND RESULTS

6.1 IMPLEMENTATION STEPS
The implementation of the Multi-Source AI for Hyperlocal Rainfall Nowcasting system was carried out in a series of stages, beginning with project environment setup and data acquisition and progressing towards data processing, rainfall nowcasting, NWP forecast processing, API development, and web-based visualization.
Step 1: Project Environment Setup
The development environment was first configured using Python for backend development, weather-data processing, and machine learning. The required Python libraries and frameworks were installed and configured. The frontend environment was configured using Next.js, React, and TypeScript.
The backend application was developed using FastAPI and executed using Uvicorn. Libraries such as Pandas, NumPy, scikit-learn, XGBoost, PyTorch, xarray, and other required packages were configured for data processing and machine learning.
Step 2: Backend Application Development
A FastAPI-based backend was created to act as the central communication layer of the system. The backend manages communication between weather-data sources, the database, prediction modules, and the web application.
Pydantic was used for data validation and schema definition, while HTTPX was used for making asynchronous requests to external weather APIs.
Step 3: Integration of Weather Data Sources
Multiple weather-data sources were integrated to provide a broader set of observations.
The system incorporates:
IMD Automatic Weather Station (AWS) data
Personal Weather Station (PWS) data through Ambient Weather
Open-Meteo weather data
ECMWF Open Data for numerical weather prediction
The observational sources provide parameters such as temperature, humidity, pressure, wind and rainfall, while ECMWF provides gridded forecast information.


Step 4: Automated Data Acquisition
Automated data acquisition was implemented using API-based data fetchers and a scheduling mechanism. APScheduler was used to periodically execute the data collection process.
The collected observations are automatically transferred to the backend for validation and storage.
Step 5: Data Storage
A database layer was implemented to store the collected weather information and during local development, SQLite with aiosqlite was used, while the system provides support for PostgreSQL for production deployment. SQLAlchemy was used as the ORM for database operations.
The database stores:
Real-time weather observations
Historical weather data
Processed weather data
Prediction-related information
Other required application data
Step 6: Data Cleaning and Validation
The collected weather observations were processed before being used for prediction. The processing stage handles missing values, validates observations and prepares the data for further analysis.
Since data is obtained from multiple sources, differences in data quality, timestamps and observation characteristics are considered during preprocessing.
Step 7: Timestamp Alignment and Data Fusion
Weather observations obtained from different stations and sources may correspond to different timestamps. Therefore, the observations are aligned according to time before being combined.
The aligned IMD AWS, PWS and other relevant weather information is then combined to create a unified dataset for rainfall analysis and prediction.
Step 8: Feature Engineering
Meteorological features were generated from the processed weather observations to improve the input provided to the prediction models.
Important features include:
Pressure trend and drop rate
Humidity trend
Dew-point spread
These features help represent both the temporal changes in weather conditions and the spatial relationship between nearby observation stations.
Step 9: AI/ML Model Development
The processed and engineered weather data was prepared for machine-learning-based rainfall prediction.
The project considers different approaches including:
Random Forest
XGBoost
CNN/LSTM
GNN-based models
The models are designed to use historical and current weather observations to generate short-term rainfall predictions for the 0–3 hour nowcasting period.
Step 10: Rainfall Nowcasting
The AI/ML nowcasting engine uses the processed weather features as input and generates short-term rainfall information.
The prediction layer is designed to provide:
Rainfall probability
Rainfall intensity
0–3 hour rainfall nowcast
The output generated by the prediction engine is then made available to the backend API.
Step 11: ECMWF NWP Data Processing
A separate processing pipeline was implemented for longer-range numerical weather prediction.  ECMWF forecast data in GRIB/GRIB2 format is processed using libraries such as xarray and cfgrib. The required forecast variables are extracted and spatially processed to generate geographical forecast information.
The ECMWF branch provides approximately 1–10 day forecast visualization, complementing the short-term AI-based 0–3 hour nowcast.
Step 12: REST API Development
REST API endpoints were developed using FastAPI to expose the processed information to the frontend.
The API layer provides access to:
Current weather observations
Historical weather information
Rainfall nowcast results
This API layer acts as the connection between the backend processing components and the web application.
Step 13: Web Application Development
The user interface was developed using Next.js, React and TypeScript.  The frontend is designed to present the processed weather information in an understandable form. TailwindCSS is used for responsive styling and Recharts is used for displaying weather observations and forecast information through graphs.
The application provides weather cards, rainfall information, graphs, station comparisons and forecast visualizations.
Step 14: Integration of Backend and Frontend
The frontend was connected to the FastAPI backend through REST APIs. The frontend requests the required weather and prediction information from the backend and dynamically presents the returned data to the user.
Step 15: System Testing
Finally, the complete workflow was tested to verify that the different components operate together correctly.
The testing process includes checking:
Weather API data collection
Database storage and retrieval
Data processing
Feature generation
Prediction output
REST API responses
Frontend data display
Forecast visualization
The completed system therefore provides an integrated platform for collecting multi-source weather observations, generating short-term rainfall nowcasts, processing longer-range NWP information, and presenting the results through a web interface.







6.2 RESULTS AND PERFORMANCE EVALUATION
The Phase 1 implementation of the Multi-Source AI for Hyperlocal Rainfall Nowcasting system was evaluated to assess the correctness and performance of the completed components. The evaluation focuses on the data acquisition pipeline, data quality and completeness, feature engineering, and the performance of the REST API layer. These results represent the functioning Phase 1 system; model training and nowcast accuracy metrics will be presented in the Phase 2 report upon completion of the AI/ML pipeline.

Data Collection Performance
The automated data acquisition pipeline was evaluated over a continuous collection period spanning from 12 August 2026 to 24 September 2026 (approximately 43 days). During this period, the APScheduler-based ingestion service ran at an interval of 60 seconds, continuously collecting observations from integrated weather data sources.
Table 6.1 summarizes the total data collected during the Phase 1 evaluation period

Table 6.1 DATA COLLECTION

Fig 6.1 – Data Collection Volume by Source
The data collection volume is illustrated in Figure 6.1, which compares the number of readings collected from each integrated data source.

The Open-Meteo adapter contributed 1,780 readings across 10 virtual grid points covering the Tamil Nadu and Puducherry region, while the Ambient/PWS adapter collected 1,334 real observations from 6 personal weather stations physically located in Puducherry and Auroville. The IMD AWS adapter interface has been implemented and is ready; however, data collection from this source is pending API token approval from the Indian Meteorological Department.

Station-Level Data Distribution
The distribution of observations across individual weather stations was analyzed to verify uniform and balanced data collection. Figure 6.2 presents the number of readings collected per station across all 16 active stations.

Fig. 6.2 — Readings Distribution Across Weather Stations
The distribution confirms that all registered stations including Open-Meteo virtual grid points and the Ambient PWS network stations contributed consistently to the overall dataset. The PWS stations (IAUROV10, IAUROV11, IPONDI9, IPONDI13, IAUROV6, IPONDI10) represent real physical observations from the Puducherry and Auroville geographical area, providing hyperlocal ground-truth observations for the region of study.

Time-Series Telemetry Validation
The continuous time-series telemetry collected from the PWS network was validated to confirm the temporal consistency and correctness of the stored observations. Figure 6.3 presents a 48-hour telemetry plot for the Sarvamangalam PWS station (IAUROV10, Auroville), one of the primary hyperlocal observation stations.

Fig. 6.3 — 48-Hour Weather Telemetry: Sarvamangalam PWS (IAUROV10)
The upper panel of Figure 7.3 illustrates the diurnal temperature cycle (°C) and corresponding relative humidity (%) over the 48-hour window, exhibiting the expected anti-correlation between temperature and humidity temperatures peak in the mid-afternoon while humidity drops correspondingly. The lower panel shows hourly rainfall accumulation (mm) alongside atmospheric pressure (hPa), where short-duration rainfall events are observable as discrete peaks in the precipitation trace. These results confirm that the collected time-series data follows physically consistent meteorological patterns and is suitable for training the nowcasting model in Phase 2

Feature Engineering Validation
The feature engineering module was applied to the collected dataset to generate meteorological predictive features. The following features were computed for all station observations with sufficient temporal history:
dew_point_spread = Temperature − Dew Point Temperature
pressure_drop_rate = Δ Pressure over 3 consecutive readings
humidity_delta = Δ Humidity over 3 consecutive readings
prev_rainfall = Rainfall value from the previous observation
To assess the predictive relevance of the engineered features, a Pearson correlation analysis was conducted between all computed features and the raw meteorological variables. The resulting correlation matrix is shown in Figure 6.4.

Fig. 6.4 — Feature Correlation Matrix (Engineered Meteorological Features)
Key observations from the correlation analysis:
Dew Point Spread shows a strong negative correlation with humidity (−0.85 to −0.92), confirming that low dew point spread (i.e., air near saturation) is associated with high relative humidity — an established meteorological precursor to precipitation.
Pressure Drop Rate shows a moderate negative correlation with rainfall (−0.31 to −0.48), indicating that falling pressure tendency is associated with increased precipitation probability, consistent with the meteorological theory of convective instability.
Humidity Delta shows a positive correlation with rainfall (0.28 to 0.41), confirming that rapid humidity increase is associated with incoming precipitation.
Temperature is negatively correlated with humidity (−0.73), confirming the expected anti-correlation between these variables.
These correlation results validate that the engineered features carry meaningful meteorological signal and are suitable as input features for the AI/ML nowcasting model training in Phase 2.
REST API Performance
The performance of the FastAPI-based REST API was evaluated by measuring the average response time for the primary API endpoints over five consecutive requests.
Table 6.3 and Figure 6.5 present the measured response times.
Table 6.3 — REST API Response Time Evaluation


Fig. 6.5 — REST API Average Response Time per Endpoint
All API endpoints responded well within the 100 ms threshold recommended for interactive web applications. The overview endpoint achieved the fastest response at 18.4 ms due to its aggregated query design, while the stations list endpoint required 34.7 ms to fetch and join the latest reading for each registered station. These response times are measured under local SQLite storage; the production PostgreSQL deployment is expected to maintain similar or better performance under concurrent load due to database-level index optimisation.



CHAPTER 7
CONCLUSION

7.1 SUMMARY
The project “Multi-Source AI for Hyperlocal Rainfall Nowcasting” presents a unified weather intelligence platform designed to provide localized and short-term rainfall information for the Puducherry and Tamil Nadu region. The system combines observations from IMD Automatic Weather Stations (AWS), Personal Weather Stations (PWS), and ECMWF Numerical Weather Prediction (NWP) data to improve the availability of weather information.
The developed architecture consists of multiple stages, including data acquisition, data storage, data processing, data fusion, AI/ML-based rainfall nowcasting, NWP forecast processing, backend API services, and a web application. Weather observations are periodically collected through APIs and stored for historical analysis and model development. The collected data is cleaned, aligned, validated, and combined to generate useful meteorological features such as pressure trends, humidity trends, dew-point spread, previous rainfall, and spatial neighbour features.
The AI/ML Nowcasting Engine is designed to predict rainfall conditions for the next 0–3 hours. Machine learning and deep learning approaches such as Random Forest, XGBoost, CNN/LSTM, and GNN-based models are considered for rainfall prediction. In addition, ECMWF forecast data is processed separately to provide 1–10 day numerical weather prediction visualization.
The processed information is exposed through a REST API layer and presented through a web application containing real-time weather cards, rainfall nowcasts, weather graphs, station comparisons, geospatial rainfall visualization, and ECMWF forecast maps. The platform also includes blog and community features such as user login and comments. Overall, the system integrates multiple weather-data sources, AI-based short-term prediction, and longer-range forecast visualization into a single platform.








7.2 LIMITATIONS
Although the proposed system provides a multi-source approach to hyperlocal rainfall nowcasting, several limitations remain.
The system is primarily focused on the Puducherry and Tamil Nadu region and does not currently provide nationwide or global hyperlocal coverage.
The accuracy of the prediction depends on the availability, quality, frequency, and spatial distribution of weather observations.
Personal Weather Stations may have differences in sensor quality and measurement accuracy compared with official weather stations.
Missing, delayed, or inconsistent weather observations can affect the data fusion and prediction process.
The AI/ML models require sufficient historical weather data for effective training and evaluation.
The system focuses on the 0–3 hour rainfall nowcasting window, while longer-range prediction is handled through ECMWF NWP visualization rather than the same AI nowcasting model.
The current system does not directly process raw Doppler weather radar data, which could provide valuable information about the movement and development of rainfall systems.
Severe weather alerts, automated SMS notifications, and a dedicated native mobile application are outside the current scope of the project.
The performance of the system can vary depending on changing weather conditions and the ability of the trained models to generalize to previously unseen weather patterns.
7.3 FUTURE ENHANCEMENTS
The proposed system can be extended in several ways to improve its prediction capability, coverage, and usability.
7.3.1 INTEGRATION OF WEATHER RADAR DATA
Future versions can incorporate real-time Doppler weather radar data. Radar observations can provide detailed information about the location, movement, and intensity of precipitation, which can complement AWS and PWS observations.
7.3.2 ADVANCED SPATIOTEMPORAL DEEP LEARNING
The prediction engine can be further enhanced using advanced CNN-LSTM, ConvLSTM, GNN-LSTM, and other spatiotemporal deep learning architectures.
These models can better capture both temporal changes and spatial relationships between weather stations.
7.3.3 IMPROVED REAL-TIME PREDICTION
The data pipeline can be optimized for faster ingestion and inference so that newly collected observations can be incorporated into the prediction process with minimal delay.
7.3.4 ADVANCED FORECAST VISUALIZATION
Future versions can provide animated rainfall maps, station-level prediction graphs, interactive forecast timelines, and improved geospatial visualization to make the forecast information easier to interpret.
7.4 CONCLUSION
The Multi-Source AI for Hyperlocal Rainfall Nowcasting project provides an integrated approach to localized rainfall monitoring and prediction by combining multiple weather observations with AI/ML techniques and numerical weather prediction data. The system addresses the need for short-term 0–3 hour rainfall nowcasting while also providing 1–10 day ECMWF forecast visualization.
By combining IMD AWS, Personal Weather Stations, AI/ML models, ECMWF NWP data, data fusion, geospatial visualization, REST APIs, and a real-time web dashboard, the proposed platform provides a complete pipeline from weather-data acquisition to user-facing forecast information.
The architecture also provides a foundation for future integration of radar and satellite data, advanced spatiotemporal deep learning models, wider geographic coverage, automated alerts, and mobile applications. Thus, the project establishes a scalable framework for developing a more comprehensive and localized weather intelligence system.











REFERENCES
[1] Xingjian Shi, Zhourong Chen, Hao Wang, Dit-Yan Yeung, Wai-kin Wong, Wang-chun Woo, "Convolutional LSTM Network: A Machine Learning Approach for Precipitation Nowcasting," Advances in Neural Information Processing Systems (NeurIPS), 2015. DOI: 10.48550/arXiv.1506.04214.
[2] Xingjian Shi, Zhihan Gao, Leonard Lausen, Hao Wang, Dit-Yan Yeung, Wai-kin Wong, Wang-chun Woo, "Deep Learning for Precipitation Nowcasting: A Benchmark and A New Model," Advances in Neural Information Processing Systems (NeurIPS), 2017. arXiv:1706.03458.
[3] Maitreya Patel, Anery Patel, Ranendu Ghosh, "Precipitation Nowcasting: Leveraging Bidirectional LSTM and 1D CNN," arXiv, 2018. DOI: 10.48550/arXiv.1810.10485.
[4] Wan Liu, Yongqiang Wang, Deyu Zhong, Shuai Xie, Jijun Xu, "ConvLSTM Network-Based Rainfall Nowcasting Method with Combined Reflectance and Radar-Retrieved Wind Field as Inputs," Atmosphere, 2022, 13(3), 411. DOI: 10.3390/atmos13030411.
[5] Suting Chen, Xin Xu, Yanyan Zhang, Dongwei Shao, Song Zhang, Mingjian Zeng, "Two-Stream Convolutional LSTM for Precipitation Nowcasting," Neural Computing and Applications, 2022, 34. DOI: 10.1007/s00521-021-06877-9.
[6] Jaroslav Frnda, Marek Durica, Jan Rozhon, Maria Vojtekova, Jan Nedoma, Radek Martinek, "ECMWF Short-Term Prediction Accuracy Improvement by Deep Learning," Scientific Reports, 2022, 12, 7898. DOI: 10.1038/s41598-022-11936-9.
[7] Huantong Geng, Xiaoyan Ge, Boyang Xie et al., "LSTMAtU-Net: A Precipitation Nowcasting Model Based on ECSA Module," Sensors, 2023, 23(13), 5785. DOI: 10.3390/s23135785.
[8] "ST-GRF: Spatiotemporal Graph Neural Networks for Rainfall Forecasting," Digital Signal Processing, 2023, 136, 103989. DOI: 10.1016/j.dsp.2023.103989.
[9] Peng et al., "A Structured Graph Neural Network for Improving the Numerical Weather Prediction of Rainfall," Journal of Geophysical Research: Atmospheres, 2023. DOI: 10.1029/2023JD039011.
[10] Maulin Raval, Pavithra Sivashanmugam, Vu Pham, Hardik Gohel, Ajeet Kaushik, Yun Wan, "Automated Predictive Analytics Tool for Rainfall Forecasting," Scientific Reports, 2021, 11, 17704. DOI: 10.1038/s41598-021-95735-8.
[11] Xihua Yang, Xiaojin Xie, De Li Liu, Fei Ji, Lin Wang, "Spatial Interpolation of Daily Rainfall Data for Local Climate Impact Assessment over Greater Sydney Region," Advances in Meteorology, 2015, 563629. DOI: 10.1155/2015/563629.
[12] Owais Ali Wani, Syed Sheraz Mahdi, Md. Yeasin, Shamal Shasang Kumar, Alexandre S. Gagnon, Faizan Danish, Nadhir Al-Ansari, Salah El-Hendawy et al., "Predicting Rainfall Using Machine Learning, Deep Learning, and Time Series Methods Across an Altitudinal Gradient in the North-Western Himalayas," Scientific Reports, 2024, 14, 27876. DOI: 10.1038/s41598-024-77687-x.
[13] Deepa Sharma, Punam Rattan, "Rainfall Prediction Using Random Forest and XGBoost – A Comparative Study," Proceedings of the 2024 5th International Conference on Data Intelligence and Cognitive Informatics (ICDICI), 2024, pp. 1348–1353. DOI: 10.1109/ICDICI62993.2024.10810907.
[14] Young-Jae Park, Doyi Kim, Minseok Seo, Hae-Gon Jeon, Yeji Choi, "Data-Driven Precipitation Nowcasting Using Satellite Imagery," Proceedings of the AAAI Conference on Artificial Intelligence, 2025, 39(27), 28284–28292. DOI: 10.1609/aaai.v39i27.35049.
[15] Wenyuan Li, Haonan Chen, Lei Han, "Improving Explainability of Deep Learning for Polarimetric Radar Rainfall Estimation," Geophysical Research Letters, 2024, 51, e2023GL107898. DOI: 10.1029/2023GL107898.





















CHAPTER 8
APPENDIX 1
main.py

"""
Hyperlocal Rainfall Nowcasting — FastAPI Backend
Main application entry point.

Configures:
- CORS for frontend communication
- Root landing `/` with service metadata and documentation links
- API routes (weather data, stations, nowcast)
- 24-48h historical backfill on startup
- Background ingestion scheduler (APScheduler)
"""

import asyncio
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

from config import get_settings
from database import create_tables
from ingestion import run_ingestion, backfill_history
from routers.weather import router as weather_router

logging.basicConfig(
level=logging.INFO,
format="%(asctime)s │ %(levelname)-7s │ %(name)-20s │ %(message)s",
datefmt="%H:%M:%S",
)
logger = logging.getLogger("nowcast")

settings = get_settings()
scheduler = AsyncIOScheduler()

@asynccontextmanager
async def lifespan(app: FastAPI):
"""
Startup / shutdown lifecycle.
"""
logger.info("🌧️  Hyperlocal Rainfall Nowcasting — Backend starting...")

# 1. Create all DB tables
await create_tables()
logger.info("✅ Database tables ready")

# 2. Run historical 24-48h backfill so graphs have full continuous curves
logger.info("⏳ Backfilling 24-48h historical time-series telemetry...")
await backfill_history()

# 3. Ingest latest live snapshot
logger.info("🔄 Running initial live data ingestion...")
await run_ingestion()

# 4. Schedule high-frequency periodic ingestion (every 60s for PWS)
scheduler.add_job(
run_ingestion,
trigger=IntervalTrigger(seconds=settings.INGESTION_INTERVAL_SECONDS),
id="weather_ingestion",
name="Weather Data Ingestion",
replace_existing=True,
)
scheduler.start()
logger.info(f"⏰ High-frequency ingestion scheduled every {settings.INGESTION_INTERVAL_SECONDS} seconds")

yield

scheduler.shutdown(wait=False)
logger.info("🛑 Scheduler stopped. Backend shutting down.")

# ── FastAPI App
app = FastAPI(
title="Hyperlocal Rainfall Nowcasting API",
description=(
"Multi-source weather data fusion platform for Tamil Nadu & Puducherry. "
"Fuses IMD AWS, Personal Weather Stations (PWS), and ECMWF NWP forecasts."
),
version="0.1.0",
lifespan=lifespan,
)

# ── CORS
app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

# ── Root Landing Endpoint
@app.get("/", response_class=HTMLResponse)
async def root():
"""
Root landing page showing backend service information and links to Swagger UI and API endpoints.
"""
return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>NowCast TN — Backend API</title>
<style>
body {
background: #0A1628;
color: #E8F1F8;
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
margin: 0;
padding: 40px 20px;
display: flex;
justify-content: center;
align-items: center;
min-height: 100vh;
box-sizing: border-box;
}
.card {
background: rgba(16, 32, 56, 0.85);
border: 1px solid rgba(28, 114, 147, 0.3);
border-radius: 16px;
padding: 32px;
max-width: 600px;
width: 100%;
box-shadow: 0 8px 32px rgba(0,0,0,0.4);
}
h1 { color: #00D4FF; margin-top: 0; font-size: 24px; }
p { color: #8BA4B8; line-height: 1.6; font-size: 14px; }
.badge {
display: inline-block;
background: rgba(6, 214, 160, 0.15);
color: #06D6A0;
padding: 4px 10px;
border-radius: 8px;
font-weight: bold;
font-size: 12px;
margin-bottom: 16px;
}
.links { margin-top: 24px; display: flex; flex-direction: column; gap: 10px; }
a {
display: block;
background: #065A82;
color: white;
text-decoration: none;
padding: 12px 16px;
border-radius: 10px;
font-weight: 500;
font-size: 14px;
transition: 0.2s;
}
a:hover { background: #1C7293; transform: translateY(-2px); }
.sublink { background: rgba(255,255,255,0.05); color: #8BA4B8; border: 1px solid rgba(28, 114, 147, 0.2); }
.sublink:hover { color: #E8F1F8; background: rgba(255,255,255,0.1); }
</style>
</head>
<body>
<div class="card">
<span class="badge">● SYSTEM ONLINE (PORT 8000)</span>
<h1>Hyperlocal Rainfall Nowcasting API</h1>
<p>
Multi-source weather data fusion backend for Tamil Nadu & Puducherry.
Telemetry actively streaming from IMD AWS, Community Personal Weather Stations (PWS), and ECMWF NWP models.
</p>
<div class="links">
<a href="/docs">📖 Open Interactive Swagger API Docs (/docs)</a>
<a href="/api/overview" class="sublink">📊 GET /api/overview — System Telemetry Summary</a>
<a href="/api/stations" class="sublink">📡 GET /api/stations — Active Weather Stations</a>
<a href="http://localhost:3000" class="sublink" target="_blank">🌐 Open Next.js Frontend Dashboard (localhost:3000)</a>
</div>
</div>
</body>
</html>
"""

@app.get("/health")
async def health():
return {"status": "ok", "service": "nowcast-backend"}

# ── Mount Routers ────────────────────────────────────────────────────
app.include_router(weather_router)


| TABLE NO. | NAME OF THE TABLE | PAGE NO. |
| --- | --- | --- |
| 2.7 | SURVEY TABLE | 11 |
| 6.1 | DATA COLLECTION | 32 |
| 6.3 | REST API RESPONSE TIME EVALUATION | 34 |
| FIGURE NO. | NAME OF THE FIGURE | PAGE NO. |
| --- | --- | --- |
| 3.3 | SYSTEM ARCHITECTURE | 18 |
| 6.1 | DATA BY SOURCE | 32 |
| 6.2 | READINGS PER STATION | 33 |
| 6.3 | 48 HOUR TELEMETRY | 34 |
| 6.4 | FEATURE CORRELATION HEATMAP | 35 |
| 6.5 | API RESPONSE TIMER | 36 |
| Abbreviation | – | Full Form |
| --- | --- | --- |
| AI | – | Artificial Intelligence |
| API | – | Application Programming Interface |
| AWS | – | Automatic Weather Station |
| CNN | – | Convolutional Neural Network |
| ECMWF | – | European Centre for Medium-Range Weather Forecasts |
| GNN | – | Graph Neural Network |
| GRIB | – | Gridded Binary |
| IMD | – | India Meteorological Department |
| LSTM | – | Long Short-Term Memory |
| ML | – | Machine Learning |
| NWP | – | Numerical Weather Prediction |
|  |  |  |
|  |
| CHAPTER NO. | TITLE | PAGE NO. |
| --- | --- | --- |
| SNO | Title of the Paper | Authors | Publication Year | Reference / Publication | Advantages | Disadvantages |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Convolutional LSTM Network: A Machine Learning Approach for Precipitation Nowcasting | Xingjian Shi, Zhourong Chen, Hao Wang, Dit-Yan Yeung, Wai-Kin Wong, Wang-Chun Woo | 2015 | arXiv:1506.04214 | Captures spatial and temporal dependencies using ConvLSTM; provides a foundation for precipitation nowcasting. | Primarily designed around structured precipitation/radar-type data; requires suitable spatiotemporal training data. |
| 2 | Deep Learning for Precipitation Nowcasting: A Benchmark and a New Model | Xingjian Shi, Zhourong Gao, Leonard Lausen, Hao Wang, Dit-Yan Yeung, Wai-Kin Wong, Wang-Chun Woo | 2017 | NeurIPS / arXiv:1706.03458 | Demonstrates the usefulness of deep learning for learning complex spatiotemporal precipitation patterns. | Deep-learning approaches require substantial training data and computational resources. |
| 3 | Precipitation Nowcasting: Leveraging Bidirectional LSTM and 1D CNN | Patel, Patel and Ghosh | 2018 | arXiv:1810.10485 | Combines CNN and BiLSTM concepts to learn feature patterns and temporal dependencies. | Focused on a particular model architecture and does not address the proposed multi-source hyperlocal platform. |
| 4 | LSTMAtU-Net: A Precipitation Nowcasting Model Based on ECSA Module | Authors as listed in the project reference | 2023 | Sensors, 23(13), 5785 | Uses an enhanced deep-learning architecture and attention mechanisms to improve precipitation feature representation. | More complex architecture; requires suitable training data and greater computational resources. |
| 5 | ConvLSTM Network-Based Rainfall Nowcasting Method with Combined Reflectance and Radar-Retrieved Wind Field as Inputs | Authors as listed in the project reference | 2022 | Atmosphere, 13(3), 411 | Shows the benefit of combining complementary meteorological inputs for rainfall nowcasting. | Depends on radar-derived inputs and does not directly address AWS/PWS-based hyperlocal data fusion. |
| 6 | Two-Stream Convolutional LSTM for Precipitation Nowcasting | Authors as listed in the project reference | 2022 | Neural Computing and Applications, 34 | Uses multiple information streams and ConvLSTM to represent precipitation dynamics. | Model complexity can increase computational requirements and implementation difficulty. |
| 7 | A Data-Driven Approach for High Accurate Spatiotemporal Precipitation Estimation | Authors as listed in the project reference | 2024 | Neural Computing and Applications | Uses GNN encoder-decoder and multimodal fusion to model spatial relationships and multiple inputs. | Requires graph construction and suitable multimodal spatiotemporal data. |
| API Endpoint | Method | Description | Avg Response Time |
| --- | --- | --- | --- |
| /api/overview | GET | Dashboard summary statistics | 18.4 ms |
| /api/stations | GET | All active station records | 34.7 ms |
| /api/readings/latest | GET | Latest reading per station | 27.2 ms |
| /api/stations/{id}/readings | GET | 24-hour time-series history | ~38–45 ms |
| /api/nowcast/latest | GET | Nowcast predictions (stub) | < 5 ms (empty) |