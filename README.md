# Bob, Payroll Compliance Bot 🤖

### Meet Bob, an AI chatbot that automates the payroll compliance process, making sure that employees are not underpaid 🚀

## How it works ✨
![Bobby-Gif](bob.gif)


#### Features:
- Upload payroll data in CSV format (PDF coming soon!)
- Ask questions about your payroll data, such as differences between actual and expected salary
- Check if your payroll data adheres to [Australian Fairwork Award legislation](https://www.fairwork.gov.au/)

## Running Locally 💻
Follow these steps to set up and run the service locally:

### Prerequisites
- Python 3.11 
- Git
- OpenAI API Keys

### Installation
Clone the repository :

`git clone https://github.com/ivan-pua/Payroll-Compliance-Bot.git`


Create a virtual environment with your preferred Python package manager:
```bash
conda create -n [YOUR ENV NAME] python=3.11
```

Install the required dependencies in the virtual environment :

`pip install -r requirements.txt`


Launch the chat service locally :

`streamlit run src/Home.py`

#### That's it! The service is now up and running locally. 🤗

## Contributing 🙌
Your feedback is welcomed! If you want to contribute to this project, please open an issue, submit a pull request. 

## Credits 
Massive thank you to Yvann for creating an open source [Robby-chatbot](https://github.com/yvann-hub/Robby-chatbot) repo. Also, check out his medium article 🖖 : [Build a chat-bot over your CSV data](https://medium.com/@yvann-hub/build-a-chatbot-on-your-csv-data-with-langchain-and-openai-ed121f85f0cd)

