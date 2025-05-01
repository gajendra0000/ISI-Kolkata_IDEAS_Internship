# Building an AI System for Identifying Fraudulent Sales Calls
This project introduces an AI-powered fraud detection pipeline that analyzes raw sales call transcripts to extract business-relevant features and detect fraudulent behavior. Leveraging Large Language Models (LLMs), specifically LLaMA 3.2 interfaced through Ollama, the system transforms unstructured textual data into a structured featured dataset. Python automates the entire feature extraction and model inference process, while Power BI visualizes insights such as fraud patterns, suspicious agent behavior, and red-flag conversations. The solution is lightweight, open-source, and customizable, offering high adaptability across domains.
Automated Feature Extraction: Design a system that can parse and process raw sales call transcripts to identify key indicators relevant to fraud.
Contextual Understanding: Leverage LLaMA 3.2, a state-of-the-art open-source large language model, to interpret the nuanced context of sales conversations.
Structuring Unstructured Data: Convert raw conversational text into a structured format with measurable features like sentiment, red flag indicators, and potential fraud scores.
Visualization and Reporting: Create intuitive Power BI dashboards to help sales managers and compliance teams monitor and assess potential fraudulent activity.
# Technologies Used:
## Python (.py)-
Used for scripting automation of the entire pipeline.
Responsible for reading raw transcript files, cleaning text, generating prompts, sending prompts to the LLM, and saving structured outputs.
## Excel-
Acts as both the input and output format.
Raw call transcripts are stored in tabular form.
Output files contain the featured dataset with fraud detection indicators.
## Ollama-
Lightweight runtime interface for running LLaMA locally.
Enables quick model loading and inference without relying on cloud APIs or GPU clusters.
Helps integrate the LLM into local or on-premise enterprise environments.
## LLaMA 3.2:latest-
A powerful open-source transformer model known for its ability to understand language context.
Extracts red flags, misleading sales tactics, and customer sentiment from call transcripts.
Responds to prompts by summarizing intent, highlighting unethical behavior, and classifying content.
## Prompt Engineering-
Prompts guide the LLM to extract relevant features (e.g., “Identify if any statements in this transcript contain exaggerated promises.”)
Fine-tuned to elicit accurate and structured outputs from the model.
## Power BI-
Transforms the structured output into visual insights.
Allows stakeholders to explore metrics such as:
Fraud detection trends over time.
Agent-specific risk dashboards.
Frequently used flagged phrases.
Correlation between call length and fraud risk.
## workflow:![image alt](![image](https://github.com/user-attachments/assets/12f2d9e4-ca68-425f-8fab-2d600611b5cc)
# Methodology:
1. Input: Raw Call Transcripts
    An Excel file where each row represents a sales call.
2. Automated Feature Extraction (Python Script)
   A Python automation script processes the transcript dataset and extracts key business intelligence and compliance-related features using two sets of carefully 
   crafted prompts:
   Tech: Python + pandas/numpy
3. Model Execution via Ollama + LLaMA 3.2
   LLaMA 3.2 is used as the Natural Language Processing (NLP) engine to analyze raw sales call transcripts and extract structured business-related and fraud- 
   detection features.The integration of LLaMA is accomplished through prompt engineering and local API deployment via Ollama,The prompt is sent to the LLaMA 3.2 
   model using the Ollama API locally.
 4. Output: Featured Dataset
 5. The model’s output is parsed and structured into a feature-rich Excel dataset, with over 35+ features classified into:
    Boolean (e.g., Fraudulent Activity, Trust Issue)
    Categorical (e.g., Sentiment labels)
    Numeric (e.g., Word Counts, Speech Ratio)
 6.Results and Analysis
  Sentiment Analysis-Fraud calls have higher negative sentiment for both agents and customers
  Speech Ratio-Agents speak less; customers speak more in fraud calls
  Tone-Agents maintain a professional tone; customers often appear skeptical
  Engagement-Fraud calls have higher back-and-forth exchanges, turns, and total word count
  Compliance-86% of fraud calls violate security protocols
  Offers/Testimonial-Rare in fraud calls; fraud agents tend to ask more and offer less









