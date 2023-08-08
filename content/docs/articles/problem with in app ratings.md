---
date: 2013-04-12
link title: My real problem with in-app rating modules
title: My real problem with in-app rating modules
weight: 10
tags: Thoughtful Design
originalURL: https://medium.com/@joshuamauldin/my-real-problem-with-in-app-rating-modules-b2c0df494783
summary: "Early work on in-app rating modules and how I made them better. This was before Apple launched their own in-app rating system."
---


![My%20real%20problem%20with%20in-app%20rating%20modules%20b6643e8967734de1a0e02dd2b0222e3a/1Gygkz7MUtV0HY6UMz5cI-w.webp](/1Gygkz7MUtV0HY6UMz5cI-w.webp)

## “Like this app? Give us 5 stars! UGH STOP PLZ.”

The conversation where folks are growing collectively tired of being asked to rate apps has been interesting to watch.

Some tech folks want to encourage users to rate an app 1 star because they asked for a rating. I think that’s unfair, because that doesn’t seem like a real review at all to me. It doesn’t tell me that the app is buggy, that it steals my data, or [doesn’t alert me to a tornado](http://xkcd.com/937/). It just tells me someone was bothered by being asked to rate an app.

To be clear, I think *just* asking for ratings isn’t the right thing, but I don’t think asking for them is wrong in and of itself. What I think is missing is this: **asking for negative feedback.**

My biggest problem with App Store reviews are this: they’re a one-way conversation. There should be something better, more conversational. I think that’s where feedback modules can be improved over the standard.

## **Feedback modules, not ‘Rate this App’ modules**

I believe a solid way to approach asking for feedback and ratings is to ask for feedback, both good and bad. If it’s positive, send them to the App Store to write a review, because you likely don’t have much to talk about. If the feedback’s negative, open a dialog.

The App Store (for better or worse) doesn’t yet offer a way to interact with a customer. I can’t think of many people that’d leave their contact information on a public spot like that, myself included. I believe we should open an email and have a conversation with that person. That lets the developer find out what the problem is, and gives them an opportunity to solve it with the person experiencing it.

## What I did to solve the problem

I implemented this pattern in a medium-sized news app with thousands of users, and read every single email that came in (there were a lot). Here’s how it worked:

- After 3 days from launch, each person saw a dialog box asking how their experience was
- Positive feedback asked people to leave a review
- Negative feedback asked people to contact us
- After telling us how you felt, you could dismiss this without emailing or rating us

We later amended this to let people dismiss this instead of prompting a positive or negative response, and let folks see this after an accumulated usage time. We found some users would launch the app (say on a Friday afternoon), quit it, and return a few days later (like Monday morning), which made it harder to get a good idea of how the app was.

Each person got a reply from the support team attempting to help with their problem. Some were angry, most confused because they lost a password, and some experienced legitimate problems that we couldn’t find on our own. **Ultimately, these emails were directly responsible for improving the product, and ultimately turned its health around.**

PS: if you go all Darth Vader here, you’re basically doing some real shady work and deserve all the karmic flack you catch for that. Death Star icon designed by

![My%20real%20problem%20with%20in-app%20rating%20modules%20b6643e8967734de1a0e02dd2b0222e3a/1UyJLFr3vj97-loLFiItSGw.gif](/1UyJLFr3vj97-loLFiItSGw.gif)

## **Darth Vader, or why feedback modules aren’t the problem**

The first thing I hear when talking about app ratings and this approach is that some would call it a [dark pattern](http://darkpatterns.org/). I don’t think of it that way—it’s a tool, just like The Force.

One could argue that this fits the definition of a dark pattern, since it directs positive feedback one way and negative another, but it doesn’t feel that way to me: it’s more about how it’s used.

Sure, it could be used for evil and silence all dissent. Just don a black outfit with a sweet cape, build a Death Star and Force Choke all those reviews to death by sending them to a never-checked inbox (see above image with caption). Or you can use it for good to get meaningful feedback from real users and help them with their problem to make your product better.

It’s been my experience that if folks are motivated to complain, they will do it to you, the App Store, and anyone else who will listen, regardless of what types of barriers you introduce for deterring that kind of feedback. More so if your app is a real stinker. If your customers have a problem, you’re doing them a service by being there to talk to them.

**Why not just have a support link?**

I prefer to have a proactive approach when it comes to feedback. I look at feedback modules as someone checking in on you to make sure things meet your expectations. If they don’t, let’s figure out what we can do to make it better. I’d rather it be me asking how things are going rather than someone coming to find me and tell me about a problem.

## I’m ok, you’re ok.

In closing, I don’t think app feedback modules aren’t bad. I’d just encourage developers to not be shady and try to inflate ratings. Talk to your customers, and it’ll help make this whole thing better.


[Original post](https://medium.com/@joshuamauldin/my-real-problem-with-in-app-rating-modules-b2c0df494783)
