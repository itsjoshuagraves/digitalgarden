---
date: 2017-05-09
title: Effective Animation
bookToc: true
tags: ["Medium"]
originalURL: https://medium.com/@joshuamauldin/effective-animation-86caade87215
summary: "Over the years, animation evolved from a nice-to-have concept to a core feature. Now, the best companies use animation to inform, delight, and reward the people using their products. Let’s talk about how animation helps and how to use it in our work."
---

![](/1*wFB80FBxmxR9PO2M_H2n7Q.webp)

Over the years, animation evolved from a nice-to-have concept to a core feature. Now, the best companies use animation to inform, delight, and reward the people using their products. Let’s talk about how animation helps and how to use it in our work.

## **Animation Provides Guidance**

I think a lot about this quote from Steve Krug in *Don’t Make Me Think*:

> “We don’t read pages. We scan them.”


Not only does it apply to interface design, it also applies to how we can use animation to communicate without words. While cleverly-written copy will likely be overlooked, an animation won’t because it doesn’t rely on words.

[https://youtu.be/8-vhbMx44qM](https://youtu.be/8-vhbMx44qM)

Flipboard for iOS.

Years ago, a trend in app design emerged where apps would have arrows on the screen, telling users where to look. That quickly became cumbersome and the need to simplify was apparent.

Flipboard came along and did a nice take on that with their onboarding. It’s not cluttered with a billion arrows pointing this way and that. It’s subtle, and we know we can swipe up to get more because that’s what the animation showed. We’re also able to understand it quicker since you don’t have to read.

[https://youtu.be/hokZqdlKuR0](https://youtu.be/hokZqdlKuR0)

SkillPop uses Stripe, which is pretty great when it comes to forms.

Another part of providing guidance is letting someone know when we need their attention. With Stripe, we see that the form shakes a bit if there’s an error, much like we shake our head when something is incorrect.

What can we take from this? When we show, rather than tell, we reduce a person’s cognitive load. This makes it easier to get into using the product. After all, who reads instruction manuals unless they absolutely have to?

## **Animation Reduces Frustration and Abandonment**

Google saw a 20% drop-off for adding half a second to their page load time. Similarly, Amazon saw a significant drop in sales for every tenth of a second they added to page load time.

This highlights how critical speed and performance are. There are times when we aren’t able to improve speed—perhaps our customers have a slower connection or the services calls are lagging. This is the perfect opportunity for animation to assist.

Viget Labs did a neat experiment showing that people are willing to wait around longer if there’s a branded loading animation. [Their case study is worth a read](https://www.viget.com/articles/experiments-in-loading-how-long-will-you-wait), but here’s the highlight: custom loading animations have an overall lower abandonment and higher wait time.

[https://youtu.be/0-UY5Xy5JRQ](https://youtu.be/0-UY5Xy5JRQ)

TunnelBear for iOS. Watch with sound on.

Here’s another example of how animation can decrease frustration: TunnelBear, a…*beary* good VPN client (not even a little bit sorry for that pun). Connecting to a VPN usually takes at least a few seconds or longer, and there’s only so much performance optimization that can be done.

Not only does TunnelBear use animation to show us what’s going on while it establishes a secure connection, it uses animation in a novel way while we wait. We see our little bear begin to dig, then it reappears a moment later on the other side of the map. This helps us understand how VPNs work as well as makes the wait easier.

[https://youtu.be/mE0mh16w5Vo](https://youtu.be/mE0mh16w5Vo)

Hopper for iOS.

Another example is Hopper, an app for finding the best price on flights. Searching and communicating with all the APIs that each airline company has takes time — some APIs have abysmal response times.

Hopper shows us a happy little rabbit hopping as fast as it can as the loader, which helps us think it’s working as fast and hard as possible. Sometimes the perception of speed can be as important as actual loading speed.

[https://youtu.be/PPLDDb1Kfew](https://youtu.be/PPLDDb1Kfew)

Kayak for iOS

If we compare this with Kayak, it feels like we’re in a different world. While the load times are almost the same, looking at a progress bar fills people with boredom and they just want it to be over.

What can we take from this? If we put effort into respecting another person’s time, they’re more likely to stick around.

## **Animation Makes an Emotional Connection**

The animations we give a product are a direct extension of the brand and need special attention. Here are two examples.

[https://youtu.be/_IaQo59eoYE](https://youtu.be/_IaQo59eoYE)

Pause, a meditation app for iOS.

Pause, an app which practically radiates relaxation and equanimity, does a perfect job of helping someone relax. The animations here are slow, deliberate, and calming. Any anxiety or feeling of being over-busy melts away as the little circle grows and pulls in tinier circles.

[https://youtu.be/PQ3Q_WOKUtY](https://youtu.be/PQ3Q_WOKUtY)

Zappos and the Super Cat for iOS.

The next app is a little more fun, and it’s Zappos. Part of their brand and mission statement is to “Create Fun and A Little Weirdness.” That’s why I was surprised and delighted to see a tiny Super Cat delivering a pair of Chucks to the cart. It made me want to add several more 😸.

## **Best Practices**

It’s great to talk about how animation can help, but let’s talk for a bit about how to put this into action.

### **Be intentional and match the brand**

Animation is best when it is intentional and reinforces the experience. Use this chart to help plot what kinds of animations to use.

![](/1*KbzAvqg5pCDG12QzB98wXw@2x.webp)

The Brand Personality Spectrum, adapted from [somewhere].

If we’re designing a quiet, meditative app like Pause, that means it’s probably more familiar, happy, reserved, quiet, and off the beaten path. We’d probably avoid giant pops and flashy transitions. It may be perfectly fine, however, to use this with an exercise app designed to motivate.

### **Timing is everything**

Most people’s brains take about 200ms to begin processing something. [Anything less than 100ms is considered instant](https://www.nngroup.com/articles/response-times-3-important-limits/) since our brains have trouble processing information at that speed.

![](/1*3sjXQNVdan_52LwlVHntjg.webp)

Animation awareness spectrum, adapted from [Val Head’s Designing Interface Animation](http://rosenfeldmedia.com/designing-interface-animation/designing-interface-animation/) and [Aerotwist](https://aerotwist.com/blog/flip-your-animations/)

This means the best spot for most animations is 200–500ms. There’s not a hard and fast rule that says every animation should be in this range—animation is more art than science. If we’re working with larger, more complicated animations, they can and should take longer because of their complexity. Compressing them to fit an arbitrary number will only make it appear choppy.

That being said, it isn’t usually advisable to have animations lasting longer than one second unless it’s with a loading sequence. The more we delay someone from completing their task, the less likely they are to stick around. Animation must help rather than hinder.

### **Don’t break accessibility**

Not everyone can hang with motion. Some of us get motion sickness. Offering a low-animation setting can help alleviate that feeling. This can be the difference between someone who stays and someone who bails on an app.

After iOS 7’s beta, people reported having motion sickness from all the visual effects. In response, Apple released a low animation setting to address that.

Finally, for people with a history of epilepsy: we need to avoid flashing the screen or big color changes more than twice a second. Anything faster than that is a trigger.

## **Wrapping Up**

In closing, animation helps people understand how to use an app, gives them feedback without overburdening their brains, and helps people create an emotional connection. Make sure to be intentional with all of your animations, time them appropriately, and don’t cause anyone motion sickness or worse by overdoing it.

## **Further Reading**

If you’re looking to read more, I highly recommend peeking at these links.

- [History of Animation](http://history-of-animation.webflow.io/) (Webflow)
- [Designing Interface Animation](http://rosenfeldmedia.com/books/designing-interface-animation/) (Val Head)
- [The Illusion of Life](https://vimeo.com/93206523) (Cento Lodigiani)
- [12 Basic Principles of Animation](https://en.wikipedia.org/wiki/12_basic_principles_of_animation) (Wikipedia)


[Original post](https://medium.com/@joshuamauldin/effective-animation-86caade87215)