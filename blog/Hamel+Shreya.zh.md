# Hamel+Shreya - Lenny's Podcast Insights
## Hamel+Shreya - Lenny's播客洞见

---

## ## 关于嘉宾 | About the Guest

**Hamel+Shreya** 与Lenny进行了关于产品管理、领导力和打造成功产品的深入对话。

**Hamel+Shreya** 与Lenny进行了深入对话，讨论产品管理、领导力和打造成功产品的经验。

---

## ## 核心要点 | Key Takeaways

---

## ## 完整对话 | Full Conversation

*以下是完整对话记录。*

*以下是完整对话记录。*

**... be really fun. Two, I love that my podcast episode just came out today is in your feed there, and it's standing out really well in that feed, so I'm really happy about that [inaudible 00**:

39:13].
Hamel Husain :
Very nice. Yeah. The recommendation algorithm is quite good.
Lenny Rachitsky :
Yes. Here we go. Hope you click on that. Don't screw my algorithm. Okay, cool. So we've done some synthesis. I know we're not going to go through the entire step. This is you have a whole course that takes many days to learn this whole process. What else do you want to share about how to go about this process?
Hamel Husain :
Okay. So you can do this through anything, and the same thing works just fine in ChatGPT, the same exact prompt. You can see it made axial codes. I really like using Julius AI. It's one of my favorite tools.
:
Julius is kind of this third-party tool that uses notebooks. I personally like Jupiter notebooks a lot, and so it's more of a data science thing, but a lot of product managers that are kind of learning notebooks nowadays, and it's kind of cool. It's like a fun playground where you can write code and look at data. But we don't have to go deeply into that. Just wanted to mention, you can use a lot. AI is really good at this.
:
So let's go to the fun part. Here we go. So now we have these axial codes. So the first thing I like to do, I have these open codes, and I have the axial codes, let's say, that we assigned from the cloud project or the ChatGPT. And so what I do is I collect them first and I take a look, like, "Does these axial codes make sense?" And I look at the correspondence between the different axial codes and the open codes, and I go through an exercise and I say, "Hmm. Do I like these codes? Can I make them better? Can I refine them? Can I make them more specific?" Instead of being generic, I make them very specific and actionable.
:
So you see the ones that I came up with here are tour scheduling, rescheduling issues, human handoff or transfer issue, formatting error with an output, conversational flow. We saw the conversational flow issue with the text messages. Making follow-up promises not kept.
:
And so basically, what I can do, what you can do now is you have these axial codes, and so I just collect them into a list, so this is an Excel formula. Just collect these codes into a list, and now we have a comma-separated list of these codes. And then what you can simply do is you could take your notes that you have, those open codes, and you can tell an AI, and this is using Gemini and AI just for simplicity, this is, again, we're trying to keep it simple, categorize the following note into one of the following categories as always.
Lenny Rachitsky :
For folks watching, I like all these different prompts and formulas you're sharing. This is the Google Sheets AI prompt.
Shreya Shankar :
Huge fan.
Hamel Husain :
And so basically, what you could do is you can categorize your traces into one of the buckets, and that's what we have here. We have categorized all those problems that we encountered into one of these things.
Shreya Shankar :
And this is automatic, which is very exciting. I mean, the AI is doing it. So this also drives home the point that your open codes have to be detailed, right? You can't just say janky because if the AI is reading janky, it's not going to be able to categorize it. Even a human wouldn't, right? It would have to go and remember why you said janky, so it's important to be somewhat detailed in your open code.
Lenny Rachitsky :
Okay. So avoid the word janky. It's a good rule of thumb.
Shreya Shankar :
Yeah. Or have it with 10 other words.
Lenny Rachitsky :
Oh, okay. What is-
Hamel Husain :
Yeah. I was being funny.
Lenny Rachitsky :
Yeah, okay. What are some of those other words that people often use that you think are not good?
Shreya Shankar :
I don't think it's specific words. I think it's just people are not detailed enough in the open code, so it's hard to do the categorization.
Lenny Rachitsky :
Great. And by the way, the reason you have to map them back is because, say, Claude or ChatGPT gave you suggestions and you change them and iterated on them, so you can't just go back and say, "Cool, whatever," in each bucket?
Hamel Husain :
Yeah, yeah.
Lenny Rachitsky :
Great.
Hamel Husain :
That's a really good question, actually. It's good to iterate and think about it a little bit like, "Do I like these open codes? Do these actually make sense to me?" Just like anything that AI does, it's really good to kind of put yourself in the middle just a little bit.
Lenny Rachitsky :
It's in the loop. Still space for us. Great.
Shreya Shankar :
One of the things that I like to do with this step if I'm trying to use AI to do this labeling, is also have a new category called none of the above. So an AI can actually say, "None of the above," in the axial code, and that informs me, "Okay, my axial codes are not complete. Let's go look at those open codes, let's figure out what some new categories are or figure out how to reword my other axial codes."
Lenny Rachitsky :
Awesome. And what's cool about this is you don't need to do this many, many times.
Shreya Shankar :
No.
Lenny Rachitsky :
For most products, you do this process once, and then you build on it, I imagine, and you just tweak it over time?
Shreya Shankar :
Absolutely. And it gets so fast. People do this once a week, and you can do all of this in 30 minutes, and suddenly your product is so much better than if you were never aware of any of these problems.
Lenny Rachitsky :
Yeah. It's absurd to feel like you wouldn't know this is happening. Watching this happening, I'm like, "How could you not do this to your product?"
Shreya Shankar :
A lot of people have no idea.
Lenny Rachitsky :
Most people. Yeah. We'll talk about that. There's a whole debate around this stuff that we want to talk about. Okay, cool. So you have the sheet. What comes next?
Hamel Husain :
Okay. So here's sort of the big unveil. This is the magic moment right now. So we have all these codes that we applied, the ones that we like on our traces. Now, you can do the ta-da, you can count them.
:
So here's a pivot table, and we just can do pivot table on those, and we can count how many times those different things occurred. So what do we find? Find on these traces that we categorized? We found 17 conversational flow issues. And I really like pivot tables because you can do cool things. You can double-click on these. You can say, "Oh, okay. Let me take a look at those," but that's going into an aside about pivot tables, how cool they are.
:
But now, we have just a nice, rough cut of what are our problems? And now, we have gone from chaos to some kind of thinking around, "Oh, you know what? These are my biggest problems. I need to fix conversational issues, maybe these human handoff issues." It's not necessarily the count is the most important thing. It might be something that's just really bad and you want to fix that, but okay. Now, you have some way of looking at your problem, and now you can think about whether you need evals for some of these.
:
So there might be some of these things that might be just dumb engineering errors that you don't need to write an eval for because it's very obvious on how to fix them. Maybe the formatting error with output, maybe you just forgot to tell the LLM how you want it to be formatted, and you didn't even say that in the prompt. So just go ahead and fix the prompt maybe, and we can decide, "Okay, do you want to write an eval for that?" You might still want to write an eval for that because you might be able to test that with just code. You could just test the string, does it have the right formatting potentially? Without running an LLM.
:
So there's a cost-benefit trade-off to evals. You don't want to get carried away with it, but you want to usually ground yourself in your actual errors. You don't want to skip this step. And so the reason I'm kind of spending so much time on this is this is where people get lost. They go straight into evals like, "Let me just write some tests," and that is where things go off the rails.
:
Okay. So let's say we want to tackle one of these things. So for example, let's say we want to tackle this human handoff issue, and we're like, "Hmm, I'm not really sure how to fix this. That's a kind of subjective sort of judgment call on should we be handing off to a human? And I don't know immediately how to fix it. It's not super obvious per se. Yeah. I can change my prompt, but I'm not sure. I'm not 100% sure."
:
Well, that might be sort of an interesting thing for an LLM as a judge, for example. So there's different kinds of evals. One is code-based, which you should try to do if you can because they're cheaper. LLM as a judge is something, it's like a meta eval. You have to eval that eval to make sure the LLM that's judging is doing the right thing, which we'll talk about in a second.
:
So, okay. LLM as a judge, that's one thing. Okay. How do you build an LLM as a judge?
Lenny Rachitsky :
Before we get into that actually, just to make sure people know exactly what you're describing there, these two types of evals. One is you said it's code-based and one is LLM as judge. Maybe Shreya, just help us understand what code-based eval even is? It's essentially a unit test? Is that a simple way to think about it?
Shreya Shankar :
Yeah. Maybe eval is not the right term here, but think automated evaluator. So when we find these failure modes, one of the things we want is, "Okay. Can we now go check the prevalence of that failure mode in an automated way without me manually labeling and doing all the coding and the grouping, and I want to run it on thousands and thousands of traces, I want to run it every week." That is, okay. You should probably build an automated evaluator to check for that failure mode.
:
Now, when we're saying code-based versus LLM-based, we're saying, "Okay. So maybe I could write a Python function or a piece of code to check whether that failure mode is present in a trace or not." And that's possible to do for certain things like checking the output is JSON, or checking that it's markdown, or checking that it's short. These are all things you can capture in code or you could approximately capture in code.
:
When we're talking about LLM judge here, we're saying that this is a complex failure mode and we don't know how to evaluate in an automated way. So maybe we will try to use an LLM to evaluate this very, very narrow, specific failure mode of handoffs.
Lenny Rachitsky :
So just to try to mirror back what you're describing, you want to test what your, say, agent or AI product is doing. You ask it a question, it gets back with something.
:
One way to test if it's giving you the right answer is if it's consistently doing the same thing, that you could write a code to tell you this is true or false. For example, will it ever say there's a virtual tour? So you could ask it.
Shreya Shankar :
Yes.
Lenny Rachitsky :
"Do you provide virtual tours?" It says yes or no, and then you could write code to tell you if it's correct based on that specific answer.
:
But if you're asking about something more complicated and it's not binary, in one world, you need a human to tell you this is correct. The solution to avoid humans having to review all this every time automatically is LLMs replacing human judgment, and you'd call it an LLM as judge. The LLM as being the judge if this is correct or not.
Shreya Shankar :
Absolutely. You nailed it.
Lenny Rachitsky :
Great.
Shreya Shankar :
So people always think, "Oh, this is at least as hard as my problem of creating the original agent." And it's not, because you're asking the judge to do one thing, evaluate one failure mode, so the scope of the problem is very small and the output of this LLM judge is pass or fail. So it is a very, very tightly scoped thing that LLM judges are very capable of doing very reliably.
Lenny Rachitsky :
And the goal here is just to have a suite of tests that run before you ship to production that tell you things are going the way you want them to? The way your agent is interacting is correct?
Shreya Shankar :
The beautiful thing about LLM judges, you can use them in unit tests or CI, sure, but you could also use it online for monitoring, right? I can sample 1000 traces every day, run my LLM judge, real production traces, and see what the failure rate is there. This is not a unit test, but still now we get an extremely specific measure of application quality.
Lenny Rachitsky :
Cool. That's a really great point because a lot of people just see evals for being this not-real-life thing. It's a thing that you test before it's actually in the real world. And what's actually happening in the real world, you're saying you should actually do exactly that?
Shreya Shankar :
Yeah.
Lenny Rachitsky :
Test your real thing running in production? And it's a daily, hourly sort of thing you could be running?
Shreya Shankar :
Totally.
Lenny Rachitsky :
Awesome. Okay. Hamel's got an example of an actual LLM as a judge eval here, so let's take a look.
Hamel Husain :
I love how Shreya really teed it up for me, so thank you so much. So what we have is a LLM as a judge prompt for this one specific failure. Like Shreya said, you would want to do one specific failure and you want to make it binary because we want to simplify things. We don't want, "Hey, score this on a rating of one to five. How good is it?" That's just in most cases, that's a weasel way of not making a decision. Like, "No, you need to make a decision. Is this good enough or not? Yes or no?"
:
It can be painful to think about what that is, but you should absolutely do it. Otherwise, this thing becomes very untractable, and then when you report these metrics, no one knows what 3.2 versus 3.7 means, so.
Shreya Shankar :
Yeah. We see this all the time also, and even with expert-curated content on the internet where it's like, "Oh, here's your LLM judge evaluator prompt. Here's a one-to-seven scale."
:
And I always text Hamel like, "Oh, no. Now, we have to fight the misinformation again because we know somebody is going to try it out and then come back to us and say, 'Oh, I have 4.2 average,'" and we're going to be like, "Okay."
Lenny Rachitsky :
It's wild how much drama there is in the evals space. We're going to get to that. Oh, man.
:
This episode is brought to you by Mercury. I've been banking with Mercury for years, and honestly, I can't imagine banking any other way at this point. I switched from Chase, and holy moly, what a difference. Sending wires, tracking spend, giving people on my team access to move money around, so freaking easy. Where most traditional banking websites and apps are clunky and hard to use, Mercury is meticulously designed to be an intuitive and simple experience.
Lenny Rachitsky :
Meticulously designed to be an intuitive and simple experience, and Mercury brings all the ways that you use money into a single product, including credit cards, invoicing, bill pay, reimbursements for your teammates and capital. Whether you're a funded tech startup looking for ways to pay contractors and earn yield on your idle cash, or an agency that needs to invoice customers and keep them current, or an e-commerce brand that needs to stay on top of cash flow and access capital, Mercury can be tailored to help your business perform at its highest level. See what over 200,000 entrepreneurs love about Mercury. Visit mercury.com to apply online in 10 minutes. Mercury is a fintech, not a bank. Banking services provided through Mercury's FDIC insured partner banks. For more details, check out the show notes.
Hamel Husain :
Okay, so this is your judge prompt. There's no one way to do it. It's okay to use an LLM to help you create it, but again, put yourself in the loop. Don't just blindly accept what the LLM does, and in all of these cases, that's what we did. With the axial codes, we iterated on this. You can use an LLM to help you create this prompt, but make sure you read it, make sure you edit it, whatever. This is not necessarily the perfect prompt. This is just the stupid, keeping it very simple just to show you the idea. It's like, "Okay, for this handoff failure," I said, "Okay, I want you to output true or false," it's a binary judge. That's what we recommend. Then I just go through and say, "Okay, when should you be doing a handoff?" And I just list them out.
:
Okay, explicit human requests ignored or looped, some policy-mandated transfer, sensitive resident issues, tool data, unavailability, same day walk-in or tour requests. You need to talk to a human for that, so on and so forth. The idea is, now that I know that this is a failure from my data, I'm interested in iterating on it, because I know this is actually happening all the time. Like Shreya said, it would be nice to have a way not only to evaluate this on the data I have, but also on production data, just to get a sense of, what scales is this happening? Let me find more traces, let me have a way to iterate on this. We can take this prompt and I'm going to use the spreadsheet again. The first step is, okay, when I'm doing this judge... I wrote the prompt.
:
Now, a lot of people stop there and they say, "Okay, I have my judge prompt. We're done. Good, let's just ship it," and the prompt says... If the judge says it's wrong, it's wrong. They just accept it as the gospel, be like, "Okay, the LLM says it's wrong, it must be wrong. Don't do that, because that's the fastest way that you can have evals that don't match what's going on, and when people lose trust in your evals, they lose trust in you. It's really important that you don't do that, so before you release your LLM as a judge, you want to make sure it's aligned to the human. How do you do that? You have those axial codes and you want to measure your judge against the axial code, and say like, "Hey, does it agree with me? My own judge, does it agree with me?" Just measure it.
:
What we have here is, okay, I say, "Assess this LLM trace." Again, I'm using just spreadsheets here, "Assess this LM trace according to these rules," and the rules are just the prompt that I just showed you. I ask it, "Okay, is there a handoff error, true or false?" Then this column, let me just zoom in a bit. Column H, I have, "Okay, did this error occur?" Column G is whether I thought the error occurred or not. You can see-
Lenny Rachitsky :
You're going through manually, you do that.
Hamel Husain :
Yeah, yeah, which we already did. We already went through it manually. It's not like we have to do it again, because we have that cheat code from the axial coding, we already did it. You might have to go through it again if you need more data, and there's a lot of details to this on how to do this correctly. You want to split your data and do all these things, so that you're not cheating, but I just want to show you the concept. Basically, what you can do is measure the agreement. Now, one thing you should know, as a product manager, is a lot of people go straight to this agreement. They say, "Okay, my judge agrees with the human some percentage of the time."
:
Now that sounds appealing, but it's a very dangerous metric to use, because a lot of times, errors, they only happen on the long tail and they don't happen as frequently, so if you only have the error 10% of the time, then you can easily have 90% agreement by just having a judge say it passes all the time. Does that make sense? 90% agreement look good on paper, but it might be misleading.
Lenny Rachitsky :
It's rare, it's a rare error. Yeah.
Hamel Husain :
As a product manager or someone, even if you're not doing this calculation yourself, if someone ever reports to you agreement, you should immediately ask, "Okay, tell me more." You need to look into it. They give you more intuition, here is like a matrix of this specific judge in the Google sheet, and this is, again, a pivot table, just keeping it dumb and simple. "Okay, on the rows I have, what did the human think? What did I think? Did it have an error, true or false? Then did my judge have an error, true or false?"
Shreya Shankar :
The intuition here is exactly what Hamel said, where you need to look at each type of error. When the human said false, but the judge said true, or vice versa, so those non-green diagonals here, and if they're too large, then go iterate on your prompt, make it more clear to the LLM judge, so that you can reduce that misalignment. You want to get to a point where most... You're going to have some misalignment, that's okay. We talk about in our course, also how to code correct that misalignment, but in this stage, if you're a product manager and the person who's building the LLM judge eval has not done this, they're saying like, "It agrees 75% of the time, we're good." They don't have this matrix and they haven't iterated to make sure that these two types of errors have gone down to zero, then it's a bad smell. Go and ask them to go fix that.
Lenny Rachitsky :
Awesome. That's a really good tip, what to look for when someone's doing this wrong.
Shreya Shankar :
Yeah.
Lenny Rachitsky :
Actually, can you take us back to the LLM as judge prompt? I just want to highlight something really interesting here. I've had some guests on the podcast recently who've been saying, "Evals are the new PRDs," and if you look at this, this is exactly what this is. Product managers, product teams, here's what the product should be, here's all the requirements, here's the how it should work. They built a thing and then they test it. Manually, often. What's cool about this is this is exactly that same thing, and it's running constantly. It's telling you, "Here's how this agent should respond," and it's very specific ways. "If it's this, this, this, do that. If it's this, this, that, do that." It's exactly what I've been hearing again and again, you could see right here. This is the purest sense of what a product requirements document should be, is this eval judge that's telling you exactly what it should be, and it's automatic and running constantly.
Shreya Shankar :
Yeah, absolutely. It's derived from our own data, so of course, it's a product manager's expectations. What I find that a lot of people miss is they just put in what their expectations are before looking at their data, but as we look at our data, we uncover more expectations that we couldn't have dreamed up in the first place, and that ends up going into this prompt.
Lenny Rachitsky :
That is interesting. Your advice is not skip straight to evals and LLM as judge prompts before you build the product, still write traditional one-pagers PRDs to tell your team what we're doing, why we're doing it, what success looks like. But then at the end, you could probably pull from that and even improve that original PRD if you're evolving the product using this process.
Shreya Shankar :
I would go even further to say you're going to improve... It's going to change. You're never going to know what the failure modes are going to be upfront, and you're always going to uncover new vibes that you think that your product should have. You don't really know what you want until you see it with these LLMs, so you got to be flexible, have to look at your data, have to... PRDs are a great abstraction for thinking about this. It's not the end all, be all. It's going to change.
Lenny Rachitsky :
I love that, and Hamel's pulling up some cool research report. What's this about?
Hamel Husain :
This is one of the coolest research reports you can possibly read if you want to know about evals. It was authored by someone named Shreya Shankar.
Shreya Shankar :
Oh, my God.
Hamel Husain :
And her collaborators. It's called "Who Validates the Validated?"
Lenny Rachitsky :
That's the best name for a researcher.
Shreya Shankar :
Thank you, thank you.
Hamel Husain :
I should let Shreya talk about this. I think one of the most important things to pay attention in this paper are the criteria drift, and what she found.
Shreya Shankar :
We did this super fun study when we were doing user studies with people who were trying to write LLM judges or just validate their own LLM outputs. I think this was before evals was extremely popular, I feel like, on the internet. We did this project late 2023 was when we started it. But then the thing that really was burning in my mind as a researcher is like, "Why is this problem so hard? We've been having machine learning and AI for so long, it's not new, but suddenly, this time around, everything is really difficult." We just did this user study with a bunch of developers and we realized, "Okay, what's new here is that you can't figure out your rubrics upfront. People's opinions of good and bad change as they review more outputs, they think of failure modes only after seeing 10 outputs they would never have dreamed of in the first place," and these are experts. These are people who have built many LLM pipelines and now agents before, and you can't ever dream up everything in the first place. I think that's so key in today's world of AI development.
Lenny Rachitsky :
That is a really good point. That's very much reinforcing what we were just talking about and that's why I'll pull this up, is just... Okay-
Shreya Shankar :
The research behind it.
Lenny Rachitsky :
Yeah, okay, great. You still got to do product the same way, but now you have this really powerful tool that helps you make sure what you've built is correct. It's not going to replace the PRD process. Cool. How many, say, I don't know, LLM as judge prompts, do you end up with usually say... I don't know. I know, obviously, depends complexity to the product, but what's a number in your experience?
Shreya Shankar :
For me, between four and seven.
Lenny Rachitsky :
That's it.
Shreya Shankar :
It's not that many, because a lot of the failure modes, as Hamel said earlier, can be fixed by just fixing your prompt. You just didn't think to put it in your prompts, so now you put it in your... You shouldn't do an eval like this for everything, just the pesky ones that you've described your ideal behavior in your agent prompt, but it's still failing.
Lenny Rachitsky :
Got it. Say you found a problem, you fixed it. In traditional software development, you'd write a unit test to make sure it doesn't happen again. Is your insight here is, "Don't even bother writing an eval around that if it's just gone"?
Shreya Shankar :
I think you can if you want to, but the whole game here is about prioritizing. You have finite resources and finite time, you can't write an eval for everything, so prioritize the ones that are the more pesky areas.
Lenny Rachitsky :
Probably the ones that are most risky to your business if they say something like Mecha Hitler, Grok.
Shreya Shankar :
Yikes.
Lenny Rachitsky :
Cool. Okay, so that's very relieving, because this prompt was a lot of work to really think through all these details.
Shreya Shankar :
But it's a lot of one-time cost. Right now, forever, you can run this on your application.
Hamel Husain :
Okay, data analysis is super powerful, is going to drive lots of improvements very quickly to your application. We showed the most basic kind of data analysis, which is counting, which is accessible to everyone. You can get more sophisticated with the data analysis. There's lots of different ways to sample, look at data. We made it look easy in a sense, but there's a lot of skills here to do to it well. Building an intuition and a nose for how to sort through this data. For example, let's say I find conversational issues, this conversational flow issues. Maybe if I was trying to chase down this problem further, I would think about ways to find other conversational flow issues that I didn't code. I would maybe dig through the data in several ways, and there's different ways to go about this. It's very similar, if not almost exactly similar as traditional analytics techniques that you would do on any product.
Lenny Rachitsky :
Give us just a quick sense of what comes next and then let's talk about the debate around evals and a couple more things.
Shreya Shankar :
What comes next after you've built your LLM judge? Well, we find that people just try to use that everywhere they can, so they'll put the LLM judge in unit tests and they will build, "Here are some example traces where we saw that failure, because we labeled it. Now we're going to make those part of unit tests and make sure that, every time we push a change to our code, these tests are going to pass." They also use it for online monitoring. People are making dashboards on this, and I think that's incredible. I think the products that are doing this, they have a very sharp sense of how well their application is performing, and people don't talk about it, because this is their moat. People are not going to go and share all of these things, because it makes sense. If you are an email-writing assistant, and you're doing this and you're doing it well, you don't want somebody else to go and build an email-writing assistant and then get you out of business.
:
I really want to stress the point that it's try to use these artifacts that you're building wherever possible online, repeatedly use them to drive improvements to your product. Oftentimes, Hamel and I will tell people how to do this up to this very point, and it clicks for people and then they never come back again. Either they have, I don't know, quit their jobs, they're not doing AI development anymore, or they know what to do from here on out. I think it's the latter, but I think it's very powerful.
Lenny Rachitsky :
Just watching you do this really opened my eyes to what this is and how systematic the process is. I always imagine you just sit on a computer, "Okay, what are the things I need to make sure work correctly?" What you're showing us here is it's a very simple step-by-step based on real things that are happening in your product, how to catch them, identify them, prioritize them, and then catch them if they happen again and fix them.
Shreya Shankar :
Yeah, it's not magic. Anyone can do this, you're going to have to practice the skill, like any new skill, you have to practice, but you can do it. I think what's very empowering now is that product managers are doing this and can do this, and can really build very, very profitable products with this skill set.
Lenny Rachitsky :
Okay, great segue to a debate that we got pulled into that was happening on X the other day. I did not realize how much controversy and drama there is around evals. There's a lot of people with very strong opinions. How about Shreya? Give us just a sense of the two sides of the debate around the importance and value of evals, and then give us your perspective.
Shreya Shankar :
Yeah. All right, I'll be a little bit placating and I say I think everyone is on the same side. I think the misconception is that people have very rigid definitions of what evals is. For example, they might think that evals is just unit tests or they might think that evals is just the data analysis part and no online monitoring or no monitoring of product-specific metrics, like actually number of chats engaged in or whatnot. I think everyone has a different mindset of evals going in, and the other thing I will say is that people have been burned by evals in the past. I think people have done evals badly. One concrete example of this is they've tried to do an LLM judge, but it has not aligned with their expectations. They only uncovered this later on and then they didn't trust it anymore, and then they're like, "I'm anti evals."
:
I 100% empathize with that, because you should be anti Likert scale LLM judge. I absolutely agree with you, we are anti that as well. A lot of the misconception stems from two things, like people having a narrow definition of evals and then people not doing it well and then getting burned and then wanting to avoid other people making that mistake. Then, unfortunately, X or Twitter is a medium where people are misinterpreting what everybody is saying all the time, and you just get all these strong opinions of, "Don't do evals, it's bad. We tried it, it doesn't work. We're Claude Code," or whatever other famous product, "And we don't do evals." There's just so much nuance behind all of it, because a lot of these applications are standing on the shoulders of evals. Coding agents is a great example of that, Claude Code. They're standing on the shoulders of Claude base model... Not base, but the fine-tuned Claude models have been evaluated on many coding benchmarks. Can't argue against that.
Lenny Rachitsky :
Just to make clear exactly what you're talking about there, one of the heads, I think maybe the head engineer of Claude Code, went on a podcast and he's like, "We don't do evals, we just vibe. We just look at vibes," and vibes meaning they just use it and feel if it's right or wrong.
Shreya Shankar :
I think that works. There's two things to that, right? One is they're standing on the shoulders of the evals that their colleagues are doing for coding.
Lenny Rachitsky :
Of the Claude foundational model.
Shreya Shankar :
Absolutely, right? We know that they report those numbers, because we see the benchmarks, we know who's doing well on those. The other thing is they are actually probably very systematic about the error analysis to some extent. I bet you that they're monitoring who is using Claude, how many people are using Claude, how many traps are being created, how long these chats are. They're also probably monitoring in their internal team, they're dogfooding. Anytime something is off, they maybe have a cue or they send it to the person developing Claude Code, and this person is implicitly doing some form of hair error analysis that Hamel talked about. All of this is evals, right? There's no world in which they're just being like, "I made Claude Code, I'm never looking at anything," and unfortunately, when you don't think about that or talk about that, I think that the community...
:
Most of the community is beginners or people who don't know about evals and want to learn about it, and it sends the wrong message there. Now, I don't know what Claude Code is doing, obviously, but I would be willing to bet money that they're doing something in the form of evals.
Hamel Husain :
We'll also say that coding agents are fundamentally very different than other AI products, because the developer is the domain expert, so you can short circuit a lot of things, and also, the developer is using it all day long, so there's a type of dogfooding and type of domain expertise that is... You can collapse the activities, you don't need as much data, you don't need as much feedback or exploration, because you know, so your eval process should look different.
Lenny Rachitsky :
Because you're seeing the code, you see the code it's generating. You can tell, "This is great, this is terrible."
Hamel Husain :
Yeah, yeah. I think a lot of people had generalized coding agents, because coding agents are the first AI product released into the wild, and I think it's a mistake to try to generalize that at large.
Shreya Shankar :
The other thing is, yeah, engineers have a dogfooding personality. There are plenty of applications where people are trying to build AI in certain domains and they don't have dogfooding for doctors, for example, or not out there trying to get all the most incorrect advice from AI and be tolerant and receptive to that. It's very important to keep, I think these nuanced things in mind.
Lenny Rachitsky :
What I'm hearing from you, Shreya, interestingly, is that if humans on the team are doing very close data analysis, error analysis, dogfooding like crazy, and essentially, they're the human evals and you're describing that as that's within the umbrella of evals. You could do it that way if you have time and motivation to do that, or you could set these things up to be automatic.
Shreya Shankar :
Absolutely, it's also about the skills. People who work at Anthropic are very, very highly skilled. They've been trained in data analysis or software engineering or AI, and whatnot. You can get there, anyone can get there, of course, by learning the concepts, but most people don't have that skill right now.
Hamel Husain :
Dogfooding is a dangerous one, only because a lot of people will say they're dogfooding. They're like, "Yeah, we dogfooded," but are they, really? A lot of people aren't really dogfooding it at that visceral level that you would need to close that feedback loop. That's the only caveat I would add.
Lenny Rachitsky :
There's also this, feels like, straw man argument of evals versus A-B tests. Talk about your thoughts there, because that feels like a big part of this debate. People are having like, "Do you need evals if you have A-B tests that are testing production level metrics?"
Shreya Shankar :
A-B tests are, again, another form of evals ,I imagine, right? When you're doing an A-B test, you have two different experimental conditions and then you have a metric that quantifies the success of something, and you're comparing the metric. Again, an eval in our mind is systematic measurement of quality, some metric. You can't really do an A-B test without the eval to compare, so maybe we just have a different weird take on it.
Lenny Rachitsky :
Yeah, okay. What I'm hearing is you consider A-B tests as part of the suite of evals that you do. I think when people think A-B tests, it's like we're changing something in the product, we're going to see if this improves some metric we care about. Is that enough? Why do we need to test every little feature? If it's impacting a metric we care about as a business, we have a bunch of A-B tests that are just constantly running.
Shreya Shankar :
This is now a great point. I think a lot of people prematurely do A-B tests, because they've never done any error analysis in the first place. They just have hypothetically come up with their product requirements and they believe that, "We should test these things," but it turns out, when you get into the data, as Hamel showed, that the errors that you're seeing are not what you thought what the errors might be. They were these weird handoff issues or, I don't know, the text message thing was strange. I would say that, if you're going to do A-B tests and they're powered by actual error analysis as we've shown today, then that's great, go do it. But if you're just going to do them, which we find that people try to do, just want to do them based on what you hypothetically think is what is important, then I would encourage people to go and rethink that and ground your hypotheses.
Lenny Rachitsky :
Do you have thoughts on what Statsig is going to do at OpenAI? Is there anything there that's interesting? That was a big deal, a huge acquisition. A- B test company people are like, "A-B test, the future." Thoughts?
Hamel Husain :
Just to add to the previous question a little bit, why is there this debate, A-B testing versus evals? I think, fundamentally, evals is... People are trying to wrap their head around how to improve their applications and fundamentally need to do... Data science is useful in products. Looking at data, doing data analytics. There's many different suite of tools, and you don't need to invent anything new. Sure, you don't need necessarily the whole breadth of data science, and it looks slightly different, just slightly, with LLMs. Your tactics might be different, so really what it is is using analytic tools to understand your product. Now, people say the word "Evals," trying to carve out this new thing, and saying evals and then A-B testing, but if you zoom out, it's the same data science as before, and I think that's what's causing the confusion is, "Hey, we need data science thinking," and AI product is helpful to have that thinking in AI products like it is in any product is my take on that.
Lenny Rachitsky :
That's a really good take, I think just the word "Evals" triggers people now.
Shreya Shankar :
Yeah.
Lenny Rachitsky :
If you just call it, "We're just doing error analysis, doing data science to understand where our product breaks and just setting up tests to make sure we know-"
Shreya Shankar :
That's boring, sounds boring. No, no, no. We need a mysterious term, like "Evals," to really get the momentum going. Your question about Statsig, I think it's very exciting. To be honest, I don't know much about it, because I just imagine that they're this company that... There's a tool that many people use, and maybe it just so happened that OpenAI acquired them. I'm sure they've been using them in the past, I'm sure OpenAI's competitors are using Statsig as well, so maybe there is something strategic in that acquisition. I have no idea, I don't know anything there, but I think those are really the bigger questions for me than, "Is this fundamentally changing A-B testing or making evals more of a priority?" I think they've always been a priority, I think OpenAI has always been doing some form of them, and OpenAI has gone so far, historically speaking, as to go and look at all the Twitter sentiment and try to do some retrospective on that, and then tie that back to their products. Certainly, they're doing-
Shreya Shankar :
Then, tie that back to their products. Certainly, they're doing some amount of evals before they ship their new foundation models, but they're going so much beyond and being like, "Okay, let's find all the tweets that are complaining about it, all the Reddit threads that are complaining about it, and go try to figure out what's going on." It goes to show that evals are very, very important. No one has really figured it out yet. People are using all the available sources signal that they can to improve their products.
Hamel Husain :
What I'll say is I'm really hopeful that it might shift or create a focus within OpenAI, hopefully. Up until now, a lot of the big labs understandably focused on general benchmarks like MMLU score, human eval, things like that, which are very important for foundation models. Those not very related to product specific evals, like the ones we talked about today, but handoff and stuff like that, they tend not to correlate.
Shreya Shankar :
Yeah, they don't correlate with math problem-solving, sorry to say.
Hamel Husain :
Exactly. If you look at the eval products, let's say the ones up until recently that some of the big labs have, they don't have error analysis. They have a suite of generic tools, cosine similarity, hallucination score, whatever, and that doesn't work. It's a good first stab at it. It's okay. At least you're doing something, getting people, maybe it's like getting people look at data. But eventually, what we hope to see is, okay, a bit more data science thinking in this eval process. That's hopefully the tools we'll get to.
Shreya Shankar :
Yeah, Pamela and I should not be the only two people on the planet that are promoting a structured way of thinking about application specific evals. It's mind-boggling to me. Why are we the only two people doing this the whole world? What's wrong? I hope that we're not the only people and that more people catch on.
Lenny Rachitsky :
The fact that your course on Maven is the number one highest grossing course in Maven, clearly there's demand and interest, and there's more people I think on your side. Interestingly, just as an example you've been sharing on Twitter that I think is informative, everyone's been saying how cloud code doesn't care about evals. They're all about vibes, and everyone's like, and they're the best coding agent out there, so clearly, this is right. More recently, there's all this talk about Codex, OpenAI Codex being better and everyone's switching and they're so pro evals.
Shreya Shankar :
I know.
Lenny Rachitsky :
Yeah.
Shreya Shankar :
It gets me every time. The Internet's so inconsistent. My favorite thing was yesterday, I believe, a couple of lab mates and I were out getting dessert or something, and somebody said like, "Oh, do you like Codex or Claude better or whatever?" The other person said, "Oh, I like Claude." Then, someone else said, "But the new version of Codex is better." Then, the first person said, "Oh, but the last I checked was two days ago, so maybe my thoughts, maybe I'm not up-to-date." I was like, "Oh, my God."
Lenny Rachitsky :
So true, so true. This is the world we live in. Oh, my God. Okay. I want to ask about just top misconceptions people have with evals and top tips and tricks for being successful. Maybe just share one or two each of each. Let me just start with misconceptions, and maybe I'll go to the Hamel first. Just what are a couple of the most common misconceptions people have with eval still?
Hamel Husain :
The top one is, "Hey, I can just buy a tool, plug it in, and it'll do the eval for you. Why do I have to worry about this? We live in the age of AI. Can't the AI just eval it?" That's the most common misconception, and people want that so much that people do sell it, but it doesn't work. That's the first one.
Lenny Rachitsky :
Shoot, many humans are still great. I think that's great news.
Hamel Husain :
The second one that I see a lot is, "Hey, just not looking at the data." In my consulting, people come to me with problems all the time, and the first thing I'll say is, "Let's go look at your traces." You can see their eyes pop open and be like, "What do you mean?" I'm like, "Yeah, let's look at it right now." They're surprised that I am going to go look at individual traces, and it always 100% of the time learn a lot and figure out what the problem is. I think people just don't know how powerful looking at the data is like we showed on this podcast.
Shreya Shankar :
I would agree with that.
Lenny Rachitsky :
Those are the top two? Okay.
Shreya Shankar :
Yes.
Lenny Rachitsky :
Is there anything else or those are the ones solve those problems.
Shreya Shankar :
Oh, those are definitely... Then, I guess the third one I would add is, there's no one correct way to do evals. There are many incorrect ways of doing evals, but there are also many correct ways of doing it. You got to think about where you are at with your product, how much resources you have, and figure out the plan that works best for you. It'll always involve some form of error analysis as we showed today, but how you operationalize those metrics is going to change based on where you're at.
Lenny Rachitsky :
Amazing. Okay. What are a couple of just tips and tricks you want to leave people with as they start on their eval journey or just try to get better at something they're already doing?
Shreya Shankar :
Tip number one is just don't be alarmed or don't be scared of looking at your data. The process, we try to make it as structured as possible. There are inevitably questions that are going to come up. That's totally fine. You might feel like you're not doing it perfectly. That's also fine. The goal is not to do evals perfectly, it's to actionably improve your product. We guarantee you, no matter what you do, if you're doing parts of these process, you're going to find ways of actionable improvement, and then you're going to iterate on your own process from there.
:
The other tip that I would say is, we are very pro-AI. Use LLMs to help you organize any thoughts that you have throughout this entire process. This could be everything ranging from initial product requirements. Figure out how to organize them for yourself. Figure out how to improve on that product requirements doc based on the open codes that you've created. Don't be afraid to use AI in ways that present information better for you.
Lenny Rachitsky :
Sweet, so don't be scared. Use LLMs as much as you can throughout the process.
Shreya Shankar :
But not to replace yourself.
Lenny Rachitsky :
Right. Okay, great. There's still jobs. It's great. Hamel.
Hamel Husain :
Yeah. Let me actually share my screen, because I want to show something. To piggyback of what Shreya said is, if you heard any phrase in this podcast, you've probably heard look at your data more than anything else. It's so important that we teach that you should create your own tools to make it as easy as possible. I showed you some tools when we're going through the live example of how to annotate data. Most of the people I work with, they realize how important this is and they vibe code their own tools, or we shouldn't say vibe code. They make their own tools, and it's cheaper than ever before because you have AI that can help you.
:
AI is really good at creating simple web applications that can show you data, that can write to a database. It's very simple. For the Nurture Boss use case, we wanted to remove all the friction of looking at data. What you see here is just some screenshots of what the application that they created looks like. It's just, "Okay, they have the different channels, voice, email, text. They have the different threads, they hid the system prompt by default." Little quality of life improvements. Then, they actually have this axial coding part here where you can see in red the count of different errors. They automated that part in a nice way and they created this within a few hours. It's really hard to have a one size fits all thing for looking at your data. You don't have to go here immediately, but something to think about is make it as easy as possible because, again, it's the most powerful activity that you can engage in. It's the highest ROI activity you can engage in. With AI, yeah, just remove all the friction.
Lenny Rachitsky :
That's amazing. Again, I think that ROI piece is so important. We haven't even touched on this enough. The goal here is to make your product better, which will make your business more successful. This isn't just a little exercise to catch bugs and things like that. This is the way to make AI products better because the experience is how users interact with your AI.
Hamel Husain :
Absolutely. If any, we teach our students, "Hey, when you're doing these evals, if you see something that's wrong, just go fix it." The whole point is not to have evals, a beautiful eval suite, where you can point at it, edit it and say, Oh, look at my evals." No, just fix your application, make it better. If it's obvious, do it. Totally agree with you.
Lenny Rachitsky :
Amazing. A question I didn't ask, but this is I think something people are thinking about. How long do you spend on this? How long does it usually take to do? The first time
Shreya Shankar :
I can answer for myself for applications that I work with. Usually, I'll spend three to four days really working with whoever to do initial rounds of error analysis. A lot of labeling, feel like we're in a good place to create the spreadsheet that Hamel had and everyone's on-board and convinced, and even a few LLM judge evaluators. But this is one-time cost. Once I figured out how to integrate that in unit tests, or I have a script that automatically runs it on samples and I'll create a Cron Job to just do this every week. I would say it's like, I don't know, I find myself probably spending more time looking at data because I'm just data hungry like that. I'm so curious.
:
I'm like, I've gained so much from this process and it's put me above and beyond in any of my collaborations with folks, so I want to keep doing it, but I don't have to. I would say maybe 30 minutes a week after that.
Lenny Rachitsky :
It's a week essentially, a week essentially upfront, and then 30 minutes to keep improving on adding to your suite?
Shreya Shankar :
Yeah, it's really not that much time. I think people just get overwhelmed by how much time they spend up front and then thinking that they have to keep doing this all the time.
Lenny Rachitsky :
Amazing. Is there anything else that you wanted to share or leave listeners with? Anything else you wanted to double down as a point before we get to a very exciting lightning round?
Hamel Husain :
I would say this process is a lot of fun, actually. It's like, okay, you're looking at data. Oh, it sounds like you're annotating things. Okay. Actually, I was just looking at a client's data yesterday, the same exact process. It's a application that sends emails, recruiting emails to try to get candidates to apply for a job. We decided to start looking at traces. We jumped right into it. "Hey, let's look at your traces." We looked at a trace, the first thing I saw was this email that is worded, "Given your background, blah, blah, blah, blah, blah." I asked the person right away, and this is where putting your product hat on and just being critical, and this is where the fun part is.
:
I said, "You know what? I hate this email. Do you like the email, given your background?" When I receive a message given your background, comma, I just delete that. I'm like, "What is this, given your background with machine learning and blah blah?" I'm like, "This is a generic thing." I asked the person like, "Hey, can we do better than this? This sounds like generic recruiting." They're like, "Oh, yeah, maybe." Because they were proud of it, they're like, "The AI is doing the right thing, it's sending this email with the right information, with the right link, with the right name, everything." That's where the fun part is, is put your product hat on and get into, is this really good?
Lenny Rachitsky :
Something I want to make sure we cover before we get to a very exciting lightning round is, this is just scratching the surface of all the things you need to know to do this well. I think this is the best primer I've ever seen on how to do this well.
Shreya Shankar :
Nice.
Lenny Rachitsky :
But I think we did it. But you guys teach a course that goes much, much deeper for people that really want to get good at this and take this really seriously. Share what else you teach in the course that we didn't cover, and what else you get as a student being part of the course you teach at Maven.
Shreya Shankar :
Yeah, I can talk about the syllabus a little bit, and then Hamel can talk about all the perks. We go through a lifecycle of error analysis, then automated evaluators, then how to improve your application, how do you create that flywheel for yourself? We also have a few special topics that we find pretty much no one has ever heard of or taught before, which is exciting. One is, how do you build your own interfaces for error analysis? We go through actual interfaces that we've built and we also live code them on the spot for new data. We show how we use Claude code cursor, whatever we're feeling in the moment that day to build these interfaces.
:
We also talk about broadly cost-optimization as well. A couple of people that I've worked with, they get to a point where their evals are very good, their product is very good, but it's all very expensive because they're using state-of-the-art models. How can we replace certain uses of the most expensive GPT-5, with 5-nano, 4-mini whatnot and save a lot of money, but still maintain the same quality? We also give some tips for that. Hamel, you're on. We also have many perks.
Lenny Rachitsky :
Yeah. Talk about the perks.
Hamel Husain :
Okay, the perks. My favorite perk is there's 160 page book that's meticulously written, that we've created, that walks through the entire process in detail of how to do evals that supplement the course. You don't have to sit there and take all these notes. We've done all the hard work for you and we have documented it in detail and organize things. That is really useful. Another really interesting thing, and something that I got the idea from you, Lenny, is, okay, this is an AI course. Education shouldn't be this thing where you are only watching lectures and doing homework assignments. Students should have access to an AI that also helps them. What we have done is we've, just like there's the LennyBot that you have.
Lenny Rachitsky :
Dot com.
Hamel Husain :
Yeah, lennybot.com, we have made the same thing with the same software that you're using, and we have put everything we've ever said about evals into that. Every single lesson, every office hours, every Discord chat, any blogs, papers, anything that we've ever said publicly and within our course, we've put it in there. We've tested it with a bunch of students and they've said it's helpful. We're giving all students 10 months free unlimited access to that alongside the course.
Lenny Rachitsky :
Amazing. Then, you'll charge for that later down the road?
Hamel Husain :
I have no idea. I just take one month at a time. I don't know where we're going with that.
Lenny Rachitsky :
Eight months and then we'll have to figure it out. I was thinking this whole interview should have just been our bots talking to each other.
Shreya Shankar :
That's amazing. I would watch that, only for 10 minutes then I don't know what they're talking about.
Lenny Rachitsky :
Yeah, maybe 30 seconds. Do you guys train it on the voice mode, by the way? That's my favorite feature of Delphi's product. If not, you should do that.
Hamel Husain :
Oh, I think, I can't remember, I should look at it.
Lenny Rachitsky :
You definitely should. Now that we have this podcast episode, you could use this content to train it. It's 11Labs powered. It's so good. Okay, so how do they get to... I guess that's okay. They get to that once they become, enter your course.
Shreya Shankar :
Yeah, sign up for the course and then you'll get a bunch of emails. Everything will be clear, hopefully.
Lenny Rachitsky :
Amazing. Okay.
Shreya Shankar :
We also have a Discord of all the students who have ever taken the class. That Discord is so active. I can't go on vacation without getting notified on the plane.
Lenny Rachitsky :
Bittersweet, bittersweet. Incredible. Okay. With that, we've reached our very exciting lightning round. I've got five questions for you. Are you ready?
Shreya Shankar :
Yes. Let's go.
Lenny Rachitsky :
Let's do it. Okay. I'm going to bounce between you two. Share something if you want. You can pass if you want. First question, Shreya, what are two or three books that you find yourself recommending most to other people?
Shreya Shankar :
I like to recommend a fiction book because life is about more than evals. Recently, I read Pachinko by Min Jin Lee. A really great book. Then, I also am currently reading Apple in China, which the name of the author is slipping my mind, but this is more of an exposition, written by a journalist on how Apple did a lot of manufacturing processes in Asia over the last couple, several decades. Very eye-opening.
Lenny Rachitsky :
Amazing. Hamel.
Hamel Husain :
Yeah, I have them right here. I'm a nerd. Okay, so I'm not as cool as Shreya is. I actually have textbooks, which are my favorite. This one is a very classic one, Machine Learning by Mitchell. Now, it's theoretical, but the thing I like about it is it really drives home the fact that Occam's razor is prevalent not only in science, but also in machine learning and AI. A lot of times the simplest, and also engineering, so a lot of times the simpler approach generalizes better. That's the thing I internalize deeply from that book. I also really like this one. Another textbook. I told you I'm a nerd. This is also a very old one, and this is Norvig algorithms. I really like it because it's just human ingenuity and it's lots of clever useful things in computing.
Shreya Shankar :
They're down the street, him and Berkeley.
Lenny Rachitsky :
The people that did that research?
Shreya Shankar :
Yeah, textbook authors.
Lenny Rachitsky :
Super cool. Oh, man, nerds, I love it. Okay, next question. Favorite recent movie or TV show? I'll jump to Hamel first.
Hamel Husain :
Okay, so I'm a dad of two parents. I have two parents. Sorry, two kids. Yeah, I'm a dad of two kids, and I don't really get the time to watch any TV or movies, so I watch whatever my kids are watching. I've watched Frozen three times in the last week.
Lenny Rachitsky :
Only three? Oh, okay. In the last week. Okay.
Hamel Husain :
That's my life.
Lenny Rachitsky :
Great, Hamel. Frozen. I love it. Okay, Shreya.
Shreya Shankar :
Yeah, I don't have kids, so I can give all these amazing answers. Actually, so my husband and I have been watching The Wire recently. We never actually saw it growing up, so we started watching it and it's great.
Lenny Rachitsky :
I feel like everyone goes through that. Eventually in their life they decide, I will watch The Wire.
Shreya Shankar :
I know, so we are in that right now.
Lenny Rachitsky :
It's like a year of your life. It's great. It's such a great show. Oh, man. But it's so many episodes and everyone's an hour long.
Shreya Shankar :
I know. I know.
Lenny Rachitsky :
It's such a commitment.
Shreya Shankar :
We get through two or three a week, so we're very slow.
Lenny Rachitsky :
Worth it. Okay, next question. Do you have a favorite product you've recently discovered that you really love? We'll start with Shreya.
Shreya Shankar :
Yeah. I really like using Cursor, honestly. Now, Claude Code. I'll say why. I'm a researcher more so than anything else. I write papers, I write code, I build systems, everything, and I find that a tool... I'm so bullish on AI assisted coding because I have to wear a lot of hats all the time. Now, I can be more ambitious with the things that I build and write papers about, so I'm super excited about those. Cursor was my entry point into this, but I'm starting to find myself always trying to keep up with all these AI assisted coding tools.
Lenny Rachitsky :
Hamel?
Hamel Husain :
Yeah, I really like Claude Code and I like it because I feel like the UX is outstanding. There's a lot of love that went into that. It's just really impressive as a terminal application that is that nice.
Lenny Rachitsky :
Ironic that you two both love Claude Code when it's just built on vibes.
Shreya Shankar :
I think it's false. It's not just built on vibes.
Lenny Rachitsky :
There we go. Okay, two more questions. Hamel, do you have a favorite life motto that you find yourself using in coming back to in work or in life?
Hamel Husain :
Keep learning in. Think like a beginner.
Lenny Rachitsky :
Beautiful. Shreya?
Shreya Shankar :
I like that. For me, it's to always try to think about the other side's argument. I find myself sometimes just encountering arguments on the internet, like this race to eval debates and really think, "Okay, put myself in their shoes. There's probably a generous take, generous interpretation." I think we're all much stronger together than if we start picking fights. My vision for evals is not that Hamel and I become billionaires. It is that everyone can build AI products, and we're all on the same page
Lenny Rachitsky :
Slash everyone becomes billionaires.
Shreya Shankar :
Yes.
Lenny Rachitsky :
Amazing. Final question. When I have two guests on, I always like to ask this question and I'll start with Hamel. What's something about Shreya that you like most? What do you like most about Shreya? I'm going to ask her the same question in reverse.
Hamel Husain :
Yeah. Shreya is one of the wisest people that I know, especially for being so young relative to me. I feel like she's much wiser than I am, honestly, seriously. She's very grounded and has a very even perspective on things. I'm just really impressed by that all the time.
Lenny Rachitsky :
Shreya?
Shreya Shankar :
Yeah. My favorite thing about Hamel is his energy. I don't know anybody who consistently maintains momentum and energy like Hamel does. I often think that I would start carrying much less about evals, if not for Hamel. Everyone needs a Hamel in their life, for sure.
Lenny Rachitsky :
Well, we all have a Hamel in our life now. This was incredible. This was everything I'd hoped it'd be. I feel like this is the most interesting in-depth consumable primer on evals that I've ever seen. I'm really thankful you two made time for this. Two final questions. Where can folks find you? Where can they find the course and how can listeners be useful to you? I'll start with Shreya.
Shreya Shankar :
Yeah, you can reach me via email. It's on my website. If you Google my name, that is the easiest way to get to my website. You can find the course if you Google AI Evals for engineers and product managers, or just AI Evals course, you'll find it. We'll send some links hopefully after this, so it's easy. How to be helpful? Two things always for me. One is ask me questions when you have them. I'll try to get to the respond as soon as I can. The other one is tell us your successes. One of the things that keeps us going is somebody tells us what they implemented or what they did, a real case study. Hamel and I gets so excited from these and it really keeps us going, so please share.
Hamel Husain :
Yeah, it's pretty easy to find me. My website is Hamel.dev. I'll give you the link. You can find me on social media, LinkedIn, Twitter. The thing that's most helpful is to echo what Shreya said, we would be delighted if we are not the only people teaching evals. We would love other people teach evals. Any kind of blog posts, writing, especially that as you go through this and learn this that you want to share, we would be delighted to help re-share that or amplify that.
Lenny Rachitsky :
Amazing. Very generous. Thank you two, so much for being here. I really appreciate it, and you guys have a lot going on, so thank you.
Shreya Shankar :
Thanks, Lenny, for having us and for all the compliments.
Lenny Rachitsky :
My pleasure. Bye everyone. Thank you so much for listening. If you found this valuable, you can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review as that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at Lennyspodcast.com. See you in the next episode.
