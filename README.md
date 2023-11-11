# AI-ChatBot

This project implements a simple chatbot using Keras with a pre-trained model. The chatbot is trained on a dataset of intents and responses. The model predicts the intent of user input and generates an appropriate response.

## Overview

This chatbot script uses a neural network model (`chatbot_model.h5`), a tokenizer (`Tokenizer.p`), and a label encoder (`LabelEncoder.p`) to understand user input and generate responses. The model is trained on a dataset of intents and responses provided in the `intents.json` file.

## Prerequisites

- Python 3.x
- Required Python packages: Keras, pandas, numpy

## Installation

1. Clone the repository:

   ```
   https://github.com/shukur-alom/AI-ChatBot.git
   ```
2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Run the chatbot script:

```
python chatbot.py
```
