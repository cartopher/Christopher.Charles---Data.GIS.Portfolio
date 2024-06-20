### Scenario 4: Map and Exhibit Creation

**Task**: Designing and producing maps and exhibits.

**Objective**: Create high-quality, informative maps and exhibits using ArcGIS Pro and ArcGIS Online to support various departments and projects within the City of La Mesa.

#### Step-by-Step Process:

### 1. **Understanding the Requirements**
   - **Initial Meeting**: Meet with the stakeholders (e.g., city planners, engineers) to understand their specific needs for the map or exhibit.
   - **Scope Definition**: Define the scope of the project, including the purpose, audience, required data layers, symbology, and any specific elements to be included (e.g., legends, scale bars).

### 2. **Data Collection and Preparation**
   - **Data Inventory**: Inventory the available GIS data layers relevant to the project (e.g., parcels, zoning, utilities, roads).
   - **Data Quality Check**: Ensure the data is up-to-date and accurate. Perform any necessary cleaning or preprocessing.
     ```plaintext
     Example: Check for missing or inconsistent attribute data, correct any spatial inaccuracies.
     ```
   - **Data Import**: Import the required data layers into ArcGIS Pro.
     ```plaintext
     Insert Tab > Add Data > Add Data from your databases or files
     ```

### 3. **Setting Up the Map in ArcGIS Pro**
   - **New Project**: Create a new project in ArcGIS Pro.
     ```plaintext
     Start ArcGIS Pro > Create New Project > Name your project
     ```
   - **Coordinate System**: Set the coordinate system to match the requirements of the project (e.g., NAD 1983 StatePlane California VI FIPS 0406 Feet).
     ```plaintext
     Map Properties > Coordinate Systems > Set the appropriate coordinate system
     ```
   - **Add Data Layers**: Add the data layers to the map.
     ```plaintext
     Insert Tab > Add Data > Select and add the required data layers
     ```

### 4. **Symbology and Styling**
   - **Layer Symbology**: Customize the symbology for each layer to ensure that the map is clear and informative.
     ```plaintext
     Right-click on the layer > Symbology > Choose the appropriate symbology
     ```
   - **Consistent Styling**: Apply consistent styling guidelines (e.g., color schemes, line weights) across all layers to maintain a professional appearance.
     ```plaintext
     Use the Symbology Pane to adjust colors, line styles, and other visual properties
     ```

### 5. **Adding Map Elements**
   - **Title and Description**: Add a descriptive title and any necessary descriptive text.
     ```plaintext
     Insert Tab > Text > Add Title > Customize the text
     ```
   - **Legend**: Add a legend to explain the symbology used in the map.
     ```plaintext
     Insert Tab > Legend > Place Legend > Customize the legend
     ```
   - **Scale Bar**: Add a scale bar to indicate distances.
     ```plaintext
     Insert Tab > Scale Bar > Choose the appropriate scale bar style
     ```
   - **North Arrow**: Add a north arrow to show map orientation.
     ```plaintext
     Insert Tab > North Arrow > Select and place the north arrow
     ```
   - **Additional Elements**: Add any other necessary elements such as inset maps, logos, or data source credits.
     ```plaintext
     Insert Tab > Insert additional elements as needed
     ```

### 6. **Map Layout and Export**
   - **Layout View**: Switch to Layout View to design the final map layout.
     ```plaintext
     View Tab > Layout View
     ```
   - **Arrange Elements**: Arrange all map elements (title, legend, scale bar, etc.) on the layout page.
     ```plaintext
     Use the Layout tools to position and size elements appropriately
     ```
   - **Export Map**: Export the map to the required format (e.g., PDF, PNG) for distribution or printing.
     ```plaintext
     Share Tab > Export Layout > Choose the format and export settings
     ```

### 7. **Creating Interactive Web Maps and Applications (ArcGIS Online)**
   - **Publish to ArcGIS Online**: Publish the map layers to ArcGIS Online for creating interactive web maps.
     ```plaintext
     Share Tab > Web Map > Publish Web Map > Configure settings and publish
     ```
   - **Web Map Creation**: Use ArcGIS Online to create an interactive web map.
     ```plaintext
     Open ArcGIS Online > Content > Create Map > Add Layers
     ```
   - **Custom Applications**: Create custom applications using Experience Builder, Survey123, Field Maps, or StoryMaps.
     ```plaintext
     Experience Builder: Create custom user interfaces and interactions.
     Survey123: Design surveys for data collection.
     Field Maps: Create maps for field data collection.
     StoryMaps: Create narrative maps combining text, images, and maps.
     ```

### Example Workflow:

#### Creating a Zoning Map for City Planners

1. **Understanding Requirements**:
   - Meet with city planners to discuss the purpose of the zoning map and the specific areas of interest.
   - Define the map’s scope: display current zoning classifications, highlight areas of potential rezoning, include parcel boundaries, and add annotations for major landmarks.

2. **Data Collection and Preparation**:
   - Gather zoning data, parcel boundaries, and landmark data from the city’s GIS database.
   - Perform quality checks to ensure data accuracy.

3. **Setting Up the Map in ArcGIS Pro**:
   - Create a new project in ArcGIS Pro.
   - Set the coordinate system to NAD 1983 StatePlane California VI FIPS 0406 Feet.
   - Add the zoning, parcels, and landmarks data layers to the map.

4. **Symbology and Styling**:
   - Customize the symbology for zoning classifications using distinct colors for each zone.
   - Style parcel boundaries and landmarks appropriately.

5. **Adding Map Elements**:
   - Add a title: “City of La Mesa Zoning Map.”
   - Include a legend explaining zoning classifications.
   - Add a scale bar and north arrow for reference.

6. **Map Layout and Export**:
   - Switch to Layout View and arrange map elements.
   - Export the map as a PDF for printing and as a PNG for digital use.

7. **Creating Interactive Web Map (ArcGIS Online)**:
   - Publish the zoning map layers to ArcGIS Online.
   - Create an interactive web map using ArcGIS Online, enabling planners to explore zoning areas dynamically.
   - Develop a StoryMap to provide context and narratives around the zoning changes.

### 8. **Review and Feedback**
   - **Peer Review**: Have team members review the map and web applications for accuracy and usability.
   - **Stakeholder Feedback**: Present the map to stakeholders and gather feedback for any adjustments or improvements.

### 9. **Final Delivery and Communication**
   - **Deliver**: Provide the final map and web applications to the stakeholders.
   - **Documentation**: Document the map creation process, including data sources, symbology choices, and any challenges encountered.
   - **Training**: Offer a brief training session if needed to help stakeholders use the interactive web map and applications effectively.

By following these steps, you can create high-quality maps and exhibits that meet the specific needs of the City of La Mesa’s various departments, enhancing their ability to make informed decisions and communicate effectively with the public and other stakeholders.