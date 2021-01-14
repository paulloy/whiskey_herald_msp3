# Whiskey Herald
## Code Institute: Milestone Project 3, Data Centric Development

Whiskey Herald is a collaborative community where users can contribute to updating a database with information on all their favourite whiskeys. 
This should facilitate community building and provide a meaningful experience to the user. A user can then leave reviews of their favourite whiskeys
 with CRUD functionality on their own reviews.
 The project should be of interest to new users looking to become a part of the whiskey community, and 
 current users who want to maintain a strong community and share their own thoughts of their favourite whiskeys.

 The main goal of this project is to provide the user a venue where they can share with a community their favourite whiskeys and publish reviews of those whiskeys.
Whiskey Herald is designed with user experience as one of our central goals. The information on Whiskey Herald is collected similarly to a wiki where the users can write and update the whiskeys on 
our database. The user’s goals are fulfilled with a responsive and user centric design with intuitive navigation and a familiar website design. Upon registration, a user can add a whiskey to the 
website that does not already exist on our database. The information on the Whiskey includes its name, type, an image address, and description. If the user thinks this information can be improved, 
they can then update the whiskeys information. Only the “admin” has permission to delete whiskeys, to prevent malicious users from undoing the hard work of other users in providing information.
 The user can read other users reviews and create, update and delete their own reviews. The user also has a profile page where they can update their username, profile icon, bio, password, or delete 
 their account.
My hope is that Whiskey Herald provides a great experience to as many whiskey lovers as possible.



# UX

## Project Goals

-	Develop a website with an intuitive design that helps the user accomplish their goals. [1]
-	Provide the user with a meaningful experience. [2]
-	Build a website in line with good coding practices. [3]

## User Goals

-	Provide filtered lists of whiskeys that may appeal to various user interests. E.g. Sort whiskeys by type, rating, most reviews, etc. [4]
-	Search the database with custom keywords.  [5]
-	A website with a familiar enough design that I can focus on accomplishing my goals rather than learn how to use the website. [1]
-	Feel that use of this website is a meaningful use of my time. [2]
-	Accessible design. [6]

[1] My website uses a common layout. Navbar toggle icon is placed at the top right of the page. All navigation is contained within the sidenav. The search bar is present in the header at all times.
[2] All users will be able to update the information on whiskeys so that the database is up to date and they may contribute to a community of like-minded individuals.
[3] HTML and CSS will be passed through validators, JavaScript will be passed through a linter, and Python will be written in accordance with PEP8 practices.
[4] The home page will feature some filtered whiskey lists that a user may scroll through.
[5] The user will be provided with a search bar that will allow them to navigate the database for what they are looking for.
[6] The website will adhere to good practices for ensuring that it is accessible for users with visual impairment.

## User Stories

As a user I want to:

- [1] Find out what other users think of a particular expensive whiskey and finding out if it is worth buying.
- [2] Add a whiskey to the website that is not appearing in the search results.
- [3] Update my username, profile icon, and bio for an individual identity.
- [4] Update my password as the one I created upon registration was too weak.
- [5] Receive feedback from the website so that I can be confident that my actions have made changes to the website.
- [6] Update one of my reviews as I feel it was poorly written.
- [7] Delete a review I left on the wrong whiskey. i.e. Left it on a 15 year bottle of Red Breast instead of the 12 year bottle.
- [8] Fix inaccurate information I have seen about one of my favourite whiskeys.
- [9] Leave a review of a whiskey.

