from flask import Flask, jsonify, request, send_file
import requests
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

app = Flask(__name__)

# External API endpoint
API_URL = "http://localhost:3000/api/export-summary"

@app.route("/generate-pdf", methods=["GET"])
def generate_pdf():
    try:
        # Fetch JSON data from the external API
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()

        # Create a PDF in memory
        buffer = io.BytesIO()
        pdf = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter

        y_position = height - 50

        # Set title
        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawString(200, y_position, "Budget Summary Report")
        y_position -= 20

        pdf.setFont("Helvetica", 12)
         # Add basic user info and summary
        pdf.drawString(50, y_position, f"User: {data.get('user_name', 'N/A')}")
        y_position -= 20
        pdf.drawString(50, y_position, f"Report Period: {data.get('report_period', 'N/A')}")
        y_position -= 20
        pdf.drawString(50, y_position, f"Total Income: ${data.get('total_income', 0)}")
        y_position -= 20
        pdf.drawString(50, y_position, f"Total Expenses: ${data.get('total_expenses', 0)}")
        y_position -= 20
        pdf.drawString(50, y_position, f"Savings Goal: ${data.get('savings_goal', 0)}")
        y_position -= 20
        pdf.drawString(50, y_position, f"Net Savings: ${data.get('net_savings', 0)}")
        y_position -= 20
        pdf.drawString(50, y_position, f"Progress to Goal: ${data.get('progress_to_goal', 0)}")
        y_position -= 40

        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(50, y_position, "Detailed Transactions:")
        y_position -= 20

        pdf.setFont("Helvetica", 12)
        for transaction in data.get("detailed_transactions", []):
            pdf.drawString(60, y_position, f"Date: {transaction.get('date', 'N/A')}")
            y_position -= 20
            pdf.drawString(60, y_position, f"Category: {transaction.get('category', 'N/A')}")
            y_position -= 20
            pdf.drawString(60, y_position, f"Amount: ${transaction.get('amount', 0)}")
            y_position -= 20
            pdf.drawString(60, y_position, f"Description: {transaction.get('description', 'N/A')}")
            y_position -= 40

            if y_position < 50:  # Create a new page if needed
                pdf.showPage()
                pdf.setFont("Helvetica", 10)
                y_position = height - 50

        # Save and return PDF
        pdf.save()
        buffer.seek(0)
        return send_file(buffer, as_attachment=True, download_name="budget_summary.pdf", mimetype="application/pdf")

    except requests.RequestException as e:
        return jsonify({"error": "Failed to fetch data", "details": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(port = 2000, debug=True)

