# SCORES
This is a simple program to demonstrate writing & reading of scores data to a spreadsheet using Python and googlesheets API.
This runs on the Code Institute mock terminal on Heroku.
The program could be used to updated scores the user has achieved to a spreadsheet for a game or team event.
The main feature of this program is the main menu which allows you to select add or view scores.

## Features 
Main menu is prompted when starting program.

![image](https://user-images.githubusercontent.com/5288061/173103565-ed6fd652-6295-41b4-a3b8-159dd43190f1.png)

- figlet ASCII font - to make terminal look less boring.

![image](https://user-images.githubusercontent.com/5288061/173122747-d1352c54-a817-4fd5-bfa8-012b2d654256.png)

### Menu Features

- __Add Scores__ Select 1 to Add score to spreatsheet.

![image](https://user-images.githubusercontent.com/5288061/173109088-98047a88-8f44-4fef-9cf3-c31a1bc9ee69.png)

All scores data is added to google sheet - scores.

![image](https://user-images.githubusercontent.com/5288061/173175320-fc7d19dc-0cd3-4bd0-9e3d-81dcb9094be8.png)

https://docs.google.com/spreadsheets/d/11v3mztB9rtfcYzGZbJNHt-KGYLiYUr5TqRkyG91WUGs/edit?usp=sharing

- __View Scores__ Select 2 to view score added spreatsheet.

![image](https://user-images.githubusercontent.com/5288061/173109333-f0fc9860-0938-4236-9701-f1139d29fb79.png)

- __Quit__ Select 3 to exit program.

![image](https://user-images.githubusercontent.com/5288061/173109451-83dd276a-7269-4e10-8daf-7bd9d24f0915.png)


### Error handling

![image](https://user-images.githubusercontent.com/5288061/173121778-60f5aaa2-1981-4636-a676-16e3667d50f4.png)

Main menu requires you to enter number selection 1-3. Entering any other number or character will result in invalid choice and loop back to menu.

![image](https://user-images.githubusercontent.com/5288061/173121479-f08c2063-1397-4d69-a8d2-d9ea5c33951e.png)

Not entering a number will result in a invalid error and keep looping until entered.

![image](https://user-images.githubusercontent.com/5288061/173144685-a93f4e66-c37c-4fec-b94e-2c5b787722d3.png)

Will get invalid data if you enter more than one value.


### Features Left to Implement

- Add input data such as player name and teams.

## Testing 

![image](https://user-images.githubusercontent.com/5288061/173120611-8ccf7304-786f-4207-be47-4fc54bb366e1.png)

Needed to add newline at end of file.

### Validator Testing 

![image](https://user-images.githubusercontent.com/5288061/173175877-e0001e5a-2f68-4647-99df-d8836621aa07.png)

- PEP8
- No errors were returned when using PEP8online.com.

### Unfixed Bugs
- No known bugs.

## Deployment

- The project was deployed using Code Institute mock terminal for Herkoku.

- Steps for deployment:
- Fork or clone repository https://github.com/niallos11/scores
- Create a new Heroku app.
- Set the buildbacks to Python and NodeJS in that order.
- Added cred.json key to Config Vars in Herkoku.
- Set Config Vars to PORT 8000 in Herkoku.
- Link the Heroku app to the repository.
- Click on Deploy. 

The live link can be found here - https://score-py.herokuapp.com/

## Credits 
Mostly relied on course content & Love Sandwiches walk through project.
