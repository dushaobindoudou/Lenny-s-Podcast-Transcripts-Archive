# Logan Kilpatrick - Lenny's Podcast Insights
## Logan Kilpatrick - Lenny's播客洞见

---

## ## 关于嘉宾 | About the Guest

**Logan Kilpatrick** 与Lenny进行了关于产品管理、领导力和打造成功产品的深入对话。

**Logan Kilpatrick** 与Lenny进行了深入对话，讨论产品管理、领导力和打造成功产品的经验。

---

## ## 核心要点 | Key Takeaways

### So the one that I had in mind, so I had a buddy of mine, [inaudible 00

30:28], who's the CEO of a company called Runway built this thing called Universal Primer which helps you learn. It's described as, "Learn everything about anything," and basically, I think, it's kind of this Socratic method of helping you learn stuff. So it's like, "Explain how transformers work in LMs," and then it just kind goes through stuff and then asks you questions, I think, and helps you learn new concepts. And I think it's the number two education GPT.
Logan Kilpatrick :

---

## ## 完整对话 | Full Conversation

*以下是完整对话记录。*

*以下是完整对话记录。*

**So the one that I had in mind, so I had a buddy of mine, [inaudible 00**:

30:28], who's the CEO of a company called Runway built this thing called Universal Primer which helps you learn. It's described as, "Learn everything about anything," and basically, I think, it's kind of this Socratic method of helping you learn stuff. So it's like, "Explain how transformers work in LMs," and then it just kind goes through stuff and then asks you questions, I think, and helps you learn new concepts. And I think it's the number two education GPT.
Logan Kilpatrick :

