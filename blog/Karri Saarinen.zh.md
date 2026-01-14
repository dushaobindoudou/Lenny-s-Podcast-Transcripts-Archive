# Karri Saarinen - Lenny's Podcast Insights
## Karri Saarinen - Lenny's播客洞见

---

## ## 关于嘉宾 | About the Guest

**Karri Saarinen** 与Lenny进行了关于产品管理、领导力和打造成功产品的深入对话。

**Karri Saarinen** 与Lenny进行了深入对话，讨论产品管理、领导力和打造成功产品的经验。

---

## ## 核心要点 | Key Takeaways

### Yeah, yeah. And the exercise is that it's important for you to be healthy or not just burn yourself out. So I think it was a balance [inaudible 00

54:17] to that.
Lenny :
Love it.
Karri Saarinen :
So I'm doing those three things.
:
I think the thinking there is, I think we often as a company also talk about this, and very early on. And I use this the same way and I think the company can use it the same way. I think there's always things that you're supposed to do or it sounds like a good idea to do. And it could be like, yeah, come to this podcast. And I actually think before it wasn't like...
:
Or I always have this question, is this impo...

### And why we do this is that we just seeing that it's a very good way to see for both of us, both for the company and the candidates to see how we work together. And I think for the candidate, what they can see is, what kind of company are you joining, what is it like to work here, and what is [inaudible 01

03:53] ownership or how do I approach this?
:
I think a lot of engineers also like that they see the code base and they're like, oh wow, this is really clean and it's not some kind of spaghetti code type of thing situation. So I think it helps the candidates as well understand what are they signing off for, which I think can be very risky sometimes. Especially with startups, it's really hard to tell how the startup is operating just from the interviews. And in large companies, I think things are...

### And then we also, one of the things we really wanted to solve is we wanted to make the application really fast. And the way we figured out we do that is we have more of this local-based data structure where all the data lives in the client, and then it gets synced on the backends with this delta [inaudible 01

09:13].
:
And back then, we were just exploring different off-the-shelf solutions and systems, but there was nothing really there, so we ended up building our own. And so we spent some time prototyping that. And then once we officially, I think, started working on the company in April 2019, and then we announced the company roughly mid-April, and we had this little website up with the wait list. And then I think by May we could use it ourselves. And then we started inviting some friends to try i...

---

## ## 完整对话 | Full Conversation

*以下是完整对话记录。*

*以下是完整对话记录。*

