# Hub UUID Hunter

This tool is designed to pull the component origins out of a particular project versions BOM for the KB team

## Setup

```
pip3 install -r requirements.txt
```


## Usage

Note: requires an API Token to work

run the application

```
python uuid-hunter.py --base-url {base_url} --api-key {api_key} --project {project_name} --version {version_name} [--no-csv] [--no-verify]
```

For internal servers, pass `--no-verify` to trust the certificate. 

To only print results on screen, pass `--no-csv`

A CSV will be generated with the project name and version name for upload to Jira

## Docker image

### Build locally

Build the image

```docker build -t uuid-hunter .```

Run the image

```docker run -v ${PWD}/uuid-hunter:/output uuid-hunter --base-url='{base_url}' --api-key='{api_token}' --project='{project_name}' --version='{version_name}' --no-verify```

### Pull from docker hub

```docker run -v ${PWD}/uuid-hunter:/output petergreen86/uuid-hunter:latest --base-url='{base_url}' --api-key='{api_token}' --project='{project_name}' --version='{version_name}' --no-verify```