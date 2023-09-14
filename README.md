# JMH result visualizer

## Compare n benchmarks with baseline

Parses benchmark name, params, utils, score lables.
Writes result in csv table.
For each additional json passed as an argument it will parse the same labels and calculate difference b/w it and the first json. 

### Usage

#### Development

`python compare_jsons.py data/baseline.json data/newline.json` 

#### Docker

`docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python compare_jsons.py baseline.json newline.json`

Creates `report_compare_jsons.csv` in project directory