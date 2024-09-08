# Steganography Programming Challenge

This repo corresponds to a short Engineering Projects in Community Service (EPICS) skill session I gave at Arizona State University in September of 2024.

# Requirements

- A modern installation of Python 3 (Later is better)
- Python image library (PIL) `pip install pillow`
- Numpy `pip install numpy`

Note, you can install both of these libraries with the `requirements.txt` file in the repo by running `pip install -r requirements.txt`.

## The Challenge

This repo contains a `main.py` script that embeds a simple ASCII message into a source image located in the repo at `./images/source.bmp`. 

You can run the script to embed your own message, but the message to recover for the challenge is located in `challenge.bmp`. The image is a picture of a dog. You are to recover the following information based on the embedding procedure defined in `main.py`:
    - What is the dog's name
    - How old is the dog?
    - Where does the dog live?

Here is the challenge image:
[![Challenge Image](./images/challenge.bmp)](./images/challenge.bmp)

Steganography is very fragile so you should work with this image by cloning this repo directly and not downloading the image from this README.