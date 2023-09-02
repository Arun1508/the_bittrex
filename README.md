# The Bittrex

This application fetches the crypto currency market updates from the [Bittrex](https://bittrex.github.io/api/v3). The two new protected APIs will fetch summary of all active crypto currency and details about a particular currency by passing it's symbol as parameter. Find the API schema for the newly created endpoint APIs @[swagger](https://app.swaggerhub.com/apis-docs/ARUNMUKESHS/Bittrex_api/1.0.0#/Details/market_details_markets__symbol__get).


## Installation

Clone the [bittrex repo](https://github.com/Arun1508/the_bittrex.git) by

``` bash
git clone https://github.com/Arun1508/the_bittrex.git

cd the_bittrex

```

Install requirements
``` bash
pip install -r requirements.txt
```


## Run application

On the root folder, run `main.py`

``` bash
python3 main.py
```

This will run a uvicorn server on `0.0.0.0:8001`. For open API documentation [click](http://0.0.0.0:8001/docs).

## Install pytest

Have implemented untesting for the existing to APIs. In order to execute them install test requirements.txt

``` bash
pip install -r tests/requirements.txt
```


## Run pytest

To excute unit testing run following commands

``` bash
python3 -m pytest -s
```

Then create code coverage html by running below command

``` bash
coverage html
```
