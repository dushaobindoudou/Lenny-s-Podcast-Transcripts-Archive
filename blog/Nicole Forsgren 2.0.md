# Nicole Forsgren - Lenny's Podcast Insights
## Nicole Forsgren - Lenny's播客洞见

---

## About the Guest | 关于嘉宾

**Nicole Forsgren** joined Lenny for an in-depth conversation on product management, leadership, and building successful products.

**Nicole Forsgren** 与Lenny进行了深入对话，讨论产品管理、领导力和打造成功产品的经验。

---

## Key Takeaways | 核心要点

### [inaudible 00

12:37].
Nicole Forsgren :
... yeah, as some proxy as some proxy for output or productivity or complexity or something. Well, now, for many of the systems, that they would sometimes whisper and not super talk about that uses lines of code, it's just blown out of the water because, "What do you mean by lines of code?" If the goal is more lines of code, I can prompt something to write the longest piece of code ever and add tons of comments. We know that agents and LLMs tend to be very verbose by de...

### Yeah. So in the context of knowing we have about four hours of good deep work... I'm sure many of us have probably hit this, right? We have good periods. Maybe it's morning, maybe it's afternoon for folks. And then you hit a time where you're like, "I'm going to clean up my inbox because that is all I can do right now. I can be functional, but I'm not going to come up with my best innovative, problem solving, authoring, code writing work." A lot of times, the way to do that and to get into it is to have these long chunks to get into flow and to get that deep work. Usually, I'm [inaudible 00

19:43] two hours-ish. An hour can be tricky because it could take time to get into that state. Okay. Well, when we think about what it used to be like, back in the old days, three years ago, three and a half years ago, we could block off four hours of time and we could probably get two or three hours of really good work done. Because we were just focused, right? There were no interruptions, minimal interruptions.
:
Now, the nature of writing code and systems itself is interrupt driven or full of...

---

## Full Conversation | 完整对话

*Below is the complete transcript of the conversation.*

*以下是完整对话记录。*

**[inaudible 00**:

12:37].
Nicole Forsgren :
... yeah, as some proxy as some proxy for output or productivity or complexity or something. Well, now, for many of the systems, that they would sometimes whisper and not super talk about that uses lines of code, it's just blown out of the water because, "What do you mean by lines of code?" If the goal is more lines of code, I can prompt something to write the longest piece of code ever and add tons of comments. We know that agents and LLMs tend to be very verbose by definition, and so it's just too easy to gain that system and then introduce complexity and technical debt into all of the work that you're doing. I will say there are some things that we can kind of watch and pay attention to because... So lines of code as a productivity metric isn't great, it's pretty bad. But now, it's kind of more relevant if we can tease out which code came from people and which code came from AI because now we can answer downstream questions.
:
"What is the code survivability rate? What is the quality of our code? Is our code being fed back into trained systems? And for that code that's retraining systems later, especially if we're doing fine-tuning and local tuning, how much of that is machine generated? What types of loops is that creating, and what types of patterns or biases might it be inadvertently introducing?" On the one hand, it's not good as a productivity metric, but it can be useful. I'll even say the same for DORA. I have done DORA metrics, their speed metrics, their stability metrics. If that's all you're looking at, it's not going to be sufficient anymore because AI has now changed the way we think about feedback loops. They need to be much faster. Now, what DORA's meant for, kind of assessing the pipeline overall in terms of speed and stability. Still, that works. But we can't just blindly apply the existing metrics we've used before because we'll miss super important phenomenon and changes in the way people work.
Lenny Rachitsky :
Interesting. You invented DORA, that was kind of the main framework people used for a long time to measure productivity. And then there's SPACE, there's Core 4, there's probably others. So what I'm hearing here is all these are kind of out of date now, where AI is contributing large portions of code.
Nicole Forsgren :
I will say if it is a prescriptive metric, it needs to be used only in the way it was prescribed.
Lenny Rachitsky :
So
Nicole Forsgren :
DORA 4, there are four key metrics. There's two speed metrics, deployment frequency and lead time. So code commit to code deploy. There's stability metrics, MTTR and change fail rate. If those are used to assess the speed of the pipeline and the general performance of the pipeline, that's great. If you're trying to use those to understand... Because implied in that is feedback loops, right, because you used to kind of get feedback from customers. But we can't just use that blindly now when we're using AI, as an example, because we have feedback loops much earlier and not even just at the local build and test phase. We have feedback loops throughout, and even sometimes in the middle of some of the pipeline, that we really want to leverage in ways that weren't as useful before. I won't say they weren't possible, but we just didn't really focus there.
:
So those are prescriptive metrics. When we think about SPACE, SPACE is a framework. It doesn't tell you what metric to use. So I'll say, sometimes people get real frustrated because I didn't tell them what to measure. But now, I think that's the power of it. We're actually seeing that SPACE applies fairly well in these new emerging contexts like AI because we still want to look at... SPACE is an acronym. We still want to look at satisfaction. We still want to look at performance, what's the outcome. We still want to look at activity. Yes, in some ways, lines of code and number of PRs can be useful for something, or number of alerts or number of things, activities or counts. Seize communication and collaboration, this is also super important and useful because it's how our systems communicate with each other, and also how our people do. "What proportion of work is being offloaded to a chat bot versus talking to a senior engineer on the team?" More isn't always better and less isn't always better, it depends.
:
And then efficiency and flow, "Can people get in the flow? How much time does it take to do things? What is the flow like through our system?" Here, I would probably add a couple of dimensions. So chatting with some of the early authors to say trust. Not to say trust wasn't important before, but now it's very, very front of mind. Right? Before you build your code, if the compile comes back, you're fine. And that's the way it is. LLMs are non-deterministic. Right now, we can't just put in a command and guess something back and accept it. We really need to evaluate it, so, "Are we seeing hallucinations? What's the reliability? Does it meet the style that we would typically write? And if it doesn't meet, is that fine?" So it depends on... Prescriptive. You got to make sure you're using it fit for purpose. Right?
Lenny Rachitsky :
We're going to get to your current thinking on the best way to do this stuff. You have a book coming out that explains how to do this well, so we're going to get to that. One thing I wanted to highlight in our last chat that we had, you highlighted that one of the biggest issues we're going to probably have with AI is trust, understanding and learning how much to trust the code that it generates, and also how much... you said this, two and a half years ago, that so much of the time is now going to be spent reviewing code versus writing code. That's exactly what I'm hearing.
Nicole Forsgren :
I think it'll be interesting to see how that impacts the way we structure work moving forward. We were talking about flow state and cognitive load. Now that our attention has to focus on things at certain times and it's broken up from how we used to do it, I think there's some real opportunity there to, not just rethink workflows, but rethink how we structure our days and how we structure our work.
Lenny Rachitsky :
Can you say more about that? Just what is that? What are you thinking will be happening? Where do you think things go? What are you seeing working?
Nicole Forsgren :
This is purely speculative. But for example, Gloria Mark has done some really good work on attention and deep work, and humans can get about four hours of good deep work a day. That's about it.
Lenny Rachitsky :
Yeah,. I feel that.
Nicole Forsgren :
That's kind of the upper limit-ish for the most part, and I'm sure people are going to be like, "Well, I am superhuman and I can do-
Lenny Rachitsky :
What if you take 20 grams of creatine?
Nicole Forsgren :
Right. What if we microdose?
Lenny Rachitsky :
Yeah, exact;y.
Nicole Forsgren :