[User Story Testing](TESTING.md#user-stories)

## UX Design Process

### Strategy

My initial idea was to have a website where a user could review whiskeys. My primary problem was that I would be unable to provide a full database with every whiskey there is,
and I could not find an API by anyone else who has attempted that feat. Providing only a small number of whiskeys would ruin the user experience as they would never be able 
to review a whiskey that is not in the database. I decided that it would be better to allow the users to add the whiskeys themselves to the database. Any whiskey currently no existing 
can be added and then the user can review them. I believe this would enhance the feeling of being part of a community as all users contribute to the website and therefore each other’s 
experience as more whiskeys become available to search for.

### Scope

#### Content Requirements

I wanted to provide the user with the name, type, an image, a description, and average rating of each whiskey on the website. Included with each whiskey will be a list of reviews 
for any user to read, and a form for a user to be able to submit their own review. I wanted the user to be able to create an identity by giving them a profile page that displays 
their username, profile icon, bio, and a list of all reviews they have left.

#### Functional Requirements

drinks {}
This collection contains all drinks that are displayed on the website. Any registered user can create and update documents within this collection. Only the website admin can delete these documents, so a malicious user cannot start deleting documents. 

reviews {}
This collection contains all the reviews written to the website. Any registered user can write a review, update their review, or delete it.

users {}
This collection contains all the data on registered users. A user writes to this collection when registering. These can delete their own document if they choose to delete their account. Some fields can be updated by the user.

drinks {}
Key | Value | Purpose
--- | ----- | -------
_id | ObjectId | ObjectId of this document
drink | String | The name of this particular whiskey.
drink_lower | String | The name of this particular whiskey in lowercase.
image_location | String | The image address of this whiskey.
type | String | The type of this whiskey.
description | String | A description of this whiskey.
average_score | Int32 | The average score of this whiskey calculated from all reviews left for it. 1 <= average_score <= 5

reviews {}
Key | Value | Purpose
--- | ----- | -------
_id | ObjectId | ObjectId of this document
username | String | The username of this particular user.
drink | Streing | The name of this particular whiskey.
title | String | The title of this particular review.
review | String | The review.
score | Int32 | The score the user has given the whiskey. 1 <= score <= 5
time | Date | The time this review was created, or updated.
profile_pic | string | Font awesome icon.

users {}
Key | Value | Purpose
--- | ----- | -------
_id | ObjectId | ObjectId of this document
email | String | The email of this particular user.
username | String | The username of this particular user.
username_lower | string | The username of this particular user in lowercase.
password | String | The hashed password of this user.
bio | String | The bio of this user.
profile_pic | String | The profile icon of this user. Font Awesome icon.

### Structure

#### Interaction Design

The user can find a whiskey by using a search bar that is always present in the website header. The whiskey name, description, and type are searched through with the value the user inputted.
For example, perhaps the user is interested in whiskeys matured in oak casks, then this will search through the whiskey descriptions for use of the word oak and return those results. 
Clicking one of the search results will display the whiskeys page. Some whiskeys are previewed on the index page below the hero image. 

#### Information Architecture

The information presented should be in a consistent format, so the user doesn’t feel confused when interacting with the website. For the whiskey page, the whiskey image, name, description,
and average score are presented at the top, and all reviews displayed below, with the review form displayed below the reviews.

### Skeleton

#### wireframes

[Initial wireframe design](static/img/README/first-wireframe.pdf)
[Updated Wireframe](static/img/README/updated-wireframe.pdf)

### Surface

# Testing

All testing and validation is contained within a separate .md file. [View TESTING.md](TESTING.md)

# Technologies Used

-	[HTML5](https://www.w3schools.com/html/default.asp) - Used for structuring and presenting content.
-	[CSS3](https://www.w3schools.com/css/default.asp) - Used to style the HTML in accordance with the project wireframes.
-	[JavaScript](https://www.w3schools.com/js/default.asp) - Used to make the project interactive.
-	[Python](https://www.python.org/) - Used to handle the backend.
-	[JQuery](https://jquery.com/) - Used to simplify DOM manipulation and JavaScript.
-	[SASS](https://sass-lang.com/) - Used for creating CSS as it is more readable with the ability to nest elements like in HTML.
-   [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Used with python and [extra modules](requirements.txt) to develop my application backend.
-	[Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools/) - Aided with responsive design, accessibility, and debugging.
-	[Gitpod](https://www.gitpod.io/) - The project was developed on the Gitpod IDE.
-	[Git](https://git-scm.com/) - Used to track website changes.
-	[GitHub](https://github.com/) - This hosted my repository and changes made with Git.
-   [MongoDB](https://www.mongodb.com/) - Used to host my database.
-   [Heroku](https://www.heroku.com/) - Used to deploy my live website.
-   [Flickity](https://flickity.metafizzy.co/) - Used for creating carousels.

# Credits

## Media

The following icons were sourced from [Font Awesome](https://fontawesome.com/)
- [fas fa-user](https://fontawesome.com/icons/user?style=solid)
- [fas fa-user-tie](https://fontawesome.com/icons/user-tie?style=solid)
- [fas fa-user-secret](https://fontawesome.com/icons/user-secret?style=solid)
- [fas fa-user-ninja](https://fontawesome.com/icons/user-ninja?style=solid)
- [fas fa-user-circle](https://fontawesome.com/icons/user-circle?style=solid)
- [fas fa-snowboarding](https://fontawesome.com/icons/snowboarding?style=solid)
- [fas fa-smile](https://fontawesome.com/icons/smile?style=solid)
- [far fa-smile](https://fontawesome.com/icons/smile?style=regular)
- [fas fa-skiing](https://fontawesome.com/icons/skiing?style=solid)
- [fas fa-poo](https://fontawesome.com/icons/poo?style=solid)
- [fas fa-taxi](https://fontawesome.com/icons/taxi?style=solid)
- [fab fa-suse](https://fontawesome.com/icons/suse?style=brands)
- [fas fa-dragon](https://fontawesome.com/icons/dragon?style=solid)
- [fas fa-chess](https://fontawesome.com/icons/chess?style=solid)
- [fas fa-radiation](https://fontawesome.com/icons/radiation?style=solid)
- [fas fa-atom](https://fontawesome.com/icons/atom?style=solid)
- [fas fa-dice](https://fontawesome.com/icons/dice?style=solid)
- [fas fa-dice-d20](https://fontawesome.com/icons/dice-d20?style=solid)
- [fas fa-ghost](https://fontawesome.com/icons/ghost?style=solid)
- [fas fa-wave-square](https://fontawesome.com/icons/wave-square?style=solid)
- [fas fa-hippo](https://fontawesome.com/icons/hippo?style=solid)
- [fas fa-paw](https://fontawesome.com/icons/paw?style=solid)
- [fas fa-dove](https://fontawesome.com/icons/dove?style=solid)
- [fas da-cat](https://fontawesome.com/icons/cat?style=solid)
- [fas fa-beer](https://fontawesome.com/icons/beer?style=solid)
- [fas fa-glass-whiskey](https://fontawesome.com/icons/glass-whiskey?style=solid)
- [fas fa-snowman](https://fontawesome.com/icons/snowman?style=solid)
- [fas da-hat-wizard](https://fontawesome.com/icons/hat-wizard?style=solid)
- [fas fa-microphone](https://fontawesome.com/icons/microphone?style=solid)
- [fas fa-code](https://fontawesome.com/icons/code?style=solid)
- [fas fa-search](https://fontawesome.com/icons/search?style=solid)
- [fas fa-bars](https://fontawesome.com/icons/bars?style=solid)
- [fas fa-times](https://fontawesome.com/icons/times?style=solid)
- [fas fa-cogs](https://fontawesome.com/icons/cogs?style=solid)

## Deployment

### Live Deployment

This project was deployed on [Heroku]((https://www.heroku.com/). The address of my live project is [http://whiskey-herald.herokuapp.com/](http://whiskey-herald.herokuapp.com/)

1. Firstly a requirements.txt file is needed so Heroku knows what dependencies must be installed to run this project. The following command in the terminal will create a .txt file for this project.
`pip3 freeze --local > requirements.txt`
1. A Procfile is needed so Heroku knows which file runs the app and how it should be run. The following command in the terminal will generate a Procfile.
`echo web: python app.py > Procfile`
1. Login to your Heroku account, select "New" and in the dropdown select "Create new app."
1. Create a unique app name and choose the region closest to you. In my case that is Europe. Select "Create app."
1. The easiest method of deployment is to set up automatic deployment from the github repository.
1. In the "Deploy" section of Heroku, select Github as the deployment method and connect the repository. Login to your Github account and search for the repository you wish
to connect, and deploy the master branch.
1. Before enabling automatic deployment, environment variables must be added so that Heroku can run the app.
1. Go to the Settings tab and select "Reveal Config Vars."
1. The following config vars are used in this project:
    - IP
    - PORT
    - SECRET_KEY
    - MONGO_URI
    - MONGO_DBNAME
1. Return to the deploy tab after the Procfile and requirements.txt have been committed.
1. Automatic deployment can now be enabled.
1. Select "deploy branch" and wait for Heroku to build the website.
1. When the message "Your app was successfully deployed" appears, clicking "view" will allow you to view the deployed website.

### Local Deployment

1. Open your favourite IDE with Git installed.
1. Click on the Code button at the top of this repository.
1. Copy the HTTPS URL.
1. Open a new terminal in your IDE and use the command "git clone" followed by the copied url.
`git clone https://github.com/paulloy/whiskey_herald_msp3.git`
1. Click enter and wait for your local clone to download.
1. You should now have access to a clone of this project.

## Content

The following regex pattern "^[a-zA-Z0-9]([._-](?![._-])|[a-zA-Z0-9]){3,18}[a-zA-Z0-9]$" was copied from [Java regex validate username examples](https://mkyong.com/regular-expressions/how-to-validate-username-with-regular-expression/)
I used [Flickity](https://flickity.metafizzy.co/) to create carousels. The code from [flickity.js](static/js/flickity.js) was copied from [Flickity Github Page](https://github.com/metafizzy/flickity)

Wireframes were developed using [JustInMind](https://www.justinmind.com/)

## Acknowledgements

- Thanks to the [Code Institute](https://codeinstitute.net/5-day-coding-challenge/?utm_term=code%20institute&utm_campaign=a%2526c_BR_IRL_Code_Institute&utm_source=adwords&utm_medium=ppc&hsa_net=adwords&hsa_tgt=kwd-319867646331&hsa_ad=417883010337&hsa_acc=8983321581&hsa_grp=62188641240&hsa_mt=e&hsa_cam=1578649861&hsa_kw=code%20institute&hsa_ver=3&hsa_src=g&gclid=CjwKCAjwwab7BRBAEiwAapqpTEswcNcDEOmOyi4fCT-PcSheBvn53AA4ovSOWQuIihlEAascEMo_nRoC5s4QAvD_BwE&gclsrc=aw.ds) for my coding lessons.
- Thanks to Maria, Tomás, Conor, Niall, Aaron, and Katie for registering accounts and beta testing my website.
- Thanks to the rest of my friends and family who tested the website during its development and helped me with their valuable feedback on the user design.
- Thanks to my tutor [Caleb Mbakwe](https://www.linkedin.com/in/calebmbakwe/) for feedback on the project.
- I got additional help from Stack [Overflow](https://stackoverflow.com/) and [W3](https://www.w3schools.com/) Schools.

## Books I Read

- [Laws of UX: Using Psychology to Design Better Products & Services – Jon Yablonski](https://www.amazon.co.uk/Laws-UX-Principles-Persuasive-Products/dp/149205531X/ref=sr_1_1?dchild=1&keywords=Laws+of+UX%3A+Using+Psychology+to+Design+Better+Products+%26+Services+%E2%80%93+Jon+Yablonski&qid=1610554449&sr=8-1)
- [Flask Web Development 2nd Edition: Developing Web Applications with Python – Miguel Grinberg](https://www.amazon.co.uk/Flask-Web-Development-Miquel-Grinberg/dp/1491991739/ref=sr_1_2?dchild=1&keywords=Flask+Web+Development%3A+Developing+Web+Applications+with+Python+%E2%80%93+Miguel+Grinberg&qid=1610554477&sr=8-2)


