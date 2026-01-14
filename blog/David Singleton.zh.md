# David Singleton - Lenny's Podcast Insights
## David Singleton - Lenny's播客洞见

---

## ## 关于嘉宾 | About the Guest

**David Singleton** 与Lenny进行了关于产品管理、领导力和打造成功产品的深入对话。

**David Singleton** 与Lenny进行了深入对话，讨论产品管理、领导力和打造成功产品的经验。

---

## ## 核心要点 | Key Takeaways

### The process is literally to help you do that. I guess maybe something I left out in explaining it is we'll often identify a buddy on the team who's going to help you through. So for what it's worth at Stripe, we write a lot of code in Ruby, we write a lot of code in other just Java type script as well. But our kind of core infrastructure is mostly implemented, core product infrastructure mostly implemented in Ruby. When I started I had never written a line of Ruby in my life and I knew I wanted to do this thing and actually done something like it before joining and I was really scared. How much credibility might I lose if I show up and I can't write a line of Ruby. But my first buddy was a guy called Ajhja who's still at Stripe doing great stuff and he helped me learn Ruby during these three days and they [inaudible 00

49:48] me a little bit, but ultimately everyone really appreciated that I've done it.
Lenny :
Imagine being the engineer has to review your PR.
David Singleton :
I tell them this is an important part of the process. Please don't treat me any different to anyone else. And obviously to make this work well you have to set the expectation that you're not going to take me action if something isn't exactly the way you want it to be. It is a moral kind of longitudinal process.
Lenny :
Is there somethin...

---

## ## 完整对话 | Full Conversation

*以下是完整对话记录。*

*以下是完整对话记录。*

