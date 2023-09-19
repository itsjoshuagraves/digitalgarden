---
date: 2013-04-03
bookToc: true
title: How smartphones could improve texting emergency services
tags: ["Medium"]
type: docs

originalURL: https://medium.com/@joshuamauldin/how-smartphones-could-improve-texting-emergency-services-876216fd8a5e
summary: "Early writing on how someone texting with emergency services would be beneficial with ideas on how it might work."
---


![Texting with 911.](/1x4bhld6IJ2CtkpC5QQc8EA.webp)

As of May 24, 2014, the main 4 carriers in the US will allow texting with 911. That’s great, but I wondered what it would look like if smartphones could build on top of that idea.

I want design to do good and feel like a moment of crisis is an ideal spot to employ thoughtful design to ease a difficult situation. Plus, it’s fun to weave different technologies together. What follows are some initial thoughts and a prototype. I’d love to hear feedback on both.

## Overview and Goals

I wanted to allow users to have an efficient way of engaging with emergency services when certain situations arise. Composing a text message could be time-consuming in a moment where every second counts; good design can make this easier.

It’s also worth considering various use cases. Someone may not be able (or in a place to) speak—the operating system should assist them in the best way possible. Think about a person who may have a physical impairment or may be in a situation where speaking could further endanger them.

Smartphones possess the ability to access user data, such as GPS-assisted location and contact information. Employing them along with the main types of emergency calls (fire, medical/accidents, crime) could speed the experience along greatly.

A portion of the device’s battery could be reserved for emergency use. During an emergency, this could suspend other applications or non-critical systems to maximize battery life.

This experience should fit within the standard experience and not create a new visual language or groundbreaking new user interface. It is worth noting that this experience would exist on multiple platforms (Android, Windows Phone, and Blackberry). Given the tools available ([Flinto](http://flinto.com/) and [Sketch](http://www.bohemiancoding.com/sketch/)!), it was easier to make it happen on iOS.

A person should be able to interact with emergency services in every way the operating system can create a text. This includes on the Lock Screen, the Messages app, and Siri. You’ll find more on that below.

It could also take advantage of the microphone during a text session if a user desires. They could initiate a one-way call without going into a call screen. This would be possible by working with a service like [Twilio](http://www.twilio.com/) to send and store this data. Collecting it could also be beneficial in a domestic violence situation. (Thanks to Ben Vandgrift for that idea.)

If a phone’s been connected to a vehicle’s collision sensors via Bluetooth, it could detect a crash and send a notice to emergency services in the event of an accident.

In the event that a message couldn’t be delivered, this application would continuously attempt delivery, rather than fail and ask the user to send it again.

## Prototyped options for sending emergency service messages

Interaction via the Lock Screen. [Play with the prototype on Flinto](https://www.flinto.com/p/a624bb9c).

![](/11yhXebq17Hhn8IKuWN_9pw.gif)

### **1) Lock Screen**

A user will tap the Emergency option on the Lock Screen, bringing up the dial pad, where the user now has the option to select Text. If a user selects Text, they can select their type of emergency, which reduces the time it takes to compose a text. They may select from any and all of the options presented, including not selecting any at all. (This is one situation where we may not want to force a choice.)

Most types of 911 calls fall into the categories of needing firefighters, medics, police, and sometimes all 3. I’ve accounted for this in this experience.

The user’s information will be pre-filled in a text message, and it will include their name, phone number, and GPS-assisted current location. The user is sent to a customized SMS screen.

**Update:** It’s important that we protect a person’s privacy. In light of that, texting through the lock screen keeps all other message threads hidden. (Thanks to @sulgi for the reminder)

### 2) Messages

A user initiates a text to emergency services (in the US, it’s 911). The interface adapts slightly to highlight calling 911 and adds a toolbar to include various information such as the user’s GPS-assisted current location and contact information.

### **3) Siri**

When a user engages Siri, perhaps by saying “Tell 911 that there’s been an accident here,” Siri will create the text, pre-fill it with the user’s name, phone number, and GPS-assisted current location. Then the user is sent to a customized SMS screen, the same as in Option 1.

## Closing thoughts

I did this as an exercise to see how good design could make a tough situation easier and more efficient. Even if this goes nowhere (I hope it doesn’t!), it feels important for designers to consider applying their knowledge to other areas.

I’d appreciate feedback on how to improve this concept. It would be wonderful to see a smartphone experience implemented—I’d love to know how, or if, that could happen.

### Further Reading & Data

- [http://www.911.gov/pdf/Current911DataCollection-072613.pdf](http://www.911.gov/pdf/Current911DataCollection-072613.pdf)
- [http://www.911.gov/whencall.html](http://www.911.gov/whencall.html)
- [http://www.fcc.gov/guides/text-911-quick-facts-faqs](http://www.fcc.gov/guides/text-911-quick-facts-faqs)


[Original post](https://medium.com/@joshuamauldin/how-smartphones-could-improve-texting-emergency-services-876216fd8a5e)
