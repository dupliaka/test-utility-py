import json
import csv
import sys


def json_to_csv(json_file, csv_file):
    data = []
    for file_content in json_file:
        # Read JSON file
        with open(file_content, 'r') as file:
            data.append(json.load(file))

    # Write CSV file
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        header = ['benchmark', 'params', 'unit', 'Baseline Score: ' + json_file[0]]
        for jf in json_file[1:]:
            header.append("Newline Score: " + jf)
            header.append("Diff: " + json_file[0] + " vs " + jf)

        writer.writerow(header)  # Write CSV header

        for item in data[0]:
            benchmark = item.get('benchmark')
            params = item.get('params')
            score_unit = item.get('primaryMetric').get("scoreUnit")
            score = item.get('primaryMetric').get("score")
            row = [benchmark, params, score_unit, score]
            for dataset in data[1:]:
                score_item = [i for i in dataset if i.get('benchmark') == benchmark
                              and set(i.get('params')) <= set(params)]
                ds_score = score_item[0].get('primaryMetric').get("score")
                row.append(ds_score)
                change = (ds_score / score - 1) * 100
                row.append(change)

            writer.writerow(row)

    print(f'Successfully converted {json_file} to {csv_file}.')


sys_args = sys.argv[1:]
csv_file = 'report.csv'
json_to_csv(sys_args, csv_file)
