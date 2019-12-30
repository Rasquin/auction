# MONICA'S AUCTION - project IV

Full Stack Frameworks with Django Milestone Project. This project consist of a full-stack site based on centrally-owned dataset  for an auction place. This site provides an  authentication mechanism for users, so that they will be able to find, bid and purchase antique artifacts. 

This project is deployed at [Heroku](https://monica-auction.herokuapp.com/)


## UX
This website has been designed to offer the users a nice experience at acquiring antique artifacts of their interest through an auction. This auction site is targeting antique items collector users.
The visitors of this website will be able to look for artifacts based on price, age and origin. Also he/she could directly by the name of the artifact. Once selected the desired criteria, a list of artifacts that fit the search criteria will be displayed. For each item, the user will be able to see a picture, the name and the item price.
After clicking on an artifact, the user will be redirected to a page where he/she would be able to know more about the object ( name, price, age, description, crafting and trajectory). If the user is interested on acquiring this item, he can bid on it or purchase it immediately for a higher price.
In order to purchase or bid, the user has to be registered and logged in.
The owner of the site will be able to earn money through each purchase.
The user will be able to pay with credit card.

- As a user, I would like a website that displays the featured artifacts, such as the last arrived item. Then the home page of the site should display those in a place easy to locate.
 
- As a user, I may be interested in objects that come from a particular age or culture. Then the site should provide the option to filter results based on age and origin.


- As user, I may have a budget to expend, so that I am interested in looking for my item based on price. Then the side should filter items by price also.

- As a user, I could like an artifact; I may find interesting how it was made, where it comes from, how old it is. Then the site should provide a picture and information about the history, origin, age, crafting and trajectory of each artifact.

- As a user, I may want to bid on an item. Then the site should provide a bidding section for each artifact, besides the user has to be authenticated before being able to bid.

- As a user, I may be pretty sure I want to acquire a special artifact, so that I dare to pay more than the bidding price to ensure the item will be mine. Then, the site should provide a mechanism that allows the user to pay a higher price to acquire the item immediately.

- As a user, I would like to pay for my purchased item, and feel secure that my card data won’t be stolen. Then the side should provide a secure payment mechanism that doesn’t expose its users to insecure situations.

- As a user, I need to register on the site to be able to participate on the auction. The site should provide a mechanism to register, logg in, log out and check the profile of a user.

- As a user, I may forget my password to loggin. The site should provide a mechanism to recover the user password.


## Features

This project works with sqlite3 database for test and postgres in production and deployment. The pricipal folder of the project is the auction folder, from there all the apps are tied though the urls and registered on the settings.
This project use a base template that is inherited to the others templates that result from the  different apps. 

### Existing Features

**Apps** (backend) Each app was built in order to control a feature of the proyject.
- Accounts app: It controls the user authentication through making an account for each of them. It consist of 5 views and 4 templates. Users can log in with their username or email. If they have missed their password they can request a new one. User can also register, check their profile and log out. There are 5 extra templates to reset the password.
 * index.html: Just render an index.
 * login.html: User can log in.
 * profile.html: User can check their profile.
 * registration.html: User can registrate on the site.
 * password_reset_complete.html
 * password_reset_confirm.html
 * password_reset_done.html
 * password_reset_email.html
 * password_reset_form.html
- Artifacts app: Here is the items list for the auction. It has the artifact model. It contains 3 views and 2 templates. 
 * artifacts.html: the user can see a list of all the artifacts with their price, a small description; if the artifact is on auction the user can see the current/minumun bidding and if the artifact is not on aution it will appear as sold. 
 * artifact.html: the user can see all the characteristics of the respective artifact as well as the state of the bidding. It give the user the option to participate in the bidding or to purchase the item inmediately.
- Bidding app: Here is where the bidding proccess happens.It has one view with logging of user required. It has no templates. Each time a new bidding is placed, the inmediate buying price is updated. The bidding has to be bigger than the minimun bidding price or than the current bidding.
- Mybiddings app: In this app the user can see the artifactcs that he has won through the auction, also those item that where inmmediately purchased or those in which the user has the current winning bid. He/she can also check if the artifact is paid or not. One view that renders to mybiddings.html
- Checkout app: When the user is ready to pay, the proccess is done through this app. Here the user has to fill a form up with his/her personal data and the respective credicard. This app works with the help of the stripe API. It has only 1 view with loggin required and render to the checkout.html
- Search app: Here the user can look for something special. He/she can search directly by the name of an artifact or can filter them by price, year or origin. It contains 2 views, one for each method (search or filter). It gives its results in the artifactcs.html
- About app: It is an app where some backgroung info about the site is given to the user. It has a view that render to about.html 

**templates** There are 14 html templates. Each of them displays a different functionality
of this website and are rendered by the different apps. All templates work with the base.html template, which contains all the html basic structure (head, body, footer) with their respective functionalities (scripts, styles, block contents, navbar).


**style** The bootstrap library was used to apply style. Besides there is the own style.
The project was made considering the "first small screen" principle, from there it
was adapted to larger sizes of screens.

**JavaScript** The project content the neccesary JS to make its components to work.
There is also own JS, mostly to make the double range bars work.

### Features Left to Implement
- That the user can give a feedback about their experience at participating at this auction site. Then the site could provide an area to display messages from users who completed their purchases process. 
- Wire up social media to the site (twitter or instagram) so users can be updated of new artifacts coming in the auction.
- Pagination: eventually the site will gorup up and pagination for the recipes would be neccesary.


## Technologies Used

This project was made with HTML5, CSS3, JavaScript and python3. Besides those, the following tools were used:

- Language: English.
- [MongoDB Atlas](https://www.mongodb.com/)
- [Heroku](https://www.heroku.com/)
- [Jinja 2.10](http://jinja.pocoo.org/docs/2.10/)


Libraries: 
- [Bootstrap v4.3.1](https://getbootstrap.com/docs/4.3/getting-started/introduction/) scripts (JavaScript, jQuery and Popper.js) to get functionality in the Bootstrap's components, and css  for most of the applied style 
- [Bootstrap-Select v1.13.9](https://developer.snapappointments.com/bootstrap-select/) scripts and css to have a more interective and styled select bottom.
- [Fontawesome Version 5.9.0](https://fontawesome.com/).
- [Google Fonts](https://fonts.google.com/?selection.family=Germania+One), from here it is got the font type of the whole website ('Germania One', cursive).


Own CSS style sheet. To make my own styles and overwrite some of the Bootstrap style library.
Own JavaScript file. To make the functionality of the add/remove ingredients and steeps in the method, also to change the color of the heart icom for the 'likes' .

## Testing
The whole code (html & CSS) was validated through the [Markup Validation Service](https://validator.w3.org/). The JavaScript was evaluated by [JSHint](https://jshint.com/)
The code was continuously monitored through the "Inspect" function of the Google Chrome Browser. Making sure that the website was completely responsive. The  project looks as expected in different browsers (GoogleChrome, InternetExplorer, Samsung internet).

Testing for the app.py:
1. each time a change in the views, form, templates or style was introduced, it was corroborated life on the browser (Django)
2.  navbar: all links of the navbar where manually tested.
3.  All the Searches by price, year, origin and name  give the expected result.
4.  All buttoms work as expected. 
5.  Each functionality of the authentication was manually checked.
6.  When clicking at the name of a recipe you are redirect to where you can get more infor about it.
7.  Form: if you try to submit it empty, a message telling you to fill the missing area appears.


Problems unsolved:


Problems solved:
- local variable 'artifact' referenced before assignment. Solved by declaring the variable at the beginning of the view and not inside the if.
- Reverse for 'checkout' with no arguments not found. 1 pattern(s) tried: ['checkout/(?P<pk>\\d+)/$']. Solved by intrucing the respective pk value together with the checkout url
- AttributeError: 'str' object has no attribute 'fields'. Solved by making sure that when passing multiple variables through the return statements so that they're accessible from the template,they were all in the same dictionary.
- Stripe was unable to pay with this car. Solved throughmaking sure the scripts for stripe were after the jquery scripts.
- ConnectionRefusedError at /accounts/password-reset/ [Errno 111] Connection refused. I had forgotten to configurate Django to send actual emails. 

Problems found by the code validator and solved:
- CSS: no errors
- HTML: It is the home of the site.It has 5 sections
   *  Error: Stray end tag div. Fixed deleting the extra </div>
   *  Error: Element spam not allowed as child of element h3 in this context. The spam wasnt really neccesary, so it was taken out.
   *  Error: Duplicate ID method. Delete the duplicated ids, they resulted to be unnecessaries.

Problems found by the code validator and NO solved (HTML):

- Error: The element a must not appear as a descendant of the button element.
- Warning: The document is not mappable to XML 1.0 due to two consecutive hyphens in a comment.
- Warning: The type attribute is unnecessary for JavaScript resources.


Result of evaluation with JSHint:
- Missing semicolon. Fixed adding the respective semicolons.
- Metrics for own script located at the end of base.html: There are 5 functions in this file. Function with the largest signature take 1 arguments, while the median is 1. Largest function has 12 statements in it, while the median is 4. The most complex function has a cyclomatic complexity value of 2 while the median is 1.


## Deployment
- This project is available in Github platform under the name of  [Cookbook](https://github.com/Rasquin/cookbook)
- This project is available in Heroku  platform under the name of [ monicas-cookbook](https://git.heroku.com/monicas-cookbook.git)


- The wireframes are located in [static/wireframes/](https://github.com/Rasquin/cookbook/tree/master/static/wireframes)

- You can check this project in the next  [Link](https://monicas-cookbook.herokuapp.com/ )


## Credits
### Content
The Auction Conditions content was taken from [Heritage Auctions](https://www.ha.com/)
The artifacts information was taken from the next websites:
- [Tiger's-Eye Slab Stone](https://fineart.ha.com/itm/nature-and-science/tiger-s-eye-slab-mt-brockman-station-pilbara-western-australia-866-x-748-x-090-inches-2200-x/a/211952-79002.s?ic4=GalleryView-Thumbnail-071515)
- [Fluorite Stone](https://fineart.ha.com/itm/nature-and-science/fluorite-xianghualing-sn-polymetallic-ore-field-linwu-co-chenzhou-hunan-china-489-x-488-x-287/a/211952-79006.s?ic4=GalleryView-Thumbnail-071515)
- [Ammonite Fossil](https://fineart.ha.com/itm/nature-and-science/ammonite-fossil-cleoniceras-sp-cretaceous-madagascar-531-x-422-x-146-inches-1350-x-1072-x-370/a/211952-79011.s?ic4=GalleryView-ShortDescription-071515)
- [The Fighting Pair - Allosaurus vs Stegosaurus](https://fineart.ha.com/itm/nature-and-science/the-fighting-pair-allosaurus-vs-stegosaurus/a/6061-49071.s?ic10=FeaturedPastSalePrices-ItemImageDesc-052317&tab=ArchiveSearchResults-012417)
- [THE FOURTH LARGEST PIECE OF THE MOON: DAR AL GANI (DaG) 1058](https://fineart.ha.com/itm/nature-and-science/from-the-far-side-of-the-moon-the-fourth-largest-piece-of-the-moon-dar-al-gani-dag-1058-lunar-breccia-lu/a/6089-49049.s?ic10=FeaturedPastSalePrices-ItemImageDesc-052317&tab=ArchiveSearchResults-012417)
- [A Large Diquis Gold Frog Pendant](https://fineart.ha.com/itm/pre-columbian/a-large-diquis-gold-frog-pendant/a/5424-70224.s?ic4=GalleryView-ShortDescription-071515)
- [A Tibetan Painted Wood Chest](https://fineart.ha.com/itm/asian-art/a-tibetan-painted-wood-chest-18th-19th-century-29-3-4-x-56-3-4-x-20-1-2-inches-756-x-1441-x-521-cm-/p/13152-28001.s?ic4=GalleryView-ShortDescription-071515)
- [A Large Dogon Post for Meeting House, Toguna](https://fineart.ha.com/itm/tribal-art/a-large-dogon-post-for-meeting-house-toguna/a/5424-70254.s?ic4=GalleryView-Thumbnail-071515)
- [Fourteen Louis XVI and Louis XVI-Style Giltwood and Upholstered Oval Back Side Chairs](https://fineart.ha.com/itm/furniture/fourteen-louis-xvi-and-louis-xvi-style-giltwood-and-upholstered-oval-back-side-chairs-circa-1775-and-later-33-x-22-x-21-in-total-/a/241950-21115.s?ic4=GalleryView-ShortDescription-071515)
- [6 wood panel Jean Dunand](https://fineart.ha.com/itm/furniture/jean-dunand-french-1877-1942-two-figures-six-panel-screen-circa-1928-lacquered-wood-57-3-4-x/a/5378-79039.s?ic10=FeaturedPastSalePrices-ItemImageDesc-052317&tab=ArchiveSearchResults-012417)
- [The Largest Gold Nugget from the Western Hemisfere - Boot of Cortez](https://fineart.ha.com/itm/nature-and-science/the-largest-gold-nugget-from-the-western-hemisphere-boot-of-cortez/a/5000-48202.s?ic10=FeaturedPastSalePrices-ItemImageDesc-052317&tab=ArchiveSearchResults-012417)
- [Rose Quartz . "La Madona Rosa"](https://fineart.ha.com/itm/nature-and-science/rose-quartz-la-madona-rosa-lavra-berilo-branco-sapucaia-do-norte-galileia-doce-v/a/5110-87153.s?ic10=FeaturedPastSalePrices-ItemImageDesc-052317&tab=ArchiveSearchResults-012417)


### Media
The photos used in this project are labelled  for reuse.
- The imagen for Good_Food_Display can be found at  [Link](https://upload.wikimedia.org/wikipedia/commons/6/6d/Good_Food_Display_-_NCI_Visuals_Online.jpg)

## Acknowledgements
The brief for this project was given by Code Institute. I received inspiration for this project from my siter Aurora, who is studying to become a cook. I always wished that we had our own cookbook full of our crazy recipes that we invent during the weekends when we share on family.

[![Build Status](https://travis-ci.org/Rasquin/auction.svg?branch=master)](https://travis-ci.org/Rasquin/auction)