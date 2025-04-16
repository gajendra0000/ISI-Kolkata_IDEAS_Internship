import pandas as pd
import ollama
import datetime
import json

# Function to parse the JSON output and extract relevant features
def parse_json(json_output):
    # Load the JSON response as a Python object (list of dictionaries)
    parsed_data = json.loads(json_output)

    # Assuming the response is a list with a single dictionary, extract the features
    if isinstance(parsed_data, list) and len(parsed_data) > 0:
        parsed_data = parsed_data[0]

    # Return the features as a dictionary
    return {
        "Agent Name": parsed_data.get("Agent Name", None),
        "Customer Name": parsed_data.get("Customer Name", None),
        "Company Name": parsed_data.get("Company Name", None),
        "Product Inquiry": parsed_data.get("Product Inquiry", 0),
        "Service Inquiry": parsed_data.get("Service Inquiry", 0),
        "Return Inquiry": parsed_data.get("Return Inquiry", 0),
        "Refund Inquiry": parsed_data.get("Refund Inquiry", 0),
        "Technical Support Inquiry": parsed_data.get("Technical Support Inquiry", 0),
        "Quality Issue": parsed_data.get("Quality Issue", 0),
        "Trust Issue": parsed_data.get("Trust Issue", 0),
        "Pricing Issue": parsed_data.get("Pricing Issue", 0),
        "Sizing Issue": parsed_data.get("Sizing Issue", 0),
        "Delivery Issue": parsed_data.get("Delivery Issue", 0),
        "Other Issues": parsed_data.get("Other Issues", 0),
        "Product Information": parsed_data.get("Product Information", 0),
        "Discount Offer": parsed_data.get("Discount Offer", 0),
        "Customer Testimonials": parsed_data.get("Customer Testimonials", 0),
        "Escalation to a Manager": parsed_data.get("Escalation to a Manager", 0),
        "Tone of the Agent": parsed_data.get("Tone of the Agent", None),
        "Tone of the Customer": parsed_data.get("Tone of the Customer", None),
        "Customer Sentiment": parsed_data.get("Customer Sentiment", None),
        "Agent Sentiment": parsed_data.get("Agent Sentiment", None),
        "Requested Sensitive Information": parsed_data.get("Requested Sensitive Information", 0),
        "Adhered to Regulatory Standards": parsed_data.get("Adhered to Regulatory Standards", 0),
        "Total Turns": parsed_data.get("Total Turns", 0),
        "Total Word Count": parsed_data.get("Total Word Count", 0),
        "Agent Word Count": parsed_data.get("Agent Word Count", 0),
        "Customer Word Count": parsed_data.get("Customer Word Count", 0),
        "Total Questions Asked": parsed_data.get("Total Questions Asked", 0),
        "Agent Questions Asked": parsed_data.get("Agent Questions Asked", 0),
        "Customer Questions Asked": parsed_data.get("Customer Questions Asked", 0),
        "Positive Word Count": parsed_data.get("Positive Word Count", 0),
        "Negative Word Count": parsed_data.get("Negative Word Count", 0),
        "Resolution_Status": parsed_data.get("Resolution_Status", 0),
        "speech_ratio": parsed_data.get("speech_ratio", 0.0),
        "Engagement_Score": parsed_data.get("Engagement_Score", 0.0),
        "Discount_Impact_Score": parsed_data.get("Discount_Impact_Score", 0),
        "Fraudulent_Activity": parsed_data.get("Fraudulent_Activity", 0)
    }

# Load your input Excel file with the 'Transcript' column
input_df = pd.read_excel('input_transcript.xlsx')

# Prepare the output dataframe (with the same columns as before)
output_df = pd.DataFrame(columns=[
    "Agent Name", "Customer Name", "Company Name", "Product Inquiry", "Service Inquiry", 
    "Return Inquiry", "Refund Inquiry", "Technical Support Inquiry", "Quality Issue", 
    "Trust Issue", "Pricing Issue", "Sizing Issue", "Delivery Issue", "Other Issues", 
    "Product Information", "Discount Offer", "Customer Testimonials", "Escalation to a Manager", 
    "Tone of the Agent", "Tone of the Customer", "Customer Sentiment", "Agent Sentiment", 
    "Requested Sensitive Information", "Adhered to Regulatory Standards", "Total Turns", 
    "Total Word Count", "Agent Word Count", "Customer Word Count", "Total Questions Asked", 
    "Agent Questions Asked", "Customer Questions Asked", "Positive Word Count", 
    "Negative Word Count", "Resolution_Status", "speech_ratio", "Engagement_Score", 
    "Discount_Impact_Score", "Fraudulent_Activity"
])

