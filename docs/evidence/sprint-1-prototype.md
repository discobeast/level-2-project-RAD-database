# Sprint 1 - Developing a DB and UI Prototype


## Sprint Goals

Develop a design for the database and a UI prototype that simulates the key functionality of the system. Test and refine the UI so that it can serve as the model for the next phase of development in Sprint 2.

### Specific Goals

**Edit these goals as needed**

<!-- - Design the database:
    - Tables
    - Fields / types
    - Primary keys
    - Default / nullable values
    - Relationships (foreign keys)
- Design the UI
    - Key pages
    - User interactions and 'flow'
    - Page layouts / features
    - Colour palette
    - Etc. -->
- Design the database:
    - Tables
    - Fields / types
    - Primary keys
    - Default / nullable values
    - Relationships (foreign keys)
- Design the UI
    - Key pages
    - User interactions and 'flow'
    - Page layouts / features
    - Colour palette
    - Etc.


## Initial Database Design


Users will be authenticated with a 7 character pregenerated code whereas they will assign themselves a name. This is required solely to track who last worked on and assign names to notes left on computers at rad.
Currently the computer table has various boolean values to describe any initial observations and the state of the computer
User last used computers will be stored as the computer ID and the last worked on date stored as plaintext DD/MM/YYYY

![DB Design](<screenshots/Screenshot 2026-08-04 140943.png>)

### Required Data Input

My database will take inputs for users as their preferred name/username
For computers users will be able to add computers to the database with their RAD id and then provide information on the state of the computer via forms.

### Required Data Output

The output for users will be their last used device and for computers it will be the table values describing the status of the computer and the ID of the computer.
Other data outputs will be

### Required Data Processing

Rows like "notes" and "need" will contain multiple values which will be split and merged with a python algorithm.
States are stored as a number from 0 to 3 which will then be translated to an actual description of the state of the device              


## UI 'Flow'

The first stage of prototyping was to explore how the UI might 'flow' between states, based on the required functionality.

This Figma demo shows the initial design for the UI 'flow':

**FIGMA FLOW - https://design.penpot.app/#/view?file-id=4ff7ff5f-2875-80f9-8008-5a6523c53270&page-id=4ff7ff5f-2875-80f9-8008-5a6523c53271&section=interactions&index=0&share-id=81f57451-85cc-819d-8008-7e6d7044ff9e**

### Testing

I gave my inital flow to one of my stakeholders (Mr taylor)

### Changes / Improvements

Mr taylor wondered why a settings menu was needed.
There are not enough settings to require a menu so the menu has been removed

<!-- *IMPROVED FIGMA FLOW - PLACE THE FIGMA EMBED CODE HERE - MAKE SURE IT IS SET SO THAT EVERYONE CAN ACCESS IT* -->
https://design.penpot.app/#/view?file-id=81f57451-85cc-819d-8008-7e75183d65db&page-id=4ff7ff5f-2875-80f9-8008-5a6523c53271&section=interactions&frame-id=bd097025-0315-8035-8008-6c68ef767fe0&index=0&share-id=67de744c-baf3-44b9-9737-bce6caaf3398

## Initial UI Prototype

The next stage of prototyping was to develop the layout for each screen of the UI.

This Figma demo shows the initial layout design for the UI:

![Alt text](<screenshots/Screenshot 2026-08-25 132619.png>)

### Testing

given to stakeholders in a mobile format

### Changes / Improvements

Mr taylor has given feedback that he would much rather checkboxes and dropdowns to text inputs due to the difficulty
of submitting text on mobile. 

Because of this I will be changing the per-device menu to a simpler y/n list of questions format for the initialization of the device,
and then using a more streamlined ui for simpler changes (Like marking the device as scrap or given out)

https://design.penpot.app/#/view?file-id=c828d3cf-7d4e-8145-8008-90767240c087&page-id=c828d3cf-7d4e-8145-8008-90767240c088&section=interactions&frame-id=fbac5124-b587-80ab-8008-9076850fd4cd&index=0&share-id=94659913-2b81-4fe5-bcf0-08a69412b3e0


## Refined UI Prototype

Having established the layout of the UI screens, the prototype was refined visually, in terms of colour, fonts, etc.

This Figma demo shows the UI with refinements applied:

<!-- *FIGMA REFINED PROTOTYPE - PLACE THE FIGMA EMBED CODE HERE - MAKE SURE IT IS SET SO THAT EVERYONE CAN ACCESS IT* -->

### Testing

<!-- Replace this text with notes about what you did to test the UI flow and the outcome of the testing. -->

### Changes / Improvements

<!-- Replace this text with notes any improvements you made as a result of the testing.

*FIGMA IMPROVED REFINED PROTOTYPE - PLACE THE FIGMA EMBED CODE HERE - MAKE SURE IT IS SET SO THAT EVERYONE CAN ACCESS IT* -->


## Sprint Review
<!-- 
Replace this text with a statement about how the sprint has moved the project forward - key success point, any things that didn't go so well, etc. -->

