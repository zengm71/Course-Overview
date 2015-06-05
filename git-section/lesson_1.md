Introduction to git and Source Control Management Systems
===


##What is source control?

Source control management or version control is a system for organizing different versions of basically anything. Version control is absolutely ubiquitous in the software development industry and will be something that you run into a fair amount as a data scientist. One widespread example of version control is called distributed source control.

Distributed source control is a wa in which companies and individuals manage documents, and versions of documents, and share them among various computers and people.

Some popular version control systems are:

- Git
- SVN (Subversion)
- Mercurial

Over the course of the next several lessons, you will learn the basics of the git version control system. This current course, as well as many other courses at UC Berkeley, will take advantage of souce control systems. The tool is integratl to your understanding of software development and the data science industry. This course, like the other courses in the Master's of Data Science program, will be focusing on using the git version control system, arguably the most widespread tool in use today.

##What problem does source/version control solve?

You've likely set up your own basic version control system in the past even without realizing it. There are lots of different kinds of version control systems. Maybe you've organized a project by labelling files like:

- `paper.doc`
- `paperv1.doc`
- `paperv2.doc`
- `paperv2FINAL.doc`

Simply by appending a certain version number or string, you're keeping track of the changes that you're making and keeping things simple so you can return to a previous state after you make some changes (that you may or may not like).

As you've surely discovered, this system can get unwieldy quickly as you start naming files with longer names or more detailed dates. Additionally, sharing these files with other people makes it difficult to manage revisions, as changes can be difficult to track as others may not understand the system by which you're organizing your versions. How do they know which one is truly the final version? What if they organize from v3 down to v1?

It is this core issue that version control seeks to solve.

A version control system provides a consistent, organized way all changes to your projects, from notes and documentation down to the source code itself. Systems like git provide a formalized vocabulary and a set of actions that you can perform in order to keep your files properly versioned and allow others to easily contribute as well. While the system will feel overly formalized at the beginning, once you get the hang of it, you'll never look back.

##The basics of version control

Now that we've got a better understanding of the problem that we're solving, let's read a bit more about git. Git is a distributed version control system, not unlike services that you've used before.

A simple example of a distributed version control system is Dropbox or Google Drive. You've got a copy of a file on your home computer, you've got a copy on Google's/Dropbox's servers and finally a copy on your work computer. When you make changes, Google and Dropbox track these changes, assure there are no conflicts with other files, then make sure that all the devices have the same copy of the same document that is up to date with the most recent version.

Think of it this way, a version control system is like Dropbox or Google Drive. You've got a copy of a file on your computer, you've got a copy on Google's Servers and a copy on a friend's computer if it's a shared folder. When you save a file, that file is automatically synced from your own computer, to Google, and on your friend's computer. It is as if Google and your friend's computer knows when that file is updated and then  to make sure it has the most up to date copy of the file.

Now Git works in a simliar way but with a key difference: rather than syncing being automatic, you have to specify exactly what happens and when. Let's go back to our previous example. When I save a file using Git, neither Google, nor my friend's computer syncs automatically to get the most up to date file.

However if I run the command:

`git push origin master`

That then manually pushes my changes to Google servers. If my friend now wants the latest and greatest, she can now pull those changes from Google with this command:

`git pull origin master`

and now all of the changes have been downloaded to my friend's computer. We will get into more on what `origin master` means later but these are the steps where you would share files using git. Unlike Dropbox or Google Drive which assumes that it knows what you want it to do, version control is much more precise - you are in control every step of the way.