**Yeah, I would say a lot of things that we do is more like that but we don't do AP testing or we don't do specific, go follow certain metrics or something. Sometimes we do have telemetry or we can look at how people use certain things and we sometimes do that, but that's not usually the goal we have in mind, like, yeah, we should move this number this much. So it's more about based on the understanding of the problem we have and based on the [inaudible 00**:

37:16], what we think is right, is this the right solution and is this a good enough solution to be released to the customers?
Lenny :
One more question along this thread is how do you actually structure these reviews? It sounds like you go straight to a prototype. Is there a design review phase? Is it all kind of informal and people just review, here's what we need your feedback on?
Karri Saarinen :
So projects don't necessarily have specific states to them, but I would say roughly, usually we do start with design. So there's some explorations on the design, there's different ways that we could approach this or sometimes there's just one way because pretty clear. But then what I said before, is that we do try to get into the building phase as quickly as possible because then we can also see is this direction actually reasonable and is there some problems it causes or how does it just generally feel here? So I think that there isn't specific review stages. It's more like, yeah, let's check on this project every week or every two weeks and then before releasing, let's also make a review of it and really test it out, is it the quality we want?
Lenny :
Awesome. So that's a good segue to another area I wanted to spend some time, which is the Linear Method. You espouse this way of building product that you call the Linear Method, which you publish online and willing to in the show notes. And I just want to ask a few questions around this way of building product. One is, you are big on this idea of building opinionated software. Can you talk about just what does that mean and then maybe give an example or two of how you actually have done that at Linear?
Karri Saarinen :
So first with the Linear Method, why did we create it in the first place? Is we just believe that there is more of this modern ways of building software and thinking about it. And we wanted to share some of our thinking on it. And that's also, it relates to how we built Linear as well. So you might understand why we make some choices because this is the way we think about making these choices. So we are trying to share our thinking behind the product and also just like, here's the product and figure it out.
:
So the opinionated piece, I personally have this belief that productivity software should be, and especially company software should be opinionated. I think that what the productivity software is trying to do is make people productive. And I think what productive means is you actually do something that matters for the company, which is, I don't know, build some new feature or fix something or design something.
:
All of those things are eventually, they provide some kind of value for the customer. I think there is this ideas or notions in the world that flexible software is great. I'm like, I think it can be great sometimes. But what happens is people start spending a lot of time figuring things out. Like, how does this feature work? You can use it in 10 different ways and then every team or everyone figures out the different way of doing it.
:
So our thinking is we like to provide this good default or good opinions. Like, this is how the feature works and this is how the workflow works. So you, as a user or as a team don't have to think about it and you can focus on the work you do. And the other thing is, my design mantra is always design something for someone. It is very hard to design everything for everyone because you just end up with a very generalized solution. So then what we are trying to do with the opinionated solution is that that's the best solution or at the most optimized solution we think of.
:
And then when you use it, hopefully you agree and you can feel that it's most optimized. So being opinionated, I think the value it provides people is you don't have to think too much or spend more time on the tool than you do on your actual work.
Lenny :
And then another core element of the Linear Method is something you call cycles. I know Linear is all around this idea of creating cycles and working in cycles. Can you talk about what is a cycle and how it works at Linear?
Karri Saarinen :
So for example, the cycles, it's optional, not that the whole team has to use it or not that the whole company has to use it, but it's there as you can turn it on or off. But basically, I think why we created cycles is that I think any team that works on software or some other products, you always have almost infinite list of things to do and that list gets longer every day. And it can be sometimes very distracting for the individual or for the team to decide, there's a new thing coming in, should we work on that or should we work on this other thing we decided in the past? So the cycles is just a way to say that for the next week or the next two weeks or whatever timeframe, we are going to work on these things and these other things we think are the priority or the focus for this timeframe.
:
And then the team can try to focus on those things. Now if something happens, like I don't know, we really need to jump on this other thing. At least there was some kind of initial state that we decided before we want to do these things and then now something else happened and so now we have to go on this thing. So you have an answer when someone comes to you to ask, "Why didn't you do this other thing before?" Then you can say, "Well, we did decide to do that, but then something happened and we had to do this other thing."
:
So the cycles, it's very similar to sprints, but we like to call it cycles because we are not really sprinting anywhere. The cycles also run on automated schedule. So it's like you don't have to think about which day does it start? Or every time, set it up manually so it just runs automatically. And so it's just meant to help the team to focus on, let's just focus on this few things and forget about the infinite list of other things that are in the background.
Lenny :
You mentioned earlier that you don't set metrics goals and so let me dig into that a little bit. Is that true? You don't really have number goals for features for launches and things like that? And so let me start there and then I have a follow-up question.
Karri Saarinen :
So we might have a company level goal sometimes, for example, weekly active users, that's a metric we want to increase or something. But in terms of specific features, we don't have goals for those. And the reason is that I think a product like us or a system that is used by different kinds of companies, and it's like a system made of multiple different parts and it's not necessarily like you want to optimize any specific thing about it. Also, companies are a little bit different, so their usage of different features can differ because they just operate slightly differently or their team size is different or the setup of the team is different or the culture is different.
:
So I think for example, I don't know, some Instagram or some of these apps, it's like, yeah, we need to drive engagement and that's the main feature. That's the main metric for every feature. We don't actually have that. We just think that there should be features that help companies and sometimes we can look at the metrics before we start working on it, like let's see what this state of things are, but we don't necessarily want to set, oh, we need to increase this specific metric by X. It's more like we want to solve this problem. And ideally, the success what it looks like customers agree that the problem is solved or they enjoy the solution and it's not like that the metrics went up.
Lenny :
So just to summarize so far, you have no metrics, you have no experiments, you have essentially no PMs, just one product leader. You spend a lot of time on design and craft and making things awesome. I'm curious just what you think it takes to make a company work in that way? Because this is pretty different from how a lot of other founders think and a lot of other product teams work.
Karri Saarinen :
We like to talk about this internally, I like this mixture of magic and science and how we described, there's always some level of science that we do. And I think some companies are very scientific on their product management that they like to measure everything and they do a lot of tests and things, but we just decided we don't think that's necessary or that's good for us. So the science for us, means that we do talk to users a lot and any project we start with, we do some level of user research and as founders, different people on the team, we might have weekly calls with customers or users. We also encourage everyone in the team, go to the customer Slack, they answer people questions. We have shared Slack channels with customers. Anyone, I sometimes go answer the questions there. I also see when they complain about something. I think the first part is the whole team has to be really understanding the product and the customers and the problems people are facing and have that empathy and as well as the understanding what is the state of things today.
:
And then we talk about that. And then sometimes we might pull up stats and see, oh, wonder, is there some kind of patterns we see, okay, these kind of companies are using this thing more and what do we think about it? But usually we have some kind of question we want to answer. It's like, I wonder what is going on. And then we look at it versus let's pull some metrics and then decide that we should increase this metric. And then the magic part is what happens when you build this understanding, everyone in the company builds. It's not like everyone has the same understanding, but everyone builds more of that customer and product understanding. Then we have discussions like what should we be doing or what decision we want to make here? Then everyone is much more informed of actual reality of the customers or the product.
:
And then we think you can much more use your intuition or thinking to do those decisions so you don't have to use data or metrics to back those things up. So I think the main thing is the whole company has to be with the customers or talk to them and then understand where the product might work well or where it might fall short.
Lenny :
That's what I imagined you were going to say, and I love hearing that. For someone that wants to create a similar culture, is there tactically anything you find, just understand if your employees and engineers, designers have enough of that context and really understand the problem?
Karri Saarinen :
I think it's always, different people in a company will have different understandings. It's not like you can expect everyone will every day go to see everything and has this. But we do sometimes sessions with the team or we do record videos with the customers, we write notes and we share this with people. I feel like again, it's fairly apparent, if you know your customers or the product, it's a very different way you can talk about it versus if you don't have any idea. I think if you don't have any idea, you probably don't even know what to say.
:
So I think it's apparent if people have that then, it's not like every project's like we need everyone to have this understanding. Probably, usually enough if one or two people have that understanding or have different understanding of different things. So I think again, I feel like it's a culture thing. I think the other thing is you just have to kind of believe in it.
:
I think sometimes people use data a lot or too much because they're worrying or they're afraid that, will I make the wrong choice? And I'm using data to make the choice for me. But then you might still feel like this is not the right choice, but the data is telling me is the right choice and then turns out maybe it was the right choice or not. But it's more like, again, like a practice thing. I think the company and you need to be okay that sometimes we make mistakes and we made the wrong choice and then we just can fix it. But at least we made that choice and the data didn't make that choice for us.
Lenny :
What's interesting about-
Karri Saarinen :
The data didn't make that choice for us.
Lenny :
What's interesting about this is if you've heard the episode on RAMP and how Ramp builds product with Geoff Charles, there's such different ways of building product. Ramp is all about velocity, shipping all the time, metrics, measuring everything. And your approach is almost the opposite. And I think what's interesting there, as a takeaway, is just there's many ways to do it. You just have to do it almost fully and you have to have really specific people. It feels like the people want to work in a certain way. And a lot of it I think also is the founder has to be natural to the way the founder operates and thinks about building and building a company.
Karri Saarinen :
Yeah, and for sure. And then if you look at successful companies and Amazon is very different than Apple in how they operate. And I think both of them are successful, but not in the same way.
:
So I think it's, again, it's like... Yeah, it's a decision you make as a company or as a founder, what kind company you want to build. I do think there is some aspects of the domain that you're in. What does that domain and the problem space require from that company? And for us, I think it's... I think we are in the retention business. And the trust business that ideally we have a company starting use Linear very early on and then they stay with us forever. And I think the only way we can do that is we need to continuously deliver them good quality product and maintain that trust that we are... That we don't fail them more or somehow otherwise mistreat them.
:
And I think some businesses are much more transactional where it's like, yeah, we just need to make this e-commerce sale. And then once it's done, we don't care what happens.
:
So our case, it's more like we really need to build this relationship over time. And then that's why I think some of the choices we make are also more about respecting the customer versus we're just wanting to drive the revenue of the company.
Lenny :
Awesome. Such an important point.
:
This episode is brought to you by Pendo, the all-in-one platform for product-led companies building breakthrough digital experiences. With all the tools you need, all in one simple-to-use platform, Pendo makes it easy to answer critical questions about how users are engaging with your product and then turn those insights into action. With product analytics, low-code in-app guides, user feedback, and session replay, customizable roadmaps, and AI generated insights and campaigns, Pendo is the only solution you need to build, ship and optimize a successful product-led motion.
:
But don't take my word for it. Create your free Pendo account today and start building better experiences across every corner of your product.
:
PS, want to take your product led knowhow a step further? Check out Pendo's lineup of certification courses led by top PLG experts and designed to help you grow and advance in your career.
:
Learn more and experience the power of the Pendo platform today at pendo. io/lenny. That's pendo.io/lenny.
:
Something you're really good at personally is focus. I find that just trying to get you on this podcast was a lot of like, "Hey Karri. Hey, have you thought about this yet?" And I know that a lot of VCs are just reaching out to you all the time, all these really fan CVCs that are just trying to talk to you and get close to you. And I just know you're really good at avoiding shiny objects and staying really focused and really heads down. And I've always wanted to just ask you, how do you do that? Do you have any tricks, systems, processes, approaches to staying focused other than just ignore the inbox mostly?
Karri Saarinen :
Yeah. I don't think there's any complicated processes. And so I think one of the things, I was in YC in 2012 and one of the main things they say there is what you should be focusing on when you build a startup is talk to customers, build the product, exercise. And if you find yourself doing something else, then those three things, it's probably the wrong thing to do.
Lenny :
And the third one you said exercise or...
Karri Saarinen :

