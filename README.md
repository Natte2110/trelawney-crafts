<img src="./design/am-i-responsive.png" center>

# [Trelawney Crafts]()

![Python](https://img.shields.io/static/v1?label=python&message=3.11.2&color=blue) 
![Flask](https://img.shields.io/static/v1?label=flask&message=2.2.0&color=092E20)

![GitHub repo size](https://img.shields.io/github/repo-size/Natte2110/trelawney-crafts?color=orange) ![GitHub pull requests](https://img.shields.io/github/issues-pr/Natte2110/trelawney-crafts)

This is a project for the Code Institute Milestone Project 3. Trelawney Crafts is a website with the purpose of serving as a portfolio for arts and crafts.

The users of this website will be able to upload images and information regarding their most recent pieces, allowing for others to view them in a gallery-style page.

View the live project [Here!](https://trelawney-crafts-174a0a88326e.herokuapp.com/)

---

## Table of Contents
1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
        - [**Color Scheme**](#color-scheme)
        - [**Imagery**](#imagery)
        - [**Typography**](#typography)
    - [**Wireframes**](#wireframes)
    - [**Database Design**](#database-design)
2. [**Features**](#features)
    - [**Current Features**](#current-features)
    - [**Planned Features**](#planned-features)
3. [**Technologies Used**](#technologies-used)
    - [**Development Technologies**](#development-technologies)
    - [**Front-End Technologies**](#front-end-technologies)
    - [**Back-End Technologies**](#back-end-technologies)
    - [**Python Modules**](#python-modules)
4. [**Testing**](#testing)
    - [**Validation**](#validation)
    - [**User Story Testing**](#user-story-testing)
    - [**Evidence Of CRUD**](#evidence-of-crud)
    - [**Compatibility**](#compatibility)
    - [**Issues**](#issues)
5. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment**](#remote-deployment)
6. [**Credits**](#credits)
    - [**Code**](#code)
    - [**Tools And Software**](#tools-and-software)
---

## UX

### User Stories

-   #### As A First-Time Visitor, I want to:

    -   View the site irrespective of what device or browser I am using.
    -   Be able to view Arts & Crafts created by content uploaders.
    -   Create my own account on the website.

-   #### As A Returning Visitor, I want to:

    -   Update my profile information, such as my name or password.
    -   Be able to freely log in and out of my account.
    -   Post a comment or reaction to other user's posts.

-   #### As A Frequent Visitor, I want to:

    -   Upload my own photos of Artwork I made.
    -   Sort the uploaded items by it's category.
    -   Reply to comments that people have left on my posted artwork.

### Design

This web application will be designed to have an elegant and artistic theme, whilst containing elements of Cornwall hidden within.

In order to speed up development, the [Creative Bootstrap Template](https://startbootstrap.com/theme/creative) will be used as it provides a foundation on which to develop.

#### Color Scheme

To keep in line with the Cornish Theme, the app will follow a colour scheme similar to that of Cornish Tartan.

<img src="./design/cornish-tartan.webp" width=200>

*Palette*: **Extracted From Above Image**

| 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| ![#A61C35](https://via.placeholder.com/15/A61C35/A61C35) | ![#BF8E34](https://via.placeholder.com/15/BF8E34/BF8E34) | ![#594319](https://via.placeholder.com/15/594319/594319) | ![#F2F2F2](https://via.placeholder.com/15/F2F2F2/F2F2F2) | ![#0D0D0D](https://via.placeholder.com/15/0D0D0D/0D0D0D) | ![#1F5B73](https://via.placeholder.com/15/1F5B73/1F5B73) | ![#3BACD9](https://via.placeholder.com/15/3BACD9/3BACD9) |
| #A61C35 | #BF8E34 | #594319 | #F2F2F2 | #0D0D0D | #1F5B73 | #3BACD9 |

The above table was extracted from the image using [Adobe Color](https://color.adobe.com/create/image) by uploading the image and selecting the colours extracted from the image.

These will be placed as *:root* variables within the style.css file in order to be used across all necessary elements.

#### Imagery

Any imagery used on the website will be pictures of places in Cornwall, keeping with the theme. 

The users will be able to upload and manage images themselves which will be displayed in the gallery.

#### Typography

The main font that will be applied to the web application is [Montserrat](https://fonts.google.com/specimen/Montserrat), with a fallback font of **Sans-Serif**.

### Wireframes

[**Desktop Wireframe**](./design/desktop-wireframe.png)

<img src="./design/desktop-wireframe.png">


[**Mobile Wireframe**](./design/mobile-wireframe.png)

The mobile version will follow the same principles as the desktop design, however the nav bar will expand once the icon is clicked so that it does not take up too much of the screen.

<img src="./design/mobile-wireframe.png">

### Database Design

Below is the schema design for the database that will hold and handle *Users*, *posts* made by those users and *comments/reactions* on the posts.

There is also another table in order to store the names of *categories*

This is a relational database handled by [PostgreSQL](https://www.postgresql.org/) which uses primary and foreign keys from each table in order to relate entries to eachother.

<img src="./design/database-design.png">

## Features

In lieu with the project requirements, I have implemented all necessary features. The below is a list of current features on the site and how they align to the requirements.

### Existing Features

-   **Creating A User Account** - Any user of the site can create an account on the website which allows them to perform more login-required actions. The user accounts are stored within the `user` database table

-   **Updating Account Details** - Once the user has a created account and has logged in, they can view their account page in order to update their details such as their username or email. This allows them to have restricted editing access over their own entry within the `user` table.

-   **Viewing Of Posts** - On the `gallery` page, users are able to view the posts created by other users in order of *most recent first*.

-   **Reacting To Posts** - If a user is logged in, they are able to "React" to a post, similar to a "like" on social media. This reaction is stored within the `reaction` table and is linked to the post via a relationship field.

-   **Commenting On Posts** - If a user is logged in, they are able to comment on a post, which will store their username and comment content within the `comment` database table and will be linked to the post they left it on. Other users will then be able to view their comments as part of the same post.

-   **Creating A Post** - If a user is logged in, they can create their own post by uploading a photo and providing a title, category and any more information about the post that they wish. This is then checked and stored within the `post` database table and will appear on the Gallery page.

-   **Deleting A Post** - If a user is logged in, they will be able to delete only their own posts on the gallery page. A 'Delete' icon will be displayed within the post if the logged in user is the creator of that specific post. This will delete the post from the `post` database table, and will CASCADE in order to delete any related reactions or comments.

-   **Deleting Of Comments** - If a user is logged in, they are able to delete comments posted by themself in a similar fashion to deleting posts.

### Planned Features

-   **Deleting User Account** - Once logged in, the user is able to delete their account using the 'account' page in order to permanently remove their account from the database and the website.

-   **Sorting Posts By Popularity** - Within the posts on the gallery page, the user is able to sort the returned posts by order of popularity.

## Technologies Used

### Development Technologies

- ![Balsamiq Wireframes](https://img.shields.io/static/v1?label=Balsamiq&message=4.7.4&color=CC0200)
    - [Balsamiq](https://balsamiq.com/) - Balsamiq was used in order to create intuitive wireframes during the initial design process.
- ![GitHub](https://img.shields.io/static/v1?label=GitHub&message=Natte2110&color=181717&logo=github&logoColor=ffffff)
    - [GitHub](https://github.com/) - GitHub was used to store and manage the project within a combined online repository.
- ![Visual Studio Code](https://img.shields.io/static/v1?label=VS%20Code&message=1.85.1&color=007ACC&logo=visual%20studio%20code&logoColor=ffffff)
    - [VS Code](https://code.visualstudio.com/) - Visual Studio Code was used as the primary development environment for the project.

### Front-End Technologies

- ![HTML5](https://img.shields.io/static/v1?label=HTML&message=5&color=E34F26&logo=html5&logoColor=ffffff)
    - [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - HTML5 was used as the primary markup language in order to structure and display the elements on the page.
- ![CSS3](https://img.shields.io/static/v1?label=CSS&message=3&color=1572B6&logo=css3&logoColor=ffffff)
    - [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - CSS Was used in order to provide styling to the web pages with custom colours and sizes of elements.
- ![Bootstrap 4.3.1](https://img.shields.io/static/v1?label=Bootstrap&message=4.3.1&color=563d7c)
    - [Bootstrap 4.3.1](https://getbootstrap.com/docs/4.3/getting-started/introduction/) - Bootstrap was used to quickly design and create the layout and look of the website.
- ![jQuery 3.3.1](https://img.shields.io/static/v1?label=jQuery&message=3.3.1&color=0769AD&logo=jquery&logoColor=ffffff)
    - [jQuery 3.3.1](https://code.jquery.com/jquery/) - jQuery was used in conjunction with bootstrap to apply javascript selectors and updating elements more efficiently.

### Back-End Technologies

- ![Python](https://img.shields.io/static/v1?label=Python&message=3.11.2&color=blue&logo=python&logoColor=ffffff)
    - [Python 3.11.2](https://www.python.org/) - Python was used as the back-end management language to pass and handle data to and from the application.
- ![Flask](https://img.shields.io/static/v1?label=Flask&message=2.2.0&color=blue&logo=flask&logoColor=ffffff)
    - [Flask 2.2.0](https://flask.palletsprojects.com/en/3.0.x/) - Flask is a python module and was used to create the web server and to manage and handle the applicaiton routing.
- ![PostgreSQL 16.1](https://img.shields.io/static/v1?label=PostgreSQL&message=16.1&color=336791&logo=postgresql)
    - [PostgreSQL 16.1](https://www.postgresql.org/) - PostgreSQL was used as the database in this project in order to store information regarding users, posts and the attributed data to them.

### Python Modules

In this section I will highlight and explain the use of each additional python package that was used within this project.

- ![Flask Login](https://img.shields.io/static/v1?label=Flask%20Login&message=0.6.3&color=blue&logo=flask&logoColor=ffffff)
    - [Flask Login 0.6.3](https://flask-login.readthedocs.io/en/latest/) - Flask Login was used alongside Flask itself in order to manage the user accounts. First, the UserMixin was used when creating the User database table in order to allow Flask login to successfully use that table as accounts. This essentially allowed the use of carrying user sessions across different pages.
- ![Flask SQLAlchemy](https://img.shields.io/static/v1?label=Flask%20SQLAlchemy&message=2.5.1&color=blue&logo=flask&logoColor=ffffff)
    - [Flask SQLAlchemy 2.5.1](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/) - Used in order to allow flask to work seamlessly with the database in order to query, create and update records within it.
- ![Hashlib](https://img.shields.io/static/v1?label=Hashlib&message=3.11.2&color=blue)
    - [Hashlib](https://docs.python.org/3/library/hashlib.html) - Hashlib comes default with python, however it is worth mentioning its use in creating secure encrypted passwords before they a stored or read from the database in order to provide account security to the users.
- ![Datetine](https://img.shields.io/static/v1?label=Datetine&message=3.11.2&color=blue)
    - [Datetine](https://docs.python.org/3/library/datetime.html) - Also default with python, datetime was used in order to log the current date at which a users post was made in order for this to be attributed to the post itself.

## Testing

Various testing methods and processes were used in order to ensure the website not only functioned as expected, but the code itself conforms to standards.

Testing the site across different devices and browsers allowed the site to be used by anyone irrespective of their device parameters.

### Validation

**HTML**

All HTML files were checked using the [W3C HTML](https://validator.w3.org/) Validator. As the validator does not recognise Jinja templating, the pages were checked via their URL's once the project was deployed.

Any errors that were identified were rectified, and checked again once the project was redeployed.

<details>
<summary>CLICK HERE to view screenshots of the validation pages</summary>

<img src="./testing/html-validation-index.png">

<img src="./testing/html-validation-gallery.png">

<img src="./testing/html-validation-register.png">

<img src="./testing/html-validation-log-in.png">

</details>

**CSS**

<img src="./testing/css-validation.png" center>

The CSS was checked using the [W3C CSS](https://jigsaw.w3.org/css-validator/#validate_by_uri) Validation service and returned no critical errors.

Warnings were returned, however these were due to rules such as `-webkit-text-size-adjust` being vendor extensions.

**JavaScript**

- `post.js` - A few errors were present, however they were fixed in Commit ID `2809e4d`

- `script.js` - One error pertains regarding a stray '.', however this is requred for the script.

- `gallery-actions.js` - A few warnings were identified when validating this file, however they were due to "Undefined '$'". This was due to jQuery not being included in the validator so they were ignored.

- `account-management` - Similar to above, all warnings excepts the ones relating to jQuery were fixed.

**Page Speed Insights**

The [Page Speed Insights](https://pagespeed.web.dev/analysis/https-trelawney-crafts-174a0a88326e-herokuapp-com/dx9d990dv4?form_factor=desktop) tool was used in order to check the website against different criteria to ensure it performs well, is suitably accessible and performs well.

Please see the screenshot below for the returned scores.

<p align="center">
<img src="./testing/page-speed-insights.png">
</p>

Originally, using this tool, it was highlighted that the foreground colour of white text was not visible enough against the lighter colour behind. Following this initial check, I used the [WCAG Color Contrast Checker](https://accessibleweb.com/color-contrast-checker/) to ensure the newly chosen colour was suitable.

### User Story Testing

In this section, The previously defined user stories will be revisited in order to ensure they have been met accordingly.

-   #### As A First-Time Visitor, I want to:

    -   View the site irrespective of what device or browser I am using.

        The site was developed with **'Mobile-First'** in mind, meaning that the elements and how they were styled were created in such a manner that whilst being visible on desktop devices, they would also be visible on other devices, screen sizes and browsers.

        Using the Chrome Developer Tools during the devlopment process, the web page was manually tested to ensure all required elements were visible when needed and the site was responsive.
        <p align="center">
        <img src="./testing/user-story-01.png">
        </p>

    -   Be able to view Arts & Crafts created by content uploaders.

        Within the site, there is the `galley.html` page, which upon loading, queries the `post` database table and loads each user post to the page.

        This is done by passing the posts from the flask back end, before being loaded into the web page using jinja templating with a `for loop` to load each post.

        Hovering the mouse over, or tapping on it on a mobile device will reveal more information about the post itself.

        <p align="center">
        <img src="./testing/user-story-02.png">
        </p>

    -   Create my own account on the website.

        The registration page on the site allows users to sign up by creating a username, providing an email address, and also a password.

        Before the user account is created, the database is checked to ensure that the current user information has not been used. This is so that usernames and emails can be unique and not repeated between accounts.

        <p align="center">
        <img src="./testing/user-story-03.png">
        </p>

        Once the users account has been created, they can log in to access more features within the site.

        The user account is stored and retrieved from the 'user' table within the PostgreSQL database.


-   #### As A Returning Visitor, I want to:

    -   Update my profile information, such as my name or password.

        Once the user has created and logged into their account, they are able to access their account information allowing them to update certain profile information, such as their username or password.

        Much like the creation of the account, the details are first checked within the database to ensure there is no duplication of email addresses or usernames before updating that user's record within the 'user' table.

        <p align="center">
        <img src="./testing/user-story-04.png">
        </p>

    -   Be able to freely log in and out of my account.

        Any user with a created account is able to log in and out as they please using the buttons available in the navigation bar/menu.

        Clicking the "Log Out" button will instantly log out the user and return them to the home page. They are then again able to log back into their account afterwards.

        <p align="center">
        <img src="./testing/user-story-05.png">
        </p>

    -   Post a comment or reaction to other user's posts.

        If a user is logged in, they are able to post comments as part of other user made posts. This is made possible by clicking the "Comment" icon, and entering their own personal comment in the pop up screen.

        The user is also able to remove their own comment, thus deleting it from the database using the bin icon next to their comment.

        The comment is immediately reflected on the users page, as well as incrementing the number of comments on that particular post.

        <p align="center">
        <img src="./testing/user-story-06.png">
        </p>

-   #### As A Frequent Visitor, I want to:

    -   Upload my own photos of Artwork I made.

        Users with accounts are able to create their own posts to share on the website. this is done by clicking the "Post your own piece" button on the gallery page, or using the relevant links within the footer.

        Once the user selects an image from their file browser, a preview is displayed so they can check their image before it is uploaded for others to see.

        They are then able to provide more information about the piece, as well as selecting one of the categories returned from the `category` database table.

        The image is stored locally on the hosting server, whilst a link to said image is stored within the `post` database table, so that it is able to be linked to the post itself.

        Once the post is uploaded, they are redirected back to the gallery page where they are able to view their newly made post.

        <p align="center">
        <img src="./testing/user-story-07.png">
        </p>

    -   Sort the uploaded items by it's category.

        On the gallery page, the users are able to use a select box in order to sort the user-made posts by their specific categories.

        This will then only display the posts with that particular category assigned to it.

        <p align="center">
        <img src="./testing/user-story-08.png">
        </p>

    -   Reply to comments that people have left on my posted artwork.

        Similar to a previous user story, the creator of a post can also comment on it in order to reply to comments that other users have left on their artwork.

        <p align="center">
        <img src="./testing/user-story-06.png">
        </p>

### Evidence of CRUD

In this section I will explain and identify how the site has different sections of CRUD activity available to its users.

#### CR - Create

The users are able to create:

- User accounts - Stored within the `user` database table.
- Reactions - Users can react to other posts which is stored in the `reaction` table and linked to the post using the `post_id` foreign key.
- Posts - Stored within the `post` table.
- Comments - Users are able to leave comments on post which are stored within the `comment` table in a similar fashion to the Reactions.

#### U - Update

Users are able to update their own personal account information as shown in the user story testing. Once confirmed with the server, the users account record is updated within the `user` table.

#### D - Delete

In a similar fashion to the create functionality, the users are able to delete:

- User Accounts - On the account page users are able to delete their accounts from the database.
- Reactions - By clicking the reaction button again, they are able to remove their reaction from the post, which is also deleted from the `reaction` database table.
- Posts - Users are able to delete their posts using the bin item at the bottom right hand corner of their own posts.
- Comments - In a similar fashion, users are able to remove their own comments under a post by clicking the bin icon.

The tables are set up in such a way that if certain things are deleted, the attributed data stored in other tables is also deleted in the following hierarchy.

**USER ACCOUNT >> POST >> COMMENT/REACTION**

This means that if a user were to delete their account, all of the posts linked to their user ID will also be deleted, along with each comment and reaction attributed to the post.

This ensures that if a certain item is removed, such as a post, the database is not storing extra records in related tables which will, in the long run reduce the size of the database and increase its performance during queries.

### Compatibility

The sites compatability was tested across multiple devices, using my own personal devices, those of friends & family, as well as emulated devices.

Below is a testing matrix created in order to show what tests were conducted across devices and web browsers

| Colour | Meaning |
|:---:|:---:|
| ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) | Works Perfectly, No Immediate Issues |
| ![#FFC300](https://via.placeholder.com/15/FFC300/FFC300) | Works mostly as intended |
| ![#EE4B2B](https://via.placeholder.com/15/EE4B2B/EE4B2B) | Contains some issues |

| Browser | Device | Responsive | Links Work As Intended | Images Displayed | Back End Functionality | Easily Navigable |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Chrome | iPhone 12 | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) |
| Chrome | MacBook Pro | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) |
| Chrome | Windows Laptop | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) |
| Safari | MacBook Pro | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) |
| Safari | iPhone 12 | ![#FFC300](https://via.placeholder.com/15/FFC300/FFC300) | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) |
| Firefox | Raspberry Pi | ![#FFC300](https://via.placeholder.com/15/FFC300/FFC300) | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) |
| Chromium | Raspberry Pi | ![#FFC300](https://via.placeholder.com/15/FFC300/FFC300) | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) | ![#00ff00](https://via.placeholder.com/15/00ff00/00ff00) |

### Issues

The whole process was mainly issue free, however I will highlight in this section a minor problem that was discovered and corrected.

- During the deployment to Heroku, I noticed that the user uploaded posts would have their images deleted, leaving an empty post with just its text information stored within the database.

    This is due to Heroku having an [ephemeral file system](https://devcenter.heroku.com/articles/dynos#ephemeral-filesystem) meaning it would be deployed with a fresh copy of the GitHub repository, thus the user uploaded images would be wiped, whilst the database remains.

    The information that helped me understand this was found on [this](https://devcenter.heroku.com/articles/dynos#ephemeral-filesystem) heroku help post.

    One solution to this would be to create an [Amazon S3 Bucket](https://aws.amazon.com/s3/) and link it to the deployed Heroku app in order to store the users uploads in a seperate cloud storage.

    However, for marking purposes I decided to create posts on a locally deployed version and commit the uploaded images to the repository so that they could be contained within the fresh deployments of the Heroku app.

## Deployment

In this section I will highlight two different ways in which you could deploy this project for yourself, and also how this project was deployed for marking purposes.

### Local Deployment

For local deployment, you must first have installed:

- ![Python](https://img.shields.io/static/v1?label=Python&message=3.11.2&color=blue&logo=python&logoColor=ffffff)
    - [Python 3.11.2](https://www.python.org/) - To run the application itself.
- ![Visual Studio Code](https://img.shields.io/static/v1?label=VS%20Code&message=1.85.1&color=007ACC&logo=visual%20studio%20code&logoColor=ffffff)
    - [VS Code](https://code.visualstudio.com/) - Or any suitable IDE in order to make changes for yourself and browse the files.
- ![PyPi](https://img.shields.io/static/v1?label=PyPi&message=23.3.2&color=blue&logo=pypi&logoColor=ffffff)
    - [PyPi 23.3.2](https://pypi.org/project/pip/) - Or other suitable python package manager in order to install and manage python requirements.
- ![GitHub](https://img.shields.io/static/v1?label=GitHub&message=Natte2110&color=181717&logo=github&logoColor=ffffff)
    - [GitHub](https://github.com/) - In order to clone and manage this repository for yourself.
- ![PostgreSQL](https://img.shields.io/static/v1?label=GitHub&message=PostgreSQL&color=blue&logo=PostgreSQL&logoColor=ffffff)
    - [PostgreSQL](https://www.postgresql.org/) - In order to create and manage the local PostgreSQL database.

I will now highlight the steps you need to take to deploy this on your own device.

#### Setup

1. The first step in local deployment is to clone this GitHub Repository.
    
    if using Visual Studio Code, when you open the window, click **"GitHub Clone"** and paste the link to this repository.

    If using the GitHub CLI, type this following command:

    `gh repo clone Natte2110/trelawney-crafts`

2. Once you have the repository on your local machine, you need to create an `env.py` with your own variables. Please check the [sample_env.py](./sample_env.py) for an example.

3. To install the python packages used in the project, type the following command into the terminal within your IDE.

    `pip3 install -r requirements.txt`

4. Setting up the PostgreSQL database can be done using the command line.

    First, create the database using:

    `psql`
    
    `CREATE DATABASE trelawneycrafts;`

    Next, the tables can be created and initialised using the below commands:

    Please ensure at this point you have correctly linked the **DB_URL** variable in the env.py. This should be ***postgresql:///trelawneycrafts***.

    `python3`

    `>>> from trelawneycrafts import db`

    `>>> db.create_all()`

    `>>> exit()`

    This will create the database tables with those specified using the SQLAlchemy ORM within [models.py](./trelawneycrafts/models.py).

    If you wish to check if the tables have been created, run the following commands.

    `psql`

    `\c trelawneycrafts`

    `\dt`

    This will display the created tables within the trelawneycrafts database.

#### Run

Once the above steps have been followed, you can run the application by typing:

`python3 run.py`

Please ensure your terminal is at the root directory for the project if using the terminal outside of your IDE.

### Remote Deployment

- ![ElephantSQL](https://img.shields.io/static/v1?label=ElephantSQL&message=PostgreSQL%20as%20a%20Service&color=79589f&logo=postgresql&logoColor=ffffff)
    - [ElephantSQL](https://www.elephantsql.com/) - To provide a cloud based PostgreSQL database, ElephantSQL was used.

    1. In order to create your own PostgreSQL instance, head to the above link and sign up for an account with Elephant SQL.

    2. Next, head to the [ElephantSQL Dashboard](https://customer.elephantsql.com/instance) and click the `Create a New instance` button at the top.

    3. Select a name for your instance, and use the 'tiny-turtle' instance for a free deployment. Select a region on the following page, and confirm all other details.

    4. Once your instance has been created, you will need to migrate your database from elsewhere in order for it to be copied to the ElephantSQL instance.

        1. Follow steps 1, 2 and 4 in the above [local deployment](#local-deployment) section to create the database on your local machine.

        2. Using the [CI PostgreSQL Migration Tool](https://github.com/Code-Institute-Org/postgres-migration-tool/blob/main/reel2reel.py), type the following command into your terminal.

            `python3 reel2reel.py`

            This will ask you to input the URI to the database that will be copied, and then the database it will be dumped to.

            For the first input, you need something similar to:

            `postgres://{USER}:{PASSWORD}@127.0.0.1:5432/{DATABASE_NAME}`

            Using **127.0.0.1** as the database host will look for said database on your local machine.

            For the second input, head to your ElephantSQL instance, and copy the `URL` value on your instance's `Details` Tab.

            This will create a dump.sql file from your locally hosted database, and dump it into the ElephantSQL database provided above.

- ![Heroku](https://img.shields.io/static/v1?label=Heroku&message=trelawney-crafts&color=79589f&logo=heroku&logoColor=ffffff)
    - [Heroku](https://dashboard.heroku.com/) - Was used in order to create a cloud based deployment of this project directly from GitHub.
    
    1. In order to deploy this project to Heroku yourself, first start by applying for an account at [Heroku](https://dashboard.heroku.com/). You can also log in with your GitHub or Google accounts.

    2. Once you have an account, head to the [heroku dashboard](https://dashboard.heroku.com/apps) and click the `New >> Create New App` button in the top right of the screen.

    3. Choose a unique name for your deployment, and then select a suitable server for the app to be hosted on.

    4. Once you have created the app, head to the `Deploy` tab. Under `Deployment Method`, click the GitHub button in order to deploy the app straight from a GitHub repository.

    5. In the box below, specify the name of the repository you wish to deploy from. If you have not yet, clone this repository on your own account in order to deploy it from your own GitHub account.

    6. Once you have connected the required GitHub repository, select the fork you wish to deploy from and click the `Deploy` button.

    7. Finally, you will need to head to the `Settings` tab in order to setup the config vars. This will link your database and provide secret keys to your app. These config vars should follow the key value pairs listed within the [sample_env.py](./sample_env.py)

    <p align="center">
    <img src="./testing/config-vars.png">
    </p>

    Hopefully the deployment process is successful, however, if you have issues, please refer to the Heroku CLI logs by typing the following command into the [Heroku CLI Terminal](https://devcenter.heroku.com/articles/heroku-cli).

    `heroku logs --app={YOUR_APP_NAME}`

    There, you will be able to see any error messages regarding the deployment process.

## Credits

### Code

Below is a list of sources where I searched for certain methods or used code from elsewhere.

[CI Database Migration Tool](https://github.com/Code-Institute-Org/postgres-migration-tool) - This was used in order to migrate my locally hosted PostgreSQL database to the ElephantSQL instance.

[Flask Login Documentation](https://flask-login.readthedocs.io/en/latest/) - This documentation was used in order to learn and implement the flask_login python package to manage user accounts.

### Tools And Software

These different tools were used either in the development or documentation processes.

[Tables Generator](https://www.tablesgenerator.com/markdown_tables) - This website was used in order to easily design the tables used in this README.md document.

[Shields IO](https://shields.io/) - Used in order to place the badges seen within this README.

[Balsamiq](https://balsamiq.com/) - This piece of software was used in order to create the wireframes shown in the [design](#design) section.

[Adobe Color](https://color.adobe.com/create/image) -  Was used in order to extract the sites colour scheme from the image of Cornish Tartan.

[Lucid Chart](https://www.lucidchart.com/pages/landing?utm_source=google&utm_medium=cpc&utm_campaign=_chart_en_tier1_mixed_search_brand_exact_&km_CPC_CampaignId=1490375427&km_CPC_AdGroupID=55688909257&km_CPC_Keyword=lucid%20charts&km_CPC_MatchType=e&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=442433236001&km_CPC_TargetID=kwd-64262996435&km_CPC_Country=1006818&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&gad_source=1&gclid=CjwKCAiAq4KuBhA6EiwArMAw1EPQV211KvYtjxyuul8wxZInPFwWe86MEzyW9NiFahIk84N9eQe04BoC6f8QAvD_BwE) - Was used in order to create the database diagram within the [database design](#database-design)

### Media

The background image used across all pages was taken from [this Countryfile source](https://www.countryfile.com/go-outdoors/walks/walk-st-michaels-mount-cornwall).

Images used for the default/demo posts on the site were artworks my wife had created.