import json

def parse_goodreads_jsonl(filename):
    # create list to add objects to
    data = []
    # open the file, iterate over lines
    with open(filename, "r") as file:
        for line in file:
            # for each line, parse it and add it to the list
            data.append(json.loads(line))
    return data

def main():
    goodreads_data = parse_goodreads_jsonl("Data/goodreads_subset_k.jsonl") # to replace with full db eventually
    print(goodreads_data[0])

if __name__  == "__main__":
    main()