**Yeah. So in the context of knowing we have about four hours of good deep work... I'm sure many of us have probably hit this, right? We have good periods. Maybe it's morning, maybe it's afternoon for folks. And then you hit a time where you're like, "I'm going to clean up my inbox because that is all I can do right now. I can be functional, but I'm not going to come up with my best innovative, problem solving, authoring, code writing work." A lot of times, the way to do that and to get into it is to have these long chunks to get into flow and to get that deep work. Usually, I'm [inaudible 00**:

19:43] two hours-ish. An hour can be tricky because it could take time to get into that state. Okay. Well, when we think about what it used to be like, back in the old days, three years ago, three and a half years ago, we could block off four hours of time and we could probably get two or three hours of really good work done. Because we were just focused, right? There were no interruptions, minimal interruptions.
:
Now, the nature of writing code and systems itself is interrupt driven or full of interruptions, at least, because you start something and then it interjects. So how do we think about that? Does that mean that a four-hour word block is still useful? Probably. But does that mean that now we can also make a 45-minute work block useful? Because getting into the flow is actually kind of handed off, at least, in part to the machine or the machine can help us get back into the flow by reminding us of context and generating diagrams of the system and all the things. So I think that's a really, really interesting area that's just ripe for questions and opportunity. And please, folks, do this research and come back to me because... It might not make my list, but it's such a great question.
Lenny Rachitsky :
That is so interesting. Essentially, every engineer is turning into an EM, engineering manager, coordinating all of these junior AI engineers. So your point is even if you have a 30-hour block, you can get deep into code, but you can unblock all these AI engineers that are running off doing tasks. Plus, your point is they remind you of just like, "Here's where you left off. Okay. You can just jump into this code, maybe make some tweaks."
Nicole Forsgren :
Yeah.
Lenny Rachitsky :
So interesting. Let me zoom out a little bit and... Before we get into your framework for how to approach developer experience, the latest thinking you've got, beyond just obviously engineers doing more is great, what's your best pitch for why companies should really, really focus on developer experience?
Nicole Forsgren :
I hate to say return of investment, but the business value is... the opportunity here is huge. In general, we write software for fun and for hobbies, but we also have software because it meets a business need. It helps us with market share, it helps us attract and retain customers, it helps us do all of these things. And I think DevEx is important because it enables all of that software creation, it enables all of that problem solving. It enables the super rapid experimentation with customers that... Before, you'd need a while for a prototype and maybe a little bit longer to actually flight it through an A/B test on a production system. You can do it in hours, right now.
Lenny Rachitsky :
Maybe the opposite end of the spectrum, getting very tactical, before we get into the larger framework, what's just one thing that you think an eng team, a product team can do this week, next week to help their developer experience maybe get more done?
Nicole Forsgren :
Honestly, I think the best thing you can do is go talk to people and listen. I love that the audience of this podcast is primarily PMs because they tend to be really good at this. And I would say start with listening and not with tools and automation. So many times companies are like, "Well, I'm just going to build this tool," or, "I'm going to build this thing." Often you build a thing that you yourself have had a challenge with or that is easy to do, easy to automate. And if you just go talk to people and ask the developers like, "Think of yesterday, what did you do yesterday? Walk me through it. What were the points that were just delightful? What were the points that were really difficult? Where did you get frustrated? Where did you get slowed down? Where was there friction?" If you go talk to a handful of people, a lot of times, you can surface a handful of things that are relatively low lift and still have impact or you can identify a process that's unnecessarily complex and slow.
Lenny Rachitsky :
So the listening to, I hear, almost is you want to help your teams move faster and be happier eng teams. Your advice is just, "Before you do anything, just go ask them what is bothering you."
Nicole Forsgren :
Go ask them, yeah. And trust me, most developers are going to be more than happy to tell you what's broken and what's bad. I'll say, there was one company that I had worked with. I remember they had a process that was really difficult and it was on an old mainframe system, and they were going to have to replat the whole thing and so they never went to work on it or talk about it. Everyone hated it because it was this huge delay. I mean, all they had to do was change a process. Sometimes all you have to do is change a process. And they changed it so that instead of... I think someone had to print it out and walk it down three or four flights, and they get approval. And then someone else had to walk it back up, and so it was just that interim. They didn't replat anything. They didn't redesign anything major. They just sent an email.
Lenny Rachitsky :
Let me push on that and... I'm curious just what are the most common things people do. If you're just starting on, "Okay, we need to focus on engineering experience," what do you find are the most... two or three most common improvements companies need to make?
Nicole Forsgren :
I'll say, I'll kind of echo that process, there's almost always a process that can be improved and that can be improved without a lot of engineering lift or a lot of engineering headcount. Most large companies, in particular, have something that is several, several steps. It's the way it is because it's the way it is, but that's no longer the way it is. And even small companies sometimes is just a little too YOLO, and you don't know what it is and you're kind of chasing everyone around. So if you can create a very lightweight process, that can also be helpful. That can be one of the best places to start, especially if you have limited exposure to the whole rest of the org. Sometimes just a team process can help.
:
I will say from a business leader's standpoint, a lot of what you can do is provide structure and support for this organizational change. Communicate what you're doing, communicate what the priorities are, communicate why this is important, to celebrate wins. Because if folks try to do this, just like a one-off side fully-isolated project, it's really challenging to get some good momentum, to get people to care, and to get them stay involved. Because it feels like it's just another internal project that isn't going to matter or that isn't going to get celebrated, but it has these huge upside potential returns for the business.
Lenny Rachitsky :
It's interesting, what I'm hearing here is nothing about tools or technologies. It's not like move to this cloud, it's not like install this new deployment system, it's processes and people and org and morale.
Nicole Forsgren :
Yeah. Now, there will be technical pieces that are very important, especially now with AI, where we're rethinking how build and test systems work. We're rethinking feedback to users so that it's very, very customized in terms of what is shared and when it is shared. There are a lot of technical pieces that are involved, but that's not the only thing. It's necessary but not sufficient, and that doesn't have to be the place that you start.
Lenny Rachitsky :
I have a hard question I want to ask you that I thought of as you were talking. I feel like this is the question that most founders and heads think about. And the question is just like, how do I know if my eng team is moving fast enough, if they can move faster, if they're just not performing as well as they can? What are just maybe smells, signs that tell you, "Yeah, my team should be moving faster," versus, "This is just the way it works. This is as fast as they can move"?
Nicole Forsgren :
Most teams can move faster, right? Also, given what we know about cognitive load, not all speed gains are necessarily good. Or the upside is going to be kind of limited once you hit kind of a certain point, and most people are not even near that point. I don't know a single team, frankly. But how do you know? You know if you're always hearing about bills breaking, flaky tests, overly long processes, if you have to request a new system or if you need to provision a new environment, or if it's really, really hard to switch tasks or switch projects. So if someone has an opportunity to go work in another part of an org and they don't for reasons that are unclear, and not political, and anyone says anything about the system, that's usually a pretty good smell that there's friction somewhere.
:
Because once you finally figure out your system and you're able to get work done, the switching costs can often be really, really high to go anywhere else. So sometimes people will do that. But I've worked with companies where switching orgs within the company, you had to basically pay the same tax as a new hire because the systems were so different and they were so full of friction, and it was so difficult to do so many things.
Lenny Rachitsky :
I love the first part of your answer especially, which is you can always move faster. I think every founder is going to love hearing that. To your point though, there's diminishing returns over time?
Nicole Forsgren :
Yeah. And you don't know about the quality, right? So I think that's the other side is that you can always move faster, but faster for what? Are we making the right business decisions? And I think that's especially where PMs come in. We can ship trash faster every single day. We need strategy and really smart decisions to know what to ship, what to experiment with, what features we want to do in what order and what rollout. The strategy is the core piece, and then think about speeding that up. If we don't have the other pieces in place, I mean, garbage in, garbage out.
Lenny Rachitsky :
I want to follow that thread, but before I do that, just to mirror back what you shared. So signs that your team... There's a lot of low-hanging fruit to improve the productivity of your team as builds are always breaking. There's flaky tests are constantly incorrect, false positives. It's hard to context switch between different projects. You just hear people talking about the system, it's just really hard to work with. Is that roughly right?
Nicole Forsgren :
Yeah.
Lenny Rachitsky :
Cool, okay. So going back to the point you just made, there's a sense that AI is making teams so much faster because it's writing all this code for them. You're going to have all these asynchronous agents, engineers working for you. It feels like a core part of your message is that's just a one part of engineering work and there's so much more, including figuring out what to build... an alignment internally. Maybe just speak to just... There is a lot of opportunity to improve engineering performance productivity, but there's so many other elements that are not improved through AI?
Nicole Forsgren :
Yes. Or could be in the future, right?
Lenny Rachitsky :
Mm-hmm.
Nicole Forsgren :
I think there are a lot of ways that we can pull in AI tools to help us refine our strategy, refine our message, think about the experimentation methods or targets of experimentation, or think about our total addressable market, but we need to have that strategy and plan fairly well aligned or at least have two or three alternatives that you want to test. Because now, the engineering can go, or at least the prototyping especially, much, much faster. We can throw out prototypes. We can run any tests and experiments that are customer facing, assuming that we have the infrastructure in place, which allows us to learn and progress much faster before. In some places, it used to take months to get something through production to do A/B testing and get feedback. We can do this in a day or two, definitely under a week. But we want to make sure that we're building and testing the right things, "Are we partnering with the right... Do we have the data that we need?"
:
And I will say AI can actually be a pretty good partner there if you have a good conversation with it, and then also check with you experts, "What type of data should I be looking at? What type of instrumentation do I need? What type of analysis can I do?" Because then, you can also go to your data science team and say, "I'm planning on doing this. I'd like to..." Let's not just YOLO A/B tests because that can be... It's a shame to do a large test and end up disrupting users or disrupting customers, or breaking privacy or security protocols and also end up with data that's unusable because you just can't get the signal that you're looking for. But now, I'm also seeing people kind of accelerate that into a few days versus a few weeks. So they can start those key stakeholder discussions from a much more informed kind of filled out space.
Lenny Rachitsky :
Today's episode is brought to you by Coda. I personally use Coda every single day to manage my podcast and also to manage my community. It's where I put the questions that I plan to ask every guest that's coming on the podcast, it's where I put my community resources, it's how I manage my workflows. Here's how Coda can help you. Imagine starting a project at work and your vision is clear, you know exactly who's what and where to find the data that you need to do your part. In fact, you don't have to waste time searching for anything because everything your team needs from project trackers and OKRs, the documents and spreadsheets lives in one tab all in Coda. With Coda's collaborative all-in-one workspace, you get the flexibility of docs, the structure of spreadsheets, the power of applications, and the intelligence of AI all in one easy-to-organize tab.
:
Like I mentioned earlier, I use Coda every single day. And more than 50,000 teams trust Coda to keep them more aligned and focused. If you're a startup team looking to increase alignment and agility, Coda can help you move from planning to execution in record time. To try it for yourself, go to coda.io/lenny today and get six months free of the team plan for startups. That's C-O-D-A-dot-I-O-slash-Lenny to get started for free and get six months of the team plan, coda.io/lenny.
:
I love that you work with a bunch of different companies and a bunch of different types of businesses. I think very few people get to see inside a lot of different places. What kind of gains are you just seeing in terms of increased productivity with AI? How big of a gain have you seen?
Nicole Forsgren :
I'd say it's real, and I would also say we don't have great measures for it yet. We're still trying to figure out what to measure and what that looks like. One of the best is going to be velocity, all the way through the system, how quickly can you get a feature or a product or something through the system so that you can then experiment a test, either from idea to final end or even kind of a feature and a piece through the system so we can test. That's really good. Now, that's also hard to tie back directly to a particular AI tool in the hands of a particular developer. But there are some other things that we can look at and we can see, and that I've seen is, again, this kind of rapid prototyping.
:
I hate lines of code, but I'm going to use the lines of code. We do see... I know I worked with some folks who had kind of a whole set of companies they were looking at, and they found that AI was generating significantly more code for the people who were using it regularly. But then, they also found that for folks who were regular users of AI coding environments, AI ADEs, the tool kind of gave them more code. And then the engineers themselves, the increase was double what the coding agent had given them. So one, I'd say, probably it's kind of a secondary or knock on or just a smell is it can unblock you. It can speed up the work that you would already do. I know sometimes when I work, the first few minutes, it's hard for me to start. But once I get started, I'm there. So they're really good at unblocking and unlocking that.
Lenny Rachitsky :
Something I've seen people on Twitter sharing is how good OpenAI Codex, especially, is at finding really gnarly bugs. And I think it was Karpathy that shared it. He was so stuck on a bug and, no AI tool could figure it out. And then the latest version of Codex spent an hour or something, looking into it, and found it for him.
Nicole Forsgren :
Yeah. I'm hearing incredible things like that, right? Well, and even also writing unit tests and spinning up unit tests, and creating documentation and cleaning up documentation because I know now people are like, "Oh. Well, we have agents. I don't need to read the docs because there's the code there." It turns out, agents rely on good data because it's all about how they've been trained or how they've been grounded. And better data gives you better outcomes, and some of that data includes documentation and comments. The better documentation and the better comments you have, the better performance you're going to get out of your AI tools.
Lenny Rachitsky :
And AI can help you write that documentation. I've been working with Devin a little bit, and it's really good at that stuff.
Nicole Forsgren :
Yeah.
Lenny Rachitsky :

