# JMH result visualizer

## Compare n benchmarks with baseline

Parses benchmark name, params, utils, score lables.
Writes result in csv table.
For each additional json passed as an argument it will parse the same labels and calculate difference b/w it and the first json. 

### Usage

`python compare_jsons.py baseline.json newline.json` 

Creates `report.csv` in project directory