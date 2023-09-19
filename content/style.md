---
title: Style Guide
type: docs
summary: " "
hidden: true
---

## Headings

# this is h1 heading
## this is h2 heading
### this is h3 heading
#### this is h4 heading


## Body Stuff

this is a standard paragraph, please look at it. it is pretty and long and gorgeous and has just the right line length and line height. it also has `code` and [links]() and **bold stuff** and _italic stuff_ and ~~strikethrough stuff~~. Cool, right?

> Here's a blockquote. This is nice and you can use it to show off how smart some of the people are who made these quotes. Or dumb, whatever.

a <a href="#">local link</a> and an <a href="https://atlasobscura.com" target='_blank'>external link</a>

<ul>
  <li>This is a list, with:</li>
  <li><b>bold</b></li>
  <li><i>italic</i></li>
  <li><a>link</a></li>
  <li><code>code</code></li>
  <ul>
    <li>This is a nested list:</li>
    <li><b>bold</b></li>
    <li><i>italic</i></li>
    <li><a>link</a></li>
    <li><code>code</code></li>
  </ul>
</ul>

```
This is a code block, which is just for fragments of computer code.
```

<pre>
The PRE element tells visual user agents that the enclosed text is "preformatted". When handling preformatted text, visual user agents:

May leave white space intact.
May render text with a fixed-pitch font.
May disable automatic word wrap.
Must not disable bidirectional processing.
</pre>

## Buttons
{{< button relref="/" >}}Get Home{{< /button >}}
{{< button href="https://github.com/alex-shpak/hugo-book" >}}Contribute{{< /button >}}


## Tables

| Item         | Price     | # In stock | Another   | #          |
|--------------|-----------|------------|-----------|------------|
| Juicy Apples | 1.99      | *7*        | 1.99      | *7*        |
| Bananas      | **1.89**  | 5234       | **1.89**  | 5234       |
| Juicy Apples | 1.99      | *7*        | 1.99      | *7*        |
| Bananas      | **1.89**  | 5234       | **1.89**  | 5234       |
| Juicy Apples | 1.99      | *7*        | 1.99      | *7*        |
| Bananas      | **1.89**  | 5234       | **1.89**  | 5234       |
| Juicy Apples | 1.99      | *7*        | 1.99      | *7*        |
| Bananas      | **1.89**  | 5234       | **1.89**  | 5234       |

## Graphs
{{< mermaid >}}
stateDiagram-v2
    State1: state1 here
    note right of State1
        Note on State 1
    end note
    State1 --> State2
    note right of State2 : This is the note to the right.
    State1 --> State3
    State3: WHOOOOO STATE 3 BAYBEE
    note left of State3 : 3 state note
{{< /mermaid >}}


## Columns and Images

{{< columns >}}
<figure>
  <img src='/uptown-sans-1.webp' alt='Maude picture'/>
  <figcaption>This is an image in a figure block, this note is in a figcaption with <b>bold</b>, <i>italic</i>, <code>code</code> and a <a>link</a>.</figcaption>
</figure>
<--->
<figure>
  <img src='/uptown-sans-1.webp' alt='Maude picture'/>
  <figcaption>This is an image in a figure block, this note is in a figcaption with <b>bold</b>, <i>italic</i>, <code>code</code> and a <a>link</a>.</figcaption>
</figure>

{{< /columns >}}

## Tabs
{{< tabs "media" >}}

{{< tab "Books" >}}

### Incoming
- Salem's Lot


{{< /tab >}}

{{< tab "Film & TV" >}}

### Incoming
- Return to Seoul (2022)

{{< /tab >}}

{{< tab "Games" >}}

### Incoming
- Horizon Forbidden West

{{< /tab >}}
{{< /tabs >}}


## Hints

{{< hint info >}}
General info hint.
{{< /hint >}}

{{< hint warning >}}
Warning info hint.
{{< /hint >}}