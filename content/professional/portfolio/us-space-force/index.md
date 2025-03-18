---
title: US Space Force
summary: "Designing a workflow and interface to help shoot lasers into space."
image: starfox.webp
tags: ["Product Design", "Design Systems"]

type: docs
date: 2019-07-01
year: 2019
bookTOC: false
---

{{< hint warning >}}
Given the nature of this work, I’m limited in what I can share.
{{< /hint >}}

My role included two parts, over the course of 8 months:

- Teach the Space Force how to design and quickly deliver modern software.
- Help the Space Force solve a difficult problem regarding laser firing requests that involved communicating across multiple secure, secret networks and multiple countries.

## Context

Space Force regularly undertakes exercises, such as shooting lasers into space to temporarily disrupt or disable satellites under specific conditions. It’s necessary to coordinate with friendly countries to ensure that Space Force doesn’t inadvertently harm another country’s operations. Sometimes these requests would take a week to resolve.

The people I helped were called Operators, and they’re the people who manage these requests. It’s a difficult job: Operators had to parse difficult-to-understand data manually, which led to errors, was time consuming, and they also needed to communicate synchronously with others within the US Military and other partners, which added unnecessary difficulty.

## Approach

Given that one goal was teaching Space Force how to design and ship software, all of this was done with at least one counterpart for each role. I had a design counterpart, the PM had one, and the engineers also had several. We worked alongside each other and eventually let them take the reins. This included teaching them how to collaborate, to understand boundaries, and modern software methodologies like sprints and scrum.

Our goal was to understand the depth and cause of these difficulties and see how to reduce the time it takes to manage a request. We hypothesized that a web portal and interface for inputting these requests would be best.

To that end, I did a deep dive into their process. I identified several areas in which they could improve the quality of work and do more of it asynchronously. The product manager, who was great at parsing complex data, helped identify areas in which we could simplify the data entry.

I created several test prototypes to see which were feasible. Given the secrecy requirements involved, some of our prototypes that would have worked in any other scenario proved themselves to be unrealistic.


## What We Delivered

- A working design library in Figma to support ten teams, complete with training someone to maintain it. This design library worked with React and Material UI and was easily consumable by engineers.
- A dashboard to manage open requests.
- A notification system that could accurately convey priority of requests.
- A method to coordinate asynchronously with others to ensure maximum clarity and ease with minimum hassle.

Of note, the design system powered ten teams. This necessitated design ops education on how to properly maintain and grow a design system so. This naturally required deep cooperation, which they military was obviously very good at, and bidirectional communication between them and their commanding officers, which they weren’t very good at.

## Results
The results of our work were great: we reduced the time it took to process a request down from 1-2 weeks to 2–8 hours. The design team grew the design system to share with others working on related projects within Space Force. And I learned a few things about shooting lasers into space, which is rad.