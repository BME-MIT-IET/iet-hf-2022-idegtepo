# Cucumber test for BDD Testing

## About BDD

 Behavior-driven development (BDD) is the idea to describe how the application should behave in a very simple user/business-focused language.
 
 ## Cucumber for PyCharm
 
 For Pycharm a Cucumber.js needs to be installed among plugins. This enables to develop in Gherkin syntax.
 
<img src="https://user-images.githubusercontent.com/56648499/170383996-ad880a80-e71a-4750-8ddc-bfe04d5290c1.jpg" width="500" height="350">

Using Gherkin we can declare test obects with the phase **given**, and after that we can test the function using the phases **when** and **then**.
With these three basic elements we can decalre test in easy to understand forms.

We can test different **Scenarios** for one **Feature** :

<img src="https://user-images.githubusercontent.com/56648499/170384785-849a9fb0-a47e-4220-8e14-7989c758886d.png" width="350" height="125">

 ## Using Behave
 
 Behave is a Cucumber alternative for PyCharm. It can be installed using pip, for every feature it a makes a **.py** file, which declares a the code behind the steps.
 When behave command is given in the root directory, it evaluates all the **Features** and shows the results of the test.
 
 ![image](https://user-images.githubusercontent.com/56648499/170385628-124e4051-db19-4da6-846d-6e0e63c3f7b1.png)
 
 These are the results of the implemented tests, we can see that all steps succeded, the scenarios were complete, the three features are tested.
 