**Okay. Let's talk about this framework, this book. So you're publishing a book called Frictionless, which sounds like a dream, "How do you create a dev team that's frictionless?" It's called Frictionless**:

7 Steps to Remove Barriers, Unlock Value, and Outpace Your Competition in the Age of AI. There's a seven-step process to this. Walk us through this and maybe give us just context on this book, who it's meant for, what problem it solves, and then the seven steps.
Nicole Forsgren :
I will say, I also wrote this with Abi Noda who has just... of DX. He has incredible experience in the space. He's worked with hundreds of companies and so it was kind of nice bouncing ideas off of him. Also, thanks to all of the engineering leads and DevEx leads, and CTOs, and engineers that we talked to to make sure that our smells were right. So who is this book for-
Lenny Rachitsky :
Let me take a tangent on Abi, and DX, since you mentioned him. This is super interesting, and I think it connects so directly with this conversation. Abi started this company called DX, which is such a great name for a company around developer experience. They just sold the company for a billion dollars to Atlassian. It's a very high multiple on their ARR. It, to me, shows exactly why this conversation is so valuable, just how much value companies are putting into improving developer experience. Atlassian would spend a billion dollars on this. It's an early stage-ish startup. It was doing really well and people loved it, but it was like early stage-ish, a billion dollars. And the idea is they have all these companies working using Jira and all their products. They're all trying to figure out how do we measure productivity. It's worth a lot of money to them. And I know you were an early advisor to them too, so-
Nicole Forsgren :
Yeah.
Lenny Rachitsky :
... it just shows us how important this is.
Nicole Forsgren :
Yeah. Well, I think it also shows us how much value you can get out of this. There's so much low-hanging fruit, there's so much unlocked potential, and it's hard to know where to start a lot of times even in... I've been at large companies that have a lot of expertise and a lot of really, really smart people. But if you haven't kind of been in this space and thinking about it this way, it's hard to know where to start or it's easy to make simple mistakes up front that mean you kind of need to start over later. So I guess it also brings us back to, "Who is this book for?" It's for anyone that cares about DevEx, so definitely technology leaders, anyone who's trying to kick off a DevEx program, or is working on a DevEx DevEx improvement program. I think it's particularly relevant for PMs because if you're PMing something that involves software building and creating software, improving DevEx will only help your team. And also, you have key skills and insights and instincts that are so important to DevEx that many times, I will say, I've seen engineering teams just miss.
Lenny Rachitsky :
Okay. What's the framework? What are the steps? Where do people start?
Nicole Forsgren :
The book goes through a seven-step process, and then also kind of provides some key kind of principles at the end. Step one is to start the journey. So assuming you're kicking off, you can start the journey. And this involves what we have already talked about. Go talk to people, have a listening tour, synthesize what you learn, visualize the workflow and tools, get a handle on what the current state is. Step two is to get a quick win. So start small, get a quick win, pick the right projects, share out what you've done. Step three is using data to optimize the work. So establish some of your data foundation, find the data that's there, start collecting new data, use some surveys for some really fast insights and may include example surveys. Step four then is to decide strategy and priority. Once you have some data, then you need to know of all the things that are potentially broken. And if you've already gotten your quick win of all the things that are left, "What should I do next?" So we walk through some evaluation frameworks there.
:
Step five is to sell your strategy. Once you've decided, now you have to kind of convince everyone else. So now you want to get feedback, you want to share why this is the right strategy right now. Step six is to drive change at your scale. So here, we address folks that have local scope of control. If you're starting on just a dev team, you want to do it yourself, kind of grassroots effort or global scope of control. If you're the VP of developer experience or something, there are some things that you can leverage for a top down, and then how do you drive change when you're kind of somewhere in the middle, because you can leverage both types of strategies. And then step seven is to evaluate your progress and show value, and then kind of loop back around.
:
I will say that we wrote this so that you could kind of jump into any step wherever you are right now. If you're kicking off a team or an initiative, you'll probably want to start at step one. You should definitely start at step one. If you're joining an existing initiative, you could jump into picking the priority or implementing the changes. So those are the seven steps. There's a seven steps, there are a few practices that we also recommend. So thinking about resourcing it, change management, making technology sustainable, and then also bringing a PM lens to this, "How can we think about developer experience as a product, and how do we think about the metrics that we have as a product?"
Lenny Rachitsky :
Awesome, okay. I have questions. Point people to the book real quick. What's the URL? How do they get it? When does it come out?
Nicole Forsgren :
Yeah, developerexperiencebook.com. Right now, you can sign up for the mailing list. We'll let you know when it's out on pre-order, and we'll also be sharing pieces of the workbook. So we've got almost a hundred page workbook that goes along with the book, and then it should be out by end of year.
Lenny Rachitsky :
Okay. So one piece of this is just this term developer experience feels very intentional in that it's not developer productivity, developer work. It's how do we make developer experiences better at our company, which includes they get more done, but also they're happier and things like that. So I think that's an important element of this, right?
Nicole Forsgren :
Yeah, absolutely.
Lenny Rachitsky :
Okay.
Nicole Forsgren :
Because, again, it's not just about productivity. We talked about this from the frame and the lens of, "We need to be building the right thing." And you want to be productive, but you also want to be thinking about... and this is what engineers are also just really incredibly good at, give them a problem and don't tell them how to solve it, and then they can solve it better. They have the freedom, they have the innovation, they have the creativity so that they can solve this problem. If it's only about productivity, then it's just lines of code or number PRs or whatever. But we really want to talk about value and how do we unlock value, and how do we get value faster. And that involves, yes, making them more productive and removing friction because then, they have the flow and the cognitive load and the things that we kind of talked about.
Lenny Rachitsky :
Awesome, okay. And then say someone wants to start this team, what does it usually look like. At Airbnb, I remember this team forming. It was just like an engineer or two, getting it started and taking charge. What do you recommend as the pilot team, and then what does it look like as it grows?
Nicole Forsgren :
There are a few ways to do this, right? So if you're doing it yourself, you could do it with a couple of engineers, maybe a PM or a PGM or a TPM to kind of help communicate. Because really, comms plans are just so important here. On a small scale, what we want to do is look for those quick wins, look for things that you can do at small scale. Some folks call them things like paper cuts. There small things that you can do to help people see the value and feel the benefit themselves, "How can a developer's work get better? How can their day-to-day work get better? Kind of build momentum from there?" If you're working from a top-down structure and you have the remit, you still want some quick wins, but those quick wins can look a little more global in scale because you have the infrastructure or the backing to make different types of changes that aren't only local.
:
So an example of a small local change could be just cleaning up your tests, your test suites. Any team could do that, any team could do that. At more global scale, it might be changing organization-wide process that is just overly cumbersome or throwing some resourcing into cleaning up the provisioning environment.
Lenny Rachitsky :
Okay. What kind of impact have you seen from teams like this forming, on the engineering teams at their companies?
Nicole Forsgren :
I'll say I've seen a huge impact for smaller companies, hundreds of thousands of dollars for large companies or in the billions. Well, also, we need to learn how to communicate that, "What does the math look like?" Many times, we can look at saving time, we can look at saving costs, we can look at a lot of different things. We can look at speed to value as speed to market. We can look at risk reduction, but the gains really are there. I will mention that it tends to follow something like the J-curve. So you'll have a couple of quick wins and it'll look like a big win, and then you'll hit kind of a little divot where suddenly the really obvious projects, the low-hanging fruit are handled. So now, we need to do a little bit of work. We might need to build out a little bit more infrastructure. We might need to build out a little more telemetry, so that we can capture the things we want to capture. And then once we get that done, then we start to see those benefits really compound.
Lenny Rachitsky :
So going back to that measurement number, what do you recommend? How do people find these numbers? Because I think that's so much of the power of this is like, "We saved a million dollars doing this." What do you look at to figure that out?
Nicole Forsgren :
I think there are a few different things to keep in mind, like who is our key audience, and we usually have a few key audiences. We really want to be able to speak to developers because they're the ones that are going to be using the systems. They'll be partnering with you on either building them or at least providing feedback about what you're doing. So for them, we often want to frame this in terms of things they care about. So time savings. If something gets faster, they can save time. They don't spend time doing setup when they don't need to anymore, related to status reduced toil. So compliance and security are super important. Also, many times it requires several manual steps that... I don't say they're not value add. They're not value add from an individual human perspective. If we can automate as much as possible, that's great, and improved focus time.
:
That's from the developer side of you. Leadership often cares about... They care about those things, but they often care more about other things. So we could talk about usually costs in dollars, "Can we accelerate revenue? What does our time to value look like? What is our velocity? How quickly can we get feedback from customers?" And for folks and organizations that are in really competitive environments, that can be really compelling because it's all about speed. We could talk about saving money. Here, we can look at maybe quantifying savings. One example is test and build. If we can clean up a test and build suite to a developer, they really want to hear about time saved and more reliable systems. There's less toil because they don't have to keep re-running tests or kind of go clean up test suites.
:
From the business perspective, cleaning up a test in a build suite can be cloud cost savings because all of those tests are running somewhere on a cloud. And if they always fail or if it's just kind of a waste of spend, that can be useful, recovering some capacity. We can always talk about time and productivity gains, "How much equivalent developer time are we losing on things that are not necessarily value add?" And then sometimes we can correlate to business outcomes and correlate is usually the best we can do here, but there can be some pretty compelling correlations in terms of speeding up time to value and increase market share, for example.
Lenny Rachitsky :
Let me follow that thread and come back to this, what I think is the biggest question people have right now with AI and productivity, and I don't think anyone has the answer yet, but I'm curious to get your take of just what should people do today? What's the best approach to understanding what impact AI tools are having on their productivity? Because they're spending all this money on there. I don't know, what are we getting out of this? So I guess things are moving faster, but I don't know. So if someone had to just like, "Okay, here's what I should probably try to do," what would be your best advice here for measuring the impact of AI tools on productivity?
Nicole Forsgren :
I would say it depends. In part, it depends on what your leadership chain really cares about. We are usually pretty good at figuring out what matters to developers and we could communicate that to them. But if we're trying to just identify two or three data points to really kind of focus on, because when we're first starting with data, sometimes it can be challenging, what do they care about? Think about the messaging you've been hearing. Have they been talking about market share? Losing market share or competitiveness in the marketplace, if that's it, focus on speed. Think about ways that you can capture metrics for speed from feature to production or feature to customer or feature to experiment and what that feedback loop looks like if they're talking about profit margin all the time.
:
Now, we always talk about money because this is business. But if that seems to be an overarching narrative, look for ways that you can save money and then translate that into recovered and recouped headcount cost. Or sometimes you'll reinvent, change a process, and then you no longer need as many vendors. So reductions in vendor spent can also help there. I say also it depends because sometimes they'll say something, leadership will say something, and it kind of comes up as a theme. If you could solve a problem that they have or it's something that they're focused on, if you can slightly reframe it even, like if they're calling everything developer productivity, go ahead and call it productivity. If they're calling it velocity, and velocity is what matters to them, think about how to frame this in terms of velocity. If they're talking about transformation or disruption, how does this help with the disruption? Because then, it will resonate with them. We don't want to make them work to understand what it is that we're doing and the value that we provide.
Lenny Rachitsky :
That is such good advice. Just to reflect back, the advice here is if your company's trying to figure out what sort of impact are AI tools having on our company, first, it's just like, what does the company care about most? What do leaders care about most? Could be market share, could be profit margin, could be velocity. We need higher velocity or we need to transform, transformation. So your advice there is figure that out based on words and phrases you're hearing. Then figure out ways to measure that, ways to measure market share growing, profit margin increasing. I love these examples, like time from feature, idea to production or to experiment, so maybe start tracking that. If it's margin, it's money saved by fewer tests, failing or some vendor you don't have to pay for, things like that. And then velocity, I imagine that's where things like DORA come in of just speed of engineering, shipping, or... What would you think about there for velocity?
Nicole Forsgren :
I would say it's actually one of those... I would pick as broad a swathe as you can. So if you can go from idea to customer or idea to experiment, how long does that take? How long does it typically take, and how long can it take, and does it take now with improved use of AI tooling and reduction in friction? That's where I will say, we talk about this a little bit in the book, how do we deal with attribution challenges? What was responsible for this? Was it the DevEx or was it AI? Go ahead and disclose that. Say, "Yes, we rolled out AI tools. We also had this effort in DevEx. They partnered very closely together." Both of them probably contributed to this, right? If we had AI tools without the DevEx improvements, we probably would've had some improvements, but not nearly as much.
Lenny Rachitsky :
If people were starting to do this today, say they're just like, "I want to start measuring developer experience," are there a two or three metrics everybody basically needs they should just start measuring ASAP?
Nicole Forsgren :
If you're just starting today and if you have nothing at all, talk to people, obviously. After that, I would do surveys because surveys can give you a nice overall view of the landscape quickly so that you know where the big kind of challenges are. I say that because if you're just starting, you might not have instrumentation through your system, all the metrics. And if you do already, it might not be what you think you want. Metrics that were designed without purpose, questionable. Metrics that were designed for another purpose, they might work for what you want, but they might not, so we can't just assume we have them. That's one reason I like surveys, and we include an example in the book. You can just ask a few questions, "How satisfied are you? What are the biggest barriers to your productivity, or what are the biggest challenges to getting work done?" and let them pick either from a set of tools or maybe a set of processes and then say... Let them pick three, just three.
:
Of those three, how often does this affect you? Is this hourly? Is this daily? Is this weekly? Is this quarterly? Because sometimes it hits you every single day, and you're just mad about it. Sometimes it only hits you once a quarter because it's end of quarter, but it's so onerous, and then kind of open text, like, "Is there anything else we should know?" That can give you incredible signal because by making folks prioritize the top three things... Let them pick everything, it makes the data super, super messy. But three things and how often, you can just come up with a score or a weighted score if you want, and then go kind of dig into, where should that data be? What data do we need? But also, then you've got at least some kind of baseline. It'll be a subjective baseline, but now you'll know what the biggest challenges are.
Lenny Rachitsky :
I love how all this just comes back just starting by talking to people and asking them these things, which is very similar to product management and just building great products is, have you talked to your customers? Everyone thinks they're doing this, but most people are not doing this enough.
Nicole Forsgren :
And I will say one thing that's challenging when you think about getting data, so interviews are data and that's important, surveys are a little more quantified because we can turn it into counts, but that's where we also want to be careful. A lot of folks go to write a survey question and they'll say something like, "Were the build and test system slow or complicated in the last week?" You're asking four different questions there. If someone answers yes, was it the build? Was it the test? Was it slow or was it flaky or complicated or something? So it can be really difficult to untangle what the signal is you're actually getting there, and so it is worth the time chatting with someone who's familiar with survey design, having a conversation with Claude or Gemini or ChatGPT around, "Here are the survey questions. Or can you propose some?" And then make sure you take a couple of rounds. Is this a good survey question? What questions can I answer from the data that I get? What problems could I solve? If you can't answer a question with data, don't get it.
Lenny Rachitsky :
And you have example surveys in your book for folks that want to just copy and paste and not have to think about this much.
Nicole Forsgren :
Yeah, example surveys, a lot of example questions. We even recommend what the format, what the flow should look like, how long it should be, how long it should not be.
Lenny Rachitsky :
One thing that I was reading is that you don't love happiness surveys specifically, asking engineers how happy they are, is that true? If so, why is that?
Nicole Forsgren :
I don't, no. Well, I'll say I don't love a happiness survey because there are too many things that contribute to happiness. Happiness is a lot, right? So happiness is work, happiness is family, happiness is hobbies, happiness is weekends, happiness... There are so many things that contribute to happiness. Now, that doesn't mean I don't care about happiness. I think happiness surveys are not particularly useful here. What can be helpful is satisfaction and people are like, "That's the same thing." It's not because you can ask, "Are you satisfied with this tool?" and then ask some follow-up questions. Now, those two are related because the more satisfied you are with your job and your tools and the work and your team, it contributes to happiness. I used to joke... Remember the golf commercials like, "Happy cows like happy cheese"?
Lenny Rachitsky :
No.
Nicole Forsgren :
I had a Calabrian. That was the best. Happy devs make happy code. They write better programs, they do better work, they're better team members and collaborators. But capturing and trying to directly influence happiness, that's not what we are here for. It's too challenging, it's too all-encompassing. Satisfaction can give us some signal.
Lenny Rachitsky :
In a totally different direction, in terms of just tools you see people using, are there any that just like, "Oh, yeah, this one's really commonly great." For people, this is just a tool people are finding a lot of success with. There's the common ones, Copilot, Cursor. I don't know. Is there anything that stands out that you want to share, just like, "Hey, you should check this tool out. People seem to love it"?
Nicole Forsgren :
I think they're huge, right? Copilot, Cursor, Gemini.
Lenny Rachitsky :
Claude Code.
Nicole Forsgren :
Yep, Claude Code. I love Claude Code.
Lenny Rachitsky :
I have a whole post coming on ways to use Claude Code for non-engineering use cases.
Nicole Forsgren :
Cool. Nice.
Lenny Rachitsky :
It's so interesting. For example, Claude Code, "Find ways to clean up storage on my laptop," and it just tells you there's a bunch of files. It's just like ChatGPT running on your computer and you could do all kinds of crazy stuff on your computer for you, like a mini God.
Nicole Forsgren :
I'm going to do that now. This is great.
Lenny Rachitsky :
It's so good. Yeah, that's why I'm writing this. I had Dan Shipper was on the podcast and he said Claude Code is the most underrated AI tool out there because people don't realize what it's capable of. It's not just for coding, and that's what I'm trying to explore more and more. Okay. Is there anything else that you think would be valuable to help people improve their developer experience, help them adapt to this new world of AI and engineering that we haven't covered?
Nicole Forsgren :
I think something that's important to think about in general is to bring a product mindset to any type of DevEx improvements that are happening, and also the metrics that we collect and capture. By that, I mean we want to identify a problem, make sure we're solving a problem for a set of users. We want to think about creating MVPs and experiments and get fast feedback, do some rapid iteration. We want to have a strategy. We want to know who our addressable market is. We want to know what success is. We want to basically have a go-to-market function. We need to have comms. We need to get continuous feedback from our customers. We want to keep improving. And, at some point, we want to think about sunsetting something. Is it in maintenance mode? Is it sun setting?
:
And I think that's important in general, but I think it's extra important now because when we have AI tools, we're using AI tools, we're embedding AI into our products, things are changing so rapidly that it can be really important to take half a beat and say, "Okay, what's the problem I'm trying to solve right here? Is this metric that we've had for the last 10 years still important or should this be sunset because it's not really important anymore? It's not driving the types of decisions and actions that I need."
Lenny Rachitsky :
Before we get to our exciting lightning round, I want to take us to AI Corner, which is a recurring segment on this podcast. Is there some way that you've found a use for an AI tool in your life, in your work that you think might be fun to share, that you think might be useful to other people?
Nicole Forsgren :
I have been working on some home design and redecorating rooms and stuff. I'm working with a designer because I know what I like, but I don't know how to get there, I'm not good at this. But I've really been loving ChatGPT and Gemini especially to render pictures for me, so I can give it the floor plan, I can give it one shot of the room that's definitely not what it's supposed to look like, and then I can give it pictures of a couple different things, and then I can just tell it change the walls or change the furniture layout or change something. It helps me and it's relatively quick. It helps me kind of visualize the things... Again, I know what I like, but I don't know how to get there, so I know if I like it or not, which is probably a very random use, but it's fun for now.
Lenny Rachitsky :
My wife does exactly the same thing. She's sending me constantly, "Here's what this rug will look like in our living room. Here's this water feature." It's so good and it keeps getting better. It's just like, "Wow, that's exactly our house with this new rug," and all you do is just upload these two photos and just like, "Cool. How would this look in our room?"
Nicole Forsgren :
Yeah, I've been impressed a couple times. Definitely the machines are listening to us. It's given me a mock-up of a room or something and then it throws in a dog bed, because I have dogs. I'm like, "I did not tell you to do that, but yeah, that's probably the color and style of dog bed that I should have in this room."
Lenny Rachitsky :
Speaking of that, have you tried this use case, ask ChatGPT, "Generate an image of what you think my house looks like based on everything you know about me."
Nicole Forsgren :
I haven't.
Lenny Rachitsky :
Because it has memory and it remembers everything you've talked about, and it's hilarious. You got to do it.
Nicole Forsgren :
Okay, that's on my to-do list.
Lenny Rachitsky :
There we go. Bonus use case. Nicole, with that, we've reached our very exciting lightning round. I've got five questions for you. Are you ready?
Nicole Forsgren :
Awesome. Let's go.
Lenny Rachitsky :
What are two or three books that you find yourself recommending most to other people?
Nicole Forsgren :
Outlive by Peter Attia is fantastic. Another one that's I guess maybe related, I hurt my back so it's not great, Back Mechanic by Stuart McGill is incredible. Shout out to anyone who has hurt lower back. It's for a lay person to read through and figure out how to fix lower back problems. It's kind of a random one. I will say I love How Big Things Get Done. I can't pronounce the names. I think one's... There's Scandinavian, one is. It kind of dissects really large projects through recent-ish history and where they failed and why. And I think it's really interesting for us to think about, especially now in this AI moment where basically all of our at least software systems are going to be changing. So how do we think about approaching what is essentially going to be a very large project? And then, sorry, I'm going to throw in a bonus one, The Undoing Project by Michael Lewis. Matt Velloso recommended it to me, and it's so good.
Lenny Rachitsky :
Yes, I read that-
Nicole Forsgren :
I audibly gasped at the last sentence.
Lenny Rachitsky :
Oh. I was like, "What?"
Nicole Forsgren :

