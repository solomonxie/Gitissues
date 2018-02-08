# 10 tips for working with Postman variables


Variables are a fundamental concept in programming, and in Postman, they can be your best friend. Instead of painstakingly updating individual values, use variables to cascade changes effortlessly through the rest of your code. If you’re not already using variables in Postman, get ready to have your mind blown.

![image](https://user-images.githubusercontent.com/14041622/35851588-70ef05f6-0b63-11e8-9b9e-ffc0b3db7af5.png)






10 tips for working with Postman variables
Use variables in the request builder – use variables in the request builder anywhere text is used, such as the URL, URL parameters, headers, authorization, request body, and header presets. Postman uses string substitution to replace variable names enclosed in double curly braces – like {{variableName}} with its corresponding value as a global, collection, or environment variable.
For example, you can store access credentials or endpoint paths as variables. In this way, you can easily configure your setup to accommodate different users or server environments.






Dynamic variables – generate and use dynamic variables in the request builder as unique IDs, timestamps, or random integers. Use dynamic variables with the double curly braces syntax – like {{$timestamp}} – in the request URL / headers / body.


