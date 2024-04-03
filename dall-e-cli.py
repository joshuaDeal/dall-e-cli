#!/usr/bin/env python3

import sys
import re
import base64
import os

# see https://platform.openai.com/docs/guides/images/introduction

from openai import OpenAI

# Print help message
def printHelp():
	print(sys.argv[0])
	print("Usage:  " + sys.argv[0], "--[option]")
	print("Options:")
	print("\t--help\t\t\tDisplay this help message.")
	print("\t--prompt \"prompt\"\tSpecify the prompt.")
	print("\t--model <model>\t\tSpecify what model to use.")
	print("\t--size <size>\t\tSpecify image size.")
	print("\t--quality <quality>\tSpecify image quality.")
	print("\t--output <file name>\tSpecify where to save the image.")


# Takes details as input. Returns image in base64 format
def generateImage(userPrompt,imgModel,imgSize,imgQuality):
	# Check inputs
	# Make sure userPrompt is a string
	if type(userPrompt) != str:
		print("Error: userPrompt should be str")
		return 0
	# Make sure imgModel is a string
	elif type(imgModel) != str:
		print("Error: model should be str")
		return 0
	# Make sure imgModel is a valid model
	elif imgModel != "dall-e-2" and imgModel != "dall-e-3":
		print("Error: model should be 'dall-e-2' or 'dall-e-3'")
		return 0
	# Make sure imgSize is a sting
	elif type(imgSize) != str:
		print("Error: size should be str")
		return 0
	# Make sure imgSize is a valid size
	elif imgSize != '1024x1024' and imgSize != '1024x1792' and imgSize != '1792x1024':
		print("Error: size should be '1024x1024', '1024x1792', or '1792x1024'")
		return 0
	# Make sure imgQuality is a string
	elif type(imgQuality) != str:
		print("Error: quality should be str")
		return 0
	# Make sure imgQuality is valid
	elif imgQuality != 'standard' and imgQuality != 'hd':
		print("Error: quality should be 'standard' or 'hd'")
		return 0

	client = OpenAI()

	# Send request to api	
	response = client.images.generate(model=imgModel, prompt=userPrompt, size=imgSize, quality=imgQuality, n=1, response_format="b64_json")
	
	# Regular expression pattern to match base64 data
	pattern = re.compile(r'([A-Za-z0-9+/]+={0,2})')
	# Find the base64 encoded image data
	image64 = re.findall(pattern, str(response.data[0]))[3]

	return image64

# Decodes base64 and saves the output to a file
def saveImage(content64, fileName):
	# Decode data
	decoded = base64.b64decode(content64)

	# Write data to file
	with open(fileName, 'wb') as file:
		file.write(decoded)

def main():
	# Some default values
	model = "dall-e-2"
	size = "1024x1024"
	quality = "standard"
	fileName = "dalle-image.png"

	# Evaluate options and arguments
	for i in range(len(sys.argv)):
		# Check for -h
		if sys.argv[i] == '--help' or sys.argv[i] == '-h':
			printHelp()
			sys.exit()
		# Get prompt
		elif sys.argv[i] == '--prompt' or sys.argv[i] == '-p':
			prompt = sys.argv[i+1]
		# Get model
		elif sys.argv[i] == '--model' or sys.argv[i] == '-m':
			model = sys.argv[i+1]
		# Get size
		elif sys.argv[i] == '--size' or sys.argv[i] == '-s':
			size = sys.argv[i+1]
		# Get quality
		elif sys.argv[i] == '--quality' or sys.argv[i] == '-q':
			quality = sys.argv[i+1]
		# Get file name
		elif sys.argv[i] == '--output' or sys.argv[i] == '-o':
			fileName = sys.argv[i+1]

	# Make sure that we aren't overwriting a preexisting file
	if os.path.exists(fileName):
		print("Warning: file \"" + fileName + "\" already exists.")
	else:
		saveImage(generateImage(prompt, model, size, quality), fileName)

if __name__ == "__main()__":
	main()
