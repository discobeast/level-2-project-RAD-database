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
    - filter a list of devices, given queries
    - Store and manage the worklogs of devices
    - delete devices


## Device creation

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
![Alt text](<screenshots/Test duplicate device 2.gif>)
![Alt text](<screenshots/Test empty device id 2.gif>)


## Active search

Test active search by searching 14022 slowly

**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE TESTING HERE**

![alt text](<screenshots/Test active search.gif>)

### Changes / Improvements

I forgot the enclosing % signs in the sql query so the wildcard was not working

**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE IMPROVED SYSTEM HERE**

![alt text](<screenshots/Test active search 2.gif>)

## Testing Deletion

I attempted to delete a device and its associated entries (worklog,checklist)

**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE TESTING HERE**

![alt text](<screenshots/Test device deletion.gif>)

While fixing I broke the deletion mechanisim due to an incorrect handling of the SQL query

![alt text](<screenshots/Test device deletion 2.gif>)

### Changes / Improvements

Added line to DB.py to enable ON DELETE CASCADE in my SQLite database

**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE IMPROVED SYSTEM HERE**

![alt text](<screenshots/Test device deletion 3.gif>)

## ETC...


## Sprint Review

I added errorchecking that will be benificial for finishing my project and somehow did most of the testing for sprint 3 unknowingly in this sprint.