
# Marking Guide   23 / 30


## Structural design 7/10
- I am missing a slightly higher level picture that combines all the diagrams into one, and shows where it interacts with Django
- you seem to have Customer as inheriting from event, when I think you want association.
- you might check https://mytardis.readthedocs.io/en/3.5/architecture.html for more examples

## Runtime design 4/5
- this was a nice diagram, a little bit confusing in the styles you chose - state machine? + layers - but a good effort. I would like to have seen some info on Django and where it fit.


## Allocation views 4/5
- Seems like a lot of use cases are handled by Manager. Doesn't that make you pause and ask if that class has too many responsibilities?

## Rationale  8/10
- "All design was made prior to coding, and all coding variables will be written in a clear and concise manner." Right! Instead, argue for how your design is flexible enough to change when necessary.
- Decorator is a good choice for MenuItem - let's see how it works in practice.
- The discussion on Django was reasonable, but did not get into enough detail. What problems could you see with Django?

## Comments
