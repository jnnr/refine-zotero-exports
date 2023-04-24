"""
This script loads a json file from zotero (BetterBibtexJson) and saves it as a CSV-table.
The script expects a path to the json and a path to the target as command line arguments.

You can configure the script by adapting the RENAME_DICT and ADD_COLUMNS.
"""
import os
import sys

import pandas as pd

from util import compress_notes, format_tags, load_json

SEP = ","

RENAME_DICT = {
    "citationKey" : "citation_key",
    "title": "title",
    "tags": "tags",
    "notes": "notes",
}

ADD_COLUMNS = [
    "Main idea/relevance",
    "Methods/theory",
    "Quote",
    "Free notes",
]

if __name__ == "__main__":
    cmd_args = sys.argv
    assert len(cmd_args) == 3, "Need to specify source and target"

    file_source = sys.argv[1]
    file_target = sys.argv[2]
    assert file_source != file_target, "Source and target must be different"

    assert not os.path.exists(file_target), "I am not allowed to overwrite an existing file"
 
    bib = load_json(file_source)

    df = pd.DataFrame(bib["items"])

    # filter and rename
    df = (df
        .loc[:, RENAME_DICT.keys()]
        .rename(columns=RENAME_DICT)
    )

    # format
    df["tags"] = df["tags"].apply(format_tags, 1)

    df["notes"] = df["notes"].apply(compress_notes, 1)

    df[ADD_COLUMNS] = None

    # save
    df.to_csv(file_target)
    print(f"CSV file saved to {file_target}")
