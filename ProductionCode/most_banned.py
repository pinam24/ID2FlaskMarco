from ProductionCode.data import bookban_data


def print_item(item):
    output = item["field"] + ": " + str(item["bans"])
    return output


def most_banned_districts(limit: int):
    most_banned_districts = count_bans(bookban_data, "district")
    most_banned_districts = most_banned_districts[0:limit]
    return map(print_item, most_banned_districts)


def most_banned_states(limit: int):
    most_banned_states = count_bans(bookban_data, "state")
    most_banned_states = most_banned_states[0:limit]
    return map(print_item, most_banned_states)


def most_banned_authors(limit: int):
    most_banned_authors = count_bans(bookban_data, "author")
    most_banned_authors = most_banned_authors[0:limit]
    return map(print_item, most_banned_authors)


def most_banned_titles(limit: int):
    most_banned_titles = count_bans(bookban_data, "title")
    most_banned_titles = most_banned_titles[0:limit]
    return map(print_item, most_banned_titles)


def count_bans(ban_data, field):
    total_bans = {}
    for ban in ban_data:
        field_value = ban[field]
        if field_value not in total_bans:
            total_bans.update({field_value: 1})
        else:
            total_bans[field_value] = total_bans[field_value] + 1
    return top_bans_from_dict(total_bans, field)


def top_bans_from_dict(total_bans, field):
    sorted_bans = []
    for key in sorted(total_bans, key=total_bans.get, reverse=True):
        sorted_bans.append({"field": key, "bans": total_bans[key]})

    return sorted_bans


def main():
    top_bans = most_banned_titles(10)
    for field in top_bans:
        print(field)


if __name__ == "__main__":
    main()