**Yeah, yeah. And the exercise is that it's important for you to be healthy or not just burn yourself out. So I think it was a balance [inaudible 00**:

54:17] to that.
Lenny :
Love it.
Karri Saarinen :
So I'm doing those three things.
:
I think the thinking there is, I think we often as a company also talk about this, and very early on. And I use this the same way and I think the company can use it the same way. I think there's always things that you're supposed to do or it sounds like a good idea to do. And it could be like, yeah, come to this podcast. And I actually think before it wasn't like...
:
Or I always have this question, is this important to do now or is it important to maybe do later? So I think, for example, the question on this podcast is I didn't feel like it was important to do it earlier because we weren't at the stage or a scale or something that I think it'd be as interesting or something. So I think it was a better timing to do it later.
:
Similarly, when we built the product, initially we were just very focused on is this really important thing to do? There's always like, yeah, you could get SOC 2 security certificate. And we know that eventually we need to get it, but we don't need it today. So we just say no to that. And if customer asks for it, so we say we don't have it. And we'll have it one day but not now. And see, a lot of times people are like, "Okay, that's fine."
:
And then internally, we also talk about this, you knowing RPG games, you have the main quest lines and then you have the side quest lines. And we often talk about the companies avoid the side quests. There's always ideas people have and it's a good thing and it's like people have ideas, but then it might be like, "Yeah, let's make this T-shirt, so let's make this thing." And then we're like, "Well, does it help the customers? Does it help the product?" This sounds like a side quest to me, and basically means we shouldn't do it. This doesn't progress the main quest line, which is building this product and making it awesome for these customers.
:
So it's similar to me. It's like I operate this way personally too, that I think about "Is this important for the main quest line in building this company for me? Or is this something that I can ignore for now, or something that I can do later and it makes more sense then?"
Lenny :
That is such incredibly good advice. Basically ask yourself, "How important is this to do now? And is this the main quest or is this a side quest?" Amazing.
:
Okay, so let's talk about hiring. As with most areas, you're very, very, very deliberate about hiring. The bar is so insanely high at Linear, and you also hire very few people. So just a few questions along these lines, just one is when you're hiring people, what do you look for that you think maybe other people are not looking for enough? And where do you spend a lot of time?
Karri Saarinen :
I think one of the things all of us founders saw in this high-growth company is that sometimes the high growth, especially on the employee side, is not that great. It can create a lot of chaos or just messiness. Or just generally in my past and working in companies, it's almost never... It was always easier to work with a smaller team, very high quality people than with a very large team of more average people. It's almost like it's always faster and better output when you have a much more smaller team.
:
That was the thing with Linear too, is we just believe that you can actually build better with less people than you can with more people. So that's the basic belief we have. So then when it goes to hiring, we've been taking very slow steps on it that in almost the first year we didn't hire anyone. Then the second year we hired a couple people, and then the second year we hired a few more. We never more than doubled in a year. And that's been our guideline that we shouldn't more than double. And this might be something we change in the future that we actually might do less than that.
:
But when we look into hiring, it is a couple things. One is also that it obviously depends on the role, but basically I would say with every role, we often talk about there needs to be some taste or some this kind of understanding of how things are done or what's the... People have more a broader perspective than whatever their role is.
:
So we talked about the engineering before that they do need to do some of this BM type of stuff. And so what we look for in them is that if they have some of this skill set or product thinking, or they can articulate why some choices are better than some others, or in their past did they disagree with some of the company's choices or the team's choices, or... So we want to have this... Obviously they need to be good developers, but also do they have this a product sensibility, or do they have a judgment around that?
:
And this goes similar to, for example, a marketing hire is... We think about, yeah, we do need the marketing skill sets, but then we also want to see that this person also maybe is a good storyteller or they have this appreciation for writing or stories or they have a taste of what's interesting and what's not.
:
So I think, or when we hire operations person, we also like to see that they maybe have understanding on HR and maybe it's not their role, but they understand it. And what happens is when you have these people that are a little bit more than their title, it's like the company is, I think, much more easier to manage because it's like people can pick up things more easily or they can work together more easily because everyone has more like a shared areas or you rarely get to the point people say it's not my job. It's more like people understand, okay, yeah, I'm kind of in operations, but today I need to help on this HR thing, which is okay. And so that's what we look for people is they are more than their... They can take more scope than their skill set would assume, or what normally is expected from them.
Lenny :
So essentially you're looking for these Venn diagram overlappings across different functions and teammates.
Karri Saarinen :
Yeah. I think the other thing is, like I said before, is we want to build much... I think a company that has less employees, which means that it's... Like I said before, we don't want that many specialized roles or too specific areas of ownership or something. We just think that we could build this... We could have less people and those people can take on more scope and they can own more scope.
:
I think traditionally, I feel like in companies, how do you get more scope is that you advance in the levels of the company because there's a lot of different teams and different levels. And then to get any kind of scope, you need to rise into this higher levels. And what we try to do is you don't actually have to have that many levels, but people can just already, when they start, they can start owning more areas.
:
And I think that can be much more also interesting, not to everyone, but I think interesting to many people. And it's kind of like how I also always felt about us being a designer is I didn't feel like my job is purely just looking at the designs. I also thought I actually need to be helping this business or helping this other area as well. So I think it's just also natural to me.
Lenny :
Awesome. So one thing you didn't mention is you have a really unique way of interviewing, which is a paid work trial. Can you just talk about what that is? And also just while you're in that area, you talked about testing for product sensibility, so whatever you can share how you actually do that would be awesome.
Karri Saarinen :
Yeah. So we do with all of the employees, we've done a paid work trial and depends on the role, what it looks like, how long it is and depends on also sometimes on the person. But basically we do fairly standard interview loops where we test... We have some hiring manager interviews and then skill interviews or tests. And then the last step of the process is the work trial.
:
And basically, they basically come as a mini contractor to the company, and we give them a very usually fairly vague problem statements. If you're an engineer, it's like, hey, there's this feature that needs to be built. How would you build it? Then go build it. And so basically they need to first understand the problem. Then they need to scope it down to something that they can do in the timeframe that they have. And then they actually go... They get the access to a code base. They can actually go and go and build a version of it. And then at the end they can present the work they did.
:

