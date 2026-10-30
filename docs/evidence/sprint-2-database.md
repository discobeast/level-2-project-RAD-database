# Sprint 2 - Implement Database and Display of Test Data


## Sprint Goals

Implement the database, populated with test data. Create queries that retrieve test data, and display this on web pages as needed. Test and refine the queries and data display, so that it stands as the basis of the next sprint.

### Specific Goals

**Edit these goals as needed**

- Implement the database
- Add test data to the database
- Create the following web pages:
    - Home page showing all devices in network
    - Test pages for each type of check
    - Final checklist for device
- Develop SQL database queries to:
    - return a numerical status once a predetermined set of conditions has been met within a device's data
    - filter a list of devices, given queries
    - Store and manage the worklogs of devices


## Testing 

<!-- Replace this text with notes about what you are testing, how you tested it, and the outcome of the testing -->
Testing the creation of a device
Testing the creation of a duplicate device
Testing the creation of a device with no ID or model

Creation of a device normally goes smoothly,
Creation of a duplicate device throws up an SQL unique error and 500 server error is shown
Creation of a device with no ID creates a link to an empty device/ page which does not exist and the entry is not possible to delete due to the absence of its page.

**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE TESTING HERE**

![Testing creations](<screenshots/Test device creation.gif>)

![Testing duplicates](<screenshots/Test duplicate device.gif>)

![Testing empty values](<screenshots/Test empty name device.gif>)
### Changes / Improvements

Improved device creation to prevent the creation of devices with duplicate ID's
by adding checks to the logic.


**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE IMPROVED SYSTEM HERE**


## Testing FEATURE NAME HERE

Replace this text with notes about what you are testing, how you tested it, and the outcome of the testing

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

