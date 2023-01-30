# **_WeShare_**

<a href="https://weshare-api-app.herokuapp.com/" target="_blank" rel="noopener">WeShare API</a>(press for Live DEMO) is a website designed as a "real world api" for <a href="https://weshare-media.herokuapp.com/">WeShare - Media</a>
# Table of contents
1. <strong>[Objective](#objective)</strong>
2. <strong>[User Experience UX](#experience)</strong>:
3. <strong>[User Stories](#user)</strong>
4.<strong>[FlowChart](#flow)</strong>
5. <strong>[Site Structure](#structure)</strong>
6. <strong>[Project Management](#management)</strong>
7.<strong>[Testing](#test)</strong>
8. <strong>[Technologies](#technology)</strong>
9. <strong>[Deployment](#deploy)</strong>
10. <strong>[Acknowledgments](#acknoledge)</strong>

# Objective <a name="objective"></a>

* The major goal was to implement the functionality to handle all the data needed to create a fully functional social media platform. The API has full CRUD(create,read,update and delete) functionality which lets registered users upload their own posts with the optional ability to include a title, image and content. The posts can be edited or deleted as long as you are the owner. In addition, signed in users can also comment, like or share on posts.

Users can follow other users and they have the ability to update their own profile.

# UX

## User Stories <a name="user"></a>
* User

| As a User | I can create a profile that I can take advantage of different features like,create post or share.               |
|-----------|-----------------------------------------------------------------------------------------------------------------|
| As a User | I edit my profile so that I can easily change profile picture, or change username.                              |
| As a User | I can share stories so that I can share beautiful locations.                                                    |
| As a User | I can view news so that I can stay informed.                                                                    |
| As a User |  I like posts so that I can show my interests.                                                                  |
| As a User |  I can follow other users so that I can easily connect with them .                                              |
| As a User |  I can create events so that I can invite people to join in.                                                    |
| As a User | I can create, update and delete comments on each post so that I can connect and share opinions with other users.|
| As a user | I can block another user so that I hide his content.                                                            |


![userstories](/static/img/users.png)

## Flowchart <a name="flow"></a>

 The Flowchart for WeShare was made in Lucidchart.
 ![lucidchart](/static/img/api.png)


## Project Management <a name="management"></a>
* Database
        * To create the database schema, I used an graph modelling tool Graph Models which shows the entire relationship between all models in the database.I would like to mention that blocked was not used on this ocassion and I am planning for better structure.
        After following the steps required to install Graph Models, I then used <a href="https://dreampuf.github.io">dreampuf</a> to present the data in a clear way. 

![color-scheme](/database.png)

<a name="#objective" >Back to Top </a>

 * Welcome message <a name="menu"></a> - A welcome message with the name of WeShareApi.

 # Future Features<a name="future-features"></a> 
 * Planning to use Blocked as on this occasion I did not use it.
 * In future I am planning on adding Share page, a pin feature.
 * Better Code Structure and organisation.

 # Technologies Used <a name="technology"></a>
## BACK-END:<a name="packages"></a>
* [PYTHON](https://www.w3schools.com/python/) to get details from the user and validate the inputs with python logic.
* [Django-Rest-Framework](https://www.django-rest-framework.org/)


# Testing <a name="test"></a>
WeShare website has been properly tested .

 ### The app was tested with PEP8 called Pycodestyle.No major errors were found.
 Pep8 Results
![PEP8](/static/img/Screenshot%202023-01-30%20at%2005.47.18.png)

# Browser Compatibility
WeShare site was tested on the following browsers with no visible issues for the user:
1. Google Chrome 
2. Safari 
3. Mozilla Firefox
* Appearance, functionality and responsiveness were consistent throughout for a range of browsers and device sizes. 

# Deployment: <a name="deploy"></a>

* The site was deployed to Heroku pages.

1. First we have to create our app on heroku website.
![createapp](/static/img/create1.png)
2. Name the app.
![create2](/static/img/create-app.png)

3. Choose Deploy Section and Connect to Github.
![heroku](/static/img/deploy.png)

 
* The site was deployed to GitHub pages. 
The steps to deploy a site are as follows:
  1. In the GitHub repository, navigate to the **Settings** tab.
  2. Once in Settings, navigate to the **Pages** on the left side menu.


 ### **To create a local clone of this project**<a name="clone"></a>
The method from cloning a project from GitHub is below:
1. Under the repository’s name, click on the **code** tab.
2. In your preffered IDE open **Git Bash**
3. Change the working directory with the location where you would like your clone to be created .
4. Type **git clone** and the paste the URL copied previously.
5. **Enter** button to be pressed and the clone will be created.


# Credits<a name="credits"></a>

* Tutors and Mentor were very helpful in making me understand the issues I have encountered throughout.
* Please note that some models are inspired by the walkthrough project done with Code Institute.
* Some of the code ideas came from  [Stack Overflow](https://stackoverflow.com/).


 # Acknowledgements <a name="acknoledge"></a>
The site was completed as a Portfolio Project 5 DJANGO REST FRAMEWORK - Full Stack Software Developer at the [Code Institute](https://codeinstitute.net/). As such I would like to thank my mentor Jubril Akolade and Code Institute Tutor Support for their help and support.

Mihaela Younas 2023.

<a href="#objective" dir='auto'>Back to Top </a>