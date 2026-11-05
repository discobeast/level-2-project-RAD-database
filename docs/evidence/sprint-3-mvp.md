# Sprint 3 - Developing a Minimum Viable Product (MVP)


## Sprint Goals

Continue to develop the web application to the point that it provides all key functionality of the system. Test and refine it so that it can serve as the basis for the final phase of development.

### Specific Goals

**Edit these goals as needed**

- Create the following web pages:
    - Device dashboard
    - Per device menu
- Develop SQL database queries to:
    - Make new device
    - Delete device
    - check if a new device is valid
    - Update checklist
    - Add worklog




## Device creation

<!-- Replace this text with notes about what you are testing, how you tested it, and the outcome of the testing -->
Testing the creation of a device
Testing the creation of a duplicate device
Testing the creation of a device with no ID or model

Creation of a device normally goes smoothly,
Creation of a duplicate device throws up an SQL unique error and 500 server error is shown
Creation of a device with no ID creates a link to an empty device/ page which does not exist and the entry is not possible to delete due to the absence of its page.

**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE TESTING HERE**

Testing device creation

![Testing creations](<screenshots/Test device creation.gif>)

Testing duplicate device creation

![Testing duplicates](<screenshots/Test duplicate device.gif>)

Testing device with empty values

![Testing empty values](<screenshots/Test empty name device.gif>)

### Changes / Improvements

Improved device creation to prevent the creation of devices with duplicate ID's
by adding checks to the logic and added systems to prevent devices with an empty ID from being created

**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE IMPROVED SYSTEM HERE**

Testing duplicate device creation

![Alt text](<screenshots/Test duplicate device 2.gif>)

Testing empty device information creation

![Alt text](<screenshots/Test empty device id 2.gif>)


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


## Testing worklog creation

<!-- Replace this text with notes about what you are testing, how you tested it, and the outcome of the testing -->

Im creating a test worklog

**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE TESTING HERE**

![alt text](<screenshots/Test worklog.gif>)

### Changes / Improvements

The timestamp was stored as a INTEGER rather than TEXT in the SQL database which created an error when the log was sent to the server.
This was fixed

**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE IMPROVED SYSTEM HERE**

![alt text](<screenshots/Test worklog 2.gif>)


## Test auto checklist

Im testing the auto submitting checklist by ticking a box and reloading a page and then adding a note and reloading the page

**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE TESTING HERE**

![alt text](<screenshots/Test checklist.gif>)

### Changes / Improvements

The checklist HTMX was replacing itself with the response from the server, by adding the tag hx-swap=none this fixed the issue

**PLACE SCREENSHOTS AND/OR ANIMATED GIFS OF THE IMPROVED SYSTEM HERE** 

![alt text](<screenshots/Test checklist 2.gif>)

<!-- ## ETC... -->


## Sprint Review
This sprint pushed my project forward by adding some features aboslutely nessasary for my project and its usefulness




