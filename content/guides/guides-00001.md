---
date: 2023-07-23
link title: Accessibility Audit Guide
title: Accessibility Audit Guide
weight: 10
tags: [Guides, Product]
---

# Success criteria for apps and websites

As of writing, the goal is to follow [WCAG 2.1](https://www.w3.org/TR/WCAG21/), but falling back to WCAG 2.0 is acceptable. The following success criteria are below. This has been helpfully adapted by [Kris Rivenburgh](https://medium.com/@krisrivenburgh).

### WCAG 2.0 AA

**Section 1: Alternatives**

- Alt text (1.1.1): All images and non-text content needs alt text (there are exceptions)
- Video & Audio alternatives (1.2.1): All video-only and audio-only content has a text transcript. Transcripts are clearly labeled and linked below the media.
- Closed captioning (1.2.2): All video with sound contains accurate closed captioning.
- Audio description (1.2.3): For any video, add an alternative video that includes an audio description of information not presented in the original video’s soundtrack (exceptions) or include a text .
- Live captions (1.2.4): Any live video presentations must have closed captions.
- Audio description (1.2.5): An audio description is optional under 1.2.3 level A but not in 1.2.5 AA.

**Section 2: Presentation**

- Website structure (1.3.1): Use proper markup techniques to structure your website’s content (e.g. use correct heading tags and HTML for ordered and unordered lists)
- Meaningful order (1.3.2): Present content in a meaningful order and sequence so that it reads properly.
- Sensory characteristics (1.3.3): When providing detailed instructions, make it so they aren’t reliant on a single sensory ability.
- Use of color (1.4.1): Do not rely on color alone to convey information.
- Audio control (1.4.2): Any audio must be able to be paused, stopped, or muted.
- Color contrast (1.4.3): There must be a color contrast ratio of at least 4.5:1 between all text and background.
- Text resize (1.4.4): Text must be able to be resized up to 200% without negatively affecting the ability to read content or use functions.
- Images of text (1.4.5): Do not use images of text unless necessary (e.g. logo).

**Section 3: User Control**

- Keyboard only (2.1.1): All content and functions on a website must be accessible by keyboard only (i.e. no mouse).
- No keyboard trap (2.1.2): Keyboard-only users must never get stuck on any part of the website; they must be able to navigate forwards and backwards.
- Adjustable time (2.2.1): If there any time limits on a website, users have the ability to turn it off, adjust it, extend it.
- Pause, stop, hide (2.2.2): If there is content that blinks, scrolls, moves, users must have the ability to pause, stop, or hide it.
- Three flashes or below (2.3.1): Web pages do not contain anything that flashes more than three times in any one second period.
- Skip navigation link (2.4.1): A “Skip to Content” or “Skip Navigation” link allows users to bypass the heading and go straight to the main content.

**Section 4: Understandable**

- Page titles (2.4.2): Each page of a website needs to have a unique and descriptive page title.
- Focus order (2.4.3): Users must be able to navigate through a website in a logical sequential order that preserves meaning.
- Link anchor text (2.4.4): The purpose of each link should be clear based on its anchor text (e.g. don’t use “click here”)
- Multiple ways (2.4.5): There are multiple ways to access different pages/information on a website (e.g. search bar, nav menus, sitemap, breadcrumbs, helpful links after content).
- Descriptive headings and labels (2.4.6): Headings and programmatic labels must be clear and descriptive. They do not need to be lengthy.
- Focus indicator (2.4.7): Any “user interface control” that receives focus from a keyboard user should indicate that focus on the current selected element (e.g. add a visible border around a text link).
- Website language (3.1.1): Set the language for your website (e.g. `html lang=en`)
- Language changes (3.1.2): Indicate any language changes for an entire page or within the content.

**Section 5: Predictability**

- No focus change (3.2.1): Nothing changes merely because an item receives focus; a user must actively choose to activate an item (e.g. hit enter to submit) before a change takes place.
- No input change (3.2.2): Nothing changes just because information is inputted into a field (e.g. form doesn’t auto submit once all fields are filled out).
- Consistent navigation (3.2.3): Keep navigation layout consistent throughout all pages of the website (e.g. same links in the same order).
- Consistent identification (3.2.4): Components that have the same function within a website are identified consistently (but not necessarily identically) (e.g. two check marks can indicate two different things as long as their function is different — one indicates “approved” on one page but “included” on another).
- Error identification (3.3.1): Make any form errors easy to identify, understand, and correct.
- Form labels and instructions (3.3.2): Programmatically label all form or input fields so that a user knows what input and what format is expected.
- Error suggestions (3.3.3): If an input error is automatically detected, then suggestions for correcting the error should be provided.
- Error prevention on important forms (3.3.4): For pages that create legal commitments or financial transactions or any other important data submissions, one of the following is true: 1) submissions are reversible, 2) the user has an opportunity to correct errors, and 3) confirmation is available that allows an opportunity to review and correct before submission.
- Parsing (4.1.1): Make sure HTML code is clean and free of errors, particularly missing bracket closes. Also, make sure all HTML elements are properly nested.
- Name, role, value (4.1.2): For all user interface components (including forms, links, components generated by scripts), the name, role, and value should all be able to be programmatically determined; make sure components are compatible with assistive technology.

