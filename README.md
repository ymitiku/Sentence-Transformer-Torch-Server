# Scripts to deploy Sentence tranformer model
This repository contains scripts to deploy sentence transformer model located [here](https://www.kaggle.com/skylord/coronawhy?select=sentence_transformer_nli) under `sentence_transformer_nli` folder. Sentence transformer saves model checkpoints inside folders. At the time of writing these scripts, [torch-serve](https://pytorch.org/serve/) does not support folder for extra files. This repository is intended to create command to deploy sentence transformer model using torch-serve. 
## How does it work?
First the scripts are used to add  `bert_` prefix for files inside `0_BERT` folder and prefix `pooling` for files inside `1_Pooling` folder. Then this prefix is used to move the files to respective folder dynamically at runtime inside. Moving the files has been handling inside [handler.py](handler.py)

One may follow the following steps to deploy the sentence transformer model. 
## Step 1 - Coverting folder structure
Since torch-serve creates working directory dynamically at runtime and there is no way to add extra folder in the command argument of `torch-model-archiver`, it is reqiured to follow some unconventional way to deploy sentence transformer. One possible way is to mark files of each folder with some identifier. This steps converts names of model-results files to required format. 

```bash
python transform_files.py --path model_results

```
The `path` argument should be respective folder of `model_results` folder located at [here](https://www.kaggle.com/skylord/coronawhy?select=sentence_transformer_nli) under `sentence_transformer_nli` folder.

## Step 2 Building command for torch-archive-model
The following script can be used to create a command to run `torch-model-archiver` program.

```bash
python build_archive_command.py;
```

## Step 3 Registering model
The following scripts can be used to register the model 
```bash
chmod +x archive-command.sh;
./archive-command.sh;
mkdir -p  model_store;
mv bert.mar model_store/;
```

## Step 4 Starting the server
Once all the above steps are followed correctly, all files required to deploy sentence transformer model are being created. The following script can be used to start the torch-serve server.
```bash
torchserve --start --model-store model_store --models bert=bert.mar;
```


## Testing the server
```
curl -X POST http://127.0.0.1:8080/predictions/bert -T hello.txt
```