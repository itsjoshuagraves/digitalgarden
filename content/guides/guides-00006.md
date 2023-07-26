---
date: 2023-07-23
link title: Designing & Testing
title: Designing & Testing
weight: 10
tags: [Guides, Product]
---

This segment helps us validate our thinking through testing and exploration. We may repeat things in segment multiple times to ensure we’re heading in the right direction before we begin building. Alternatively, we may truncate this process should our intuition or client's knowledge help us reach a better solution faster.

## This covers

1. Using the right fidelity and tool for the job
2. Thinking in systems
3. Collaborating with your team
4. Designing for accessibility
5. Presenting effectively
6. Validation and user testing

## Expected outcomes

- Validation on our ideas from users, stakeholders, and our team
- An inclusive, accessible design
- A ready-to-build design (or design system)

---

# Use the right fidelity and tool for the job

When designing, we need to work at the right fidelity. Sometimes that can be a whiteboard or simple sketch, roughed out HTML code with links, or a prototype.

Working at lower fidelity frees you from the obsession of perfect alignment, color, and size. If you find yourself obsessing, pull back to lower fidelity. Don't get stuck in pixel-perfect design until the time's right.

Also consider the platforms you're designing for. If it's a responsive site, make sure to design the mobile and desktop views at the same time. It's much easier to scale a design up than it is to shoehorn a larger design into a smaller space.

Make sure to use the right tool for the job. If our client is deeply embedded with one design tool (say, Adobe XD), then it likely doesn't make sense to force them to change to another. Meet them where they are and use their tool.

# Think in systems

We practice holistic thinking in our design, which means we think a level above what the interface looks like—we think about how an entire system works together and how components can be repurposed. This type of thinking also frees us from spending time on low-value tasks such as button colors and sizes and allows us to think about the most valuable problems.

Thinking in systems is a key part of designing for scale.

This takes a few forms:

```
- Design systems
- Design libraries (e.g. Figma libraries)
- Style tiles

```

A **design system** enables our clients to use pre-made components to decrease their design and development time. A design system can and should evolve over time, with new components added as necessary. These typically include a web-based, wikipedia-like site complete with code examples and variants. Any design we create should be made should take users' and platforms' expectations into account—sometimes we subvert them, but we're always aware of what users expect by default.

A **design library** typically lives in the design tool, like Figma. This is a set of components, color swatches, and text styles that a designer or product manager can use to quickly mock up an idea. Sometimes these are based off of an existing design language (e.g. Material Design or iOS). Sometimes they're home-spun.

A **style tile** is an example of what a design might look like. Look at it as the beginning of a design library. These typically contain a few text styles, possibly a screen, colors, and words that describe the tone and voice.

# Collaborate with your team early and often

Design doesn't live in a vacuum. It's important to regularly share your ideas with engineers and product managers to get their insights. Often, you'll learn something to make your product better or life easier.

If you're finding yourself waiting several days between check-ins with your team or client, you're probably aren't communicating enough.

# Accessibility

**Under no circumstances** can we design without considering those with accessibility needs. It is neither difficult nor time-consuming to design with this in mind. Not only is it the right thing to do for users, it's the right thing to do for our clients because they are liable under the ADA.

## Design

Ensure you use proper color contrast ratios. There are design and web tools that help you do this. There are 3 levels of accessibility under the WCAG: A, AA, and AAA. We aim for the middle unless our client requires full AAA compliance. What's the difference? Stricter contrast ratios and a more limited color palette.

## Code

It's important to use semantic HTML, which is using the correct HTML tags (e.g. `article` , `section` ) so those using screen readers can understand the structure on a page.

When you're adding images, ensure to include proper `alt` text. It is not sufficient to use the file name, we need to take the time to accurately describe the image.

Similarly, when working with videos and audio, ensure you've got captions for them.

# Present effectively

The real magic happens here: how we present a design influences our client's response. To that end, we hold the following beliefs:

- We show work that's as close to reality as possible
- We will strive to remove all jargon from our presentations
- We scope our feedback

In showing work that's as close to reality as possible, this means we don't just send screenshots to our clients. Instead, we show designs to clients in HTML or something they can interact with. App design is a notable exception here, as it's much more complex to build a UI there, so Figma prototypes can suffice.

It's also important that we **don't show things with lorem ipsum**, clients often get tripped up by this. Instead, make data look as close to reality as possible. Taking the extra time to do this will help your clients get the most out of your time together. Remember, clients didn't go to design school and won't understand our shorthand. Make it easy for them to connect the dots.

Next, be mindful of your language. For example, instead of saying "once we finalize the IA and hierarchy, we'll move onto quantitative research," say "once we lay the foundations, we'll dig into some numbers." This makes it easier for us to connect with our clients, and it makes our intentions clear.

Scoping our feedback is equally important. To that end: one question we should never ask our client is "do you like this?" Get specific on the feedback you want, for example: "we want to get your feedback on if this interface steps out of line with your brand guidelines."

Another helpful tool in scoping feedback is Asana's do/try/consider framework. This is useful because it isn't always clear what's a directive or just a passing thought.

### Tactics

- Greyboxing
- Clickable Prototypes
- Do, Try, Consider
- Moodboards/Style Inspiration
- Tools we like

# Validation and user testing

We will adapt this part of the design process to the type and length of each engagement.

What's crucial is that we realize the need to build the right product *for the users*, not the product we want. We are not our users. To that end, we prefer real-world data, which can be accomplished in a few ways:

- User Interviews & Tests
- A/B tests, preference campaigns
- Analytics reviews
- Stakeholder review (see the section above on presenting effectively)
- Ad buy campaigns and landing pages to gauge interest
- See if PMs and clients can use your design system in figma