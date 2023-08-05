---
title: Aperture Health
image: /aperture.webp
summary: "Modernizing a 20 (!) year old medical credentialing system."
tags: ["Product Design", "Strategy"]
date: 2021-01-01
year: 2021
---

Aperture Health had a credential system in need of an update called CredSmart. This system helped providers track, renew, and remind themselves about the expiration or renewal dates of medical licenses, certificates, and other important medical documents that allowed them to continue practicing medicine.

## Role
My role on the team was the sole product designer. I worked two PMs and a rotating team of 6-10 engineers. We partnered closely with sales and the product leadership team at Aperture.


## Challenge
The system they use is old. Like, really old. As of writing, some elements in the system were over 20 years old. This old and outdated experience caused providers to spend a disproportionate amount of time on administrative work that could better be spent with patients. The goal was to reduce the time spent on each credentialing event and give providers a system that manages as much of this for them as possible.

It was difficult to quantify exactly how many hours were spent per credential, as the method for renewing each one varied. The process of filling out a form was relatively straightforward, but the time it took to validate and get approval averaged about 20 days per credential. And each credential required unique ways of following up. To call it frustrating for a provider and their admin was an understatement.


<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Fproto%2F1IFNLnZ7srjlc5PKpu3Pyk%2FProvider-Portal%3Fpage-id%3D212%253A0%26type%3Ddesign%26node-id%3D529-12230%26viewport%3D1227%252C157%252C0.07%26t%3DfmW8mt8dIU92lMpj-1%26scaling%3Dscale-down%26mode%3Ddesign" allowfullscreen></iframe>

## Approach

We hypothesized that:

- Modernizing the experience will make it easier to track expiration dates and proactively remind providers to update their information will reduce back and forth when it’s time to submit for re-credentialing.
- Making it easier to identify missing information and notify providers to give said information will reduce the time it takes to submit and receive updated credentials.

To modernize this, we looked at the workflows for providers and the admins that support them. Getting to the providers and their staff was difficult, as Aperture was hesitant to show that they may be considering any changes to a client’s workflow and were initially resistant to our team speaking with anyone outside of the sales department.

Once we presented them with a user research plan and script on what we wanted to validate, as well as help them position the conversation with their customers, we were able to proceed and learn a ton along the way.

The results of our learnings and testing and interviews were:

- We need to allow providers to delegate their accounts to their admins.
- We need to improve the ability for admins to fill data gaps for applications for two use cases: new providers who have no data and existing providers who need data updates
- We need to allow admins to notify providers of expiring information and credentials

We tested several iterations of prototypes, ultimately arriving at one that saved providers and their admins hours of work, and proactively notified them about upcoming deadlines.

I also wanted to give them a design library that could scale as the team took on new tasks after we left. Accessibility and scalability were paramount, so we started with the US Web Design System and began to modify components and create a React library for engineers to consume.

## Results

This project had an unusual ending which prevented us from seeing this through to launch: the company was acquired nearing the end of our engagement. The results of our tests showed that had we launched, we would have reduced the headache and time spent renewing credentials by at least 75%.