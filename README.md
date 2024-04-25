# Dall-E-cli
A simple python script for interfacing with dall-e-2 or dall-e-3 in the command line.

## Usage
`dall-e-cli.py --help`

```
dall-e-cli.py
Usage:  dall-e-cli.py --[option]
Options:
        --help                  Display this help message.
        --prompt "prompt"       Specify the prompt.
        --model <model>         Specify what model to use.
        --size <size>           Specify image size.
        --quality <quality>     Specify image quality.
        --output <file name>    Specify where to save the image.
```
### Examples
Try running `dall-e-cli.py -p "Anime style. A young female programmer testing her code for bugs." -o ./output.png -m dall-e-3`
The program will wait for a short period of time and after it finishes a new file called "output.png" will be created in the working directory.
The resulting image should look something like the following.
<img src="./example-images/example01.png" alt="This image is an example.">

## Dependencies
The following are dependencies that you may need to install.
- openai

## Installation / Configuration
### Installation
1. Clone this git repository.

	`git clone https://github.com/joshuadeal/dall-e-cli`

1. Change to repository directory.

	`cd ./dall-e-cli/`

1. Install dependencies.

	`python -m pip install -r ./requires.txt`

### Configuration
1. You'll need to set up the OPENAI_API_KEY evnironmental variable.

   1. `echo "export OPENAI_API_KEY='put your api key here'" >> ~/.bashrc"`
   1. `source ~/.bashrc`

   To test if this has been done correctly run ```echo $OPENAI_API_KEY```. The output should be your API key.