**So we use the practice across lots of different functions and in lots of different ways at Stripe, but it is the case that almost every product team has someone, it's often the PM, sometimes it's the engineering manager who has a regular repeating loop of going through the end-to-end flow of the product and writing a friction log. For years and years, I have gone through the process of onboarding [inaudible 00**:

33:28] user to Stripe once a month, writing a friction log and then tagging in the right people across the company that might need to take action on some of the things that we're observing.
:
And one of the reasons that that kind of process of taking a big step back is useful is at this stage we have many people, we have thousands of engineers who are working in parallel. And while everyone cares a lot about being meticulous, paying attention to detail, getting the details can have to end up with experiences that diverge and going through this process of looking at it all together on a regular rhythm with friction logging really helps us maintain a cohesive whole while we all operate in parallel. And so therefore senior leaders, executives, I guess of our larger areas will often do this as a practice themselves in order to make sure that everything that they're responsible for is coming together well. So it happens kind of recursively at different layers.
:
To your question about is there a template, so relatively simple process. So yes, there is a template and in fact there's a Stripe talk dev article that maybe we can put into the show notes that has the template, but it literally is say what you want to do, be very explicit about the user that you are trying to have a mental model for because that helps you make the right choices as you go through the flow. And then really just keep a very clear stream of consciousness log of what you're finding as you build.
:
By the way, also really important, praise the stuff that's good. So I'll often send these docs around to a lot of folks inside of the company. It's a great opportunity to recognize great work done. So if I ran into that error message that links to the documentation, that's a great example where I'd be like, this is awesome. Nice work.
Lenny :
Being a PM that has received emails from the CEOs of companies with all the problems they ran into and they're trying to book, it's often like, oh God, I have so many goals I got to hit and I have this timeline, I have these things I'm working on. What is the culture like slash how do you give teams space to do these things that are just like, we're just going to make the experience better? How do you actually do that so that PMs aren't stressed out when they get these things?
David Singleton :
It starts with our operating principles. So because we have operating principles of users first and being meticulous in our craft, we actually tend, all of our ways of building plans tend to be wired quite well around this idea that we're going to reserve enough time to really make the experience good. Maybe the most pronounced version of that is not even the issues we identify in friction logs. Maybe in a bit we can talk about how we invest in reliability and so forth, but things go wrong.
:
And one of the things that's very important to me is that we are a learning organization. We need to understand why they went wrong and then take action to stop the same thing going wrong in future. And so that means that we identify instant remediations, that's what we call those and we prioritize those carefully and most of them, the ones that matter actually get prioritized before other work on the roadmap, which means that as a PM when you're building your roadmap and your plans, you do have to think about, well approximately how much bandwidth do I need to reserve in this area in order to address and polish stuff that might come up through friction logging and also to take care of those kind of operational things as well?
:
It varies by team and varies by stage of product. So there is no Stripe kind of like we will reserve 50% of our time to do this stuff. That wouldn't make any sense. But we do encourage and ask every team to think hard about how much should they be setting aside for those kind of activities. Does that make sense?
Lenny :
Absolutely. I was going to ask you if there's a percentage and basically you trust the teams to set aside the right amount of time.
David Singleton :
That's right.
Lenny :
Awesome. Okay, so along the same lines, I actually asked Shreyas Doshi what I should ask you.
David Singleton :
Oh cool.
Lenny :
You had no idea I was going to do this. And what he said is I should ask you how you did UX reviews pre shipping right after you joined Stripe and you just said you were very good at this. And so what is that like and how should people learn from your experience?
David Singleton :
The way that I did UX reviews very early on in my time at Stripe and the way that every group at Stripe does these reviews is employing some of the techniques we talked about already. So that act of friction logging, it's very often done asynchronously. So someone will sit down and reserve an afternoon and go through the product and make meticulous notes and that's super useful.
:
We also find it very valuable to go through that process together. So we will bring together both the team that built the product that we're looking at, but also a lot of their cross-functional partners. So things like the support folks that are going to be handling or are building the process to handle questions from users about it. Executives in the org that they're a part of to do these walkthroughs where we're taking exactly the same approach as I described with friction logging so imagining we're a particular user and experiencing the product together. And then just discussing very openly actually the way that we do this today is we have a log of issues that we want to talk about that anyone can type into while the PM usually is walking us through the flow. And then we'll get together at the end and actually talk about each issue and does this need to be addressed? What do we really think about it? So that that's the approach both that I took early on and that we take in at general at scale today.
:
There's a lot of benefit to doing this together. So someone once described this to me as if you were a chef, you're going to taste the soup and you're going to talk to your kitchen staff about what went into the soup when it was good and wasn't so good. If you run a movie studio, you're going to sit down and watch a lot of movies together. And so actually kind of looking at product together I find extremely energizing and also really valuable in actually teaching some of the kind of bar for craft and values around how we want the product to interoperate for our users at scale across the company.
:
And building on that, there's something that we do occasionally and I've done occasionally a Stripe called Walk the Store where we'll actually do that process of looking at the product together with the whole company. So we have a weekly meeting called Friday Fireside where you don't have to attend, but the majority of the company does attend and we've done a few series where we'll actually go through some really, really interesting critical product flows together and talk about how this is reflecting various priorities that we have and shifts that we're trying to make, but in particular with the user experience and a particular user at the core. And that turns out to have a tremendous amount of benefit and value in helping just everyone have a shared language, we're talking about things and get on the same page about everything.
:
So yeah, those are some of the techniques that Shreyas might have been thinking of.
Lenny :
It's amazing how many directions you all come at to create this high quality end product walking the store, friction logging these entire company meetings, looking at the product, UX reviews, this is how it's possible to build something so high quality. It's not just we have this value and we're going to be building great stuff. It's like you have to come at it from so many places.
David Singleton :
Yeah, that's an interesting observation. I think almost anything that you talk about is a value. I mean, being a value matters, but you need to have a practice behind that. That means that the value becomes real for everyone. So we very frequently find that for any product development team, so long as they identify the right metrics that actually represent the experience that they want to deliver for their users and then get together frequently like predictably to look at how the team is doing against those metrics. But then everything else just happens naturally because you understand what you're trying to move and every little micro decision you're making within your own time prioritization and then in terms of the actual work you're doing will ladder up to that. And so why do I say that? It is like you have to have the predictable and regular thing that ladders up to the value you're trying to deliver in order to make it happen.
Lenny :
Coming back to the UX review, just a question there. Presenting to the CTOs often very stressful in a review like that. What advice would you give PMs and designers and just leads of a team for how to prepare for a meeting like that, whether it's Stripe or anywhere?
David Singleton :
I personally try to be as friendly and unscary as possible, but I know that no matter how much I do that, these can't be high stakes meetings. At Stripe, and I think it's probably goes for most companies, but at Stripe, the main answer here is put your user's hat on and if you understand your user well and what they're seeking to get out of the experience and anchor any questions you get asked or wobbles you may feel of like, oh, that was an out of the blue question back to well here's, remember what we're trying to do for our users, that usually makes any meeting like that go really well. And so that would be my main piece of advice.
:
So I mean a risk that exists in any company as you get to run a bigger team or whatever is that individual contributors, individuals will have a very small amount of time with you in general. So there's always a risk that you might make a kind of fairly unimportant remark and it will be taken out of context to be something very important. So I personally also try very hard to anchor feedback I'm giving in what's the user experience we're trying to deliver? Does this actually matter? Recognizing that that is a risk and yeah, it definitely takes constant practice.
Lenny :
You've touched on a couple of these things, but just if someone's trying to get better at building product, either a PM, designer, engineer, what kind of advice do you often give for helping people just build better product?
David Singleton :
Almost always goes back to things we've already talked about here. So remember at the very top I talked about iterating very closely with users? If you have a mechanism to listen to users, get something in their hands quite quickly and then get their feedback on it to run it back through a feedback loop, you're very unlikely to go wrong. Especially if you put a lot of thought into these being the right users whose needs you want to focus on because they ladder up to your strategy. It's actually very hard to go wrong if you have that feedback loop working really well.
:
So if you don't have that feedback loop, and actually it's remarkable as I talk to folks across the industry and so forth, it's remarkable how frequently that feedback loop doesn't exist in product development cycles. So if you don't have that, go figure out how to create it and if you do have it, but you can't get something into user's hands very rapidly from you having the idea that this might matter to getting their feedback on it, figure out how to make that go faster as well. And at Stripe, we focus a lot on all of our developer tooling and infrastructure on making it possible for changes to get delivered continuously to production so we can get them in front of users very rapidly and that's really important.
Lenny :
This episode is brought to you by Braintrust, where the world's most innovative companies go to find talent fast so that they can innovate faster. Let's be honest, it's a lot of work to build a company and if you want to stay ahead of the game, you need to be able to hire the right talent quickly and confidently. Braintrust is the first decentralized talent network where you can find, hire and manage high quality contractors in engineering, design and product for a fraction of the cost of agencies.
:
Braintrust charges a flat rate of only 10%, unlike agency fees of up to 70% so you can make your budget go four times further. Plus they're the only network that takes 0% of what the talent makes so they're able to attract and retain the world's best tech talent. Take it from DoorDash, Airbnb, Plaid, and hundreds of other high growth startups that have shaved their hiring process for months to weeks at less than a quarter of the cost by hiring through Braintrust network of 20,000 high quality vetted candidates ready to work.
:
Whether you're looking to fill in gaps, upskill your staff, or build a team for that dream project that finally got funded, contact Braintrust and you'll get matched with three candidates in just 48 hours. Visit usebraintrusts.com/lenny or find them in my show notes for today's episode. That's usebraintrust.com/lenny for when you need talent yesterday.
:
Something that I've heard about you is that you get into the weeds, you get really deep as a CTO of a company at the scale of Stripe and I came across this term engineerications, which I think connects to this. Can you talk about that and how you think about just getting in the weeds?
David Singleton :
First of all, in terms of how much getting in the weeds matters. At Stripe, we find that it's very important for engineering managers in particular, but really all managers to really have a very detailed understanding of whether their teams are kind of on the right track and where they're getting stuck in order to make sure that we make the most progress in unit time for our.
David Singleton :
We're getting stuck in order to make sure that we make the most progress in unit time for our users. So we find that, again, the nature of the problems we're solving, really reward domain expertise, like assimilating a deep understanding. And we ask all of our managers to be kind of the editors in chief of their teams plans. And I think the only way to do that is to get the right loop for yourself to understand what is actually going on the ground. Now, it would be really damaging if I was only doing work at the IC engineering level every day. That doesn't ladder up to someone who's able to help guide the team or whatever. So it's important to just judiciously but done on the right cadence. I think it's very, very valuable. So engineer occasion is something that I personally do. So it's obviously a port man of engineer and vacation, but it's not a vacation.
:
The way we get to the name of the tower, at least the way I think about it is what you do on engineer occasion is I'll clear, other people track do this as well. I'll clear several days in a road, three or four days actually join a team, pick up a small task, hopefully a small feature that we can get all the way from start to finish in production and do that going through the exact experience the team has. So you get to understand the developer tools, the build infrastructure, how you get stuff reviewed, how good is the documentation, how long did I have to wait in order to actually see my thing live in order to start that feedback loop that I talked about with users. So you're actually going and joining a team and doing some work.
:
While one does that, it's really valuable and important to keep a friction log because then what you want to do is write up the experience both as an aid memoir for yourself because it then helps you go and for all of the next year's worth of conversations I might be involved in around making trade offs and helping set priorities, that context really helps. So I actually reread these reports periodically and it's also really valuable to actually share them work with the team, which then demonstrates, well I understand what it's actually like and here's how we're going to make sure that we're carrying that information through prioritization. So that's what you do. The name is, it's the often the hardest thing about these is finding the time to clear your calendar for that many days. So the reason I think about it is a vacation is of course people go on vacation.
:
By the way, I work very hard to use all my vacation days every year. I think that taking a break and recharging your creative juices is valuable. So the point is when you're on vacation, the world goes on and it's all fine. So I treat it like I'll decline every meeting in order to clear my schedule and have a maker schedule in order to do that. And so I've done this many times at Stripe. I advise engineering managers at Stripe that they should do an engineer occasion sometime in their first quarter to six months at the company. It gives you a tremendous amount of context for what your teams are actually experiencing and then for folks who do it once a year on an ongoing basis and it provides a tremendous amount of context.
Lenny :
That is insane. I've never heard of that process. How do you stay knowledgeable and up to date on the infrastructure and the code that you have to code and all of a sudden things move so fast?
David Singleton :

