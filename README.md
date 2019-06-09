# rest_api_tutorial

Code without tests is broken as designed. — Jacob Kaplan-Moss

In software development, testing is paramount. So why should I do it, you ask?

Tests have a short feedback loop, enabling you and your team to learn faster and adjust
Less time is spent debugging, allowing you to spend more time writing code
Tests act as documentation for your code!
They improve code quality while reducing bugs
After refactoring code, your tests will tell you whether the change has broken previously working code, and...
*Tests can prevent your hair line from receding! *
Table of Contents
A Bucketlist
Django Rest Framework
Creating the Rest API app
Let The Coding Begin
Serializers
Views
Handling Urls
Let's Run!
Reading, Updating and Deletion
Wrapping it up
Conclusion
The best way to do code testing is by using Test-Driven Development (TDD).

This is how it works:

Write a test. – The test will flesh out some functionality in your app
Then, run the test – The test should fail, since there's no code to make it pass.
Write the code – To make the test pass
Run the test – If it passes, you are confident that the code you've written meets the test requirements
Refactor code – Remove duplication, prune large objects and make the code more readable. Re-run the tests every time you refactor the code
Repeat – That's it!
Being a fan of best practices, we are going to use TDD to create a bucketlist API. The API will have CRUD (Create, Read, Update, Delete) and authentication capabilities. Let's get to it then!