# POSTMORTEM

A technical postmortem is a retrospective analysis of events that resulted in
a technical failure.

The purpose of a technical postmortem is to register and document the failure
spots and how to solve it.

When you are configuring many machines or a complex architecture it is easy to
move something which makes the server fail. When it happens you run into a
solution, read documentation and write in forums. It can take you a few minutes
or can take several hours. If you find the solution, you can think that it's
finished there, and maybe you're right, you solve that problem and it doesn't
appear again.
But the problem comes when the same error appears again after, you must find
again all the information and read a huge amount of documentation again,
when you solve the problem last time you try to solve it in different
ways until one of those works. So now you need to remember what works or go
again, throw away the pain of reading and try all again.

Here is where the postmortem appears, it is nothing of the other world, and is
the most logical solution. Not only for tech problems almost any kind of
problem can be documented and the documentation will be useful. In a few words
a postmortem report details how to solve a problem and how to avoid it. isn’t
it easy?
You can write your postmortem report as you like, but make sure to include the
next information, and remember, having the same format on all your reports is
important to make it easy to read and don't forget anything when you are
writing it.

## What happened?

You can’t analyze what you don’t understand, so make sure to detail what raises
the problem. Remember to explain it with all kinds of details, maybe the next
time you are not trying to solve it.

## Why did it happen?

If you want to be a good professional you can’t only solve problems you must
avoid the problems, if a failure makes your production server goes down and
you only work on the problem when your clients are waiting for the service to
work again… let me say you are kinda stupid. Why if you can avoid the problem
you wait until it makes you lose time and money? So make sure to write why the
problem arises so you can be careful to don’t do it again.

## How did we respond and recover?

Remember, a good postmortem can be understood by anyone. Put in your postmortem
report what steps you follow until you find the solution. The idea here is not
only to reach the solution, it’s also about the process, a piece of documentation
is so useful! but if you are reading a postmortem and can learn about what the
writers do wrong and what they do well, you can learn how to solve a problem faster.
So please be honest in the report. An important part of team work is the honestity,
and detecting our own problems. Here you can try doing a timeline and relate
all the things you or your team do until you detect the problem and find the solution.

## How can we prevent similar unexpected issues from occurring again?

When you configure a server, start an app… you find similar problems each time,
some of those you can solve it in a few minutes, because you already solve those
many times, but some similar problems, and more complex, sometimes rises and
there you have a problem, all the points on this article are very important to
take care. You can add more if you need. I try to explain why you need each of
those, and this point, last but not least, is important because the same mistake
can raise different problems.

Remember a postmortem can be only a guide step by step, explaining how to solve
a problem. But if you really want to make your project or your company better,
work faster, learn and improve your skills, you need to learn about the errors
and success of yours and other people. Take a postmortem as an opportunity to
learn all about you and other people, it’s the better way to take.

## Example

### Date: 09-28-2021 00:00

### What happened?

The server stops working and raises error 500 after devops enginers change the
wordpress settings. The databases and other servers still working.

### Why did it happen?

After get notice of the problem and what was done before the page goes down
we decide to use 'strace' trying to find whath rises the problem, fortunally
we find the problem in the '/var/www/html/wp-settings.php' file, also the output
of 'strace', provides first line who is raising a problem and points out the
problem. with that output we conclude that the problem is a sintax one.

### How did we respond and recover?

We don’t find any problem with php or mysql so we decide to use the
'strace' command to read the all the applications logs, we read the output
until we find the first point of failure, there we find all the information
about what is the error cause. After change the sintax error and restart the
service the problem get solved.

### How can we prevent similar unexpected issues from occurring again?

Any body can missclick a key and makes a sintax error, But for that reason,
we encorage you to uses a code editor who notifies you about that kind of
errors.
configure the server with a text editor with a languaje server.
