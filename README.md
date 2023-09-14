# JMH result visualizer


## Compare n benchmarks with baseline

Parses benchmark name, params, utils, score lables.
Writes result in csv format.
For each additional json passed as an argument it will parse the same labels and calculate difference b/w it and the first json. 

### Usage

#### Development
###### Compare json files

`python compare_jsons.py jmh data/baseline.json data/newline.json` 

###### Compare by horreum urls

` python compare_jsons.py horreum data/baselineHorreum.json data/newlineHorreum.json`

#### Docker

`docker run -it --rm --name report_script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python compare_jsons.py jmh data/baseline.json data/newline.json`

Creates `change_report.csv` in project directory