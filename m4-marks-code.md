# Code Quality and Design Marks.  9/15

# BCH Score: 10/10

# Comments

## Install
- a number of Django modules were missing
- use a  `requirements.txt` to collect dependencies
- don’t include your db in the git repo. Have scaffolding that can reproduce it

## Design 
You followed the Django template. 
- have a common prefix for all your apps. e.g. codecatz.login. ...This helps in managing large systems with many apps
- I liked the way you arranged the code into a series of apps. This is nice and Django-y and I hope you can appreciate how this approach relates to the notion of modularity that we covered in the course.
- UI and user experience code were bare bones, to say the least. Even though this wasn't a HCI course, you could have tasked someone with improving this. It's still code.


## Code quality and BCH 
- the code quality was in general adequate. A few comments:
    + you might want to offload db initialization to a CSV file. That way you separate test data from your code.    
    + there was a lot of duplicate code. This is exactly where a superclass would help. E>g. all the autocomplete code.
- there were a lot of Pylint errors. BCH only gets you so far. Try runnig a tool like that to see what standard you could be holding yourself too.

## Models 
YOu did a good job here. Some of it was a bit hard to change and hard-coded.

## Tests
I could find no tests.

## Docs
Docuentation was limited or non-existent in the code. E.g. no docstrings.

## Overall
The code was well organized, largely because Django enforces this. You did a reasonable job following Django's framework. Code quality was low, and the design was overcomplicated and hard to follow.
