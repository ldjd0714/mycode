#!/usr/bin/env python3

def main():
    """On this farm there was a..."""

# create a list of strings
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for farm in farms:
        print(farm.get("name", "Unknown Farm"), end=":\n")  # this is like saying, "farm['name']"
                                                 # only it will not return an error
        for agri in farm.get("agriculture"):     # from a single "farm" get the list from the key "agriculture"
            print("  -", agri)                   # each time through the list "agriculture", print out an item

if __name__ == "__main__":
    main()
