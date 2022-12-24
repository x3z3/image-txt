# image-txt
Encoder and Decoder to convert an image into text.

## Working of System

### 1. Encoder

Name the image that you want to encode as sample.jpg (or rename the original file in encoder.py). Run the program, and wait for it to produce the encoded.txt file. The program also produces a sample_encoded.jpg file which is a downscaled version of the original image.

### 2. Fragmenter

Breaks the encoded.txt file into fragments of max size. Edit the max char length in the fragmenter.py file. Add a buffer to potentially add some headerfile information (Next TODO).

### 3. Networking

Send the fragments across the network of your preferred choice.

### 4. Aggregator

Joins the fragmented files in serial order from the fragments folder into a single file to be able to be decoded. Produces a file called aggregated.txt.

### 5. Decoder

Make sure you have the aggregated.txt file in same directory as decoder.py. Run the program, and wait for the sample_decoded.jpg to be produced. (Alternatively, the file can be renamed to have any encoded file)

## Motivation

Imagine finding yourself in a flight where you can send unlimited text messages through social media apps, but you aren't allowed to send images. This image encoder can help you break your image into a series of text messages (which you could send through the app) which can finally be decoded to convert the text messages back into the original image.