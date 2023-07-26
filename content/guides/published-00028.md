---
date: 2018-05-08
link title: What I learned making my first VR app (Prototypr)
title: What I learned making my first VR app (Prototypr)
weight: 10
categories: published
tags: Reflection
originalURL: https://medium.com/prototypr/what-i-learned-making-my-first-vr-app-e6c19a160342
---

[Original post](https://medium.com/prototypr/what-i-learned-making-my-first-vr-app-e6c19a160342)

Virtual Reality Experience by Mooms from the Noun Project

![What%20I%20learned%20making%20my%20first%20VR%20app%20Prototypr%20cd206b10c83e4a66b23ebe8e3354b23d/1CXpmVqUYLVDUVEYTKcAjBg.png](/img/1CXpmVqUYLVDUVEYTKcAjBg.png)

I recently made my first VR app for a client who commissioned an app to celebrate their 100th anniversary. In it, you walk through a 3D art gallery complete with with audio and imagery to understand their history.

Having primarily designed for mobile over the last few years, this was a fun new medium to explore. The new constraints and considerations were interesting, too.

For instance, I found typography worked a little differently here. Things like motion and interaction took on an entirely new form, too. Not only that, but the process for making VR apps were also a little different than most other projects. I’ll walk you through those here.

# Interactions

We have two main ways of using VR apps: with **our gaze** or a **controller**. each method has something different to consider, but I’ve found that they both affect how you design in similar ways. Let’s start with how they affect interactive objects like buttons.

Apple recommends buttons have a 44pt minimum touch target size for apps. You’re going to want to go larger for VR. If you use Google’s VR framework, Daydream, it recommends a default size of 64pt. While that’s considerably bigger, I found that increasing the size allowed for much better usability.

If you’ve ever heard of Fitt’s Law, you’ll recall that one of its key points is to make important elements larger and positioned closer to someone. That concept goes double for VR.

VR environments, because of their immersiveness, make it easy to miss a button. If you’re using a controller, remember that it’s tougher to direct a pointer than it is to tap a button on your phone.

It’s fine if you want to focus on only using someone’s gaze to navigate. If that’s what you’re doing, show a timer or some other sort of progress bar when someone gazes on an interactive object. This makes it clear what will happen if someone keeps staring and it. Doing this also prevents accidental interactions. I’ve found that anywhere from half a second to one second for a timer is a good idea.

# Motion

What makes VR so much fun is its immersiveness and movement. We have into two main areas to consider here: **how your body moves** and **how you move around within the app**.

## How your eyes and body move

First, I’m really thankful for the work of [Mike Algers](https://www.youtube.com/watch?v=id86HeV-Vb8&t=0s&list=PLzag1H05l3TI7yiOpxg0OmB5bjv_hEC_J&index=1) and Alex Chu here because they articulated these principles so well. Here, we’ll talk about eye movement as well as body movement.

If you want someone to see something without them turning their heads, you’ve got about **30º in any direction**. Anything outside of that is out of focus and causes eye strain.

We can comfortably turn our heads about **60º in any direction** before our muscles begin to fatigue. Moving more than 60º in any direction can trigger motion sickness, which we’re keen on avoiding.

Its important to consider how far you’re making someone stretch themselves to use your app. Unless you’re making a VR app for yoga, remember that less stretching is better.

## How you move within the app

The other type of movement is the motion someone experiences while using your app. While we can have more fun with snappy animations on desktop and mobile, we must be more considerate and delicate here.

Don’t vary your motion speeds here, this is a huge trigger for motion sickness. No one should feel like they’re on a rollercoaster (unless that’s what you’re going for). In general, opt for slower or instant transitions.

Most of my transitions take anywhere from 1–2 seconds in VR. That’s a much longer timeline than the 500 milliseconds most of my app animations take. It feels slower, but at least I’m not getting motion sickness here.

# Typography

Reading…kinda sucks in VR. I have a really big interest in typography (so much that [I made my own typeface](https://www.fontspring.com/fonts/joshua-mauldin/uptown-sans)), so I spent a lot of time understanding this.

There are two reasons why reading isn’t so great: **our devices** and **methods of experience** greatly vary.

## Our devices

We have so many different devices capable of VR, all at varying resolutions and sizes. Some run at ultra-high resolutions, like the Galaxy S9, while others are at lower resolutions, like the iPhone. There are a few in between, like Playstation VR.

Because the resolution can vary so much, text can look blurry or crunchy. That’s especially true on lower-resolution devices.

## Methods of experience

The other factor is the methods we use to experience VR. We can use anything from a head-mounted visor that straps to your head to a Google Cardboard that you hold up to your face. They both come with their own set of benefits and tradeoffs.

While holding something like Google Cardboard is the easiest and cheapest way to get into VR, what you gain in convenience you lose in comfort. Holding the VR device in your hands causes fatigue after a little while — we’re not used to sustaining that position. It also causes the experience to be a little shakier, which can cause eye strain and motion sickness.

The head-mounted visors are my favorites because they allow you to stay in the experience longer. You also get to use your hands if you want. These are generally a little more expensive than a Google Cardboard, which will be a barrier for some.

## So what can we do to have better typography?

Downplay any kind of longer-form reading. Think about PowerPoint summary slides, that’s about the right amount of text to use.

Focus on infographics and imagery when you can, even if they’re simple. This helps communicate your message with much more clarity and makes for quicker scanning.

You will inevitably have to set some text in paragraphs (and that’s okay!). Here are some considerations:

- Use only medium-to-bold fonts. Even on high resolution devices, thin fonts look crunchy and hurt both legibility and readability
- Make your default text size larger than usual. My starting point is about 24pts
- Shorten your line length from 50–75 characters to 30–40 characters
- Use as much contrast as you can with text, so consider setting your paragraph inside of a semi-transparent, dark background

# Process considerations

I haven’t encountered a designer-friendly environment for VR yet. The best thing you can do to get started is learn the basics of how to navigate within Unity and become good buddies with your engineer.

For a simpler experience, you could try Sketch-to-VR. You’ll need to realize that this is only to help you get a basic idea of what you’re building; the sizes and positioning won’t match your design 100%.

You’ll need to do a little work to test it out — it’s not so bad, I promise! [Here’s how to do it.](https://blog.prototypr.io/sketch-plugin-sketch-to-vr-4e23ced47e6)

# Wrapping up

Clearly there’s a lot to VR, and a lot to be excited about. Best practices and patterns are still being worked out, but we know that we have to make different considerations for typography, motion, and interaction.

It’s my hope that one day a good prototyping environment will come around for VR, but the best thing seems to be to get close to your engineer pals here. Have fun!

# Resources

- [Google Cardboard design principles](https://designguidelines.withgoogle.com/cardboard/designing-for-google-cardboard/a-new-dimension.html)
- [Facebook’s VR Prototyping Template](https://facebook.design/vr-template)
- [Google Daydream Sketch template](https://developers.google.com/vr/design/sticker-sheet)
- [YouTube VR Playlist](https://www.youtube.com/watch?v=id86HeV-Vb8&list=PLzag1H05l3TI7yiOpxg0OmB5bjv_hEC_J) (I curated this, it’s got some great videos!)