---
title: Meta
type: docs
bookTOC: false
summary: "Credits and other information about the site."
categories: ["Overview"]
status: evergreen
date: 2025-01-02

---

## Launch
The current version of this site launched in July of 2023 as a digital garden, replacing a very cute but very resource-intensive site. See [my rationale](/about/digital-gardening) for more on this.

## Typography
This site uses [Commercial Type's Atlas Grostesk](https://commercialtype.com/catalog/atlas/atlas_grotesk/) and [Paratype's PT Mono](https://www.paratype.com/fonts/pt/pt-mono) for body text and preformatted text, respectively. The headlines are set in [DJR Type's Roslindale](https://djr.com/roslindale).

## Site
[Hugo](https://gohugo.io) powers this site, it's an open source framework for building static sites. There are no trackers, cookies, or anything weird. It's good old HTML, CSS, and some JS for styling and the search function.

This site is based off the `hugo-book` theme by [Alex Shpak](https://themes.gohugo.io/themes/hugo-book/). 

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

[![Image Caption with a link](/Devil.webp)](/journal)
<--->
[![Image Caption with a link](/Devil.webp)](/journal)
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