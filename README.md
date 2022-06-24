# Diagrams
Create diagrams as code.

# Requirements
* Docker
* IDE

## Optional
If you would like to develop the diagrams it is helpful, but not required, to have a python3 environment set up on your local machine. If you choose to do so, ensure the following is installed.
* Python3
* [Diagrams](https://diagrams.mingrammer.com/)
    * `pip3 install diagrams`

# How to Use

## Build Image
```bash
docker pull mattbangert/python-diagrams:1.0.0
```

## Create Diagram
```bash
docker run -it --rm -v "$PWD"/src:/src -w /src mattbangert/diagrams:1.0.0 simpleAws.py
```