Read the [version control introduction](http://git-scm.com/book/en/v2/Getting-Started-About-Version-Control) on the git-scm website to get a more precise definition of version control. That will also gives us exact definitions of local, centralized, and distributed version control systems. Once you've learned that, we'll take the next step and get started on our own computer.



##The Vocabulary

One of the most difficult transitions for new users is the vocabulary used in version control systems. As with anything, the language takes a little bit of time to adjust to but with time it becomes second nature. We reccommend that you spend some time familiarizing yourself with the vocabulary, we'll be using it throughout the course. That being said, don't worry if you don't understand all the terms or their definitions. These are meant to be a foundation for future reference, a way to get a better understanding of what the words mean before we see how to use them.

####Nouns:

- Repository (repo)
	- A repository is a copy of a project. It can either be on your local computer or on a server. It houses all the data associated with that project including both files and folders.
- Branch
	- An independent copy of the project where changes can be made without disrupting the source of truth: the *master branch/trunk*
- Master Branch/Trunk
	- A master branch is the core tree trunk of your project. Plese note: you can branch off of the trunk but the master branch is the core branch in the project. Think of it as the source of truth of the project.
- Staging
	- The staging area is one where you prepare and review to make a commit to a branch. Staging is where you might run tests to make sure that the code you are about to commit is ready to be committed.
- Remote Repo
	- The remote repository is a version of the project on a remote computer or on a remote system like GitHub.
- Local Repo
	- A local repository is one on a particular machine. Typically any changes you make will be made in your local repository, then pushed to a server or service like GitHub.
- Pull Request
	- A formalized request to the owner of a remote repository that they integrate a branch into the codebase.

####Verbs:

- Fork
	- To create a copy of a repository, that you don't own, in your own personal repository. This is most commonly associated with creating a copy on someone else's GitHub in your own so that you can make changes as you see fit.
- Pull
	- Pulls a remote branch down to your local repository. For example, you might pull down the master branch from your remote repository in order to make sure that your local branch is up to date with the remote branch.
- Branch
	- Creates a new branch in your local repository. When you perform this action, it will be created off of the branch that you are currently on.
- Merge
	- Merges a the changes of a branch into another branch.
- Push
	- Pushes a local branch to a remote repository.
- Pull Request
	- A request to other people collaborating on the project to *pull* a particular branch and review the changes. That way someone else can proofread your changes before those changese are *merged* to the master branch.
- Commit
	- Commits a files/lines in files in the staging environment to the current branch in the repository.
- Checkout
	- Switches your repository to a particular branch (or tag or commit, but that is out of the scope of this tutorial). For example, you would *checkout* your friend's *branch* if they initiated a *pull request* for you. You would then see your repository with all of your friend's changes. You then can switch back to the *master branch* when you want to go back to the source of truth.
- Clone
	- Copies a remote repository to the local environment.



##Getting Setup & Your First Repository

Now we've talked through an abstract introduction of git and version control, let's get started!

First we'll need to install git. So head over to the [git homepage](http://git-scm.com/) and click the button on the right hand side for your Operating System (Mac OS X, Linux, Windows).

Once you've got that installed let's go ahead and get started.

Read up on the [git basics](http://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository).

Now that we've read the intro, let's make our first git repository. Open up your terminal and let's navigate to the Desktop.

```sh
cd ~/Desktop
```

once there let's go ahead and create a new folder

```sh
mkdir git_test
```

Now that we've created that folder let's change directories into it

```sh
cd git_test
```

Now that we're in here, let's initialize a git repository.

```sh
git init
```

This creates a folder labelled `.git` in the current directory. **NEVER EDIT THIS FOLDER MANUALLY** as you'll get yourself in all kinds of trouble. It's just good to be aware that it is there and it is what stores all the information about this repository. If you delete the project folder, you delete the version informaiton as well.

Now that we've created that folder, let's create some files to track!

Start by running:

```sh
touch hello.py
touch ignore_me.txt
```

This will create a python file and a text file in the current directory. Now you'll want to edit them. Open up the python file in the editor of your choice.

In the python file let's write a couple of lines.

```py
print("Hello World. I'm learning how to program in python.")

# Here is a commment

print("I'm also learning git because I value good coding practices!")
```

Let's go ahead and make sure that it works. We can do that by executing the python file from the command line. Go ahead and run

```sh
python hello.py
# to execute it with python3
python3 hello.py
```

Keep in mind that this course operates with python version 3. While the majority of your code will work with both versions, we will be grading you based on whether or not your code is version 3 compatible.

Now that we've made those edits, let's return to the command line and commit those changes. first we'll run:

```sh
git status
```

and you'll get a print out like:

```
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	hello.py
	ignore_me.txt

nothing added to commit but untracked files present (use "git add" to track)
```

So at this point we've got our base git repository with no files being tracked. In order for git to track changes, we've got to add a file so it knows to track changes to this file. We do that with `git add FILENAME`. You can also add folders instead of specific files.

Let's go ahead and add our `hello.py` file.

```sh
git add hello.py
```

Now run git status again and you can see that things have changed

```sh
git status
```

```
On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   hello.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	ignore_me.txt

```

Now our `hello.py` file is `staged` or `in staging` and ready to be committed. Git hasn't started tracking the file changes yet - it just know that we're preparing to commit that file to our formal history.

Now let's do just that, commit it to the formal history. We can do that with:

```sh
git commit
```

This will bring up a prompt that will ask us for our commit details, basically a message that we want to leave to others recording the changes that we made. In the prompt, go ahead and write "My first commit".

If the prompt is vi you may need to hit the `i` key before you can type.

```
Added hello.py file.
```

If you're in vi, hit escape and then type `:wq` which stands for `write quit` and that will write the changes, making them permanent.

We'll get some feedback telling us something like

```
[master (root-commit) 1e73b2f] test
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 hello.py
```

Now we've permanently saved this version of hello.py to our history. One cool thing about git is that you can choose to commit whole files or just lines in files to the history, for the most part individual files are granular enough but it's a good feature to be aware of.

Now all that remains is our ignore file. This is an example of a file that we don't want to track changes to, even if it changes. This may be a file with some notes in it that you don't need to track officially, even if they change. Git can be ordered to ignore certain files or folders and this is done with a plain text file called a `.gitignore` file.

Let's go ahead and create that with the command line.

`touch .gitignore`

Now typically files that start with . are hidden on unix systems, so you may not see this show up in your folder view. However we can edit it all the same, we're going to edit is with the `echo` command from the command line.

Go ahead and run:

```sh
echo "ignore_me.txt" >> .gitignore
```

This will append the quoted text "ignore_me.txt" to our `.gitignore` file. Now when we run

```sh
git status
```

We'll see:

```
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)

	.gitignore

nothing added to commit but untracked files present (use "git add" to track)
```

Our ignore file has disappeared! This is because git reads the .gitignore file and ignores any file names or folder names that it finds in there. Nifty huh! However we now need to add our .gitignore file so that git can keep track of the files that we want to ignore.

Let's do that now.

```sh
git add .gitignore
```

Feel free to run git status to see how it has moved to staging. At this point we're going to commit that change. We can do that with the short hand `-m` flag.

```sh
git commit -m "Added gitignore"
```

You'll notice that I used the `-m` flag, this means that we're going to just append the message as a text string right after. This greatly simplifies the way in which you can add messages. However if you're writing a longer one, the `git commit` command allows you to do so easily.

Now you've learned the basics of git on your local machine! This has taught you a lot about running a local git repository. Of course there's plenty more to learn but that's all we need to start with!

*References:*

- [Git Website](http://git-scm.com/)
- [Git Cheatsheet](http://jonas.nitro.dk/git/quick-reference.html)
- [Better Explained](http://betterexplained.com/articles/a-visual-guide-to-version-control/)