**And why we do this is that we just seeing that it's a very good way to see for both of us, both for the company and the candidates to see how we work together. And I think for the candidate, what they can see is, what kind of company are you joining, what is it like to work here, and what is [inaudible 01**:

03:53] ownership or how do I approach this?
:
I think a lot of engineers also like that they see the code base and they're like, oh wow, this is really clean and it's not some kind of spaghetti code type of thing situation. So I think it helps the candidates as well understand what are they signing off for, which I think can be very risky sometimes. Especially with startups, it's really hard to tell how the startup is operating just from the interviews. And in large companies, I think things are more standardized. So I think they're more similar and it's easier to make that choice. But with startups, it can be very different how companies operate.
Lenny :
Yeah. That is so unique and I rarely hear of a company being able to hire that way. I imagine one of the reasons you can get away with that where people don't have a full-time job for a while, while we're doing a paid trial is because Linear is such an enticing place to work. I imagine for a lot of companies they can't really do that. But I guess any thoughts on just maybe more companies can actually pull this off?
Karri Saarinen :
Yeah, I think it's always like if you don't ask, you don't know. I think in our case that's just been the standard and we try to work with the candidate. Let's figure out maybe we do it on the weekend or maybe we do it some other vacation holiday or something. So there can be ways we can schedule it so that it causes as little kind of problems to the candidate as possible.
:
And I think we only had only a few people probably have ever declined it. It's not like I think everyone else has been, at least after the fact, they've been happy that they did it because they felt like they had a much better sense of the company they're joining. And then also during that workshop, they can actually join our meetings, they get access to our Slack and Notion, and they also have one-on-one chats with some of the other people on the team.
:
So they already get to know people. So it's a good way for them to evaluate us as well. And then for us, it's obviously we can see... What is important for us to see is how does this person operate in this kind of environment and how do they approach problems? How do they think and are they able to make progress in a very short timeframe, which I always think it's very important for startups. In large companies, you have maybe all the time in the world to do stuff. But I think any kind of startup, even with us when we take our time doing things sometimes, it's still important. We can do things quickly if we have to.
Lenny :
Super cool. Just to close the thread on product sensibility, is there anything you could share of just how you actually help understand someone's strength and ability there?
Karri Saarinen :
Yeah. I wouldn't say we have some kind of very scientific or some special way figure it out for this. So I think a lot of it, it's like a discussion of... And I often think ask people that... Ask about their projects and I try to go deeper. It's like why was this decision made? Why do you think the decision was made? And I might ask, "Do you think it was the right decision or did you agree on it?" Or ask about what you think you would have done differently or something.
:
So I think it's more like I'm trying to... In this area and what their answers is. And people's answers can be very different levels. Some people might be, "Yeah, I didn't like it. Which yeah, it's not opinion, but it's not based on anything. It's just like you didn't like it. You should be able to expand on it saying well, I don't like it because in this case it would not work well for this kind of users or in this kind of context or for this kind of purposes.
:
So they have more of this reasoning or some kind of rational why they think this way and they can articulate that. So I think that's what we often testing for is can they do this and how well they can do it. Then there can be very wide ranges of how people do it. And when you see someone who really thinks about this stuff, it's very clear to see that they can just talk about it forever and they can go deeper and deeper. And then some people that maybe haven't had the experience or don't think this way, they're like, yeah, I don't really know. I just built it and then seemed fine.
Lenny :
Let's transition to the third area I wanted to spend some time on, which is growth. And basically I'd love to just understand how Linear grows and what you figured out around growth, especially in B2B SaaS.
:
So our first question here is just how long did it take from starting to work on Linear to launching, say, V1, something that a number of people can use?
Karri Saarinen :
So we started officially in 2019. Some, I think, months before that we were already exploring and prototyping the product. So I think we prototyped different kinds of designs a little bit.
:

