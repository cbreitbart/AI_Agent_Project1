import ollama
import PyPDF2

# Open the PDF file
with open('symptoms.pdf', 'rb') as file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(file)
    
    # Initialize a variable to store the extracted text
    pdf_text = ""
    
    # Iterate through each page in the PDF
    for page in pdf_reader.pages:
        # Extract text from the page and add it to the pdf_text variable
        pdf_text += page.extract_text()

# Check if text was extracted
if pdf_text:
    print("Text extracted from PDF")
else:
    print("No text found in PDF")

prompt1 = f"{pdf_text} #### From this text extract possible causes of a fever "
# print("<Agent 1>: Prompt: " + prompt1)
#print()

print("<Agent 1> Generating response...")
print()

# Agent 1 - Extractor 
response_1 = ollama.chat(model='llama3', messages=[
    {
        "role": "user",
        "content": prompt1,
    }
])

# print(response_1["message"]["content"])

# Agent 2 - Interpreter
prompt2 = f"{response_1['message']['content']} #### Explain the possible causes to the user in a simple, clear and concise way. "

print("<Agent 2>: Prompt: " + prompt2)
print()

print("<Agent 2> Generating response...")

# Get response from Agent 2
response_2 = ollama.chat(model='llama3', messages=[
    {
        "role": "user",
        "content": prompt2,
    }
])

print("Agent 2 Response: " + response_2["message"]["content"])

