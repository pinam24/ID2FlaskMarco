from ProductionCode.data import goodreads_data

def print_book_short(book):
    # pretty prints basic book info
    # looks like "title by author, author, author (ISBN: isbn)"
    output = book["title"] + " by "
    output += ", ".join(book["authors"])
    if book["isbn"] != None:
        output += f" (ISBN: {book["isbn"]})"
    else:
        output += " (ISBN not found)"
    return output

def fuzzy_match(data, query, partial):
    # match case-insensitive and without whitespace
    # option for if it should be a partial match
    if partial:
        return query.lower().strip() in data.lower().strip()
    else:
        return query.lower().strip() == data.lower().strip()

def query_data(data, key, value, partial_match=False):
    # create list to add objects to
    matches = []
    for entry in data:
        # for fields that are lists, match if any value is the same
        if type(entry[key]) is list:
            if any(fuzzy_match(item, value, partial_match) for item in entry[key]):
                matches.append(entry)
        # for fields that are strings, just match the string
        elif type(entry[key] is str):
            if fuzzy_match(entry[key], value, partial_match):
                matches.append(entry)
    return matches

def search_title(title):
    # allow titles to partially match (ie "Harry Potter" matches "Harry Potter and the...")
    entries = query_data(goodreads_data, "title", title, True)
    # for this query, only print short info
    entries = map(print_book_short, entries)
    return entries

def search_author(author):
    entries = query_data(goodreads_data, "authors", author)
    # for this query, only print short info
    entries = map(print_book_short, entries)
    return entries

def search_genre(genre):
    entries = query_data(goodreads_data, "genres", genre)
    # for this query, only print short info
    entries = map(print_book_short, entries)
    return entries

def main():
    search_results = search_title("kingdom of the")
    for result in search_results:
        print(result)
    print("----------")
    search_results = search_author("dori hillestad butler")
    for result in search_results:
        print(result)

if __name__  == "__main__":
    main()