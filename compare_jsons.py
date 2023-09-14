import json
import csv
import sys


def get_horreum_input(json_files):
    horreum_reports_json = get_file_input(json_files)
    extracted_jmh_report = []

    for report in horreum_reports_json:
        jmh_report = report.get('jmhData')
        extracted_jmh_report.append(jmh_report)
    return extracted_jmh_report


def get_file_input(json_files):
    data = []
    for file_content in json_files:
        # Read JSON file
        with open(file_content, 'r') as file:
            data.append(json.load(file))
    return data

def compare_jmh_reports(data, line_name):
    # Write CSV file
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        header = ['benchmark', 'params', 'unit', 'Baseline Score: ' + line_name[0]]
        for jf in line_name[1:]:
            header.append("Newline Score: " + jf)
            header.append("%Diff: " + line_name[0] + " vs " + jf)

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

    print(f'Successfully converted {line_name} to {csv_file}.')


def get_input(it, source):
    if it == "jmh":
        return get_file_input(source)
    elif it == "horreum":
        return get_horreum_input(source)
    else:
        print("No such input type" + it)


input_type = sys.argv[1]
source_names = sys.argv[2:]
csv_file = 'change_report.csv'
reports_data = get_input(input_type, source_names)
compare_jmh_reports(reports_data, source_names)
