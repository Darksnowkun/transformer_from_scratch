import yaml

def load_data(sample_of_data=10, dataset="oo-labeled_correct.gpt4.sharegpt.jsonl", write_to_file=False):


    rows = None
    with open(dataset, 'r') as fp:
        raw_rows = fp.readlines()
        if sample_of_data is not None:
            rows = raw_rows[:sample_of_data]
        else:
            rows = raw_rows
        conversations = []
        for row in rows:
            yaml_data = yaml.safe_load(row)
            conversations.append(yaml_data)
        if sample_of_data is not None and write_to_file:
            with open('conversations.yaml', 'w') as fpp:
                yaml.safe_dump(conversations, fpp)
        return yaml.safe_dump(conversations)

def generate_less_sample_data(sample_of_data=10, dataset="oo-labeled_correct.gpt4.sharegpt.jsonl", write_to_file=False, lower_file_name="conversations.yaml"):
    """
    Loads data from a dataset. By default, function only returns first 10 rows of data.
    Optionally, also write this sample to a yaml file for better view of the input.

    Change sample_of_data to be None, if data is not to be sampled. This will read the entire file and output the entire file.
    """
    with open(dataset, 'r') as fp:
        rows = fp.readlines()
        if sample_of_data is not None:
            lower_data = rows[:sample_of_data]
        else:
            lower_data = rows
        if write_to_file:
            with open(lower_file_name, 'w') as fp:
                yaml.safe_dump(lower_data, fp)
        return lower_data