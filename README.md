# Autonomous SQA

**Software quality assurance (SQA) aims to make sure that software behaves as expected.  Autonomous SQA strives to automate the testing process to reduce time and improve the accuracy and repeatability of testcases.**  

### Risk-based approach
Software is complex.  The environment where software operates has many unexpected challenges.  You may be testing a busy streaming video website or flight control systems that fly airplanes or a popular social media app or a security system or an autonomous vehicle or many other types of software.  First, consider the risks that your software will encounter.  Make a list of risks in a risk register.  Evaluate each risk.  Think about how often the risky situation occurs.  Consider how big the problem will be if the risk does occur.  Look at how easy it is to discover the risky situation.  Rank each risk so you can tackle the biggest risks first.  Think about how you can prevent or deal with these risks.  This is called risk mitigation.  Develop a plan to mitigate each risk.  You may be able to prevent the risk from occurring by testing the code involved.  Perhaps you can buy insurance to take care in case the risk occurs.  Perhaps you can train the people who use the software.  The process described here is a "risk-based approach" to software quality assurance.  

### Preventing software risks by testing
One way to deal with risks, is to test the software by entering valid and invalid or unexpected input.  You do this by creating testcases.  Testcases help find bugs so developers can fix them.    You repeat the tests until you prove that the software behaves as expected in situation being tested by the testcase.  It may take several tries before all the software bugs are fixed, so autonomating the tests is faster and more accurate than repeating manual checks.

### Using Python and Selenium to automate software testcases
You can use Python and Selenium to control each step of a testcase and report results.  Here are some simple examples to get started:

[Simple script to automate testing web input forms](01-generic_web_input_form.md)

[Using the Page Object Model design pattern to test web input forms](02-generic-pom-tests.md)

[Simple script that automates testing the I3 Marketplace login](03_simple_web_input_form.md)

[Using the Page Object Model design pattern to automate I3 login tests](04-pom-tests.md)