**I love that. [inaudible 00**:

30:53] is incredible, so...
Lenny :
Yes, it's true. Let me tell you about a product called Arcade. Arcade is an interactive demo platform that enables teams to create polished, on-brand demos in minutes. Telling the story of your product is hard and customers want you to show them your product, not just talk about it or gate it. That's why Product Four teams such as Atlassian, Carta and Retool use Arcade to tell better stories within their homepages, product change logs, emails and documentation.
:
But don't just take my word for it. Quantum Metric, the leading digital analytics platform created an interactive product tour library to drive more prospects. With Arcade, they achieved a 2X higher conversion rate for demos and saw five times more engagement than videos. On top of that, they built the demo 10 times faster than before. Creating a product demo has never been easier. With browser-based recording Arcade is the no-code solution for building personalized demos at scale.
:
Arcade offers product customization options, designer approved editing tools and rich insights about how your viewers engage every step of the way. Ready to tell more engaging product stories that drive results? Head to arcade.software/lenny and get 50% off your first three months. That's arcade.software/lenny.
:
I want to talk about just what it's like to work at OpenAI and how the product team operates and how the company operates. So you worked at... Your two previous companies were Apple and NASA, which are not known for moving fast. And now you're at OpenAI, which is known for moving very fast, maybe too fast for some people's taste, as we saw it with the whole board thing. And so what I'm curious is just what is it that OpenAI does so well that allows them to build and ship so quickly and at such a high bar? Is there a process or a way of working that you've seen that you think other companies should try to move more quickly and ship better stuff?
Logan Kilpatrick :
Yeah, there's so many interesting trade-offs and all of this tension around how quickly companies can move. I think for us, again, if you think about Apple as an example, if you think about NASA as an example, just older institutions, lots of... Over time, the tendency is things slow down. There's additional checks and balances that are put in place, which drags things down a little bit. So we're young and a new company, so we don't have a lot of that institutional legacy barriers that have been put in place.
:
I think the biggest thing, and there's a good Sam tweet somewhere in the ether about this from, I think, 2022 or something like that, but finding people who are high agency and work with urgency is one of the most... If I was hiring five people today, those are some of the top two characteristics that I would look for in people because you can take on the world if you have people who have high agency and not needing to either get 50 people's different consensus, because you have people who you trust with high agency and they can just go and do the thing, I think, is one of the most... It is the most important thing, I'm pretty sure, if you were to distill it down.
:
And I see this in folks that I work with. Folks are so high agency. They see a problem and they go and tackle it. They hear something from our customers about a challenge that they're having and they're already pushing on what the solution for them is and not waiting for all the other things to happen that I think traditional companies are stuck behind because they're like, "Oh, let's check with all these seven different departments to try to get feedback on this." People just go and do it and solve the problem. And I love that. It's so fun to be able to be a part of those situations.
Lenny :
That is so cool. I really like these two characteristics because I haven't heard this before. Those are the two, maybe the two most important things you guys look for, high agency, high urgency. To give people a clear sense of what these actually look like when you're hiring, you shared maybe this example of customer service. Someone's hearing a bug and then going to fix it. Is there anything else that can illustrate what that looks like, high agency? And then a similar question on urgency other than just move, move, move, ship, ship, ship.
Logan Kilpatrick :
I think the assistants API that we released for dev day, we continue to get this feedback from developers that people wanted these higher levels of abstraction on top of our existing APIs, and a bunch of folks on the team just came together and were like, "Hey, let's put together what the plan would look like to build something like this," And then very quickly came together and actually built the actual API that now powers so many people's assistant applications that are out there. And I think that's a great example of it wasn't this top down, oh, someone's sitting there being like, "Oh, let's do these five things," and then like, "Okay, team, go and do that." It's like people really seeing these problems that are coming up and knowing that they can come together as a team and solve these problems really quickly. And I think the assistants API, and there's like 1,001 other examples of teams taking agency and doing this, but I think that's a great one at the top of my head
Lenny :
That makes me want to ask. Just how does planning work at OpenAI? So in this example is just like, "Hey, we think we need to build this. Let's just go and build it." I imagine there's still a roadmap and priorities and goals and things that that team had. How does road mapping and prioritization and all of that generally work to allow for something like that?
Logan Kilpatrick :
I think this is one of the more challenging pieces at OpenAI. There's so many. Everyone wants everything from us, and today, especially, in the world of ChatGPT and how large and well-used our API is, people will just come to us and say, "Hey, we want all of these things." I think there's a bunch of core guiding principles that we look at. One, going back to the mission, is this actually going to help us get to AGI? So there's a huge focus on there's this potential shiny reward right in front of us, which is optimize user engagement, or whatever it is. And is that really the thing? Maybe the answer is yes. Maybe that is what is going to help us get to AGI sooner, but looking at it through that lens I think is always the first step of deciding any of these problems.
:
I think, on the developer side, there's also these core tenets of reliability like, "Hey, it would be awesome if we had additional APIs that did all these cool things like new endpoints, new modalities, new abstractions, but are we giving customers a robust and reliable experience on our API?" And that's often the first question. And I think there have been times where we've fallen short on that, and there was a bunch of other things that we've been thinking about doing and really bringing the focus and priority back to that reliability piece because, at the end of the day, nobody cares if you have something great if they can't use it robust and reliably.
:
So there's these core tenets. And I think, again, we have very, other than all the principles about how we're making the decision, I think the actual planning process is pretty standard. We come together. There's H1 Q1 goals. We all sprint on those. I think the real interesting thing is how stuff changes over time. You think we're going to do these very high level things and new models, new modalities, whatever it is. And then as time goes on, there's all of this turmoil and change, and it's interesting to have mechanisms to be like, "Hey, how do we update our understanding of the world and our goals as everything the ground changes underneath of us as is happening in the craziness of the AI space today?"
Lenny :
It's interesting that it sounds a lot like most other companies. There's H1 planning. There's Q1 planning. Are there metrics and goals like that that you guys have OKRs or anything like that? Or is it just, Here we're going to launch these products?"
Logan Kilpatrick :
I think it's much higher level. I actually don't think OpenAI is a big OKR company. I don't think teams do OKRs today and I don't have a good understanding of why that's the case, whether or not. I don't even know if OKRs are still the industry. You're probably talking to a lot more folks about who are making those decisions. So I'm curious. Is that something that you're seeing from folks? Is it still common for people to do OKRs?
Lenny :
Yeah, absolutely. Many companies use OKRs, love OKRs. Many companies hate OKRs. I'm not surprised that OpenAI is not an OKR driven company. Along those lines, I don't know how much you can share about all this stuff, but how do you measure success for things that you launch? I know there's this ultimate goal, AGI. Is there some way to track we're getting closer? What else do you guys look at when you launch, say DPT Store or assistants or anything that's like, "Cool, that was exactly what we're hoping for." Is it just adoption?
Logan Kilpatrick :
Yeah, adoption is a great one. I think there's a bunch of metrics around revenue, number of developers that are building on our platform, all those things. And a lot of these, and I don't want to dive... I'll let Sam or someone else on our leadership team go more into details, but I think a lot of these are actual abstractions towards something else. Even if revenue is a goal, it's like revenue is not actually the goal. Revenue is a proxy for getting more compute, which is then actually what helps us get towards getting more GPUs so that we can train better models and actually get to the goal. So there's all these intermediate layers where even if we say something is the goal, and you hear that in a vacuum and you're like, "Oh, well OpenAI just wants to make money," and it's like, "Well, really money is the mechanism to get better models so that we can achieve our mission." And I think there's a bunch of interesting angles like that as well.
Lenny :
I don't know if I've heard of a more ambitious vision for a company, to build artificial general intelligence. I love that. I imagine many companies are like, "What's our version of that?" Before we leave this topic, is there anything else that you've seen OpenAI do really well that allows it to move this fast and be this successful? You talked about hiring people with higher agency and high urgency. Is there anything else that's just like, "Oh wow, that's a really good way of operating?" I imagine part of it's just hiring incredibly smart people. I think that's probably an unsaid thing, but yeah, anything else?
Logan Kilpatrick :
I think there's a non-trivial benefit to using Slack, and I think maybe that's controversial and maybe some people don't like Slack, but OpenAI has such a slack heavy culture and it really... The instantaneous real time communication on Slack is so crucial. And I just love being able to tag in different people from different teams and get everybody coalesced. So everybody is always on Slack, so even if you're remote or you're on a different team or in a different office, so much of the company culture is ingrained in Slack, and it allows us to really quickly coordinate where it's actually faster to send someone a Slack message sometimes than it would be to walk over to their desk because they're on Slack and they're going to be using it.
:
And I saw, if you saw, the recent Sam and Bill Gates interview, but Sam was talking about how Slack is his number one most used app on his phone and, "I don't even look at the time thing on my phone anymore because I don't want to know how long I'm using Slack," but I'm sure the Salesforce people are looking at the numbers and they're like, "This is exactly what we wanted."
Lenny :
I also love Slack. I'm a big promoter Slack. I think there's a lot of Slack hate, but such a good product. I've tried so many alternatives and nothing compares. I think what's interesting about Slack for you guys is one of the... You don't know if someone in there is just an AGI, that is not actually a person that's just there working at the company.
Logan Kilpatrick :
I know there are real people. There is no AGIs yet. But I think, yeah, even Slack is building a bunch of really cool AI tools, which I'm excited to... And that's why there's so much cool AI progress. And at the end of the day, it's so exciting, from being a consumer of all these new AI products. Google's a great example. I'm so happy that Google is doing really cool AI stuff because I'm a Google Docs customer and I love using Google Docs. I like a bunch of their other products, and it's awesome that people are building such useful things around these models.
Lenny :
How big is the OpenAI team at this point, whatever you can share? Just to give people a sense of the scale.
Logan Kilpatrick :
Yeah, I think the last public number was something around like 750 near the end of last year, 780 or something like that near the end of last year. And we're still growing so quickly, so I won't be the messenger to share the specific updated numbers, but the team is growing like crazy and we're also hiring across all of our engineering teams and PM teams, so folks who are interested, would love to hear from folks who are curious about joining.
Lenny :
Maybe one last question here. So you're growing, maybe getting to 1,000 people, clearly still very innovative and moving incredibly fast. Is there anything you've seen about what OpenAI does well to enable innovation and not slow down new big ideas?
Logan Kilpatrick :
Yeah, there's a couple of things, one of which is the actual research team, who seed most of the innovation that happens at OpenAI, is intentionally small. Most of the growth that OpenAI has seen is around our customer facing roles, our engineering roles to provide the infrastructure for ChatGPT and things like that. The research team is, again, intentionally kept small and there's all of this talk. And it's really interesting. I just saw this thread from one of our research folks who was talking about how in a world where you're constrained by the amount of GPU capacity that you have as a researcher, which is the case for open AI researchers, but also researchers everywhere else, each new researcher that you add is actually a net productivity loss for the research group unless that person is up-leveling everyone else in such a profound way that it increases the efficiency.
:
If you just add somebody who's going to go and tackle some completely different research direction, you now have to share your GPUs with that person and everyone else is now slower on their experiments. So it's a really interesting trade-off that research folks have that I don't think product folks... If I add another engineer to our API team or to some of the ChatGPT teams, you can actually write more code and do more. And that's actually a net beneficial improvement for everybody. And that's always not the case in the case of researchers, which is interesting, in A GPU constrained world, which hopefully we won't always be in.
Lenny :
I want to zoom out a bit and then there's going to be a couple follow-up questions here. Where are things heading with OpenAI? What's in the near future of what people should expect from the tools that you guys are going to have in launch?
Logan Kilpatrick :
Yeah, new modalities. I think ChatGPT continuing to push all of the different experiences that are going to be possible. Today, ChatGPT is really just text in, text out or, I guess three months ago, it was just text in, text out. We started to change that with now you can do the voice mode and now you can generate images and now you can take pictures. So I think continuing to expand the way in which you interface with AI through ChatGPT is coming.
:
I think GPTs is our first step towards the agent future. Again, today when you use A GPT, it's really you send a message, you get an answer back almost right away, and that's kind of the end of your interaction. I think as GPTs continue to get more robust, you'll actually be able to say, "Hey, go and do this thing and just let me know when you're done. I don't need the answer right now. I want you to really spend time and be thoughtful about this."
:
And again, if you think back to all these human analogies, that's what we do as humans. I don't expect somebody, when I ask them to do something meaningful for me, to do it right away and give me the answer back right away. So I think pushing more towards those experiences is what is going to unlock so much more value for people.
:
And I think the last thing is GPTs as this mechanism to get the next few hundred million people into ChatGPT and into AI. So I think if you've had conversations with people who aren't close to the AI space, oftentimes you talk about, even if they've heard of ChatGPT... A lot of people haven't heard of ChatGPT, but if they have, they show up in ChatGPT and they're like, "I don't really know what I'm supposed to do with this blank slate. I can kind of do anything. It's not super clear how this solves my specific problem."
:
But I think the cool thing about GPTs is you can package down like, "Here's this one very specific problem that AI can solve for you and do it really well," and I can share that experience with you and now you can go and try that GPT, have it actually solve the problem and be like, "Wow, it did this thing for me. I should probably spend the time to investigate these five other problems that I have to see if AI can also be a solution to those." So I think so many more people are going to come online and start using these tools because very narrow vertical tools are what's going to be a huge unlock for them.
Lenny :
So in that last case, a classic horizontal product problem where it does so many things and people don't know what exactly it should do for them. So that makes a ton of sense. Just being a lot more template oriented, use case specific, helping people onboard makes tons of sense. A common problem for so many SaaS products out there. The other ones you mentioned, which was really interesting, basically more interfaces to more easily interact with OpenAI voice. You mentioned audio and things like that. That makes tons of sense. And then this agents piece where the idea is, instead of just it's a chat, it's like, "Hey, go do this thing for me."
:
Kind of along those lines, GPT-5, we touched on this a bit. There's a lot of speculation about the much better version. People just have these wild expectations, I think, for where GPT is going. GPT-5 is going to solve all the world's problems. I know you're not going to tell me when it's launching and what it's going to do, but I heard from a friend that there's kind of this tip that when you're building products today, you should build towards a GPT-5 future, not based on limitations of GPT-4 today. So to help people do that, what should people think about that might be better in a world of GPT-5? Is it just faster? It's just smarter? Is there anything else that might be like, "Oh wow, I should really rethink how I'm approaching my product?"
Logan Kilpatrick :
If folks have looked through the GPT-4 technical report that we released back in March when GPT-4 came out, GPT-4 was the first model that we trained where we could reliably predict the capabilities of that model beforehand based on the amount of computes that we were going to put into it. We did a scientific study to show like, "Hey, this is what we predicted and here is what the actual outcome was." So it'll be, one I think, just as somebody who's interested in technology, but interesting to see does that continue to hold for GPT-5, and hopefully we'll some of that information whenever that model comes out.
:
I also think you can probably draw a few observations. One of them, which is GPT-4 came out. The consensus from the world is, "Everything is different. All of a sudden everything is different. This changes the world. This changes everything." And then slowly but surely, we come back to reality of like, "This is a really effective tool and it's going to help solve my problems more effectively."
:
And I think that is the, undoubtedly, the lens in which people should look at all of these model advancements, like GPT-5 is surely going to be extremely useful and solve some whole new echelon of problems. Hopefully it'll be faster. Hopefully It'll be better in all these ways, but fundamentally, the same problems that exists in the world are still going to be the same problems. You now just have a better tool to solve those problems.
:
And I think going back to vertical use cases, I think people who are solving very specific use cases are just now going to be able to do that much more effectively. I don't think that's going to... People have these unrealistic expectations that GPT-5 is going to be doing back flips in the background in my bedroom while it also writes all my code for me and talks on the phone with my mom or something like that.
:
I'm like, "That's not the case." It's just going to be this very effective tool, very similar to GPT-4, and it's also going to be become very normal very quickly. And I think that is actually a really interesting piece. If you can plan for the world where people become very used to these tools very quickly, I actually think that's an edge, and assuming that this thing is going to absolutely change everything, and in many ways I think it's actually a downside, is the wrong mental framing to have of these tools as they come out.
Lenny :
Kind of along these lines, you guys are investing a lot into B2B offerings. I think half the revenue, last I heard, was B2B and then half is B2C. I don't know if that's true, but that's something I heard. What is it that you get if you work with opening AI as a company, as a business? What does it unlock? Is it just called OpenAI Enterprise? What's it called and what do you get as a part of that?
Logan Kilpatrick :
Yeah, so I think a lot of our B2B customers are using the API to build stuff. So I think that's one angle of it. I think if you're a ChatGPT B2B customer, we sell Teams, which is the ability to get multiple subscriptions of ChatGPT packaged together. We also have an enterprise version of ChatGPT. There's a bunch of enterprise-y things that enterprise companies want, around SSO and stuff like that, related to ChatGPT Enterprise.
:
I think the coolest thing is actually being able to share some of these prompt templates and GPTs internally. So again, you can make custom things that work really well for your company with all of the information that's relevant to solving problems at your company and share those internally. And to me, that's like you want to be able to collaborate with your teammates on the cool things you create using AI. So that's a huge unlock for companies. I think that those are the two biggest value adds. There's higher limits and stuff like that on some of those models, but I think being able to share your very domain specific applications is the most useful thing.
Lenny :
I think if you're a company listening and you think a lot of employees are using ChatGPT, basically the simplest thing you could do is just roll it up into a business account with single sign-on and that probably saves you money and makes it easier to coordinate and administer.
Logan Kilpatrick :
Yeah, there's also a bunch of security stuff too, like if you want to control. You don't want people to use certain GPTs from the GPT store because you're worried about security or privacy and stuff like that. You don't want your private data going in places. It makes a lot of sense to sign up for that so that you have a little bit more control over what's happening.
Lenny :
Okay, got it. There's a launch happening tomorrow, I think, after we're recording this. Can you talk about what is new, what's coming out? I think this is going to come out a couple weeks after recording, but just what should people know that's new that's coming out from OpenAI tomorrow in our world?
Logan Kilpatrick :
Yeah, updated, so there's a few different things. A couple of quick ones are updated GPT-4 Turbo model, updated the preview model that we released that dev day. There's an updated version of that. It fixes this, if folks have seen online people talking about this sort of laziness phenomenon in the model. We improve on that and it fixes a lot of the cases where that was the case. So hopefully the model will be a little bit less lazy. The big thing is the third generation embeddings model. So we were talking off-camera before recording about all of the cool use cases for embedding. So if folks have used embeddings before, it's essentially the technology that powers many of these question and answering with your own documentation or your own corpus of knowledge. And like you were saying, you actually have a website where people can ask questions about recordings of the podcast.
Lenny :
Lennybot.com. Check it out.
Logan Kilpatrick :
Yeah, lennybot.com. And my assumption was that lennybot.com is actually powered by embedding. So you take all of the corpus of knowledge. You take all the recordings, your blog post. You embed them, and then when people ask questions, you can actually go in and see the similarity between the question and the corpus of knowledge and then provide an answer to somebody's question and reference an empirical fact, something that's true from your knowledge base. And this is super useful and people are doing a ton of this. It's like trying to ground these models in reality, in what they know to be true. We know all the things from your podcast to be at least something that you've said before and to be true in that sense, and we can bring them into the answer that the model is actually generating in response to a question. So that'll be super cool.
:
And these new V3 embeddings models, again, state-of-the-art performance, the cool thing is actually the non-English performance has increased super significantly. I think historically, people really were only using embeddings for... It only worked really well for English, and I think now you can use it across so many new languages because it's just so much more performant across those languages and it's five times cheaper as well, which is wonderful. There's no better feeling than making things cheaper for people. I love it. I think now it's like you can embed, I'm pretty sure, it was like 62,000 pages of text for $1, which is very, very cheap. So lots of really cool things that you can do with embeddings and exciting to see people invent more stuff.
Lenny :
What a deal. Final question before we get to a very exciting lightning round. Say you're a product manager at a big company, or even a founder, what do you think are the biggest opportunities for them to leverage the tech that you guys are building, GPT-4, all the other APIs? How should people be thinking about, "Here's how we should really think about leveraging this power in our existing product," or new product, whichever direction you want to go.
Logan Kilpatrick :
Yeah, I think going back to this theme of new experiences is really exciting to me. I think consumers are just going to be... You are going to have an edge on other people if you're providing AI that's not accessible in a Chatbot. People are using a ton of chat and it's a really valuable service area. It's clearly valuable because people are using it. But I think products that move beyond this chat interface really are going to have such an advantage. And also, thinking about how to take your use case to the next level. I've tried a ton of chat examples that are very, very basic and providing a little bit of value to me, but I'm like, "Really this should go much further and actually build your core experience from the ground up."
:
I've used this product that allows you to essentially manage or view the conversations that are happening online around certain topics and stuff like that. So I can go and look online. What are people saying about GPT-4? And what I just said out loud, "What are people saying about GPT-4," is the actual question that I have. And in a normal product experience today, I have to go into a bunch of dashboards and change a bunch of filters and stuff like that. And what I really want is just ask my question. What are people doing? What are people saying about GPT-4? Get an answer to that question in a very data grounded way.
:
And I've seen people solve part of this problem where, oh, they'll be like, "Oh, well here's a few examples of what people are saying and, well, that's not really what I want. I want this summary of what's happening." And I think it just takes a little bit more engineering effort to make that happen. But I think it's like that is the magical unlock of like, "Wow, this is an incredible product that I'm going to continue to use," instead of like, "Yeah, this is kind of useful, but I really want more."
Lenny :
Awesome. I'll give a shout-out to a product. I'm not an investor, but I know the founder, called visualelectric.com, which I think is doing exactly this. It's basically a tool specifically built for creatives, I think specifically graphic design, to help them create imagery. So there's like Dali, obviously, but this takes it to a whole new level where it's kind of this canvas, infinite canvas, that you could just generate images, edit, tweak them, and continue to rate until you have the thing that you need. Visualelectric.com.
Logan Kilpatrick :
I'm going to try that out. Is it similar to Canva?
Lenny :
It's even more niche, I think, for more sophisticated graphic design, I think, is the use case. But I'm not a designer, so I'm not the target customer. But I will say my wife is a graphic designer. She had never used AI tools. I showed her this and she got hooked on it. She paid for it without even telling me that she was going to become a paid customer, and she created imagery of our dog and all this art. And now it's like on our TV. The art she created is now sitting... It's like we have a frame TV, and that's the image on our TV. So anyway...
Logan Kilpatrick :
I love that. What was it called again?
Lenny :
Visualelectric.com. Anyway, anything else you wanted to touch on or share before we get to a very exciting lightning round?
Logan Kilpatrick :
I've made this statement a few times online and other places, but for people who have cool ideas that they should build with AI, this is the moment. There are so many cool things that need to be built for the world using AI. And again, if I or other folks on the team at OpenAI can be helpful in getting you over the hump of starting that journey of building something really cool, please reach out. The world needs more cool solutions using these tools, and would love to hear about the awesome stuff that people are building.
Lenny :
I would've asked you this at the end, but how would people reach out? What's the best way to actually do that?
Logan Kilpatrick :
Twitter, LinkedIn. My email should be findable somewhere. I don't want to say it and then get slammed with a bunch of email. You should be able to sign my email, if you need it, online somewhere. But yeah, Twitter and LinkedIn is usually the easiest place.
Lenny :
And how do they find you on Twitter?
Logan Kilpatrick :
It's just Logan Kilpatrick, or I think my name shows up as Logan.GPT or-
Lenny :
Logan.GPT?
Logan Kilpatrick :
Or official Logan K.
Lenny :
Yeah. Awesome. Okay. And we'll link into it in the show notes. Amazing. Well Logan, with that, we've reached a very exciting lightning round. Are you ready?
Logan Kilpatrick :
I'm ready.
Lenny :
First question, what are two or three books that you've recommended most to other people?
Logan Kilpatrick :
I think the first one is one that I read a long time ago and came back to recently, is the One Room Schoolhouse by Sal Khan. Incredible. Yeah, I don't want... It's the lightning round so I won't say too much, but incredible story and AI is what is going to enable Sal Khan's vision of a teacher per student to actually happen. So I'm really excited about that. And the other one is, that I always come back to, is Why We Sleep. Sleep science are so cool. If you don't care about your sleep, it's one of the biggest up-levels that you can do for yourself.
Lenny :
What is a favorite recent movie or TV show that you really enjoyed?
Logan Kilpatrick :
I'm a sucker for a good inspirational human story. So I watched, with my family recently over the holidays, this Gran Turismo movie, and it's a story about someone who, a kid from London, who grew up doing SIM racing, which is a virtual race car, and did this competition, ended up becoming a real professional race car driver through some competition. And it's just really cool to see someone go from driving a virtual car to driving a real car and competing in the 24-hour Le Mans and all that stuff.
Lenny :
I used to play that game and it was a lot of fun, but I don't think I have any clue how to drive a real car, race car. So that's inspiring. Do you have a favorite interview question that you'd like to ask candidates that you're interviewing?
Logan Kilpatrick :
Yeah, I'm always curious to hear what people's... The thing that they so strongly believe that people disagree with them on.
Lenny :
What do you look for in an answer that seems like, Wow, that's a really good signal?"
Logan Kilpatrick :
Oftentimes, it's just an entertaining question to ask in some sense, but it's also... It's interesting to see what somebody's deeply held strong belief is, I think. And not to judge whether or not I believe in that, but just curious to see why people feel that way.
Lenny :
What is a favorite product that you've recently discovered that you really like?
Logan Kilpatrick :
On the narrative of sleep, I have this really nice sleep mask from this company called... Not being paid. I just say this, but it's called Manta Sleep or something like that. It's a weighted sleep mask and it feels incredible when I... I don't know. Maybe I just have a heavy head or something like that, but it feels good to wear a weighted sleep mask at night. I really appreciate it.
Lenny :
I have a competing sleep mask that I highly recommend. I'm trying to find it. I've emailed people about it a couple of times in my newsletter for gift guides.
Logan Kilpatrick :
Yeah.
Lenny :
Okay. My favorite is called the Waoaw Sleep Mask, W-A-O-A-
Logan Kilpatrick :
What do you like about it?
Lenny :

