---
date: 2023-07-29
title: Self-Reliance & Tech
weight: 10
categories: ["Tech"]
type: docs
bookTOC: false
summary: "On craftsmanship, curiosity, and the love of know-how."
status: budding

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
I’ve used Nextcloud in the past and have recently revived my interest in it. I want my own platform-agnostic cloud. I’d eventually like to host things on a raspberry pi and have it be powered by solar. Maybe I start with a local version on an old Mac mini. 

I wrote a guide on how to set up your own Google Drive/Dropbox/iCloud replacement: [Tech Independence](/journal/tech-independence).

## Social
After things really went south on Twitter (see: when some new idiot took over), I started hosting my own Mastodon instance: [hooray.computer](https://hooray.computer). It's been a really fun ride, and showing me that small social networking is a much better connector with fewer people screaming into various voids.

It was a difficult learning curve, and ultimately I ended up destroying it before bringing it back a couple years later. 

## Personal LLM
I’m in search of a personal LLM that helps me be me. Not one that helps me be incredibly productive or something I’m not. But it would search my personal knowledge and notes, provide provocative questions, and fulfill what I see as the role of ultimate extension of my memory.

I've used [Simon Wilson's LLM](https://simonwillison.net/2023/Mar/11/llama/) to install a few local versions of gpt4-all and Ollama to install other LLMs. It's fun. Mostly, my benefits have come in the form of helping me debug code, but that in and of itself is fantastic because I’m only going to spend time searching on stack overflow. I do need to make sure I’m not building dependence on it and engaging mindfully with it. And I’m definitely not using it to create art.

## Repair
You may have already seen my [iPod restorations](/tinkering/ipods), but I want to continue this trend and be able to maintain my own tech when it breaks. Or crack it open if I wanna do something cool.