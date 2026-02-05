from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import sys

load_dotenv()

client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

def readLogFile(filename):
    filepath = "assets/" + filename

    log = open(filepath, 'r')

    lines = log.readlines()
    linesNoEmptyStr = []

    for line in lines:
        if(len(line) == 1): continue
        linesNoEmptyStr.append(line)

    return linesNoEmptyStr

def joinStr(lines):
    output = ""
    for line in lines:
        output += line

    return output

def generateResponse(prompt):

    Permission = [
        "Permission for you: ",
        "1. You reader of log file and format it to json file, without interaction with user.",
    ]

    Format = [
        "You MUST answer in this format: ",
        "1. Json file format.",
        "2. Compliance PEP8!",
    ]

    Limit = [
        "You're limitations: ",
        "1. Nothing extra, just JSON with PEP8 Standart.",
    ]

    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        config = types.GenerateContentConfig(
                system_instruction = " ".join(Permission + Format + Limit)),
        contents = prompt
    )

    return response.text

if __name__ == '__main__':
    fileName = ""
    fileOutput = ""
    if len(sys.argv) < 2:
        raise ValueError('Usage: lab3.py assets/<logfile> [outputfile]')

    fileName = sys.argv[1]

    fileOutput = (sys.argv[2] if len(sys.argv) > 2 else 'output') + '.json'
    
    text = ""

    if len(fileName) > 0:
        text = generateResponse(joinStr(readLogFile(fileName)))

    output = open(fileOutput, 'w')

    output.write(text)