**The process is literally to help you do that. I guess maybe something I left out in explaining it is we'll often identify a buddy on the team who's going to help you through. So for what it's worth at Stripe, we write a lot of code in Ruby, we write a lot of code in other just Java type script as well. But our kind of core infrastructure is mostly implemented, core product infrastructure mostly implemented in Ruby. When I started I had never written a line of Ruby in my life and I knew I wanted to do this thing and actually done something like it before joining and I was really scared. How much credibility might I lose if I show up and I can't write a line of Ruby. But my first buddy was a guy called Ajhja who's still at Stripe doing great stuff and he helped me learn Ruby during these three days and they [inaudible 00**:

49:48] me a little bit, but ultimately everyone really appreciated that I've done it.
Lenny :
Imagine being the engineer has to review your PR.
David Singleton :
I tell them this is an important part of the process. Please don't treat me any different to anyone else. And obviously to make this work well you have to set the expectation that you're not going to take me action if something isn't exactly the way you want it to be. It is a moral kind of longitudinal process.
Lenny :
Is there something that you found in this process that comes to mind that was really surprising or interesting or just kind of lasting in the past set of couple years?
David Singleton :
One of the most interesting things that I think I've run into is there are a lot of places that as we scale, we know that it makes a lot of sense to invest in automation and there were a bunch of places in our development process where while we've done that, we were working hard to help each other out and actually saying, hey, please come talk to this other team if you want to use this thing. And if you're working for instance, a different time zone from someone else, it's often the case that actually it would be much better just to document it well and automate it and then maybe make the consultation available. And so running into those kind of pieces of friction and then having a good conversation about it has really helped. But one good thing about Stripe I think is that kind of change doesn't depend on me doing anything.
:
So we really care about making Stripe a place where engineers can do some of the best work of their careers and that means being enabled with good tools and good developer productivity. So we invest a lot in developer productivity. We have a team who work on our dev tools and they actually run exactly the same product development process that I just described for our external users internally. So understand your users really well. Talk to them a lot, as so for instance, we do a monthly survey. We operate in enough scale where we can ping enough people once a month that we get a statistically significant sample of the entire organization without having to get everyone to respond. Every individual respond once every six months. And we ask very directly, what's the experience you're having? And then we use that to prioritize the roadmap of our developer productivity team. We also measure everything so we know where people are getting stuck and when we compare both the kind of free responses and the data, it helps us invest in the best places to make everyone else more productive.
Lenny :
Okay, that's exactly where I was hoping to go next. And let me set this question up. So I saw a tweet of yours recently where I have some notes here I'm going to read that you deploy changes to your core, API 16.4 times a day on average. Your uptime has been 99.999% and one in 10 people in the world have transacted with a business powered by Stripe at this point. And so my question is just what does it take to achieve something like this, especially in terms of tooling and culture and everything else you're just talking about?
David Singleton :
Well I think it's worth saying at Stripe we are trying to do something I think relatively unique, which is what we power for the businesses to build on Stripe our users, it's really business critical to them. We're literally talking about money coming into your business to help you run your operations or make it even possible for you to run your operations and maybe pay your employees and so forth. All the revenue automation that we do around billing subscriptions, our financial automation products, helping you close your books, this stuff matters. You cannot get it wrong. And we also operate, Stripe today, we move as much money as all of e-commerce was when Stripe got started. So we operate very significant scale and so business critical significant scale, we just have a tremendous duty to our users to get this right and be extremely reliable and available for them.
:
So we do think about that a lot. Now there's one way to be very reliable, which is to try to change things as infrequently as possible. Never change anything than you have many fewer opportunities for things to break. But we don't take that approach. The needs of our users are evolving so rapidly, the number of ways that we want to serve them and can serve them is evolving rapidly enough that it matters a lot that we can operate in a kind of constantly changing environment. Hopefully I've explained why that matters like that type feedback because it's only possible if you can actually get something in their hands. So we choose to design the way we work to hold those two things true at the same time and it does take a lot of care and attention and it takes a lot of systems. So maybe just kind of build this up.
:
First of all, there's a lot in our development process and the ways that we take changes into our product that makes this possible. One of those is we really care a lot about having really good test suites. So we believe in automated testing. We don't have manual testers because manual testers couldn't possibly cover the vast array of API endpoint and configurations that we offer but automated test can. So we work hard to have a lot of automated test coverage and then every single change that an engineer produces gets run through this battery of tests before it can even possibly go towards production. And then we work very hard as changes end up in production to put them through increasingly realistic and then more broadly exposed environments. So we have a bunch of staging environments where we'll send a battery of more realistic end-to-end tests. Then finally when something actually goes to production, it starts at very small percentage of the traffic and then wraps up to the hole.
:

