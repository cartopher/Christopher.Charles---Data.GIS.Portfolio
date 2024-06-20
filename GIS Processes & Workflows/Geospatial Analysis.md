### Workflow 5: Geospatial Analysis

**Task**: Performing spatial analyses to support city planning and operations.

**Objective**: Conduct various types of geospatial analyses, such as proximity analysis, network analysis, or suitability modeling, to provide actionable insights that support decision-making processes within the City of La Mesa.

#### Step-by-Step Process:

### 1. **Understanding the Analysis Requirements**
   - **Initial Meeting**: Meet with stakeholders (e.g., city planners, transportation departments) to understand their specific needs and objectives for the analysis.
   - **Define Objectives**: Clearly define the objectives of the analysis, including the questions to be answered and the expected outcomes.

### 2. **Data Collection and Preparation**
   - **Data Inventory**: Identify and gather the necessary GIS data layers relevant to the analysis (e.g., parcels, roads, population data, zoning).
   - **Data Quality Check**: Ensure that the data is accurate, up-to-date, and in the correct format.
     ```plaintext
     Example: Check for missing attributes, correct spatial inaccuracies, and ensure data consistency.
     ```

### 3. **Setting Up the Project in ArcGIS Pro**
   - **New Project**: Create a new project in ArcGIS Pro.
     ```plaintext
     Start ArcGIS Pro > Create New Project > Name your project
     ```
   - **Coordinate System**: Set the coordinate system to match the requirements of the project (e.g., NAD 1983 StatePlane California VI FIPS 0406 Feet).
     ```plaintext
     Map Properties > Coordinate Systems > Set the appropriate coordinate system
     ```

### 4. **Performing Geospatial Analysis**
   - **Proximity Analysis**
     - **Objective**: Identify optimal locations for new public transportation stops.
     - **Steps**:
       - **Buffer Analysis**: Create buffer zones around existing stops to analyze service coverage.
         ```plaintext
         Analysis Tab > Tools > Buffer > Set parameters and run the analysis
         ```
       - **Service Area Analysis**: Use Network Analyst to identify areas within a specified travel time or distance from existing stops.
         ```plaintext
         Analysis Tab > Network Analyst > Service Area > Set parameters and run the analysis
         ```
       - **Results**: Identify gaps in coverage and propose new stop locations within underserved areas.

   - **Network Analysis**
     - **Objective**: Optimize emergency response routes.
     - **Steps**:
       - **Network Dataset**: Create or use an existing network dataset for the city's road network.
         ```plaintext
         Analysis Tab > Network Analyst > New Network Dataset > Build Network
         ```
       - **Route Analysis**: Use the Route tool to find the quickest or shortest paths for emergency vehicles.
         ```plaintext
         Analysis Tab > Network Analyst > Route > Set parameters and run the analysis
         ```
       - **Results**: Generate optimal routes for different emergency scenarios and integrate these into the city’s emergency response plan.

   - **Suitability Modeling**
     - **Objective**: Determine suitable areas for new park development.
     - **Steps**:
       - **Criteria Definition**: Define criteria for suitability (e.g., proximity to residential areas, land availability, environmental factors).
       - **Weighted Overlay**: Use the Weighted Overlay tool to combine different criteria layers and generate a suitability map.
         ```plaintext
         Analysis Tab > Tools > Weighted Overlay > Set parameters and run the analysis
         ```
       - **Results**: Identify the most suitable areas for new parks based on the combined criteria.

### 5. **Visualizing and Interpreting Results**
   - **Map Creation**: Create maps to visualize the analysis results.
     ```plaintext
     Insert Tab > New Map > Add Analysis Results
     ```
   - **Symbology**: Use appropriate symbology to highlight key findings and ensure the map is clear and informative.
     ```plaintext
     Symbology Pane > Adjust colors, styles, and labels
     ```
   - **Charts and Graphs**: Generate charts and graphs to support the visual representation of the analysis.
     ```plaintext
     Insert Tab > Chart > Create Charts
     ```

### 6. **Documenting the Analysis Process**
   - **Process Documentation**: Document each step of the analysis process, including data sources, methods used, parameters set, and any assumptions made.
     ```plaintext
     Example: Detail the buffer distances used, the criteria for suitability, and the network dataset parameters.
     ```

### 7. **Communicating the Results**
   - **Report Generation**: Prepare a comprehensive report summarizing the analysis results, including maps, charts, and interpretation of findings.
     ```plaintext
     Example: Explain the implications of the proximity analysis for transportation planning, or the suitability modeling for park development.
     ```
   - **Presentation**: Create a presentation to communicate the results to stakeholders, using visual aids such as slides, maps, and charts.
     ```plaintext
     Tools: PowerPoint, ArcGIS StoryMaps
     ```

### 8. **Interactive Web Maps (Optional)**
   - **Publish to ArcGIS Online**: Publish the analysis results as interactive web maps to allow stakeholders to explore the data dynamically.
     ```plaintext
     Share Tab > Web Map > Publish Web Map > Configure settings and publish
     ```
   - **Web Applications**: Develop custom web applications using Experience Builder, Dashboards, or StoryMaps to enhance data accessibility and user engagement.
     ```plaintext
     ArcGIS Online > Create Web App > Choose appropriate template and add analysis results
     ```

### Example Workflow:

#### Conducting Proximity Analysis for New Public Transportation Stops

1. **Understanding Requirements**:
   - Meet with the transportation department to define the objectives: identify underserved areas and propose new stop locations.
   - Determine the necessary data layers: existing stops, road network, population density, major landmarks.

2. **Data Collection and Preparation**:
   - Gather data: existing public transportation stops, road network, population density.
   - Perform quality checks to ensure data accuracy.

3. **Setting Up the Project in ArcGIS Pro**:
   - Create a new project in ArcGIS Pro.
   - Set the coordinate system to NAD 1983 StatePlane California VI FIPS 0406 Feet.
   - Add the collected data layers to the map.

4. **Performing Proximity Analysis**:
   - **Buffer Analysis**: Create buffer zones around existing stops to identify service coverage.
     ```plaintext
     Analysis Tab > Tools > Buffer > Set buffer distance (e.g., 0.25 miles) > Run
     ```
   - **Service Area Analysis**: Use Network Analyst to analyze travel time from existing stops.
     ```plaintext
     Analysis Tab > Network Analyst > Service Area > Set travel time (e.g., 5 minutes) > Run
     ```
   - **Identify Gaps**: Analyze the results to identify areas not covered by existing services and propose new stop locations.

5. **Visualizing Results**:
   - Create maps showing existing stops, buffer zones, and proposed new stops.
   - Customize symbology to clearly differentiate between existing and proposed stops.
   - Generate charts showing the population served by each stop.

6. **Documenting the Analysis Process**:
   - Document the steps taken, parameters used, and any assumptions made.
   - Include details on data sources and processing steps.

7. **Communicating the Results**:
   - Prepare a report summarizing the findings, including maps and charts.
   - Create a presentation for the transportation department to explain the analysis and proposed new stops.

8. **Interactive Web Maps (Optional)**:
   - Publish the results to ArcGIS Online as an interactive web map.
   - Develop a StoryMap to provide context and narrative around the analysis, allowing stakeholders to explore the data interactively.

### 9. **Review and Feedback**
   - **Peer Review**: Have team members review the analysis for accuracy and completeness.
   - **Stakeholder Feedback**: Present the findings to stakeholders and gather feedback for any adjustments or improvements.

By following these steps, you can conduct thorough and insightful geospatial analyses that provide valuable information to support city planning and operations for the City of La Mesa.
