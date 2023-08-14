---
date: 2023-07-29
title: Self-Reliant Tech
weight: 10
tags: tech
summary: "On craftsmanship, curiosity, and the love of know-how."

---

It’s so damned easy to find a service that will take your money and create a website for you, or use a cloud to host your project. But with ease comes trade-offs. Namely, creativity and self-reliance.

When we use these tools, our expression and creativity become constrained by how the makers of the services crafted their tools. The medium shapes the message, as Marshall Mccluen said. And there’s usually little flexibility around that, as those makers (justifiably) have a vision to achieve and letting others tamper with that doesn’t jibe well with said vision. 

The other loss is self-reliance. What happens if we forget how to make these digital things ourselves, the places we go for knowledge aren’t reliable or reachable, or an internet isn’t available?

I don’t mean to imply everything will crash. That’s always possible, but what I’m saying is that I want to preserve the ability to craft and understand these technologies ourselves.

## Offline Knowledge
I built an offline knowledge database. It's powered by [Kiwix](kiwix.org) and has about 150GB of data, including all of wikipedia (as of 2023/08/01), everything from Project Gutenberg, and other personal info. All of this is open source, and I can plug this in anywhere, on any machine, and have instant access to the world's knowledge. No ads, no tracking, no internet required.

If I decide to take this further, I'll:
- Look into compiling the data so it'll work on a low-power device like a kindle.
- Host it specifically on a raspberry pi and have it available via my local network.
- Use a [waterproof USB stick](https://www.gorilladriveusb.com) and try it while camping.

## Search
I tried using [wiby.me](https://wiby.me/) to make my own search engine. The retro feel and embracing of the small web was really interesting to me. After a couple of attempts, I gave up. The site loaded, but I wasn't enough of an expert to diagnose all the issues that come with debugging a mysql database and crawlers. 

It was fun, and I felt really powerful there for a minute, churning through config files and creating databases and writing code myself. Maybe some other time I'll come back to it.

## Hosting
I’ve used Nextcloud to make my own platform-agnostic cloud, which was great. I’d like to host things on a raspberry pi and have it be powered by solar. Maybe I start with a local version on an old Mac mini. 

## Personal LLM
I’d also like a personal LLM that would search my knowledge and notes, provide provocative questions, and fulfill what I see as the role of ultimate personal assistant. 

I've used [Simon Wilson's LLM](https://simonwillison.net/2023/Mar/11/llama/) to install a few local versions of gpt4-all. It's wildly fun. Mostly, all it's good for is helping me debug code, but that in and of itself is fantastic.

I don't care one iota about using it for creativity, it's all programmatic stuff for me. If I'm able to add more data to the training model (which I'm investigating), it'll be great. I've archived a ton of neat websites over the years (nerds: learn `wget` and you will not regret it). 

## Repair
You may have already seen my [iPod restorations](/art/2022-01-01-ipod-restorations/), but I want to continue this trend and be able to maintain my own tech when it breaks. Or crack it open if I wanna do something cool.