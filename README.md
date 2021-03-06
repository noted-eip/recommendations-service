# Recommandations Service

Service that'll permit to make natural language processing operations.

## Setup

### Git Submodules

First of all, if you just cloned the repo, initialize the git submodules : 

```bash
make init-submodules
```

Then update them :
```bash
make update-submodules
```

### Dependencies

In order to install NLP's and grpc's python dependencies, use the requirements.txt:

```bash
pip install -r requirements.txt
```

### Download language models (spacy)

Add the name of the `spacy`'s model to download in the `models_array` and run the script

```bash
models_array=("fr_dep_news_trf")
```

```bash
misc/download_languages.sh
```
## Run the service

```bash
python3 main.py
```

## Docker

The docker image uses [BuildKit](https://github.com/moby/buildkit)'s cache features. Since the `requirements.txt` and the language model download are quite long (~10 minutes all together), they're both cached.
In order to build the `recommendations-service` docker image use the Makefile rule:

```bash
DOCKER_BUILDKIT=1 make build 
```

or if you already activated BuildKit 

```
make build
```

Same for running

```bash
make run
```

By default the service runs on the port 3000.

## Configuration

| Env Name                             | Flag Name | Default | Description                                      |
| ------------------------------------ | --------- | ------- | ------------------------------------------------ |
| `RECOMMENDATIONS_SERVICE_PORT`        | -         | `3000`  | The port the application shall listen on.        |
| `RECOMMENDATIONS_SERVICE_MAX_WORKERS` | -         | `8`     | Number of threads the application should run on. |

Currently, one NLP algorithm is implemented (`YAKE!`, used to extract keywords), it's possible to configure it a bit with ENV variables.

| Env Name                                     | Flag Name | Default | Description                                                                 |
| -------------------------------------------- | --------- | ------- | --------------------------------------------------------------------------- |
| `RECOMMENDATIONS_SERVICE_CO_OCCURENCE_WINDOW` | -         | `3`     | A window (in words) for computing left/right contexts                       |
| `RECOMMENDATIONS_SERVICE_NUMBER_OF_KEYWORDS`  | -         | `5`     | Number of keywords that will be extracted from one text extraction request. |
| `RECOMMENDATIONS_SERVICE_N_GRAM_LENGTH`       | -         | `2`     | Length of candidate's sequence of words                                     |
| `RECOMMENDATIONS_SERVICE_THRESHOLD`           | -         | `0.75`  | Used to remove redudant results                                             |
| `RECOMMENDATIONS_SERVICE_LANG`                | -         | `fr`    | Used to tell the algorithm in which language we will run the service        |
