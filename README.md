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
* User Registration: The API should provide endpoints for users to register for the platform by providing basic information such as name, email address, and password.

* User Authentication: The API should provide endpoints for users to authenticate themselves by logging in with their registered email and password.

* User Profile: The API should provide endpoints for registered users to create a profile that includes information such as their name, profile picture, bio, and other optional details.

* Post Creation: The API should provide endpoints for registered users to create new posts by uploading an image and adding a title and content. 

* Post Editing: The API should provide endpoints for registered users to edit their own posts, including the title, content, and image.

* Post Deletion: The API should provide endpoints for registered users to delete their own posts.

* Commenting: The API should provide endpoints for signed-in users to leave comments on posts created by other users.

* Liking: The API should provide endpoints for signed-in users to "like" posts created by other users.

* Users can follow other users and they have the ability to update their own profile.

# User Stories <a name="user"></a>
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
WeShare website has been tested as followed:

## Unit Testing was performed for :
* Events : 
The setUp method is used to set up the test environment by creating a user and an event object with some predefined attributes.

The first test case, test_event_saved_correctly, verifies that the event is saved correctly by checking that the attributes of the event object created in setUp match the expected values.

The second test case, test_is_owner_method, tests the is_owner method of the Event model.

* Posts:

In the setUp method, two user objects are created to set up the test environment.

The first test case, test_follower_creation, creates a Follower object with the owner and followed fields set to the two user objects created in setUp. This test case checks that the created Follower object has the expected attributes, including a non-null created_at field.

The second test case, test_duplicate_follower_creation, creates a Follower object with the same owner and followed fields as the Follower object created in the previous test case. This test case checks that trying to create this duplicate Follower object raises an exception.

The third test case, test_follower_ordering, creates two Follower objects with different owners and follows, and checks that they are ordered correctly when retrieved from the database by the created_at field, in descending order. 

* Followers :
The setUp method is used to set up the test environment by creating two user objects.

The first test case, test_follower_creation, tests that a Follower object can be created successfully and that its attributes match the expected values.

The second test case, test_duplicate_follower_creation, tests that creating a Follower object with the same owner and followed as an existing Follower object raises an exception.

The third test case, test_follower_ordering, tests that the Follower objects are ordered correctly by the created_at field in descending order.
## Manual Testing endpoints:
### Posts 
- Verify that you receive a response from the server. The response should include a list of posts in JSON format, with each post represented as a dictionary of key-value pairs.

- verify if logged in user can edit and save the post.
- verify if another user can edit or delete the posts if it's not his own.

![Posts1](/static/img/posts.png)

### Profiles 
- verify if logged in user can edit and save/delete the profile.
- verify if another user can edit or delete the profiles if it's not his own.

![Profile](/static/img/profile.png)
![Profile2](/static/img/different-profiles.png)

### Likes 
- verify if user can like or delete a like 

![Likes](/static/img/likes.png)

### Stories 
- verify if logged in user can edit and save/delete the stories.
- verify if another user can edit or delete the stories if it's not his own.

![stories](/static/img/story.png)
![stories](/static/img/story%20detsils.png)

### Events 
- verify if logged in user can edit and save/delete the event.
- verify if another user can edit or delete the events if it's not his own.

![Events](/static/img/edit-event.png)

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
![config](/static/img/config.png)

3. Add the following config vars:

* SECRET_KEY: (Your secret key)
* DATABASE_URL: (ElephantSQL key)
* ALLOWED_HOST:
* CLIENT_ORIGIN: url for the client front end react application that wil be making requests to these APIs
* CLIENT_ORIGIN_DEV: address of the local server used to preview and test UI during development of the front end client application
* CLOUDINARY_URL - to store the images .

Click the deploy tab

Scroll down to Connect to GitHub and sign in / authorize when prompted

In the search box, find the repositoy you want to deploy and click connect

Scroll down to Manual deploy and choose the main branch

Click deploy

![heroku](/static/img/deploy.png)

 
 4. ### Connect Database : 
 * ElephantSQL is a cloud-based PostgreSQL database hosting service that provides an easy and reliable way to deploy, manage, and scale PostgreSQL databases in the cloud.
 * A convenient and scalable way to store and manage data, allowing you to focus on developing your API logic without worrying about the underlying database infrastructure.


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
The site was completed as a Portfolio Project 5 DJANGO REST FRAMEWORK - Full Stack Software Developer at the [Code Institute](https://codeinstitute.net/). As such I would like to thank Code Institute Tutor Support for their help and support.

Mihaela Younas 2023.

<a href="#objective" dir='auto'>Back to Top </a>