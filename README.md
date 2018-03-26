This project is an exercise that is part of the interview process for joining [Checkr](https://api.checkr.com).

#### Checkr Interview

## Climate Disasters exercise

This project consists of building two small services:

 - A simple REST API that gives access to natural disasters in US based on the [FEMA dataset](https://www.fema.gov/api/open/v1/DisasterDeclarationsSummaries.csv)
 - An web app interface using this API to present the data distributed over time and location

## Tech Stack Used
- Python and Flask, CSS, HtML, JQuery and JavaScript.  Mapbox api for map rendering.  Heroku to deploy. 

## Features
- Allows user to filter FEMA data by year and disaster type, visualizing the number of incidents by state through a mapbox map with color coded layering.

## Questions Considered, issues, and Future development thoughts
- A question I had was whether the api I was building should be accessible to other customers and should have more information than just what the visualization by number of incidents called for by the project requirements.  I was told to use my best judgment.  Given time limitations, I decided to only return the number of incidents per state needed to render the map.  Given more time, I could change the api and the function in the csv_parse.py to return more details about each incident.
- Related to above, future features could include either a Popup feature upon hover over a state that lists each incident with information like County, FEMA assistance given, and year declared, or another div below the map that would list these (since, depending on the time range entered, this list could be many hundreds long and not suitable for a popup).
- Another question that arose was what to do with information about disasters that occurred in territories that are no longer part of the US, such as the Marshall Islands.  Given time contraints, I chose to ignore those.  With more time, I might add them to the statesData by looking up the coordinates for the geometry in order to add them to the map rendering.
- A current issue is the app is not mobile friendly.  Upon resizing, once the screen gets smaller than ~595px wide, the form inputs get hidden underneath the map div.  Still need to figure out how to make the map div responsive to the size of the form div so it doesn't overlay.
- Future development: I would want to find a way to make the layering and legend more dynamic, changing the colors and numbers depending on the data that comes back.  For example, if the year range is narrow or an uncommon disaster type is chosen, and the numbers coming back are between 0-20 for each state, refactor the legend and the layering to reflect a more nuanced gradation of colors.

