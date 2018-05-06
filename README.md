# Realtime speech keyword parsing for Cook-Health
Converts speech to text in real time through Google's Speech to Text NN.
Then uses heuristics to identify the most relevant keywords for display
in the Cook-Health UI.

# Usage
First have the python 3 and portaudio development libraries installed
```
> sudo apt update && sudo apt install python-all-dev portaudio19-dev
```
Clone the repository with
```
git clone https://github.com/cook-health/keywords.git
```

Then create a virutal environment to keep everything organized
```
cd keywords
virtualenv env
```

Install the dependencies
```
pip install -r requirements.txt
```

Download a service key for Google cloud Speech Transcriber and place the .json 
credential files in the keywod directory. Then set ```GOOGLE_APPLICATION_CREDENTIALS``` to the
file path.
```
GOOGLE_APPLICATION_CREDENTIALS="./gcloud.json"
```
Run the keyword service with
```
python speech.py
```
