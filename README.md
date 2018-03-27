This project is an exercise that is part of the interview process for joining [Checkr](https://api.checkr.com).

#### Checkr Interview

## Climate Disasters exercise

This project consists of building two small services:

 - A simple REST API that gives access to natural disasters in US based on the [FEMA dataset](https://www.fema.gov/api/open/v1/DisasterDeclarationsSummaries.csv)
 - An web app interface using this API to present the data distributed over time and location

## Tech Stack Used
- Python and Flask, CSS, HtML, JQuery and JavaScript.  Mapbox api for map rendering.  Unittest for testing. Heroku to deploy. 

## Features
- Allows user to filter FEMA data by year and disaster type, visualizing the number of incidents by state through a mapbox map with color coded layering.

## Development Approach
- I broke the development of this project down into small steps.
- 1. Use the index.html template provided and write a simple flask app to render as is.
- 2. Write a simple function to read in the fema csv file, returning a dictionary of state names to number of total incidents.
- 3. Write an ajax call to get that dictionary from the server, and map the incident numbers onto the us-states format as a new property, feeding that into the map for layers
- 4. Write some initial route testing.
- 5. Refactor the python function to take in additional filtering parameters.
- 6. Write a form to take inputs from the user to pass into the parses_csv function.
- 7. Refactor the ajax call and api route to capture the user inputs and send to server.
- 8. Refactor the ajax call to rerender the map with new data upon each submit click.
- 9. Add a legend for layer colors.
- 10. Add a little more testing.
- 11. Clean up code, removing debugging print statements and console logs.
- 12. Deploy on Heroku.

## Questions Considered, issues, and Future development thoughts
- A question I had was whether the api I was building should be accessible to other customers and should therefore have more information than just what the visualization by number of incidents called for by the project requirements.  I was told to use my best judgment.  Given time limitations, I decided to only return the number of incidents per state needed to render the map.  Given more time, I could change the api and the function in the csv_parse.py to return more details about each incident.
- Related to above, future features could include either a Popup feature upon hover over a state that lists each incident with information like County, FEMA assistance given, and year declared, or another div below the map that would list each incident with that additional information (since, depending on the time range entered, this list could be many hundreds long and not suitable for a popup).
- Another question that arose was what to do with information about disasters that occurred in territories that are no longer part of the US, such as the Marshall Islands.  Given time contraints, I chose to ignore those.  With more time, I might add them to the statesData by looking up the coordinates for the geometry in order to add them to the map rendering.
- A current issue is the app is not properly responsive to extra large and small screen sizes.  Upon resizing, once the screen gets smaller than ~595px wide, the form inputs get hidden underneath the map div. On extra large screens there is a gap between the input div and the map. Still need to figure out how to make the map div responsive to the size of the form div so it doesn't overlay.
- There is not enough test coverage.  If I had more time I would include jest testing for the front end logic written in Javascript.
- Future development: I would want to find a way to make the layering and legend more dynamic, changing the colors and numbers depending on the data that comes back.  For example, if the year range is narrow or an uncommon disaster type is chosen, and the numbers coming back are between 0-20 for each state, refactor the legend and the layering to reflect a more nuanced gradation of colors.

