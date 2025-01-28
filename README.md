# CODENEST

![CODENEST LOGO](/Documentation/Text-Logo.PNG)

Welcome to CODENEST – a dynamic platform tailored for the software development community. This forum is designed to foster collaboration, share knowledge, and engage in meaningful discussions around all things software development.

What Is CODENEST

The forum provides a space where developers of all skill levels can connect, seek advice, share insights, and grow together. It includes features such as user authentication, discussion threads and like/dislike for a streamlined and intuitive user experience.

Why I Built It

I wanted to create a space where developers can easily connect, share their knowledge, and help each other out. Building this forum was a chance for me to put my coding skills to the test and learn more about what it takes to make something useful and user-friendly.


Deployed site [CodeNest](https://code-nest-b4f5033f8eff.herokuapp.com/)

---

## CONTENTS

* [User Experience](#user-experience-ux)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)

* [Features](#features)
  * [General Features on Each Page](#general-features-on-each-page)
  * [Future Implementations](#future-implementations)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)

    * [Bugs](#bugs)


* [Testing](#testing)

* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

---

## User Experience (UX)

### User Stories

#### User Registration (Must Haves)

As a user, I want to register an account, so that I can login and create my own posts and interact with others.

#### Secure Login/Logout (Must Haves)

As a user, I want to log in and out securely, so that I can ensure my account is safe and private.

#### Responsive Front-End (Must Haves)

As a user, I want to interact with a responsive front-end, so that I can have a seamless experience on any device.

#### Comment on Posts (Must Have)

As a logged-in user, I want to comment on posts, so that I can share my thoughts and interact with others.

#### CRUD Functionality (Must Haves)

As a user, I want to create, read, update, and delete (CRUD) posts and comments, so that I can manage my them effectively.

#### Form Validation (Must Haves)

As a user, I want forms with validation, so that I can avoid errors when submitting information.

#### Clear Login State (Must Haves)

As a user, I want clear visual indicators of my login status, so that I know if I am logged in or not.

#### Publish Own Post (Should have)

As a logged-in user, I want to publish my own post, so that I can share my thoughts and ideas with others.

#### Profile Customization (Should have)

As a user, I want to customize my profile, so that I can personalize my experience.

#### Social Media Integration (Could Have)

As a user, I want to link my social media accounts, so that I can log in or share content easily.


## Design


### Colour Scheme

![CODENEST Colour Scheme](/Documentation/Colour%20scheme.jpg)

The reason I chose this colour schem is it has high contrast for readability.
The black and white provide excellent contrast, ensuring that text or interactive elements are easily readable.
The addition of Seasalt softens the harshness of pure white, giving a balanced and approachable feel to the design.


### Typography

I imported the following monospaced fonts from [Google Fonts](https://fonts.google.com/):

Courier Prime (Heading Font) - Ideal for headings due to its bold and impactful style that draws attention.

Fira Code (Sub Heading Font) - Slightly rounded shapes give it a friendly and approachable appearance.

Source Code Pro (Paragraph Font) - A professional and clean look, especially suitable for development-related content.


![Heading Font](/Documentation/Courier%20Prime%20(Heading).jpg)
![Sub heading Font](/Documentation/Fira%20Code%20(Sub%20Headings).jpg)
![Paragraph Font](/Documentation/Source%20Code%20Pro%20(Paragraphs).jpg)


### Imagery

Use this section to explain what sort of imagery you plan to use through your site.

### Wireframes

![Home Page Wireframe](/Documentation/Home%20Page.jpg)
![Login Page Wireframe](/Documentation/Login%20Page.jpg)
![Logout Page Wireframe](/Documentation/Logout%20page.jpg)
![Sign Up Page Wireframe](/Documentation/Sign%20Up%20page.jpg)
![Sign Up Page Wireframe](/Documentation/Post%20detail%20page.jpg)

## ERD diagram

![ERD](/Documentation/ERD.jpg)

## Features

### General features

CodeNest is set up as a community forum/blog with these main features:

**CRUD Functionality**

* A logged in user can create update and delete a post
* A new user can create a new profile
* Logged in users can update thier profile
* A logged in user can create update and delete thier own comments
* Vistors to the site can read posts, other users profiles and comments if they whish to create update and delete   thier own content then they must sign up.

**User Authentication** 

There’s a Login/Signup option, and once signed in, a user can see their profile avatar & username in the navbar.

**User Profiles** 

After logging in, a user can view and edit their profile details by clicking on their avatar and selecting the view profile or edit profile options, a logged in user can also view other users profiles by clicking on thier avatar if they have published a post.

**Post Creation** 

A “Create a Post” feature allows users to write a title, upload an optional image, and format their content with a WYSIWYG (Summernote) editor.

**Navigation Bar** 

The top navigation includes links to Home, Create a Post, and a user dropdown menu (Profile, Edit Profile, Logout).

**Forum/Blog Home Page** 

Displays a welcome message, posts with date, time, a breif extract from the post and the users username. Users and visitors can view these posts by either clicking on the title or the read post button. Logged in users will be able to comment on a post and have CRUD for thier comments as mentioned above. Visitors will only be able to read the post. 


### Future Implementations

I would like to implent this user story in the future to make it easier for new users to sign up. 

As you can see from my Project board it was moved into the wont have section during development [Project Board](https://github.com/users/tomMckechnie-90/projects/10/views/1)

![Social Media](/Documentation/Socail-media.jpg)


**Search bar**

I would also like to add a search funtionality for users and visitors to search for posts and other users.

**Live notifications**

Adding live notifications for users to be alerted when another user interacts with thier content.

## Technologies Used

### Languages Used

* HTML
* CSS
* PYTHON
* JavaScript

### Frameworks, Libraries & Programs Used

* Django
* Bootstrap v5
* GitHub
* Balsamic
* FontAwesome

## The use of AGILE during development

I used GitHub Projects as my Agile tool, creating a project board with columns like To Do, In Progress, bugs, wont have and Done. Each user story was added as an issue with the use of must have, should have and could have labels, and moved through the board as it was developed, tested, and completed. This gave me a clear, real-time view of progress which ensured each feature was documented and tracked from start to finish. 

[CodeNest Project Board](https://github.com/users/tomMckechnie-90/projects/10/views/1)

## Deployment
1. Set DEBUG to false in settings.py
2. Add, Commit and Push your code to GitHub
3. Login to Heroku and click on the app you are developing via the dashboard
4. Navigate to the deploy tab, make sure your Github repo is linked
5. Finally click deploy branch making sure you have the main branch selected

Now your app should be deployed!

## Bugs
### Loading static bug
![Script bug](/Documentation/script%20bug%20project%20board.png)


![Script bug](/Documentation/Script%20bug.png)

While testing my features as I usaully do when I open up my workspace in the morning, I realised for some reason my comments.js script had stopped loading on the browser I tried resolving this issue my self by looking back on my commit history to see if I had changed anything by mistake for example deleting the script tag in error or script tag in the wrong place but that was not the issue, after scratching my head for arounf 20 minutes I reached out to the coding coach and class channel. Spencer our SME got in touch:


I took his advice and the script was loading again! Thank you Spencer!
![Script bug](/Documentation/Spencer%20answer.png)

![Script bug](/Documentation/Script%20bug%20console%20clear.png)

### Editing profile bug

I came across this bug trying to get a default placeholder profile image to load on a user's profile if they did not upload one. 

I clicked on the save changes button which I nicknamed "Buggy button" while debugging.

![Editing profile bug](/Documentation/Buggy%20button.jpg)

Which then showed this error message.

![Editing profile bug](/Documentation/error%20message%20.jpg)

I got stuck in and tried resolving the issue, but was having no joy. So I turned to ChatGPT by copy and pasting the error message and after a few more prompts I got this solution. which redirects the user to their profile page (view_profile) and passes the required username parameter when the save button is clicked.

![Editing profile bug](/Documentation/line%20of%20code%20(AI%20solution).jpg)

And yes it worked! Thank you AI. 

![Editing profile bug](/Documentation/Success%20message.jpg)


## Testing and Validation

### Responsive testing

CodeNest is responsive and works across all devices without any issues. Feel free to test this via dev tools.

### Validating HTML CSS, Python and JavaScript

#### **HTML**

I tested my HTML templates using the link below by clicking on the validate by direct input tab and copying my code into the input field and then clicking the check button.

[HTML Validator](https://validator.w3.org/)

As you can see from the image below I got some errors that relate to the use of summernote and cloudinary, as this was beyond my control I left my code as is. 

I removed a few extra </P> and </div> tags that it spotted I left these in by mistake when editing my code throughout the project.

![HTML Validation](/Documentation/HTML%20testing(summernote%20&%20cloudinary%20errors).jpg)

#### **CSS**

I tested my CSS using the link below by clicking on the validate by direct input tab and copy my code into the input field and then clicking the check button.

[CSS Validator](https://jigsaw.w3.org/css-validator/)

No issues to report!

![HTML Validation](/Documentation/CSS%20validation%20(Pass).jpg)

#### **JavaScript**

I tested my JavaScript my copying my code over to the link below, before running the tests I clicked on configure and checked New JavaScript features (ES6).

[JavaScript Validator](https://jshint.com/)

One issue came up, this was due to the use of bootstrap. This was beyond my control so I left the code as is.

![JavaScript Validation](/Documentation/JavasScipt.jpg)

#### **Python**
I tested my python code using the link below

[Python Validator](https://pep8ci.herokuapp.com/)

All my code now meets the PEP8 guidlines as you can from the screen shots below

![Python Validation](/Documentation/admin.jpg)

![Python Validation](/Documentation/forms.jpg)

![Python Validation](/Documentation/models.jpg)

![Python Validation](/Documentation/urls.jpg)

![Python Validation](/Documentation/views.jpg)

## The use of AI during development

I mainly used ChatGTP to assit me during development details on how AI helped can be seen in this section.

 ### Unit testing with AI

As well as some manual tests I ran unit testing on my forms.py file using Copilot in VS code

I used a breif prompt 

![Unit Testing](/Documentation/prompt.jpg)

It gave me this code

![Unit Testing](/Documentation/code.jpg)

I ran the tests in the terminal and got a pass

![Unit Testing](/Documentation/results.jpg)

### Code Creation with AI

I used ChatGTP to assit me with creating the code for my User Profiles app, it helped me understand how the code worked and really sped up development time, I did not copy and paste any code it provided, I wrote it so I could get used to the syntax and get a better understanding of how all the functionality works. 

### Debugging With AI

AI was a big help on explaining an error pages that django threw at me during development, I copy and pasted any errors that stumped me and asked it to guide me through the troubleshooting. 

### Perfomance and UX with AI

I found that AI provided me with a nice flow of code through out development leading to a improved user experience.

### A reflection on AI role during development

AI was a huge help for me, It was like having a senior developer in the room who was always on hand to assit me.
For me its biggest strength was catching any errors and helping with debugging, I would get AI to check my code for any errors daily as I am prone to a typo that can break your whole project!

All in all AI played a vital role during this project and was a great learning tool. 

Thank you AI!


## Credits

### Code Used

Credit goes to the code insitutes LMS content for the Django Blog code which I used as a template for my post and comment models. [I Think therfore I blog](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101_WTS+4/courseware/713441aba05441dfb3a7cf04f3268b3f/824fccecd0fe4e44871eeabcbf69d830/)

###  Acknowledgments

I would like to Aknowledge Amy, Vasi, Roo and Spencer for providing great advice through out this project and my time on the bootcamp. 

Also my fellow students who are always on hand to offer advice! Thank you guys!