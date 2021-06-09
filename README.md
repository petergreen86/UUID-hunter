# Hub UUID Hunter

This tool is designed to pull the component origins out of a particular project versions BOM for the KB team

## Setup

```
pip3 install -r requirements.txt
```


## Usage

Create a file called `TOKENFILE` with an API key from your system

run the application

```
python uuid-hunter.py --base-url BASE_URL --token-file TOKEN_FILE --project PROJECT_NAME --version VERSION_NAME [--no-csv] [--no-verify]
```

For internal servers, pass `--no-verify` to trust the certificate. 

To only print results on screen, pass `--no-csv`

A CSV will be generated with the project name and version name for upload to Jira