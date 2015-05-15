Introduction to git and Source Control Management Systems
===

####What you need to know to be effective


#What is Source Control?

Source control management or version control is a system for organizing different versions of basically anything although it is particularly popular in the software development industry. Distributed source control management is a process by which companies and individuals manage documents (and versions of documents) and share them among various computers and people.

Some popular version control systems are:
- Git
- SVN (Subversion)
- Mercurial

This course as well as your courses at UC Berkeley will likely take advantage of source control systems and it's an integral thing to understand in the software industry. We will be focusing on using the git system as it is the most widespread tool in use today.


#What problem does source/version control solve?

You've likely set up your own basic version control system in the past. Maybe you've organized a project by doing something like

- `school_paper.doc`
- `school_paperv1.doc`
- `school_paperv2.doc`
- `school_paperv2FINAL.doc`

However as I'm sure you've discovered this can get pretty unwieldy pretty fast as you start naming files with longer names or more detailed dates. Imagine when you start sharing these files with other people as well. How do they know which one is truly the final version? What if they organize from v3 down to v1?

Enter the version control system, a consistent, organized way to control versions of files. Systems like git provide a formalized vocabulary and a set of actions that you can perform in order to keep your files properly versioned and others can contribute as well!

Now that we've explained the problem set that way - let's read a little bit more about get and getting started with verison control by defining more specifically the differences between local, centralized, and distributed version control systems.

Think of it this way, a version control system is like Dropbox or Google Drive. You've got a copy of a file on your computer, you've got a copy on Google's Servers and a copy on a friend's computer if it's a shared folder. Rather than syncing being automatic, you have to specify exactly what happens and when. If I want to send a file to the Github server, I've got to `git push origin master` the file. Unlike Dropbox or Google Drive which assumes that it knows what you want it to do, version control is much more precise - you are in control every step of the way.

Read the [version control introduction](http://git-scm.com/book/en/v2/Getting-Started-About-Version-Control) on the git-scm website to get a more precise definition of version control. That will also gives us exact definitions of local, centralized, and distributed version control systems.

Now that we've gotten those definitions, let's learn some of the vocabulary and basic commands.

#The Vocabulary
*Work in progress...*

####Nouns:

- Repository (repo)
	- A repository is a copy of a project. It can either be on your local computer or on a server.
- Branch
	- Is an offshoot of a project or a version of the project. *needs to be more precise*
- Master Branch/Trunk
	- A master branch is the core tree trunk of your project, you can branch off of the trunk but it is the core branch in the project.
- Staging
	- The staging area is one where you prepare and review to make a commit to a repository. It's where you might run tests to make sure that the code you are committing is valid.
- Remote Repo
	- The remote repository is a version of the project on a remote computer.
- Local Repo
	- A local repository is one on a particular machine typically your own.

####Verbs:

- Fork
	- To create a new master branch in your personal remote repository.
- Pull
	- Pulls a remote branch down to your local repository.
- Branch
	- Creates a local copy of the current branch.
- Merge
	- Merges a branch into another branch.
- Push
	- Pushes a local branch to a remote repository.
- Pull Request
	-
- Commit
	- Commits a files/lines in files in the staging environment to the current branch in the repository.
- Checkout
	- Checks out a file or a commit **something...**
- Clone
	- Copies a remote repository to the local environment



#Getting Setup & Your First Repository

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

This creates a folder labelled `.git` in the current directory. **NEVER EDIT THIS FOLDER MANUALLY** as you'll get yourself in all kinds of trouble.

Now that we've created that folder, let's create some files to keep track of.

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

print("I'm also learning git.")

```

Let's go ahead and make sure that it works. We can do that by executing the python file from the command line. Go ahead and run

```sh
python hello.py # to execute it with python3 run python3 hello.py
```

Now return back to the command line and let's commit those changes. first we'll run:

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

So at this point we've got our base git repository with no files being tracked. In order for git to track changes, we've got to add a file to it or tell it to track a specific file. We do that with `git add FILENAME`. You can also add folders instead of specific files.

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

Now our `hello.py` file is `staged` to be committed. Git hasn't started tracking the file changes - it just know that we're preparing to commit that file to our formal history.

Now let's do just that, commit it to the formal history. We can do that with:

```sh
git commit
```

This will bring up a prompt that will ask us for our commit details, basically a message that we want to leave to others recording the changes that we made. In the prompt, go ahead and write. If the prompt is vim you may need to hit the `i` key before you can type.

```
Added hello.py file.
```

If you're in vim, hit escape and then type `:wq` which stands for `write quit` and that will write the changes, making them permanent.

We'll get some feedback telling us something like

```
[master (root-commit) 1e73b2f] test
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 hello.py
```

Now we've permanently saved this version of hello.py to our history. One cool thing about git is that you can choose to commit whole files or just lines in files to the history, for the most part individual files are granular enough but it's a good feature to be aware of.

Now all that remains is our ignore file, one that we don't want to track changes to - even if it changes. Git can be ordered to ignore certain files or folders and this is done with a plain text file called a `.gitignore` file.

Let's go ahead and create that with the command line.

`touch .gitignore`

Now typically files that start with . are hidden on unix systems, so you may not see this show up in your folder view on the Desktop. We'll go ahead and edit it from the command line. Go ahead and run:

```sh
echo "ignore_me.txt" >> .gitignore
```

This will append the file name to our `.gitignore` file. Now when we run

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

Our ignore file has disappeared! This is because git reads the .gitignore file and ignores any file names or folder names that it finds in there. Nifty huh! However we now need to add our .gitignore file. Let's do that now.

```sh
git add .gitignore
```

Feel free to run git status but at this point we're going to commit that change. We can do that with the short hand `-m` flag.

```sh
git commit -m "Added gitignore"
```

You'll notice that I used the `-m` flag, this means that we're going to just append the message as a text string right after. This greatly simplifies the way in which you can add messages. However if you're writing a longer one, the `git commit` command allows you to do so easily.

Now you've learned the basics of git on your local machine! This has taught you a lot about running a local git repository. Of course there's plenty more to learn but that's all we need to start with!

That concludes our first git lesson.

*References:*

- [Git Website](http://git-scm.com/)
- [Git Cheatsheet](http://jonas.nitro.dk/git/quick-reference.html)
- [Better Explained](http://betterexplained.com/articles/a-visual-guide-to-version-control/)