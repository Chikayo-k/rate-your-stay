# Rate Your Stay

This is the fourth project in the code institute diploma in full stack software development. It is a full stack website designed for travellers to visit where they can provide travel reviews for people who are thinking about travelling and also people who want to to just browse what the site has to offer. The backend of the project was built using Django, Python and a Postgres relational database to store the site's data. The project is deployed using Heroku. The project was managed using githubs built in boards so I could create Sprints to track the Epics and user stories.

## Project Goals

### Project Goal

The goal of this project is to create an interactive space where travellers from all over the world can share their travel experiences, tips, and guides. The website should provide users with a simple user interface. A good understanding of what the site provides and what it offers.

### Target Audience

- People who travel a lot and enjoy sharing their experiences.
- People who are planning to travel and want to get a feel for the places they are going.

### User Goals

- As a site user I want to explore holiday ideas and also want to know other people's opinions.

- As a site user I want to be able to create an account so I can login and add reviews of places I have visited. I want to have control over the reviews I create and be able to make changes or delete them if I want. I want to be able to access the site's socials so I can share my reviews with family and friends not using the site. I want to be able to view reviews left by other people.

- As a site user who does not have an account I want to be able to view the articles on the site and read reviews that have been left by people that can help me plan a trip.

- As a site user I want to be able to log out of the website and keep my details safe and secure.

### Site owner goals

- As a site owner I want to offer a platform that will connect people and let them share their reviews on locations they have visited.
- As a site owner I want to grow the site by using social media to share details.

## User Experience (UX)

### Project Features

#### Navigation bar

- The site uses a responsive navigation bar made up of four pages, these are the Home page, About Us, Register, and Login pages. It also contains a simple logo just which is the name of the website. The logo and Home can be used to navigate to the top of the home page. 
- A user can easily access the other pages on the site and see what page they are currently on by looking at the menu in the navigation bar.

![Navigation bar image](docs/images/nav.png)

#### Hero Image / Login / Log Out / Ragister / leadmessage

- Login and register feature. Which has an image with some simple action buttons which gives the user a clear picture of the feature. The use of the image of someone relaxing gives the user an idea this is a holiday reviewing website. Users can see the lead message and understand the website at a glance.

- A register button and login button above the image aim to lead users to register for an account for the website which is the website owners goal. This is to increase the active users on the website. 
When a user is logged in, the buttons switch to show only a logout button. 

![Hero image](docs/images/main-img.png)

- When a user is logged in, the register button will change to the logout button. (Navigation bar buttun will be changed to logout as well) 
The user can see that the user is logged in clearly.

![Hrto image loggedin](docs/images/main-img-loggedin.png)

#### Article review section

- A user can click the explore button on any of the articles without an account to view reviews that have been left by users on each of the locations. User’s have easy access to jump to the details on the article page. 

- A user can view reviews without needing to sign up or create an account. This shows the user what is available on the website. It also allows more users to access the website content if they don’t want to create an account.

- Each article has an image, category, name of the place, description and the explore button.
This gives the user a better understanding of what the article is about and allows users to create an image themself what the place is like.

- The category shows users a clear understanding of what the location is famous for. The categories are Historic sites, Beaches, and Cities.

![Article section image](docs/images/article-section.png)

#### Detail Page

- When a user clicks on the explore button it will open this view.

- Here users can read a short article about the location and then view the reviews that have been left by people.

- Users can learn a little bit about the location and read all the reviews left by other users. This benefits users as it can help them make a decision on what kind of trip they want to take.

![Detail Page Image - Top](docs/images/detail-page-top.png)

#### Review Section

- The write a review button only shows up when the user logged in. 

- There is a counter that displays how many people left the review on each article. The counter will give users a quick understanding of how popular the article is and the number of reviews without having to scroll down through the review.

- Reviews will be displayed so that users can enjoy reading them.

- Only the user who wrote the review can see the edit and delete button to prevent someone else from editing or deleting the review.

![Review Section Image](docs/images/review-section.png)

- The back to top button will be shown when there is one or more reviews at the bottom and the user has scrolled down to give the user the ease of returning to the top by the click of a button.

![Back To Top button Image](docs/images/back-to-top-btn.png)

#### Review form

- The review form is only visible when the write button is clicked otherwise it is hidden. This will give the website a cleaner look and only show things when the user wants to see them.
