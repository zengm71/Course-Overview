Introduction to git and Source Control Management Systems
===

####What you need to know to be effective

#GitHub and Collaborative Source Control

Now that we've learned most of the basics on our local machine, now we've got to get this setup for use with GitHub.


#What is GitHub?

[GitHub](https://github.com/) is a popular location for people to store code. During your time as a data scientist you'll frequently come across github when searching for packages, documentation, or for better understanding issues. You can do all sorts of great things with it like hosting projects or even your personal portfolio of projects.


#Getting Set up

First, you're going to need to create a GitHub account. You can do this on the [GitHub website](https://github.com/) by clicking the `Sign Up` button. Now we'll need to make sure that our local version of git can communicate with GitHub's.

Follow these instructions to set up Git and GitHub to work together.

[https://help.github.com/articles/set-up-git/](https://help.github.com/articles/set-up-git/)

Once that is set up, let's go ahead and create a repository, go ahead and create a public repository and follow the instructions!

[https://help.github.com/articles/create-a-repo/](https://help.github.com/articles/create-a-repo/)

#Committing to a Repository

Now that we've created our repository, we want to push the code we've written to it! To "push code" means to copy a branch from a local repository to a remote repository. Let's break that down

What we need:

- [X] Code (the code that we've written in our local repository)
- [X] A Local Repository (the one that we've been working with in previous lessons)
- [X] A Remote Repository (the Github repository you just created)
- [ ] A link between the remote repository and our local repository.


So we're really only missing one thing at this point, the link between the two and that's what we'll create now.

##Linking local and remote repositories

First we need to see which, if any, remote repositories we have connected to our repository. We do this by running:

```sh
git remote
```

If we run this in our local repository, we won't get any printout at all because we haven't added a remote repository yet, let's do that now.



The command to do this is `git remote add <name> <url>` (the name and url will be filled in by us).

So we need to give it a name, and a url, seems simple enough. Now by convention, the standard name for the core remote repository is `origin`. This can change as projects increase in complexity but it's what we'll be using here.

Now we need our url. On the GitHub repository page, on the right side you'll see a **Clone URL.** We'll be using this to allow our local repository to talk with our remote one. Copy the url there.

Now we can type the command into the command line.

```sh
git remote add origin git@github.com:MIDS-Python-Bridge-Course/Course-Overview.git
```

Your url will be different that the one listed above, however the layout should be the same. Now we can run

```sh
git remote
```

which should print `origin`

Now that we've linked those up, let's push our code up to that repository. Firstly we'll want to run `git status` to confirm the branch that we are on as well as what state our code is in. You cannot push code that is in `staging`, you can only push code that is committed (however you can run the command without fully committed code). For this exercise, make sure that you are on the master branch and that all your code is currently committed.

Now we can push our code, the layout of the command is straight forward `git push <remote_name> <branch>` where remote name and branch will be filled in by us. For this exercise we're going to be pushing to `origin` and we'll be pushing the `master` branch.

```sh
git push origin master
```