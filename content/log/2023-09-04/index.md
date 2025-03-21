---
date: 2023-09-04
title: Markdown to Word Doc, Writing, Notes on Complexity
bookToc: false
aliases:
  - /2023-09-04
---
I’m considering what to do once We Need To Talk is done. I’ll still promote and coach, but what else? Considering:
- Writing a couple more horror stories
- Working on a sculpture project with resin (and skulls, probably)
- Relaxing and doing nothing, which I seem incapable of doing 

While in the course of doing some research, I came to a realization about oneself: if another person demands a change to your life or self in order to gain their acceptance, they have already decided to not accept you. No amount of change will do for them—either your change will not be enough or they will invent more things which need changing. 

## Reading
Finished Notes on Complexity, which was a good read on a unifying theory of everything. It addresses the question of "are we a collection of cells or a whole being" and presents a pretty compelling answer to it being both. Metaphysical belief systems arrived at such conclusions long ago and embraced the interconnectedness of everything, though without the rigor that is customary for scientists and researchers today. 

In it, I learned about Gödel, who was a legendary thinker. At an early age, he said something along the lines of the joy of cognition being his life's purpose. He had invented Gödel Numbering, which was part of his incompleteness theorem. From Wikipedia:
> In hindsight, the basic idea at the heart of the incompleteness theorem is rather simple. Gödel essentially constructed a formula that claims that it is unprovable in a given formal system. If it were provable, it would be false. Thus there will always be at least one true but unprovable statement. That is, for any computably enumerable set of axioms for arithmetic (that is, a set that can in principle be printed out by an idealized computer with unlimited resources), there is a formula that is true of arithmetic, but which is not provable in that system. To make this precise, however, Gödel needed to produce a method to encode (as natural numbers) statements, proofs, and the concept of provability; he did this using a process known as Gödel numbering.

## Markdown to Word Doc Conversion from Notion
Lastly, for Notion users: I found a way to convert the .md files that Notion exports to word doc files. I have no idea why this isn't something that's built into the app, but here it is anyway. It relies on python3 and `pandoc`.

```
# install pandoc
# $ apt-get install pandoc  # On Debian/Ubuntu systems
# $ brew install pandoc     # On macOS
```

Take this script, put it in the directory with your `.md` files (I called it `rename.py`) and run it. If you use the proper markdown formatting (which Notion respects), you'll get a pretty decent export. You won't have it honor things like `callout` and other more customized functions, so you'll need to account for that on your own. 

```
import os
import subprocess

def convert_md_to_docx(folder_path="."):
    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):
            input_file_path = os.path.join(folder_path, filename)
            output_file_path = os.path.join(folder_path, filename.replace('.md', '.docx'))
            
            # Call pandoc to perform the conversion
            subprocess.run(['pandoc', input_file_path, '-s', '-o', output_file_path])

if __name__ == '__main__':
    convert_md_to_docx()

```