**And then we also, one of the things we really wanted to solve is we wanted to make the application really fast. And the way we figured out we do that is we have more of this local-based data structure where all the data lives in the client, and then it gets synced on the backends with this delta [inaudible 01**:

09:13].
:
And back then, we were just exploring different off-the-shelf solutions and systems, but there was nothing really there, so we ended up building our own. And so we spent some time prototyping that. And then once we officially, I think, started working on the company in April 2019, and then we announced the company roughly mid-April, and we had this little website up with the wait list. And then I think by May we could use it ourselves. And then we started inviting some friends to try it out.
:
But then I think in June, I think we started more inviting people from the wait list. And around June, July, I think we had about, I don't know, 100, 200 users on it and maybe about 10 companies or something. And then we were in this private beta stage for almost a year. And the way we did it was just like we had this wait list of people on the wait list. There was few survey questions, like what kind of tools you use today and then why do you want to use Linear and what's the company size?
:
And we invited people based on... We invited more smaller companies using the tools we currently supported. And then also I was trying to see who is more interested versus just, I don't know, I just want to try it out type of people. And then a year later, in June, we launched it publicly. And back then maybe we already had, I don't know, several hundred of companies using it. And then we also launched the pricing and I think almost all of them... Maybe one company didn't subscribe, but everyone else subscribed to that paid plan.
Lenny :
Okay. There's a number of really interesting things here. So one is you're in private beta for a year and then a year later, you launched. How long was that period between starting to incubate and starting to build to that private beta milestone?
Karri Saarinen :
Yeah, I think it's just a few months. I think just-
Lenny :
Just a few months of building the V1?
Karri Saarinen :
Yeah.
Lenny :
Wow, okay. I thought it was a lot longer. That is so interesting. Okay. What a team you've got over there.
:
Okay. And then this survey piece is really interesting. I've heard a little bit about this story. So essentially you launched it on Twitter. You had kind of a following. Your founders had a bit of a following, so I think that helped build up the initial wait list.
:
But what you did there wasn't just like, hey, go sign up for a wait list and you just add email addresses. It's a survey asking them what tools they use, whether it's GitHub or something else, and then also the size of the company and their interest. And that helped you basically prioritize who to go after and who to onboard. Is that right?
Karri Saarinen :
Yeah. And the reason we did it, because we know that we didn't support everything and what I said before and the focus is we want to also be focused on let's just build a version that can work for some people or some companies. We don't have to try to address everyone in the world in the first months of the business. And even before, after that. So it was very selective process. And I think we were fortunate that we were able to get people sign up on a wait list and I think after a month or so we had maybe 4,000 people on the wait list.
:
And then we had this internal... I think initially it was just a very manual process, but eventually we built this invite tool that we could just send invites. But in the beginning, I would go read the actual surveys in a spreadsheet, then I copied the email, and then I emailed them the invite link from my personal email. And then I would just email them after a few days or a week and it's like, "Hey, what do you think?"
:
And the reason we... And so we would invite only like... In the beginning, we maybe invited like 10 people a week. And eventually we increased those amounts. But the reason we did it that way was that we thought that if you just invite everyone at once or a lot of people at once, all of those people are going to probably hit the same problems in this kind of software that is very early stage. So I don't know. They hit the same bug or the same problem in the software. So then they will all send us feedback like, hey, there's this problem. And then we felt like it was a wasted effort.
:
So we would just do these cohorts. Let's invite these people and then they say, hey, this is a problem. This doesn't work, or something. Then we go fix that. Then after we fix that, we invite the next cohort of people. Then they say, well, there's this thing that is needed or this doesn't work, then we fix that.
:
So for that year, we did these cohorts and then always get the feedback from the cohort saying this is wrong or this doesn't work, and then we'll fix that. So eventually, I think it was much more... I think an effective way of doing the initial development than just inviting or letting everyone to use the product right at the beginning.
Lenny :
There's so many interesting lessons from this. I wanted to ask how you got your first 10 customers. And what I'm hearing essentially was from this wait list, you launched it on Twitter, people signed up, you picked people to let onboard, you worked with them over the course of a year to make it what they needed, and then eventually you started charging.
Karri Saarinen :
Yeah. I think the first 10 companies using it, I think maybe a little over half. Maybe there was three friends that have startups and they used it. And then I think the majority of them were just from this wait list. But they didn't pay us anything. We didn't have pricing in the beginning or during the private beta. At some point we started building the payments function, so we just added a page in the settings that you can optionally pay.
Karri Saarinen :
The page in the settings that you can optionally pay and then we just give you a slider that's, how much do you want to pay per seat? Then we just see if... I know some people paid $28 per seat and some people pay $1, but it doesn't matter, we just wanted to test the functionality and see what people think. After a year, when we launched, we already had... In the, I don't know, first week of launching, we had probably some hundreds of customers.
Lenny :
I have never heard of the approach to pricing as just an actual sliding scale where people can slide the scale themselves on how much they want to pay. Did that help you figure out what to charge, or is it mostly just an experiment?
Karri Saarinen :
I don't think it gave enough data to decide, but I think it was good to see that there was some people that went... I think that 20 was probably the maximum that people could pay, so I think there was some people that went to it and they felt like, "Actually, yeah, I really love the products. I'm happy to pay $20." I think at least it gave us some confidence that, if we charge for this and it's something under $20, there's going to be market for it.
Lenny :
I want to hear about the story of how you've started to feel product market fit, whatever that means to you. When did you start to feel like, "Wow, this is actually going to work and maybe this is going to be a real business"?
Karri Saarinen :
Yeah, I think we've always been, I don't know, some paranoid or... I guess maybe a paranoid is a good way about the product market fit. I think it's paranoid in a way, we are always wondering, "Do we really have it?" And, "With who do we have it?" I think it's true in our business, that... I think we started feeling it very early on, and when people first started using it and we could see, "Now the whole company is using it and they seem happier using it and the feedback is good and they might have some additional asks for us," but we started feeling like there was definitely a product market fit with certain customer and these were more smaller, early-stage companies maybe where the founder is still running the product and they care about the speed of the shipping or they have certain values in a way, so it was a good fit with them.
:
Then I think we always know that we want to address the whole market and also just these early-stage customers, but we knew that if a Fortune 500 company came to us then, or even today, we might not be... I don't think we can provide them the solution today that works for them, so I don't think the fit is there. For us, the way we think about is, "Do we have the fit in the specific segments?" And how strong that fit is. In the company's journey, the first year, we just focused on, "Can we get the fit..." In the first two years, we focused on, "Can we get the fit in the early stage startup segment?" Basically, the goal was, "We want to be the default for startups, the default tool that the startups pick, and I think we were able to accomplish that, but we just purely focused on that segment and getting the product market fit there.
:
At the same time, we started getting some larger companies and we saw, "Yeah, it's not really great for you right now, but let's work on it, making it better," so I think the last two years we've been focusing on that. It's like, "How do we make the software work better? How do we get the product market fit stronger in this larger company segments that are hundreds of people or 1000 people?"
Lenny :
I think this is such a good way and smart way of thinking about product market fit. A lot of people see product market fit as this binary, "I have it or I don't," and, "When am I going to really feel product market fit?" What you're describing is what I often hear, it's more of this spectrum of more and more confidence that there's product market fit and, even more specifically, it's product market fit with segments of the market. It's this map of the world and you're just slowly acquiring territory in the market with specific elements and then, over time, it grows and grows.
Karri Saarinen :
Yeah, I think a spectrum is a good way to think about it, too. I feel like there's this blog post written in the past where you know when you have product market fit and I think it probably... It's like that for some, I don't know, social consumer apps. If it's taking off or not, then you don't really have a lot of different segments, or you don't really think about it, you have millions of users and then you see it's taking off, so you have a product market fit. I think in more like a B2B world. I think there's always... You can have different sizes of customers, you can have different domains the customers are in, or there's different categories where you might be doing really well in one category and then not that well another.
:
I think maybe the countering to do things is that, actually, if you're doing really well in some category, just double down on that. This is something I talked to the Zoom founder, Eric, at some point in the company's lifecycle, and this is also what he said. When they were building Zoom in the early days, they would get this one type of customer. I don't know, maybe it's a university and then it worked really well for them. Then they're like, "How do we get more of the universities?" They would always focus on a certain customer rather than, "Let's just try to get everyone, so let's focus on everything," which is not possible. Again, it's about the focus. If you see that something is working really well, then it's almost like you should focus on doing that more until you hit some point. It's like, "Okay, now we do have that category captured or handled as much as we want," and we should expand to new area.
Lenny :
Essentially, look for pull and just follow that and pay attention to that.
Karri Saarinen :
Yeah. I think, for us, there can be sometimes... For example, now we have... Most of the AI companies are using us, so I think it's always... Before that, it was a crypto company, so I think there's... When we see these kinds of things happening, then we start to think like, "Could we do something differently or could we get more of these AI companies on board?"
Lenny :
Such a great lesson. Just a few more questions, you mentioned that you launched on Twitter and that led to a large wait list and a growing wait list. Is there anything you did before that to build this following? That sounds really amazing, "Cool, we just announced it on Twitter and we have this large wait list and then we grow and we get all these customers." Is there anything you did ahead of time in anticipation of this launch? Would you recommend people work on building some kind of following online before they work in a startup? Was it just like, "Hey, we happen to have this following," and it worked out? Anything along those lines you would recommend to founders these days?
Karri Saarinen :
Yeah. I think definitely if you have a following and, obviously, depends on what kind of following, but I think my background as a designer, I would say at Airbnb and Coinbase and other places, and I did some talks in conferences and write some blog posts. I was definitely out there and had some of that following, which was helpful, but it wasn't like I have hundreds of thousands of followers or millions, or something. I had maybe 10,000 or something, which is a significant number, but then I think the other thing is... I think with the announcement, one of the things we did, I think, well is I think sometimes startups do try to emulate successful, large companies too much and you do this fancy announcements where it's like, "Hey, now we are doing this fancy thing and it sounds very corporate or something."
:
With our announcement, we wrote it more direct or authentic to us like, "This is what we're going to do and this is why, and these are some of the things we're going to do." On a Twitter, we did the same thing. All of us founders, we wrote our own reasons why we're doing this, and I think it was just much more... I think people like us could resonate more with it, so we were writing to the right audience. I think that's probably the first thing when you're announcing your company, you think about, "Who is my first audience? Who would be the best early users for this product and where are they?" And then, "How do they think about things and what kind of language do they use?" For us, it came very naturally, because we are these people.
:
We are in building software and these companies, and other people have seen similar things we have seen, so I think the way we announced it resonated with a lot of people. Then I think we did have some friends... I said we got some angel round where we got some friends involved. The main reason we did it was that we just felt like, in the early days, it's good to have... You feel like a real company in a way, that you have someone to answer for in a way. Even though the investors normally run your company or they don't have that much power, it's more like, "I took someone's money so I now need to make it worth it," kind of. With the announcement, again, we could use some of those people to spread the message as well.
Lenny :
To close out our conversation, just a couple more broad questions. You have a pretty unique culture at Linear, and I know one fun thing that you do is you have this baking competition. Can you talk about that and what it is you do there?
Karri Saarinen :
Yeah. Since we are a fully remote and distributed company, so we have people in Europe and US, a lot of group gatherings are challenging. Remote group sessions are challenging, because the time zones are so different, so some of the basic things, like happy hours, don't really work that well. Also, Zoom happy hours is probably not that fun anyway. I think a lot of people in the company watch The Great British Baking Show, so we decided, "Maybe we do something like that," where basically, we would just pick a recipe. Firstly, it was baking, now we expanded to cooking recipes, too. We just pick a recipe that is somewhat reasonable to do in a few hours, in a couple of hours, and it doesn't require tons of equipment or skill, or something. Then we just tell people, "Go buy the ingredients, use the company card," everyone has a company card, "And then hop on Zoom on this day."
:

