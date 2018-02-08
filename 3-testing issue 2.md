# Using variables inside Postman and Collection Runner
Posted on 20 Feb, 2014Author abhinav
Variables are among the most powerful features in Postman. Using variables in your Postman requests, eliminates the need to duplicate requests, which can save a lot of time!







With Jetpacks, you get even more power to play with variables. You can extract data from responses and set variable values automatically. You can chain requests one after the other with minimal effort. Variable values are also available inside tests to help you make them more generic.

Data variables let you test multiple instances of a request in one go. Imagine that you want to test an API which let's users post comments on a post. Using data variables you can test for hundreds of variations of a request with different IDs, tokens or content bodies.


Let's look at how you can use variables in your workflow inside Postman.

Create an environment

For this example, let's assume we want to create two environments, production and dev.

Click on "No environment" in the header.
![image](https://user-images.githubusercontent.com/14041622/35851658-9f210762-0b63-11e8-86a6-327eb0c3119d.png)

2. Select "Manage environments" and then on the "Add" button in the modal that comes up.





To use a variable you need to enclose the variable name with double curly braces – {{my_variable_name}}.

With our environments created, let's try out a sample request. Set the base URL field for the API to {{url}}/post.





Variables with test scripts

You will need the Jetpacks upgrade for writing test scripts. If you still haven't purchased it, I strongly recommend that you do!

Inside Postman test scripts, you can set environment and global variables using the postman.setEnvironmentVariable and postman.setGlobalVariable functions. You can also access these values using the special environment and globals dictionaries.

Check out this blog entry about how you can extract values from response bodies and assign them to variables. Subsequent calls are made using these values. This is an extremely powerful feature and I am sure you will wonder how you went by without it!

Data variables

Data variables are used inside the Collection Runner. T


