from parse_csv import parse_bookban_csv
from parse_jsonl import parse_goodreads_jsonl

bookban_data = parse_bookban_csv("Data/bookbans-merged.csv")
goodreads_data = parse_goodreads_jsonl("Data/goodreads_subset_k.jsonl")