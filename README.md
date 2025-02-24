# Microservice-A
Microservice A implemented for Software Engineering I course

README must contain...
o	Clear instructions for how to programmatically REQUEST data from the microservice you implemented. Include an example call. Do not advise your teammate to use your test program or require them to, your teammate must write all of their own code.
o	Clear instructions for how to programmatically RECEIVE data from the microservice you implemented. Include an example call.
o	UML sequence diagram showing how requesting and receiving data works. Make it detailed enough that your teammate (and your grader) will understand.

How to REQUEST data:
    Open the budget_report.txt file and write the budget report information to it in the following
    format:
    ---------------------------------------------------------
    directory to place pdf
    Monthly Expenses:
    Expense 1
    Expense 2
    Expense 3
    ...
    Expense n
    ###
    income
    savings goal
    distance from savings goal
    ---------------------------------------------------------

    Example Call:
    ---------------------------------------------------------
    budget_report
    Monthly Expenses:
    50.00
    10.00
    750.00
    40.00
    ###
    5000.00
    1000.00
    300.00
    ---------------------------------------------------------

How to RECIEVE data:
    The budget report will create a pdf in the specified directory. Then it will read the rest
    of the text file and write that information to the pdf. Once this is done, the microserivce
    will overwrite the information in the text file with "###complete###". Then the user can
    navigate to the directory and access the pdf file. The main program will know the microservice
    has completed by reading the text file and the first line being "###complete###".

    
