#!/usr/bin/python3

import os
import sys

if len(sys.argv) != 2:
    print("There are %d arguments" % (len(sys.argv)-1))
    print("Arguments should be")
    print("1-Root path")
else:
    root = sys.argv[1]

    print ('Root:  %s' % (root))

    for folder, subFolders, files in os.walk(root):
        markdowns = [f for f in files if f.endswith(".md")]

        for f in markdowns:
            filePath = folder + "/" + f
            print("Markdown:  ", filePath)

            with open(filePath, 'rt') as lines:
                newLines = [line.replace("**Syntax**", "## Syntax").replace("**Arguments**", "## Arguments").replace("**Returns**", "## Returns").replace("**Example**", "## Example").replace("**Examples**", "## Examples") for line in lines]
                with open(filePath, 'wt') as fileOut:
                    fileOut.writelines(newLines)
