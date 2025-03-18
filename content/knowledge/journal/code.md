---
Date: 2025-03-10
title: Code Snippets
type: docs
status: seedling
categories: ["Tech"]
summary: Little bits of code that help.
---

Sync everything in a folder to a remote server:

```
rsync -ahv --progress -e "ssh" ~/path/to/file/ user@SERVER_IP:/path/to/folder/
```
---
Copy all text from a PDF into a TXT file:

```
pdftotext -layout file.pdf
```
---
Convert image formats:

```
mogrify -format webp -quality 90 *.jpeg
```