### WCAG 2.1 AA

- Orientation** **(**1.3.4**): Style your website so that it does not lock on or require a single display mode
- Input (**1.3.5**): Make it so forms can autocomplete information for users.
- Reflow (**1.4.10**): Ensure someone can zoom in on your website without requiring scrolling or without causing poor experience.
- Non-text contrast (**1.4.11**): All meaningful non-text content on your website should have sufficient contrast with the background.
- Text spacing (**1.4.12**): Make sure your text spacing is able to be adjusted without causing a poor experience.
- Content on hover or focus (**1.4.13**): Make it so any additional content (e.g. pop-ups, submenus) can be dismissed or remain visible if the user desires
- Keyboard shortcuts (**2.1.4**): If you have a keyboard shortcut, make sure a user can either 1) turn it off, 2) there’s a way to add another key in the shortcut, and/or 3) have the shortcut only active while focusing on a specific component
- Pointer gestures (**2.5.1**): Provide simple alternatives (e.g. single tap vs. swipe) to potentially complex finger motions on touch screens
- Pointer cancellation (**2.5.2**): Provide a way to cancel the trigger when you click down on a mouse or press down/touch with your finger
- Label in Name (**2.5.3**): Make sure any programmatic labels you make are aligned with the corresponding visual text
- Motion Actuation (**2.5.4**): For any functions that are activated by motion, provide a simpler, alternative means of action. Also, give users the option to turn off motion activation.
- Status Messages (**4.1.3**): When a status message appears, it should be coded with role or properties so that people using assistive technologies (e.g. screen readers) are alerted without losing focus

# Other considerations

## Semantic HTML

It’s important To use the correct type of HTML element, as they tell search engines and accessibility devices what they’re looking at. If you see a layout done entirely with `div` or `span` , this should be a clue that work is needed. Sections should be organized with the `section` tag, blog posts contained within an `article` tag, and so on.

Jeremy Keith wrote a great book on HTML5 elements and how to use them.

## Text size

While this is general design consideration, it’s worth mentioning here that our text shouldn’t be too small. Shoot for your body copy to be around 16pt, and the smallest text (e.g. legal text in a footer) should be around 9pt.

## Apps

Each mobile platform has its own accessibility tools built in. I recommend navigating through the app with VoiceOver (or the Android equivalent) enabled. You should be able to hear each part meaningfully identified as you navigate.

Having a proper touch target size is critical. Apple's Human Interface Guidelines recommend 44x44pt as the minimum size for a touch area. It is possible to have smaller buttons, but ensure there is still enough invisible space around the button that makes it tappable.

# How to share out

If possible, make changes yourself or pair with an engineer. This will depend on the size of the site as well as the amount of issues.

It's important to show a list of what to address. This can take several forms:

- A Pivotal Tracker/Trello instance
- PDF

# Tools & Templates

You should prefer to use automated tools to assist us, not to perform the entire audit. You use these tools to identify problem areas, then apply expertise to solving them.

- [IBM Equal Access](https://chrome.google.com/webstore/detail/ibm-equal-access-accessib/lkcagbfjnkomcinoddgooolagloogehp?hl=en-US) (requires Chrome)
- [Stark](https://www.getstark.co/)