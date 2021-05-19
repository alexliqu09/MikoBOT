import random
import json
import torch
from model import Net
from utils import DataProcess

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

with open("../MIKOBOT/intents.json", "r", encoding="utf-8") as f:
    intents = json.load(f)

FILE ="data.pth"
data = torch.load(FILE)
preprocess_dataset = DataProcess()

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["ouput_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]
model = Net(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()


def chat(sentece):
    bot_name = "Miko"
    sentence = preprocess_dataset.tokenize(sentece)
    x = preprocess_dataset.bag_word(sentence, all_words)
    x = x.reshape(1, x.shape[0])
    x = torch.from_numpy(x).to(device)
    x = x.float()
    output = model(x)
    _,predictions = torch.max(output,dim=1)
    tag = tags[predictions.item()]

    probs = torch.softmax(output,dim=1)
    prob = probs[0][predictions.item()]

    if prob.item()>0.65:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                return f"{bot_name}: { random.choice(intent['responses'])}"
    else:
        return f"{bot_name}: Aun estoy aprendiendo su lenguaje..."

