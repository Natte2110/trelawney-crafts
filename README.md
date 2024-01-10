# [Trelawney Crafts]()

![Python](https://img.shields.io/static/v1?label=python&message=3.6.7&color=blue) 
![Flask](https://img.shields.io/static/v1?label=flask&message=3.0.0&color=092E20)

![GitHub repo size](https://img.shields.io/github/repo-size/Natte2110/trelawney-crafts?color=orange) ![GitHub pull requests](https://img.shields.io/github/issues-pr/Natte2110/trelawney-crafts)

This is a project for the Code Institute Milestone Project 3. Trelawney Crafts is a website with the purpose of serving as a portfolio for arts and crafts.

The users of this website will be able to upload images and information regarding their most recent pieces, allowing for others to view them in a gallery-style page.

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
    -   Sort the uploaded items by order of popularity.
    -   Reply to comments that people have left on my posted artwork.

### Design

This web application will be designed to have an elegant and artistic theme, whilst containing elements of Cornwall hidden within.

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

[Desktop Wireframe]()

[Mobile Wireframe]()

### Database Design

Below is the schema design for the database that will hold and handle *Users*, *posts* made by those users and *comments/reactions* on the posts.

There is also another table in order to store the names of *categories*

This is a relational database handled by [PostgreSQL](https://www.postgresql.org/) which uses primary and foreign keys from each table in order to relate entries to eachother.

<img src="./design/database-design.png">