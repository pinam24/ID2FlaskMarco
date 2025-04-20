'''
The eventual location for the command line interface (CLI) for the project.
This will be the entry point for the project when run from the command line.
'''
from search import search_title, search_author, search_genre
from most_banned import most_banned_districts, most_banned_authors, most_banned_states, most_banned_titles
import sys
import argparse


def main():
    """Main function for the command line interface (CLI) for the project."""
    parser = argparse.ArgumentParser(
        # The command line interface (CLI) for the project.
                prog="cl.py",
                description="Command line interface for the project",
                epilog="This is the command line interface for the project.",
                usage="%(prog)s [options] [args]")
    parser.add_argument(
        #Search for a title in the database
                        "--search-title",
                        "--st",
                        "-st",
                        help="Search for a title in the database",
                        type=str,
                        metavar="TITLE")
    parser.add_argument(
        #Search for an author in the database
                        "--search-author",
                        "--sa",
                        "-sa",
                        help="Search for an author in the database",
                        type=str,
                        metavar="AUTHOR")
    parser.add_argument(
        #Search for a genre in the database
                        "--search-genre",
                        "--sg",
                        "-sg",
                        help="Search for a genre in the database",
                        type=str,
                        metavar="GENRE")
    parser.add_argument(
        #Get the most banned districts in the database
                        "--most-banned-districts",
                        "--mbd",
                        "-mbd",
                        help="Get the most banned districts in the database",
                        type=int,
                        metavar="LIMIT")
    parser.add_argument(
        #Get the most banned authors in the database
                        "--most-banned-authors",
                        "--mba",
                        "-mba",
                        help="Get the most banned authors in the database",
                        type=int,
                        metavar="LIMIT")
    parser.add_argument(
        #Get the most banned states in the database
                        "--most-banned-states",
                        "--mbs",
                        "-mbs",
                        help="Get the most banned states in the database",
                        type=int,
                        metavar="LIMIT")
    parser.add_argument(
        #Get the most banned titles in the database
                        "--most-banned-titles",
                        "--mbt",
                        "-mbt",
                        help="Get the most banned titles in the database",
                        type=int,
                        metavar="LIMIT")
    args = parser.parse_args()
    if args.search_title:
        search_title(args.search_title)
    elif args.search_author:
        search_author(args.search_author)
    elif args.search_genre:
        search_genre(args.search_genre)
    elif args.most_banned_districts:
        most_banned_districts(args.most_banned_districts)
    elif args.most_banned_authors:
        most_banned_authors(args.most_banned_authors)
    elif args.most_banned_states:
        most_banned_states(args.state_limit)
    elif args.most_banned_titles:
        most_banned_titles(args.most_banned_titles)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
    
        