**For me, since I'm in California, it's like 8**:

00 AM, so we started the baking or cooking then. We've made things like roll cake and lemon meringue pie, and we made some [Portuguese 01:26:35], which is Portuguese pastry. Then we just hop on the Zoom, everyone's doing their thing, following the recipe, and then sometimes people have questions like, "Hey," I don't know, "I'm stuck with this," or, "My dough looks weird, does your dough look like this?" People can help each other and then also chitchat about whatever random things at the same time. Then we do the thing and then everyone takes pictures and posts on the Slack channel, it's what they achieved. I think we have friendly competitions like who did it best, so people sometimes put a lot of effort into the decorations and visuals.
:
In a way, it's, again, a craft thing that we do. I think baking and cooking and these kinds of things are also a craft, so we liked it that way. Yeah, we've been basically doing it quarterly since the beginning of the company. Yeah, the latest thing, we were a little bit... I think didn't have that much time, because we decided to do an easier thing, which is a summer drink recipe, so I think people made matcha drinks and some coconut drinks or white iced tea, or something. Yeah, that was interesting to do.
Lenny :
Have you ever won one of these competitions yourself?
Karri Saarinen :
I don't know if we declare winners that much, but I do think I do... Since I'm a designer, I do have some advantages on the visual presentation, so I think that I generally do well on that. Obviously, with this remote competition, that's the only thing you can really look for. It's not necessarily about the taste or the texture, because you can't really taste it through the Zoom.
Lenny :
Maybe as a last question, just again broadly, you've gone from being an IC designer, manager of designers, to the CEO of very fast-growing company. What's something that you've learned about leadership over the journey of Linear that maybe you didn't expect?
Karri Saarinen :
For some reason, it was surprising to me, I think, that being a CEO or some of these leadership roles is that you end up doing so many different things. When I was a designer, even if I would be some high-level designer in some company, you're just mostly focusing on the design and that's your job, but then when you're a CEO, then every week or every day, there's some different thing going on. Sometimes there can be problems, but a lot of times, it's like, "Hey, we need to figure out how we're going to do this. How are we going to do this compensation?" Or, "How are we going to do this marketing plan?" Or, "How are we going to do this offsite thing?" What's definitely challenging for me is handling that different kinds of things that come to you and staying somewhat focused, still, on something.
:
I think I haven't necessarily fully figured it out, but I also figured it out, that hiring and delegation helps with this, that if you can find other leaders that can take on certain areas, that's helpful. That's the main thing, that it's a very wide range of things that you maybe didn't have experience before, but also, I think it's interesting for me to learn about these things. You learn about the financials and you learn about legal things, and then you start to feel like, "Actually, I know something about this thing," over time.
Lenny :
For the actual final question, before we get to very exciting lightning round, what's just the future of Linear? What's coming? What's happening in the future? Anything you can share?
Karri Saarinen :
Yeah, I think there's always things we're working on and improving. One, a newer thing we're working on is this feature called Asks. Basically, what it is is that... We see that, in a company, there can be a lot of different people that need to interact with the product team or different people that need to interact with this team, but they're not necessarily in Linear or part of this team. We'd be building this an Ask feature, which is an integration to Slack where you can very easily go to a Slack channel and then ask your question. You need something from this team, maybe it's the IT team, that you need a laptop, or maybe it's the infrastructure team and you need something from them, then the team that is handling the request, they can very easily send it to Linear, into this triage that we have, and then they can start doing stuff with it.
:
If they have questions or additional questions to the actual person who requested it, we can send those messages back to the person through Slack, so they don't actually have to go to Linear or they don't have to be a Linear user to use it. We think this is just a good way for the company, or the whole company, to be more potentially involved in the product operations without having to be a power user of Linear, because not every function really uses it or needs to use it.
Lenny :
Awesome. What a cool peek at something coming out soon, or maybe out by the time this comes out. With that, we've reached our very exciting lightning round. I've got a bunch of questions for you. Are you ready?
Karri Saarinen :
Yeah, I'm ready.
Lenny :
All right. What are two or three books that you've recommended most to other people?
Karri Saarinen :
Timeless Way of Building by Christopher Alexander. He wasn't really an architect, but he, I think, taught in Berkeley. He has these interesting thoughts about building things and he focuses on buildings and towns and these kinds of spaces, but I think there's a lot of things that are also interesting for building software. The other book that I like is the Zen and the Art of Motorcycle Maintenance, because it also talks about the quality of things and I think that's one of the main themes of the book. The thing is also that quality is so hard to define. If you actually start thinking about it, it's like, how do you define it? It's really hard to pin down, but it's like when you try something or see it, then you know if it's quality or not.
Lenny :
What are some recent movies or TV shows you've really enjoyed?
Karri Saarinen :
I think that the movie is probably John Wick 4. Obviously, there's no story in that movie, but I think it's very true to its nature, so I like that fact. Also, recently, I started watching the Silo on Apple TV, and I think I like it. It's like a good mystery and then, also, it reminds me of the Fallout games, so I like it that way, too.
Lenny :
I actually read the Silo books and I was really excited for the show to come out, but I mentioned this on a previous podcast, the show is so little to do with actual books. The core ideas are the same, but there's all these stories that they're just making up on the show, so I stopped watching, because that's not what I was hoping for, but-
Karri Saarinen :
Okay, interesting. Maybe I need to check the books later, once I watch the show.
Lenny :
Yeah. Definitely, read the books, but there's three of them and only the first one is actually good. The other ones are not actually very good and I should not have read them, because it just went off the rails a little bit. Anyway, next question. What is a favorite interview question that you'd like to ask candidates when you're interviewing them?
Karri Saarinen :
I think, usually, I like to ask, what is the candidate most proud of and why? On their professional life or otherwise, what they're most proud of and why. Then I think we can go deeper on that, but I think it gives you a little bit of indication, what the person values and how they think about things. Also, I think it's always nice that people can share something they think they did really well and we can spend time on it versus just asking something more like negative things.
Lenny :
What are some favorite products you've recently discovered that you really, really like?
Karri Saarinen :
I'm not sure if I discovered them recently, but recently in this home office, I've been installing some of these hue lights and I really like them, because throughout the day, I can have more harsh lighting, because I'm in meetings or something, and then in the evening, I can change the temperature. I make it much more red or orange, or something. I think it's nice that you can transition the space. It's like, "Okay, now I'm working and now I'm doing something else." You can use the lights to indicate that.
Lenny :
That is so cool. Do you automate the schedule or you manually change the color?
Karri Saarinen :
Yeah, I just manually change it. On my home app, I have scenes that... There's the night scene and then there's the day scene, or the morning scene, so I just click that button and then it changes the lights.
Lenny :
That is extremely cool, I'm going to try that myself. What is a favorite life motto that you like to repeat yourself or share with people? Something you come back to a lot.
Karri Saarinen :
Go slow to go fast. I think, for me, it's about that. Sometimes people have a tendency to rushing into things and especially, I think, in startups, but other places too, you have this like... I think urgency is important, but then sometimes you have too much urgency and you are rushing things, and what happens is that you rushed it and now you need to come back to fix it. I think sometimes I like to think that you should take some time to actually think about it and, "What are you going to do?" And then do it. In the end, it's going to be faster that way than going back and forth and fixing things.
Lenny :
What is the most valuable lesson that your mom or your dad taught you?
Karri Saarinen :
I think it's respecting people and things. I think the people respect is pretty obvious, but I think with the things you have, also, I think you should take good care of them when you use them. I don't know, clean them or put them away, and then they're ready for the next time. I think I like that, though. Rather than you treating things like they're trash or not that valuable, you should treat things that they are valuable.
Lenny :
Final question. You were born in Finland, I think you grew up in Finland. What is a Finnish food that people should definitely try to get as soon as they can?
Karri Saarinen :
One is this salmon soup, and it might sound weird, a fish soup, maybe it's not going to be that interesting. It's a creamy soup, it's on potatoes, carrots, and other things, and it's almost like a little bit of sweet flavor to it. You can make it yourself at home or you can... If you go to Finland, there's probably always a few restaurants that offer it.
Lenny :
Okay, amazing. Is that something we could get here or you have to go to Finland to get it?
Karri Saarinen :
I don't think I've ever seen it here in the US in any restaurant, but it's not very hard to make it yourself. You can probably Google a recipe. Basically, you just need some salmon, some basic spices and some cream and some fruit, vegetables.
Lenny :
All right. Next episode, we're going to do a cooking show with Karri. Karri, thank you so much for being here. You're building a very special company in a really unique way, and I think many founders and many product builders can learn a ton from watching you operate in the business that you're building. Again, thank you so much for being here. Two final questions. Where can folks find you online if they want to reach out, maybe ask you some more questions, and how can listeners be useful to you?
Karri Saarinen :
Yeah. I'm on Twitter, my name, Karri Saarinen. We also have the Linear account, which I think is interesting. That's just @Linear. I hope everyone can check out Linear and see if it could work for them in their company, and figure out if there's a pilot. I think we are always happy to assist on those things, if you just want to try it out and try it with the team, we can help you to set it up and help you to understand how to use the product.
Lenny :
Awesome. It's just Linear, the app, right? Is that the URL?
Karri Saarinen :
Yes.
Lenny :
Awesome. Okay, easy-peasy. Amazing. Karri, again, thank you so much for being here. Bye, everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review, as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.
