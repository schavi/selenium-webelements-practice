## Practice project for Selenium Python

Testing out interactions with various web elements and page structures found on [the-internet](https://the-internet.herokuapp.com/).

Not all subdomains were tested - I've tried to focus on those that were interesting to me.

When making the POM and the tests, I've tried to use different approaches - this means there may be slight inconsistencies in the tests and in the object locators.

The tests are independent of the order in which they are run. I've made an effort to keep the code readable and flexible. Comments were kept to a minimal, I've used docstrings and type hinting. Tried to use locators that are simple, concrete and easy to modify if the structure of the HTML were to change.