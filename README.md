# IG

## DESCRIPTION
This is a web application that allows users to post photos about their life and following thier friends.similat to popular photos
app website instagram.

## AUTHOR
Neville Oronni

## USER STORIES
A **user** should be albe to:
1. Sign in to the application to start using.

2. Upload pictures to the application.

3. See my profile with all my pictures.

4. Follow other users and see their pictures on my timeline.

5. Like a picture and leave a comment on it.

6. Download a picture I like and save it to my machine.

## SPECIFICATIONS
| Behaviour | Input | Output |
| --------------- | :----------:| --------: |
|Sign into application |click sigin button | logged into the index page|
|Upload pictures | Click post button & add image url | see posted image display in profile page |
|See profile with posted images | Click profile page link | see profile page with profile details and image posts |
|Follow other users| Navigate the users posted image & click follow button | list of followed users should be dispayed in users index page |
|Like a user picture| Click like button on post | should see no. of likes increment by 1 every time you like |
|Download a photo | Click download button on image | should see downloaded image on local machine after completion |  

## SETUP/INSTALLATION
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

* Clone the repo
  * git clone **repo_url** e.g git clone https://github.com/nevooronni/unsplash-new.git
* Create and start a virtual environment inside project directory
  * virtual venv virtual
  * source virtual/bin/activate

* Install all the dependencies in the file > requirements.txt
  * pip install -r requirements.txt
* Start the development server
  * python3.7 manage.py runserver

## PREREQUISITIES
* Python3.6
* Django

## TECHNOLOGIES USED
* Python3.6
* Django
* Postgresql
* Bootstrap3

## BUGS
No known bugs

## CONTACT
[nevooronni@gmail.com](nevooronni@gmail.com)

## LICENCE
Licenced under a MIT licence