**So we can detect problems before they become huge problems. There's a number of things that we had to do to make that all possible. So for instance, every change that Strip engineer submits [inaudible 00**:

55:23] test, it actually ends up in production automatically over the course of the next 45 minutes or so. And I don't think there are a lot of financial services companies, at least not until maybe the last few years that have operated that way. And so that takes a certain mind shift. You actually have to assume that that's going to happen and put the right systems and processes in place. And then the other thing that's important is to recognize that we have to obsess about getting very systematically good at addressing anything that can go wrong. So I mentioned earlier it's really important to me that we are a continuously learning organization.
:
And I mean something else that matters of course is things will go wrong. Sometimes there is a downstream partner where something breaks, other times there is a particular kind of network outage side of our control or whatever. So things will go wrong. So it's important that we have the right systems in place that minimize the damage that any individual thing going wrong can cause. And we work hard on that. We have redundant systems in a bunch of places. We think hard about how something that breaks for one user wouldn't kind of carry over into other users and then we actually very actively work hard to put things right when they are wrong. So that's called instant response at most companies including Stripe. I actually think Stripe is very, very good at instant response. We've got very good tools for both declaring incidents and then pulling the right people together to put them right.
:
But we don't stop there. We really obsess about reviewing them carefully and identifying not only what would've stopped this thing happening, but how could we prevent this whole class of issues in the future. And as I said earlier, we prioritize working on that stuff ahead of anything else on the roadmap that's because of remember what it is we're trying to do, how important it is and how if we don't do that well, we can't move quickly for our users. So that's how we do it.
:
By the way, I don't want to come across here and sound like we've got it all figured out. Of course all of this is always entirely influx. We're always anxious to figure out how we can make it go better. For instance, in recent years we realize that we could get a lot of benefit from what we call chaos testing. That's like injecting errors and making sure that the systems respond in such a way that it doesn't cause any impact on users. So it's constantly evolving and we really enjoy learning from other companies and learning from our users as well. But it's something we care about and think very rigorously and systematically alone.
Lenny :
Did you say that it takes only 45 minutes from pushing code to it going into production?
David Singleton :
Typically yes. So that battery of tests that I described, that gets run on every change, that gets run in parallel to when you send it for review by another human. So it's run once, typically takes about 15 minutes and then once the changes merged into our code base, we run that same test suite one more time. So another 15 minutes then typically takes about 30 minutes for the systems to automatically deployed in production. That's how we run and think about establishing that tight feedback loop with users, that means you can get feedback from a user in the morning, you can figure out how to address it and you can actually put something back in their hands by the end of the day. And that loop running inside of 24 hours I think is pretty important.
Lenny :
That's incredible. I remember times that Airbnb where took hours for tests to finish because there's a lot of them and they fix that over time. But I'm used to more on that scale.
David Singleton :
It takes constant effort to hold. Those numbers by the way are important. Those are about the right numbers I think for a company operating our kind of scale. Of course as you add more stuff, you add more tests. So we've had to work on, we had to invent mechanisms to make it run more in parallel, we now have a thing called selective test execution where we figure out for not the battery that runs before it goes into production that we run everything and just run it in more machines to make it parallelize. But for the changes or the tests that we run for individual changes, we actually have systems that figure out, well which tests are the ones that might be material for this particular thing? And that's been a real source of innovation. In fact, our distributed change and test environment at Stripe is the biggest distributed system that we actually run. And so running that requires just as much energy and effort and rigor and craft as everything else.
Lenny :
What are some of the things you've done that have had the most impact on developer productivity?
David Singleton :
We've touched on a couple of these already. That auto deploy mechanism definitely had a very significant individual impact. So before we introduced that, sometime within the last five years each deployed to production required an engineer to actually babysit it, to watch it as it, make sure all the charts look good. And it was a bit of kind of game of roulette because you always wish that your change would get bundled in with someone else's so that they were paying attention to it for you. So literally being able to be fingers on keyboard on something else while your change is going live and it's going to automatically monitored, that was a big improvement in our productivity. Also, very small things. This is just like optimizing checkout, very small changes really compounded in a big way. So for instance, by eight months ago we made it possible, we use a tool for code review.
:
It's quite popular, it's GitHub enterprise, but we've built a bunch of our own experiences and controls around that and we have a little tick box that you can tick on your pool request. That's what you call an individual change that an engineer produces that is auto merge, which means once the reviewer says this is good, I don't need to come back and look at it again, the system should just take over and that just cuts out one whole kind of human distraction step and that laddered up to a big change in productivity as well. So these very small changes can if you're deliberate with them, ladder up to a big impact.
Lenny :
I'm going to go in a different direction now. AI very hot right now. Has AI impacted the way you all build product yet? And if not, where do you think it starts to go in the next few years?
David Singleton :
Yeah, we're very excited about AI. Now to just take one step back, Stripe has been using machine learning and advanced machine learning techniques at the heart of our products since the very early days. Radar is our solutions for payment fraud and it has used, I mean this is the very core of our products and has used machine learning since we introduced it. We also, if you think about the nature of Stripe, we operate in an environment where we have to do a lot of work to kind of catch bad actors in the system, fraudsters or fraudulent businesses. So we've been employing a lot of machine learning techniques there again for years and we couldn't operate the company without them. So the difference between ML and AI, I think when we think about AI today we're mostly talking about the applications of large language models, but those are really based on this new technology called Transformers.
:
It was a paper that came out of Google a while back about four years ago, five years ago. And we put transformer technology into those systems at some point more than a year ago. And it's proved to have a very profound impact on our ability to solve those problems for our users, which is great. But we are also excited about the applications of large language models. I mean there's really two dimensions to this. Number one, we feel privileged to be able to help serve and power a lot of businesses getting started in this space. One big difference between AI startups and others is it's actually quite expensive to operate an AI startup in terms of the compute resources. Like running this stuff in these GPU machines is quite expensive. So typically these companies need to have a monetization model from day one. And I'm really excited to say most of the AI on these is running on Stripe and we're working very hard to make sure we serve all their needs.
:
Open AI, for instance, using us for monetizing chat GPT plus and all their other products. But they don't just stop there. We're actually helping power all of their subscriptions and revenue tracking and financial operations around the business. And the point about that is we've been putting very large engineering teams on this stuff for years and that means anyone who wants to build a reconciliation product and a subscriptions business model, if you want to do that yourself, you have to put big engineering teams on them. But if you can use Stripe instead, you can actually focus those really precious engineering resources on keeping up with the rate of breakneck innovation in this space. So we're excited about that, but we're also really excited about the applications of these AI techniques on our own ability to serve our users better. And so for instance, at sessions we'll be talking about a few of these.
:
We started working with OpenAI when they had the beta. It was a kind of private beta of GPT four available at the beginning of this year. The first thing we thought of was we've got a lot of documentation on Stripe and we put a lot of care attention into making it good. But if you want to achieve something with your Stripe integration, you're typically going to spend quite a lot of time reading docs and kind of synthesizing them as an end user. We realized we can have GPT four read all of our docs, store them as embeddings and then answer questions for developers. And so we now have that available in kind of early stage release inside of our documentation. It's turning out to be pretty valuable. We've also been able to apply these techniques to other areas of our products. So something that we're going to show an early version of IT sessions is we have a really powerful product as part of our revenue and financial automation suite, which we call Sigma.
:
It allows you to write sequel queries across all of your Stripe data so you can interrogate your Stripe data to understand your business and really fine grain detail. Which country has the fastest growing sales, which segment in which country has particular attributes to it? Very powerful product, but it's one that is potentially challenging for non-developers to adopt. You do have to know how to write sequel queries unless you just use the ones in the menu in order to get the full value out of the product. Well it turns out with large language models, we can apply this technology where you can ask questions in natural language and our engine will actually write the sequel query for you. And we've had to do a lot of work to kind of tune that to make sure that it's reliable and understandable and it's going really well. And we also see great applications in actually applying these technologies to make us more efficient internally, answer users questions faster, help each other out more quickly. And so we're doing those things as well. One concrete thing that we did, which I'm pretty excited about is not long after we saw chat GPT come out, we realized it would be really awesome if we could apply that to many use cases inside of Stripe. But as you can imagine, a lot of the data that we are dealing with on a daily basis is very sensitive to our business, to our users and we care a lot and we have a lot of governance around this, but we wanted to make that technology bill. We couldn't say, Hey Stripes, go and use chat GPT. So we stood up an integration to GPT four and an internal UI to use models like that. But here's the thing that I want to kind of relate to all of your viewers. We find that we built presets into that.
:
So when you work with large language models, you want to write a prompt that then helps get the model into a state where it's going to be able to solve the particular problem at hand. And we find that writing prompts is something that's accessible to folks across lots of different job families, not just engineers. Folks in our marketing team, folks in our user support team have been able to use this as well. But you can put a lot of care and attention to getting a prompt that works really well and we not make it possible for those to be shared across the company. So I can grab the preset to help me write a blog post with the right kind of tone and I find it extremely valuable in helping me and many other people across the company. So I think there's a lot of innovation in high companies serve their users and operate is possible right now and we are working hard to employ all of that on behalf of our users.
Lenny :
What about as engineers? Are pro co-pilot, is there some along those lines that you find useful weary of? How do you think about that?
David Singleton :
We're excited about co-pilot. We've made co-pilot available to our engineers internally. We ran a fairly rigorous trial to make sure that we felt good about its actual impact on our ability to write code and the code it was actually generating and find that it was very effective for us. Both in productivity but also just in helping our engineers feel like they could direct their energy towards some of the bigger problems. How should this stuff fit together rather than some of the micro problems. So because we had such great feedback on that, we've made it available very broadly internally and we'll be very excited to see where that space develops over time.
Lenny :
Do you have a sense of the productivity gain that say imagine you have a lot of 10X engineers, the gains that an amazing engineer gets out of a co-pilot versus a newer engineer?
David Singleton :
It's honestly too early to tell because we've only recently made it available at scale. What we're typically seeing is that the kind of tasks that it accelerates are, remember I mentioned how much energy we put into having comprehensive test suites. It's actually using co-pilot to generate your test cases, turns out to be extremely valuable. There's a reasonable amount of boiler plate that is kind of like repeated code and concepts that goes into writing good tests. But you also have to reason very carefully about is this actually testing is exactly what I want? So co-pilot takes a lot of that boiler plate generation out of the way. So you're actually thinking about the stuff that really matters. And I think that is going to have a profound impact on quality of code that we write as well. But it's a little too early to say, because we literally just folded out what kind of actual measurable impact is having.
Lenny :
I was talking to an engineer and he's just like, I like the active writing code and it makes me sad that this is doing this for me. So he turns it off.
Lenny :
This is doing this for me, so he turns it off. I think over time people will be like, "Eh, that's true. I never really enjoyed this part of it."
David Singleton :
Yeah, I'll speak from personal experience. I love writing code. I really love writing code. It's pretty much what I do for fun. I also love writing code with Copilot, because as I said, it means that I can focus on the parts that really matter. I think that's been a fairly consistent experience across Stripe as well.
Lenny :
Awesome. You run a massive engineering team. I don't know if you shared the numbers of engineers, but I know there are many. What are, and this is a broad question, just what are some lessons you've learned about managing people and/or managing engineers, whichever direction you want to go?
David Singleton :
Wow, big question. There are so many different directions we could take that. I'll share a few observations. They don't necessarily all have a particular theme to them. I think as I've been responsible for bigger and bigger teams over time, one of the things that just I repeatedly learn is I personally will not be involved in really any of the decisions that matter and happen. There are thousands of decisions that an organization of any skill is making every single day, every individual engineer or PM is making hundreds of small decisions and some big ones every day that affect the kind of general trajectory.
:
The most important thing is to really focus on hiring the right people, and that means hiring people that you can trust with a tremendous amount of autonomy. If I try to get involved in lots of decisions, everything will grind to a halt. How do you do that? It is important, obviously, to be rigorous. We've described already what our hiring process is. I really lean into getting to know folks in very, very well as we're hiring them. By the way, something I didn't mention earlier that is I think important here is we pay a lot of attention at Stripe during the hiring process to references.
:
This is typically later in the process, but if you put someone through an interview process, you've probably spent what, eight hours total with them? If you talk to people that actually have worked with them before, you're probably benefiting from thousands of hours of direct experience. We take this very seriously, and we try to ask smart questions that will help get real signal out of that. I certainly find when it comes to hiring folks that have then gone on to really make a transformative impact, that references are often the time that you get the best conviction on the hire or not.
:
Hire the right people, and then you have to trust them. Now, trust is interesting. Is actually quite challenging to trust people that you've just hired, right? Well, you've got no stake really on you yet. What I find is you do actually just have to be generous in giving trust and assuming trust by default at the beginning. Then you do need to hold people accountable enough that they are proving that they can handle that trust. Sometimes, that means hiring someone who you think quite plausibly can end up in a very big role into a smaller role to begin with. Other times, you just have the big role that you need to fill, in which case, it's important to be quite conscious about really trusting and delegating to them with a lot of support.
:
I'm always working hard to delegate sometimes a little bit more than I'm comfortable with, because that's the only way to really operate at significant scale. I think something else, and sorry, this is really a smorgasboard is what a lot of differences.
Lenny :
Perfect.
David Singleton :
Something else I've realized as the organizations I work with and been responsible for have grown is that you have to be extremely conscious about managing your own time. There are hundreds or thousands of people who, quite legitimately, might want to get some time with you. If you just let the places that you spend your time and energy be controlled by the stuff that comes into your inbox, or the stuff that gets put on your calendar, that's going to be random. It's quite likely that that's not laddering up to the biggest impact. I personally have been running a loop for, I don't know, maybe 10 years, where on Sunday evenings, and usually, well, it usually starts on Sunday afternoons, I read a lot of what happened last week.
:
Then on Sunday evenings, I actually write a list for myself of, you asked me a question at this podcast, which is like, what would be great success for this podcast from your perspective?
:
I basically think about that for my week every Sunday night. I make a list of if we got these things done this week, that is a good week, but obviously, we need to be dynamic. Things will surprise you through the week. Honestly, then, that drives a lot of just where I decide to spend my time. I try to encourage everyone to think that way throughout the organization. I think it does ladder up to more impact over time. I think the final thing I'll say here is I mentioned how important operating principles are to the culture. I think for any manager and any leaders, that includes ICPMs as well, but for any manager, any leader, how you show up really does set the culture that is around you.
:
I try very hard to show up very consistently every day, even though there will very frequently be things that are going wrong and are bad and are hard. It's actually very important to show up quite consistently. Certainly, in line with all the values that we have and the culture that we want to set, in order to really kind of model that at scale. Different days, that can be easier and harder. The final thing is, I think it's quite important to manage your own energy.
:
There are some tasks that I do that are maybe not the most important thing, but I know that I get a lot of joy and energy from them, and then that carries over into the other stuff that also needs to get done.
Lenny :
Just two more questions before we get to our very exciting lightning round. One is just I feel like Stripe is incredibly good at planning and organizing, prioritizing. I know every inside, it's always not as beautiful as it may seem on the outside, but what have you learned? What has Stripe learned about planning and prioritizing that you think other companies might be missing?
David Singleton :
Yeah. Well it's funny you say that. I would say planning inside of Stripe does not get the highest net promoter score that you might imagine. I do think it is actually quite effective. By the way, the reason I think that planning, the way we do planning at Stripe doesn't always get the best internal rep is we have grown very rapidly. That means that almost every time we come back around to planning, we actually, and this is kind of a theme at Stripe, we think about a lot of the ways that we work internally from First principles.
:
We will tend not to by default just pick a system off of the shelf that some other company has run or that we've used before. We'll think hard, considering what we are doing for our users. How should we do this? When we're thinking even first principles, we'll often go out and talk to a lot of other companies, and try to learn from their experience. It's actually something I've really appreciated and enjoyed at Stripe. A lot of the learning I've done here has come not only from folks that are at the company, but also talking to a bunch of folks that we have the privilege to work closely with because their business is building on Stripe, or they're a similar stage of scale to us.
:
A good example of this is Amazon. Amazon is a Stripe user. Because we work with them, in my first couple of weeks at Stripe, I was actually able to meet with Charlie Bell, who then ran operations at Stripe. A lot of the things that, sorry, who then ran operations at Amazon. A lot of the things that we actually now do at Stripe have come from learning from that experience. It wasn't just, oh yeah, we'll take this thing cause Amazon did it, talk to him. Lots of other companies hard to learn. The point is we care about learning from others and then we apply it.
:
Bringing this back to planning, because we tend to think a lot from first principles and we've been growing rapidly. The right planning process for us as a company has actually changed quite dramatically and quite significantly over the years. We do planning in a relatively deep way once a year, and then in a slightly lighter way halfway through the year. If you imagine doing someone once a year and you're growing rapidly, you're going to want to revisit exactly how you do it. I think for anyone who has the privilege of running the same planning process again and again, you can really iterate it and tune it. We've had to make more deliberate and more sweeping changes as we've gone along. There are a couple things at the core of how we do this. One is it's really important to focus on who are the users that we are seeking to serve for any given product area that we're working in? Kind of holding their needs front and center in your plans is important. Again, at Stripe, we do something that is, it's not unconventional, but it's not the most common practice in the industry, which is we work very hard to serve companies from the very, very small. The folks that are literally just starting their company on Stripe, with Stripe Atlas, all the way up to multinational, 10 Fortune five companies, fortune one companies, I guess.
:
There's a very different set of user needs across those businesses. For any given area, it's very important for each team to be clear about who are they serving. Then we run a kind of inverted W process. We typically have teams surface what their immediate thoughts are on the most important things to do. We'll then have a group of product leaders get together and try to synthesize the most important parts of that into a kind of draft overall company strategy, and then take that back down to teams to figure out, "Well, if that's where we're making a big push, should that tweak my plans at all?"
:
We bring it back up for synthesis, and then back down for everyone to really distribute with a lot of context within their orgs. We find that at our current scale, very, very effective.
Lenny :
I haven't mentioned this yet, but I actually, Stripe for my newsletter, I check the app many times a day, so I'm probably in the Fortune 1 million, somewhere in that.
David Singleton :
Do you have any feedback? Genuinely, I'd love to hear your Stripe feedback.
Lenny :
It's great. The app tells me that I'm ...
David Singleton :
No, no, don't tell us it's great. What bugs you?
Lenny :
Well, it's interesting for churn, for cohort retention, which I care a lot about for the newsletter, I actually use a different tool that feels like gives me better, a table of per cohort, how many people are still around? There's an opportunity to have better cohort retention metrics.
David Singleton :
Cool. Okay. Well, maybe we can email about that. Quite genuinely at Stripe, anytime we talk to a Stripe user, we are always looking for feedback that goes for any occasion. We often bring users into the beginning of our Friday fireside I already mentioned, and we're always asking them for their feedback and we really, really want to act on it.
Lenny :
Well, I wish I had more. It's works great. Final question, Stripe Session's coming up, it's going to happen before this comes out. What should folks be watching for? What's next for Stripe?
David Singleton :
We've touched on a few of the things that we're sharing broadly for the first time at Stripe Sessions on this call already. Per our development process, these have been in the hands of some Stripe users for a significant amount of time and we've really kind of crafted them with them. I'm super excited about a number of the things that we're going to be talking about next week. One is I've mentioned our revenue and financial automation suite.
:
We've really been crafting the features there for some time, and really nice example actually of how building closely with users really, really helps build things at scale. We've a set of features that we work with companies like Atlassian and CloudFlare to enable their businesses on Stripe Billing. They have relatively complex models. For instance, you might sign a deal where it has a discount in the first year, and then there's another product that's being used in the second year, and then something else happens in the third year. You can now model all of that in Stripe Billing, and we're going to be showing how you can do that in the dashboard at Stripe Sessions next week.
:
It's now going into general availability for all Stripe users. It's giving all of our users from the very small to the very large, the same power that the world's best SAS platform might have. Excited about that. It's also the case that we didn't talk about it in this call, Stripe Connect is our product for platforms of marketplaces. If I may actually just take one second, it's a really good example of how focusing on the needs of our users in one area took us into a really valuable space to solve for many users in other areas.
:
The ideas behind Stripe Connect came from working with companies like Lyft and Shopify. In the very early days, they were using Stripe for pay-ins, but we realized, "Oh, these companies are operating these multi-sided marketplaces, and there's a ton of heavy lifting you have to do to make that work really well." We have to have a bunch of regulatory licenses in place, but also there's a lot that you need to do to actually make the money move and kind of account for it in the right way. Connect is our product for platforms and marketplaces.
:
One of the things that we've done over the course of the last year or so is actually taken a lot of the features that we've built in the Stripe Dashboard to help folks manage things like gathering the right documents from their users, or handling refunds and so forth. We've actually made them available as embed-able UI components that are also completely customizable, which these platforms can take and put inside their own dashboards so they can present a lot of the power that Stripe is enabling to their customers, without having to do a ton of engineering work themselves.
:
Look, generating engineering leverage for our customers is just very frequently the main thing that we can do to help their businesses. We're going to show a bunch of that stuff next week, which I'm excited about. Then finally, we touched on it already, but it'll be great to show some of the innovation we've had around AI and large language models. Again, I think it's going to make a big impact over the coming years.
Lenny :
Well, with that, we've reached our very exciting lightning round. First question, what are two or three books that you've recommended most to other people?
David Singleton :
Most means that you have to integrate under the curve, so I'd say High Output Management by Andy Grove is definitely the book that I've recommended the most. It was a book that really opened my eyes to how to get the most out of teams over the whole course of my career. Definitely check that out if you haven't read it already. Recently, we talked about being meticulous in our craft. I've really enjoyed Build by Tony Fidel. Tony worked on the iPod, and then the iPhone, and then was the founder of Nest.
:
He puts a tremendous amount of thought into his users and how to build really great crafted experiences. I had the privilege of working with him very briefly at Google, but I thought the book was excellent in terms of helping provide some practical pointers there. Then I would be remiss if I did not mention Claire Hughes Johnson's book, Skilling People. Even though it only just came out, I've recommended it a lot. There's actually some stuff in here where I'm sharing some techniques that we've used at Stripe, so you might enjoy that. Then if I may share one ...
Lenny :
Here's my copy.
David Singleton :
You've got it too.
Lenny :
... it supports ...
David Singleton :
Amazing.
Lenny :
... Supports my laptop on here, and ...
David Singleton :
I hope you've read it.
Lenny :
I've had her on the podcast. I've read, I've skimmed it as much as I can.
David Singleton :
Yeah.
Lenny :
I'm not building a business right now. She was in the top 10 bestseller list on the Wall Street Journal, I saw.
David Singleton :
That's right, that's right. It has a ton of very practical advice, so I recommend that one a lot.
Lenny :
What's a ,favorite recent movie or TV show?
David Singleton :
Okay, I'm going to cheat here because I'm going to interpret that as what's the best video content you've seen recently?
Lenny :
Sure.
David Singleton :
I have fallen in love with YouTube for learning about the really fast moving AI space. It has been remarkably valuable, and Andre Carpassi has a bunch of really good seminars, but not just that. Across the whole spectrum, I think there's just so much gold on YouTube if you want to learn a new skill these days.
Lenny :
Is that the channel you recommend, Andre Carpassi's channel?
David Singleton :
His channel is awesome if you want to learn about AI.
Lenny :
He's the ex-Tesla AI?
David Singleton :
That's right. I believe recently, gone to OpenAI, but was doing this kind of on his own for a few months and has produced a bunch of great YouTube content.
Lenny :
Great pick. Most people pick White Lotus or something like that and you go with a AI YouTube channel. I love it. What's a favorite interview question you like to ask?
David Singleton :
Okay, well, actually, you will find some recommended interview questions from me in this book. One I really like actually, because it sounds like a softball and then it's not, is I often ask people, especially for leadership hiring, which leader that they've worked with they admire most and why. It sounds like a softball, but it actually tells you a lot about what this person really cares about in leadership.
:
Sometimes, I'll follow up and ask, "How does that manifest in your own leadership style?" Then, and this I think is really quite telling, I always ask folks, I'm going to spoil my interview question, I'm revealing it in your podcast, but I always ask folks, "Okay, so imagine you were their manager. Tell me the performance review or the development feedback you'd give them to help them be more effective." I think everyone always has things that they could improve, certainly myself included.
:
Folks' ability to think critically about someone that they kind of admire or lionize, and how they could actually be more effective, I find quite telling.
Lenny :
What are some favorite products you've recently discovered that you love?
David Singleton :
The products that I have recently discovered and definitely love is Mid-Journey, also building the business side of their business on Stripe. For folks who don't know, Mid-Journey is an AI tool for generating images using stable diffusion, but it's really pretty awesome. I've been using it a lot with my daughter. We'll come up with stories and we'll generate beautiful looking images with Mid-Journey, and then she'll drop them into books and she'll write the pros. The reason I think it's pretty cool is I was very surprised and skeptical at its UI to begin with, because its UI is Discord.
:
They drop you into Discord and you are in a channel where you have to prompt the artificial intelligence. I find it very confusing at the beginning. It's like, this is not the right interface for this tool, but actually, it's very smart because you learn from other people on Discord, how they're prompting the AI in order to get the kind of results that they're looking for. I find that made it possible for me to get a lot more power and value out of the tool. I definitely subscribe to Mid-Journey and have had a lot of fun playing with it.
Lenny :
What's your favorite image that you've created, if there's one that comes to mind?
David Singleton :
We made a cover for a book that my daughter is writing. My daughter is nine years old by the way, so we're talking here, good children's stories. She made an image of a wolf wearing a purple velvet cloak, sitting in front of a campfire with a shack in a forest and a nebula behind. It's beautiful. We actually built that with by combining two images, the wolf and the shack. Actually getting the wolf out of one image and putting it onto the other, we used the new Apple image segmentation copy and paste thing, which worked great. It's also fun combining these AI tools, but that one has been pretty good.
Lenny :
What a world. Two final questions. What's something relatively minor you've changed in your product development process that has had a tremendous impact on your ability to execute as a team?
David Singleton :
We talked a bit or about this already, auto deploys and that auto merge feature, but probably the most profound thing is we put a little button in every single developer tool at Stripe. It is an emoji of an octopus that is crying. If you click it, it makes it possible to just type in what's gone wrong. Then we have our developer productivity team read all of those and use them to prioritize what they're up to. Just like frictionless problem recording turned out to be really valuable. We call those paper cuts.
Lenny :
Crying octopus. I love that.
David Singleton :
Yeah.
Lenny :
Who else from Stripe or Former Stripe should I have on the podcast is my final lightning round question?
David Singleton :
I see how this works.
Lenny :
This isn't how this works.
David Singleton :
Two Stripes I think you should have on. Emily Sands is our chief economist and leads our information org. I think includes data science, but also the teams that build all of our, a lot of our internal tools. I think Emily just has great frameworks for thinking about how to translate what's really going on for users into great sets of metrics that you can then use to get the right action happening. As I described before, that's super important.
:
The second person would be Michelle Boo. Michelle joins Stripe as an engineer in the very, very early days, and has been with us for obviously a long time. She's really our principal product design architect in terms of the actual abstractions that we use to model our users' businesses on Stripe. I think she has very deep insight into how to think about getting those things right. I think you would enjoy talking.
Lenny :
David, I so appreciate you making time for this, especially during this hectic period ahead of sessions. Two final questions. Where can folks find me online if they want to reach out, maybe learn more about what you're up to you, and then how can listeners be useful to you?
David Singleton :
Cool. Okay. Well, I am @DPS on Twitter. That is definitely the best place to get hold of me, but you can also check right my personal blog at blog.singleton.io. Useful, honestly, please send me Stripe feedback. You can do that on Twitter. You can discover my email address on my blog as well. I would love to hear how we could serve you better.
Lenny :
David, thank you again for being here.
David Singleton :
Thank you. It was a lot of fun, Lenny.
Lenny :
Same. Bye, everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcast, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review, as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at LennysPodcast.com. See you in the next episode.
