# GPT-3 Model fine-tuning workflow -- Word to JSON

### Orgainize and convert Word to .txt
- gather .doc and .docx files place in a folder called inputs
- run the following code in the terminal in the root folder containing the inputs folder
`textutil -convert txt filepath/*.doc`


### run a python script to push the contents of the .txt files to a .csv (JSON still pending)
`python3 .txt2csv.py`


### csv to json??
tbd


### Run the training on Google Colab
- upload the json file to your Google Drive
- run this colab: https://colab.research.google.com/github/wandb/examples/blob/master/colabs/openai/Generate_Doctor_Who_Synopses_with_GPT_3_and_Weights_%26_Biases(video).ipynb#scrollTo=hE0mWHRh3iuZ 
- use the .jsonl in the frontend 