print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - Starting...")

# Process only the first transcript (index 0)
row = input_df.iloc[0]  # Get the first row (first transcript)
sample_transcript = row['Transcript']

# Define the prompt
prompt = """You are a highly detailed and structured data extraction tool specializing in analyzing customer service call transcripts. Your task is to meticulously parse a provided transcript and generate a JSON formatted output consistent with the following template. Each JSON object should represent a single turn in the conversation, capturing relevant information. Follow a strict, standardized format - this template is crucial, for consistent data analysis. Here is the template for each JSON object: Agent Name: String - The name of the agent who spoke. Customer Name: String - The name of the customer. If null, set to null. Company Name: String - The name of the company. If null, set to null. Product Inquiry: Integer - 1 if the product-related inquiry is made else 0. Service Inquiry: Integer - 1 if service-related inquiry is made else 0. Return Inquiry: Integer - The number representing the return-related inquiry is made else 0. Refund Inquiry: Integer - The number representing the refund-related inquiry is made else 0. Technical Support Inquiry: Integer - The number representing the technical support inquiry. Quality Issue: Integer - The number representing the quality issue is made else 0. Trust Issue: Integer - The number representing the trust issue is made else 0. Pricing Issue: Integer - The number representing the pricing issue is made else 0. Sizing Issue: Integer - The number representing the sizing issue is made else 0. Delivery Issue: Integer - The number representing the delivery issue is made else 0. Other Issues: Integer - The number representing the other issue is made else 0. Product Information: Integer - 1 if product or service info is given else 0. Discount Offer: Integer - 1 if discount offer is given else 0. Customer Testimonials: Integer - 1 if customer testimonials is given by agent else 0. Escalation to a Manager: Integer - 1 if agent escalated the issue to a manager else 0. Tone of the Agent: String - Choose Among (Professional, Sales-Oriented, Apologetic, or Neutral). Tone of the Customer: String - Choose Among (Neutral, Skeptical, Frustrated, or Interested). Customer Sentiment: String - Choose Among (Positive, Neutral, or Negative). Agent Sentiment: String - Choose Among (Positive, Neutral, or Negative). Requested Sensitive Information: Integer - 1 if request for sensitive info made by agent else 0. Adhered to Regulatory Standards: Integer - 1 if agent adhere to regulatory standard else 0. Total Turns: Integer - The number of turns in the conversation. Total Word Count: Integer - The number of words in the conversation. Agent Word Count: Integer - The number of words in the agent's statement. Customer Word Count: Integer - The number of words in the customer's statement. Total Questions Asked: Integer - The number of questions asked. Agent Questions Asked: Integer - The number of questions asked. Customer Questions Asked: Integer - The number of questions asked. Positive Word Count: Integer - The number of positive words in the conversation. Negative Word Count: Integer - The number of negative words in the conversation. Resolution_Status: Integer - 1 if Customer issue resolved else 0. speech_ratio: Float - Agent Questions Asked / Customer Questions Asked. Engagement_Score: Float - 0.4 Total Turn + 0.6 Total Questions Asked. Discount_Impact_Score: Integer - Discount Offered * Resolution Status and last one is Fraudulent_Activity: Integer - 1 if call sounds fraudulent else 0. Now, please generate the JSON output exactly as described. Do not change anything - strictly adhere to the template."""

# Generate the full prompt for the first transcript
full_prompt = prompt + sample_transcript + "\n\nNow generate only the JSON and nothing else :"

# Call the Ollama API to process the first transcript
response = ollama.chat(
    model="llama3.2:latest",
    messages=[{"role": "user", "content": full_prompt}]
)

# Get the JSON output from the response
json_output = response["message"]["content"]

# Parse the JSON response using the parse_json function
features = parse_json(json_output)

# Append the features to the output dataframe using concat 
output_df = pd.concat([output_df, pd.DataFrame([features])], ignore_index=True)


# Save the output DataFrame to an Excel file
output_df.to_excel('output_transcript_first.xlsx', index=False)

print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - Processing complete for first transcript. Output saved to 'output_transcript_first.xlsx'.")

