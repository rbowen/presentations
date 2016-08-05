# How To Ask And Answer Questions The Smart Way

This document is [CC Attribution 2.0
Generic](https://creativecommons.org/licenses/by/2.0/)

*[betterfm.org](http://betterfm.org)*

## Introduction

It is important to ask questions well, if you want to get helpful answers. This
involves doing some work ahead of time, clearly stating what problem you're
trying to solve, and also what you're trying to accomplish, in case there's a
better path to the solution than what you've considered.

You'll also need to develop a little bit of a thick skin, since there is a long
tradition of treating beginners like lower life forms. This attitude is actively
encouraged by documents such as ESR's original [How To Ask Questions The Smart
Way](http://catb.org/~esr/faqs/smart-questions.html) document, which inspired
the creation of this one.

Don't be deceived - it is still absolutely critical that you ask smart
questions. But we realize that in today's IT world, it's simply impossible to
know everything about everything, and that most of us are very
solutions-oriented. When we need to solve a problem, we typically don't have
time to learn the entire stack before solving that problem. Thus, this document
is addressed both to the asker and to the answerer.

While acknowledging that much of the burden rests on smart questions, the
authors of this document also believe that patience, respect, and kindness are
an important part not merely of answering questions, but of being human.

## Asking

### Before You Ask

Before asking a technical question by e-mail, on IRC, or on a website chat
board, do the following:

* Try to find an answer by searching the Web.
* Try to find an answer by searching the archives of the forum or mailing list you plan to post to.
* Try to find an answer by reading the manual.
* Try to find an answer by reading a FAQ.
* Try to find an answer by inspection or experimentation.
* Try to find an answer by asking a skilled friend.
* If you're a programmer, try to find an answer by reading the source code.

When you ask your question, it's useful to display what you have already tried,
so that you don't get a list of things to try that you've already tried.
Furthermore, this demonstrates that you're not asking for people to do your work
for you, but that you've done some research yourself.

Try to phrase your question in terms of goals, rather than in terms of steps.
That is, state what you are trying to accomplish, rather than merely stating
what step isn't working. Thinking carefully about the problem statement often
leads you to thinking of alternate solutions. Also, having a larger context,
rather than single breaking step, will help the answerer have a better idea of
why the step matters, and thus motivate them to help.

### Where to ask

It is often far from obvious where the best place to ask a question is going to
be, and it varies a great deal from one software project to another. It's worth
your time to look around at the various support venues, and see what kind of
conversation happens in each, to judge where you're likely to get the best
results. Some rules of thumb are:

* If your question feels quick, IRC is probably right.
* If your question requires a lengthy introduction, the mailing list or web forum will be better.
* Look for 'official' support channels, such as the mailing lists or IRC channel, if the question relates to the source code, new features, or a possible bug.
* For common operator tasks, third-party sites are often populated by practitioners who have hands-on experience, and practical advice.
* Do try to find a venue related to the right topic. Off-topic questions tend to be answered by a redirection to a different venue, and you've wasted your time as well as the answerer's.

#### Search the Web

You are not alone. Someone else has had exactly the problem that you are asking
about. Lots of someones. And several of them have written blog posts or articles
about it. Several more of them have asked your question on various mailing lists
and websites.

Search the web for the exact error message that you are seeing. In most cases,
this will lead directly to the solution you need, or, at least, to a discussion
of what to investigate.

#### StackExchange

The [StackExchange](http://stackexchange.com) family of websites have become the
de-facto documentation for many software projects, as well as many non-technical
topics. Over time, the wealth of questions a thorough answers has grown to the
point where you can almost always find a discussion of your problem written up
there, complete with exhaustive solutions and links to further discussion.

Because these sites are question-based, rather than traditional documentation,
the answers tend to be very solution-based, providing ready-to-use examples that
you can use to solve practical problems.

The down side to these sites is that every scenario is slightly different, and
so the specific problem statement might be different enough from yours that the
solution doesn't exactly match.

Stack Exchange consists of close to 150 distinct sites, which are
topic-specific. Here's a quick overview of the major sites.

* [Super User](http://superuser.com) is for questions about general-purpose computing. Questions about how to use your computer, or end-user applications, go here. This forum is very Windows-friendly.

* [Stack Overflow](http://stackoverflow.com) is for questions about programming.

* [Server Fault](http://serverfault.com) is for questions about server and network administration.

* Several projects have their own specific sites, including [Ubuntu](http://askubuntu.com/), [game development](http://gamedev.stackexchange.com/), [WordPress](http://wordpress.stackexchange.com/), and [graphic design](http://graphicdesign.stackexchange.com/). Check the [Stack Exchange](http://stackexchange.com) site for an up-to-date list.

#### IRC

IRC - Internet Relay Chat - is a means of having a live conversation with a
group of people over the Internet. There are several very popular IRC networks
where you're likely to find help on a wide variety of topics.

To use IRC, you'll first need an IRC client - software used to connect to the
IRC servers. Popular ones include xChat, Colloquy, mIRC, IRSSI, and others.
Wikipedia has a [comparision of IRC clients](http://en.wikipedia.org/wiki/Comparison_of_Internet_Relay_Chat_clients)
which will help you choose one that's right for your needs. Also, most major IRC
networks have a web interface, if you don't want to install a client.

We do recommend, however, that you obtain and install an IRC client, as you are
likely to need IRC frequently in your quest for knowledge.

Popular IRC networks include:

* [Freenode](http://freenode.net)
* [EFnet](http://efnet.org)
* [DALnet](http://dal.net)

Other networks are listed on [the mIRC
website](http://www.mirc.com/servers.html).

Several helpful tips for asking on IRC:

* Don't ask to ask - just go ahead and ask your question.
* Don't paste large quantities of text into a channel. If it's more than a single line, use a pastebin site such as [pastie](http://pastie.org) or [hastebin](http://hastebin.com/), and then paste the URL into the channel. See [pastebin appendix](#pastebin) for more detail.
* Be patient. You will not get an instant answer. It may take minutes, or even hours, to get an answer, depending on the channel.
* Read the channel topic, as it will often contain links to FAQs and other useful information.

[IRCHelp](http://www.irchelp.org/) is a great place to start if you're an IRC
newbie and you want to get up to speed on the arcana of using IRC.

#### Web Forums

Many projects have moved to web forums for technical support. They have the
advantage that answers are archived forever, but the disadvantage that answers
tend to arrive much more slowly than on live channels such as IRC.

If a project has a web forum, it will be linked to from the website. Use the
search feature before you dive in with your question, because someone else has
probably already had the same problem.

Note that many projects just rely on the StackExchange family of sites. (See
above.)

#### Project Mailing Lists

Most software projects have one or more mailing lists. Mailing lists are
probably the very best place to get support, because everyone that's involved in
the project is practically guaranteed to be there.

Here, too, the conversation is usually archived somewhere, although the ease of
use of mailing list archives varies greatly. Sites like
[GMANE](http://gmane.org/) and [MarkMail](http://markmail.org/) archive
thousands of open source mailing lists in searchable formats, which may be
easier to use than the official archives, which tend to be less searchable.

Most projects will have (at least) two mailing lists - one which is
user-centric, where it's appropriate to ask questions, and another which is
developer-centric, where the work of developing the software happens.

To ask a question on a mailing list, you will typically have to subscribe to the
mailing list first. This may be by sending email to a special address (for
example, users-subscribe@httpd.apache.org) or via a web interface (for example
the [rdo-list subscribe
page](https://www.redhat.com/mailman/listinfo/rdo-list)).

Simply sending email to a mailing list that you are not subscribed to usually
doesn't work, as replies will go back to the list, and you won't see them.

Mailing lists may be a handful of people, or they may be tens of thousands of
people scattered across every time zone. Be patient. It may take a full day for
the right person, in the right time zone, to see your question.

Some helpful tips that will contribute to you getting good answers are:

### Use a meaningful subject line

Mailing lists can get a lot of traffic. Frequent answerers tend to filter by
subject line. That is, they will skip messages that don't appear to be in their
area of interest or expertise. Your subject line should say what the message is
about. If possible ask the question in the subject line. If not, make sure you
mention important keywords.

Subject lines like "Help!", "I have a question." or "Looking for assistance"
will cause your message to be ignored by many potential helpers. Subject likes
like "[OpenStack Neutron] Failed to find some config files:
/etc/neutron/plugins_conf.ini" on the other hand, will draw the attention of the
right helper.

As an added benefit, good subject lines make your message easier to find in a
search by a future person in need of help. Remember that it may even be
yourself, searching your own email for that answer.

### Provide all the details

In your question, you should provide all of the details, including all error
messages. If you have log files, provide them, either in the message body if
they are reasonably short, or on a pastebin, or downloadable on your website.

The more details you provide, the less time you'll waste in being asked for yet
another piece of information.

Don't say things like "it doesn't work" or "it's broken", but rather say what
you're trying to do, what is happening, and in what way it differs from what you
expect to be happening. This is absolutely critical, and skips the step where
the helper says "what do you mean by *doesn't work*".

Never say "I'm getting an error" without saying what that error is. (This would
be a good time to search Google for that error.)

If you've already tried some things, mention that. Copious use of
[pastebins](#pastebin) for code and configuration examples are very helpful
here.

If you are following a particular howto or tutorial, mention that, providing a
link. Say how far you got.

Mention what operating system you're using (Windows, Mac, Linux), and, if
relevant, what version (Fedora 22, Windows 8, etc.). Say what version of the
software in question you're using (Apache web server 2.4.10) and what associated
programs are involved (PHP 5.4.41).

If you are experiencing a consistently repeatable problem, mention the steps
that are involved in creating that problem scenario.

Be thorough, but also attempt to be concise. Don't provide random additional
information that may cloud the issue. If you're unsure, provide additional
information on a [pastebin](#pastebin), and link to it.

### Be specific as to what your question is

Make sure that you actually ask a question. Describing a scenario, but not what
your actual question is, feels very open-ended, and, thus, a huge potential time
sink. Make sure you state very specifically what problem you're trying to solve,
and what your intended outcome is.

### Be patient

As mentioned above, open source communities may be scatterd all across the
globe. It may take a day or two for it to reach the right person in the right
time zone.

The response may come from someone who does not share your first language. Focus
on the message, rather than on the phrasing or grammar.

Don't ask people to reply to you off-list, and don't ask if you can contact
someone personally off list. These are considered rude, anti-cmmunity behaviors.
There's a public mailing list because your question, and the answers to it,
benefit the entire community. Taking that conversation off-list is seen as
selfish.

### When asking about code

* Show the smallest possible example
* Show your input and output

### Don't post homework questions

### Don't use weasel words

* Urgent
* Panic
* Lose my job

### Be polite

### Follow up when you find a solution

* Tells people to stop looking
* For the archives

## How To Interpret Answers

### Dealing with rudeness

### If You Can't Get An Answer

# How To Answer Questions in a Helpful Way

* Be polite
* Ask for more information - be specific
* Remember you were ignorant once, too
* Be patient
* Remember posterity - write up your question thoroughly, put it online, so that you can link to it next time.

# Appendices

## pastebin

A pastebin is a place where you can paste large quantities of text, so that
someone else can then find it later, without having to paste that text into
email, an IRC channel, or other similar place.

Popular pastebin sites include [pastie](http://pastie.org) and
[hastebin](http://hastebin.com/). We recommend that you avoid pastebin.com
because it tends to be blocked in large parts of the world, including China.
