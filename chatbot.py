from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Simple intent matcher
def get_response(user_input):
    """
    Analyzes user input and returns a canned response.
    This function uses simple keyword matching.
    """
    user_input = user_input.lower()

    if "health" in user_input:
        # Fixed the multi-line string syntax
        return "Health insurance is a financial safety net that covers medical expenses due to illness, injury, or hospitalization. Key Highlights: - Coverage: Doctor visits, hospital stays, surgeries, medicines. - Payment: You pay a premium (monthly/yearly); insurer pays your medical bills. - Types: Individual, family floater, critical illness, group plans. - Claims: Can be cashless (direct payment to hospital) or reimbursement. - Bonus: No-claim years often earn you extra coverage or discounts."

    elif "car" in user_input or "vehicle" in user_input:
        return "Car insurance protects your vehicle against accidents, theft, and damage."
    
    # Re-ordered conditions for better logic
    elif "process" in user_input or "claim" in user_input or "endorsement" in user_input:
        if "policy inwarding" in user_input:
            # Re-phrased to avoid multiple identical checks
            return "If you are issuing a policy through IPDS V2, you do not require any documents. Just select the quote finalized by the client/producer and proceed to issue with the payment details. Let me know if you want to go through the non-rater or manual process."
        elif "non-rater" in user_input or "manual" in user_input:
            # Fixed the multi-line string syntax
            return "Although this process is a bit time consuming, lets do it. First you need to collect the requirements like a quotation approved by the underwriter, a proposal form, payment details, and KYC details. Now you need to select the product in IPDS V2 like Home, AIGC, Marine etc. Click on the rater option, fill in client details like name, address, contact etc. Upload the documents like UW approval, GST and payment details, and push the case to COPS for policy issuance. Don't forget to keep a track of the status until the policy gets issued."
        elif "endorsement" in user_input:
            return "Few endorsements can be processed directly through IPDS V2, while others can be processed via non-rater. Shall we proceed with a non-rater endorsement?"
        elif "yes proceed" in user_input or "proceed" in user_input:
            return "Go to the CL endorsement and select the type of endorsement and proceed as per the steps."
    
    elif "saira" in user_input:
        # A more specific check would be ideal to avoid conflicts
        return "Saira's husband is Sadique."

    elif "marine" in user_input or "marine insurance" in user_input:
        # Fixed the multi-line string syntax
        return "Marine insurance is a contract that protects goods, ships, and cargo during transit—whether by sea, air, or land—from risks like damage, theft, or accidents. Key Points: - Covers: Ships, cargo, terminals, and transport vehicles. - Purpose: Ensures financial compensation for losses during transit. - Types: Cargo insurance, hull insurance (for ships), freight insurance. - Used by: Exporters, importers, shipping companies, and logistics providers."

    else:
        return "I am getting trained now hence i am not able to undersand this query , lets try another question?"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    # Correctly handle JSON data from the front end
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"reply": "Invalid request. Please provide a message."}), 400
    
    response = get_response(user_input)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
