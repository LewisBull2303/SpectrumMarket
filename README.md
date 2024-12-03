# Spectrum Market

This webpage is an online market where users can list their items up for saLe and enquire about new items they may want to buy. Users can message one another and sell and buy items

![image](https://github.com/user-attachments/assets/ae626a21-4ed1-428b-95fa-dfc1ed0616a0)

## Features

- ### Sign Up Form
  - One of the first things a user will do is sign up to the website, It has a button in the top left
  - The user can select a username and password which is stored in a database and will only allow them to login if they know the username and password.
  - The sign up menu has been styled and positioned to look good to the users and let them see the sign up table unobstructed

![image](https://github.com/user-attachments/assets/0a8f0578-b6f0-48d0-8643-d3ad96d896a7)


- ### Login Page
-   This page allows the users to login if they know their username and password
-   Only users who have an account can login to their account

![image](https://github.com/user-attachments/assets/edb144f3-361c-420f-bf92-1dbfa27586e5)


- ### Dashboard
-   The dashboard shows all items available for the user,
-   The User can click on any of the items on there and see a description page for the items
-   At the bottom there is a footer so the user can look for items of a certain category
  
![image](https://github.com/user-attachments/assets/27861900-2984-4878-9186-84c08873b086)

![image](https://github.com/user-attachments/assets/15ea0429-978c-4dbc-8326-5d4cdaa2f8ea)


- ### Item Description Page
-   When the user clicks on an item the item description page will come up and show the user a description of the item as well as the ability to message the seller of the item
-   The page has an image on the left, showing the item, a description on the right and a title
-   Near the bottom of the page shows items that are similar to the one you are viewing based on category

  ![image](https://github.com/user-attachments/assets/bd67b8fe-8a13-4443-bbef-75a295e567fb)


- ### Browse Item Page
-   When the user clicks the browse button, which will appear after logging in, It will bring up the browse items page
-   This page allows the user to search for items, as well as filter for items based on category
  
![image](https://github.com/user-attachments/assets/8406ee80-16f2-4b4b-8929-ec8ebb519641)


- ### Edit Item/Add Item Page
-   When the user creates an Item the add item page will appear, this is also what the edit item page looks like
-   This page allows the user to create new items as well as edit old items.
  
![image](https://github.com/user-attachments/assets/737f9843-7247-4170-99dd-3c30d01614a0)

![image](https://github.com/user-attachments/assets/075cacdc-3c88-40ac-aeaf-302409fa4c5e)


## Testing

 - I tested that this page works in different browsers: Edge, Firefox Chrome, Safari and OperaGX
 - I confirmed that this project is responsive, looks good and functions on all standard screen sizes using the devtools in chrome and edge.
 - I confirmed that all text is easy to read and has correct spelling and grammar in places where needed.
 - I have confimed that all buttons fucntion as intended.

## Bugs

- I had a bug with the items being too small of the boxes that they were placed in
- I fixed this by editing the code and removing an accidental value that I added in

- I had an issue where the project would not open correctly
- This was because I forgot to activate my environment in my app which caused errors when I tried to run the app
  
## Deployment
- Heroku
- The App live link is: https://brain-tumor-detector-e5d30222dbc4.herokuapp.com/
- Set the runtime.txt Python version to a Heroku-20 stack currently supported version.
- The project was deployed to Heroku using the following steps.
- Log in to Heroku and create an App
- Log into Heroku CLI in IDE workspace terminal using the bash command: heroku login -i and enter user credentials
- Run the command git init to re-initialise the Git repository
- Run the command heroku git:remote -a "YOUR_APP_NAME" to connect the workspace and your previously created Heroku app.
- Set the app's stack to heroku-20 using the bash command: heroku stack:set heroku-20 for compatibility with the Python 3.8.14 version used for this project
- Deploy the application to Heroku using the following bash command: git push heroku main
- The deployment process should happen smoothly if all deployment files are fully functional. On Heroku Dashboard click the button Open App on the top of the page to access your App.
- If the slug size is too large then add large files not required for the app to the .slugignore file.
- Forking the GitHub Project
- To make a copy of the GitHub repository to use on your own account, one can fork the repository by doing as follows:

- On the page for the repository, go to the 'Fork' button on the top right of the page, and click it to create a copy of the repository which should then be on your own GitHub account.
- Making a Local Clone
- On the page for the repository, click the 'Code' button
- To clone the repository using HTTPS, copy the HTTPS URL provided there
- Open your CLI application of choice and change the current working directory to the location where you want the cloned directory to be made.
- Type git clone, and then paste the previously copied URL to create the clone

The Live link to this repository can be found here - [https://lewisbull2303.github.io/SpectrumMarket](https://spectrum-market-cc7b3d0a9cef.herokuapp.com/)