**I was [inaudible 01**:

03:48]. Yeah, I was not expecting it.
Lenny Rachitsky :
I read that and I do not remember that last sentence. Oh, man. Okay, cool. Next question. Do you have a favorite movie or TV show you recently watched and enjoyed?
Nicole Forsgren :
I'll say I watch Love Is Blind. If I got to shut down at the end of the day, Love Is Blind is fun.
Lenny Rachitsky :
There's a new season out.
Nicole Forsgren :
Yeah, very excited... and Shrinking. Have you seen Shrinking?
Lenny Rachitsky :
No. I think I started The Therapist and yeah, I gave it a shot.
Nicole Forsgren :
Strongly recommend it. It's cute.
Lenny Rachitsky :
Sweet. Is there a product you've recently discovered that you really love? Could be an app, could be some kitchen gadgets, some clothing.
Nicole Forsgren :
Yeah, the Ninja Creami is-
Lenny Rachitsky :
Did you say this last time?
Nicole Forsgren :
I don't know. I may have. I don't think so.
Lenny Rachitsky :
Somebody said this and I still remember it. It's like-
Nicole Forsgren :
It's so good.
Lenny Rachitsky :
... you make ice cream and stuff with it, right?
Nicole Forsgren :
Yeah, and you can basically freeze a protein shake and then it turns it into ice cream-
Lenny Rachitsky :
Oh, man.
Nicole Forsgren :
... which is delicious. Another one is a Jura coffee maker. I'd love good coffee and I'm not great at making it, so I can just push the button and it'll give me anything I want, including lattes, cappuccinos or anything. So that's kind of fun.
Lenny Rachitsky :
Sweet, okay. Do you have a favorite-
Nicole Forsgren :
Just sugar and caffeine. I just need a power through the day.
Lenny Rachitsky :
There's the engineering productivity 101.
Nicole Forsgren :
Yes.
Lenny Rachitsky :
Oh, man. Okay, two more questions. Do you have a favorite life motto that you often find useful in work or life and come back to in various ways?
Nicole Forsgren :
Yeah, I think one that's come up a couple times, it's not a verbatim thing, I think it's more the vibe, hindsight is 2020, but it's also really dumb. I think if we made the best decision we could at the time with the information that we had available, then it is what it is. If you make a bad decision because you made a bad decision and you knew better, you had the information, not great. I don't think we give ourselves or other people enough grace because we always end up finding more information out later.
Lenny Rachitsky :
Hear, hear. Final question. I was going to ask you something else, but as we are preparing for this, you shared that you have a new role at Google. Maybe just talk about that, what you're up to there, why you joined Google, anything folks should know.
Nicole Forsgren :
Sure. I am senior director of developer intelligence and core developer. It's super exciting and super fun because of all of these things we've been talking about. It's focused on Google and all their properties and their underlying infrastructure, how can we improve developer experience, developer productivity, velocity, all of these things we've been talking about and, because kind of the numbers person, how do we want to think about measuring it, how does measurement change, how do feedback loops change, how can we improve the experience throughout and then kind of drive that change through an organization in ways that are meaningful and impactful and faster than they've been before.
Lenny Rachitsky :
Nice job, Google, getting Nicole. What a win. I need to get some more Google stock ASAP. Okay, two follow-up questions. Where can folks find you online and find your book online if they want to dig deeper? And how can listeners be useful to you?
Nicole Forsgren :
Online, you can find the book at developerexperiencebook.com, I'm at nicolefv.com, and LinkedIn occasionally. Sometimes it's a mess. I try to wade through all of the noise. I get there to be useful, sign up for the book and the workbooks. The workbooks are free. I'd love to get any kind of feedback on what works, what doesn't. I always love hearing those kind of stories.
Lenny Rachitsky :
Nicole, thank you so much for being here.
Nicole Forsgren :
Thanks for having me, Lenny.
Lenny Rachitsky :
My pleasure. Thanks, again. Bye, everyone.
:
Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennyspodcast.com. See you in the next episode.
