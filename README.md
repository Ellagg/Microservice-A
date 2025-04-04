# Microservice-A

Run generate_report.py by enter each line into the terminal: 
1. python -m venv .venv
2. .\\.venv\Scripts\activate
3. pip install requirements.txt
4. python generate_report.py

#### How to REQUEST data:
    Request the generate report endpoint and create a response variable to store the return.
    
    JSON Summary format for request:

        {
            "user_name":"Name",
            "report_period":"report,period"
            "total_income":<total income amount>,
            "total_expenses":<total expenses amount>,
            "savings_goal":<savings goal amount>,
            "progress_to_goal":<progress to goal amount>,
            "detailed_transactions": [
                {"date":<date>, "category":"category name", "amount":<transaction amount>, "description":"transaction description"}
                {"date":<date>, "category":"category name", "amount":<transaction amount>, "description":"transaction description"}
                ...
                {"date":<date>, "category":"category name", "amount":<transaction amount, "description":"transaction description"}
            ] 

        }

    
##### Example Call:

    response = requests.get("http://localhost:2000/generate-pdf")

Important Note:
generate_report.py assumes the JSON endpoint has the URL "http://localhost:3000/api/export-summary". If this is not the case, then the microservice will fail. 
    
#### How to RECIEVE data:
The budget report will return binary data for the pdf so the recieving server needs to read this and save it as a PDF file. The request example call stores the return value of generate_report.py in a variable called request. Use this to interact with the pdf data.

##### Example Call:

    with open("budget_summary.pdf", "wb") as file:
        file.write(response.content)

#### UML Sequence Diagram:

![alt text](<UML 2.png>)