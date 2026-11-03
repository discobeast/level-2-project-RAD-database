# Sprint 4 - Developing a Refined and Complete System


## Sprint Goals

Develop the system until it is fully featured, with a refined UI and it satisfies the requirements. The system will be fully tested at this point.

### Specific Goals

**Edit these goals as needed**

 - Finish sprint 0 - 3
 - Finish Website color scheme
 - Finalize website structure
 - Add worklog deletion 


## Testing Status Pill

First issue was that the status pill would always return an error (Shown as a refresh of the pill with no change) because the value being handed to the server was invalid, this was due to the buttons in the webpage having values that didnt match the values I specified in my backend,
Second issue was getting the pill to change to "In progress" when anything is done to a computer,
This was via an update query in the worklog and checklist update functions that returned a "Database locked" error

**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE TESTING HERE**

First issue

![alt text](<screenshots/Test Pill 1.gif>)

second issue

![alt text](<screenshots/Test Pill 2.gif>)

![alt text](<screenshots/image.png>)

### Changes / Improvements

First I changed the HTML to match the backend expected values
The second issue was adressed by making the function to update the device status on first change instead of having its own "With connect_db() as db" use the db instance created by the worklog/checklist functions which solved the error

**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE IMPROVED SYSTEM HERE**

![alt text](<screenshots/Test Pill 3.gif>)


## Testing Device dashboard display pill

**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE TESTING HERE**

### Changes / Improvements

Replace this text with notes any improvements you made as a result of the testing.

**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE IMPROVED SYSTEM HERE**


## Testing FEATURE NAME HERE

Replace this text with notes about what you are testing, how you tested it, and the outcome of the testing

**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE TESTING HERE**

### Changes / Improvements

Replace this text with notes any improvements you made as a result of the testing.

**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE IMPROVED SYSTEM HERE**


## ETC...


## Sprint Review

Replace this text with a statement about how the sprint has moved the project forward - key success point, any things that didn't go so well, etc.