**W-A-O-A-W. I'll link to it in the show notes. It makes a lot of room. It's very large and there's space for your eyes, so your eyelashes and whatever eyes aren't pressed on, and it just fits really nicely around the head. And my wife, we both wear eye masks at night. It just, speaking of sleep, really helps us sleep. [inaudible 01**:

02:37] It doesn't have the weight-ness piece, so it might be worth trying, but everyone I've recommended this to is like, "That changed my life. Thank you for helping me sleep better." And so we'll link to [inaudible 01:02:51].
Logan Kilpatrick :
Look at that.
Lenny :
Look at us. So adult. Two more questions. Do you have a favorite life motto that you often come back to share with friends or family, either in work or in life?
Logan Kilpatrick :
Yeah, I've got it. It's on a Post-It note that I... Right behind my camera and it's "Measure in hundreds." I love this idea of measuring things in hundreds, and it's for folks who are at the beginning of some journey. I talk to people all the time, they're like, "Yeah, I've tried this thing and it hasn't worked." And if your mental model is to measure in hundreds, "I measure in hundreds," the five times that you failed at something, you failed and tried zero times. And I love that. It's such a great reminder that everything in life is built on compounding and multiple attempts at stuff. And if you don't try enough times, you're never going to be successful at it.
Lenny :
I love that. I could see why you are successful at OpenAI and why you're a good fit there. Final question. So I asked ChatGPT for a very silly question. "Give me a bunch of silly questions to ask Logan Kilpatrick, head of developer relations at OpenAI," and I went through a bunch. I have three here, but I'm going to pick one. If an AI started doing standup comedy, what do you think would be its go-to joke or funny observation about humans?
Logan Kilpatrick :
I think today, I think if you were to do this, I think the go-to question would be something along the, "So an AI walks into a bar," and likely because, again, it's trained on some distribution of training data, and that's the most common joke that comes up, and that's probably... I wonder if you came up with a joke right now, whether or not that would show up in one of the examples.
Lenny :
I love it. What would be the joke though? We need the joke. We need the punchline. I'm just joking. I know you can't come up with amazing-
Logan Kilpatrick :
That's what we have ChatGPT for.
Lenny :
We're already irrelevant. Amazing. Logan, thank you so much for being here. Two final questions, even though you've already shared this information, but just for folks to remind them. Where can folks find you if they want to reach out and ask you more questions? And how can listeners be useful to you?
Logan Kilpatrick :
Yeah, Twitter and LinkedIn, Logan Kilpatrick or Logan.GPT on Twitter. Please shoot me messages. I get a ton of DMs from people and it's always really, really interesting stuff. I think the thing that I would love to have help on is if people find bugs and things that don't work well in ChatGPT, I oftentimes see people be like, "This thing didn't work really well." And the key, and I think we as OpenAI need to do a better job of messaging this to people, but having shared chats or actual, tangible, reproducible examples, are the two things that we need in order to actually fix the problems that people have. The model laziness was a good example where it was hard to figure out what was going on because people would be like, "Oh, the model's lazier," but it's hard to figure out what were the prompts they were using. What was the examples, all that stuff? So send those examples as you come up on things that don't work well and we'll make stuff better for you.
Lenny :
Amazing. And I'll also just remind people, if you're listening to this and you're like, "Oh, okay, cool. A lot of cool ideas for OpenAI and ChatGPT," what you need to do is actually just go to chat.openai.com and try this stuff out. There's a lot of just theorizing, but I think once you actually start doing it, you start to see things a little differently. And at this point, every day I'm in there doing something, like asking for ideas for questions, doing research on a newsletter post, and it's just a tab I'm always coming back to. And I know there's a lot of people just talking about this sort of thing, and I just want to remind people. Just go. Sign in. Play with it. Ask it questions on something you're working on and just see how it goes and keep coming back to it. Is there anything else you want to share along those lines to inspire people to give this a shot?
Logan Kilpatrick :
I love it. I think the phrase of people being worried about humans being replaced by AI, and I've seen this narrative online, that it's not AI that's going to replace humans. It's other humans that are being augmented and using AI tools that are going to be more competitive in a job market and stuff like that. So go and try these AI tools. This is the best time to learn. You're going to be more productive and empowered in your job and the things that you're excited about. So yeah, excited to see what people use ChatGPT for.
Lenny :
And then you can expense your account. I think it's 10 or 20 bucks a month. A lot of companies are paying for this for you, so ask your boss if you can just have it expensed and make sure you use the latest version. Anyway, Logan, thank you again so much for being here.
Logan Kilpatrick :
This is awesome, Lenny. Thanks for having me in. Thoughtful questions. Hopefully those weren't all from ChatGPT.
Lenny :
Nope, only the last one. I did have a bunch of others I had in the belt or in the pocket. I don't know what the metaphor is. In the back pocket, that's the metaphor, but I did not get to them because we had enough great stuff. So no, that was all me. Human AI.
Logan Kilpatrick :
Thank you.
Lenny :
Thanks, Logan.
Logan Kilpatrick :
Lenny.ai.
Lenny :
I love it. Lennybot.com, check it out. Okay, thanks Logan. Bye everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.
