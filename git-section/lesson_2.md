Introduction to git and Source Control Management Systems
===

####What you need to know to be effective


#Branching

At this point we've introduced git and created our first git repository. We've committed some files, we've ignored some files. We've really moved through all the basic parts for individual git management. However things change when we want to make complex changes or work with others.

Imagine that you want to try out a new version or formatting of the documents/code that you're tracking in your github repository, but you're not sure if it will work or not. This is an ideal situation for a branch which sounds just like it is - it's a branch of your code that doesn't interfere with the other branches.

You've seen that we are on a specific branch when we've run `git status` in the past. Go ahead and run it in our repository again and you'll see what I mean.

```sh
$ git status
On branch master
nothing to commit, working directory clean
```

We can see that we are on the master branch which is typically the main branch or the "trunk" of your (and most everyone's) repositories. Now since we want to start off with a feature that we're not sure will be any good, let's go ahead and create a new branch.

```sh
$ git checkout -b super_cool_feature
Switched to a new branch 'super_cool_feature'
```

We can see here that we've now switched to a new branch. the `-b` flag means that we want to checkout a new branch that we called super_cool_feature. Now let's make some changes. It's important to remember that this branch is completely seperate from our other branches, any code, changes, modifications to this branch are completely isolated from the other branches. 

Go ahead and open up `hello.py` in your favorite editor and let's make things a bit more complicated. Instead of just having it print some simple statements, let's make it a bit more interactive. Erase what we have and let's put it.

```py

import sys

print(sys.argv)
```

This file is pretty straight forward and once we run it you should be able to see what this is doing.

The `sys` package is imported, meaning that we can use some of the tools that it provides. We take advantage of the `argv` part of the `sys` module using the dot syntax. Argv is a list, and we'll see of what as soon as we run.

```py
python3 hello.py
# Should print ['hello.py']
```

```py
python3 hello.py world
# Should print ['hello.py', 'world']
```

Are you getting a sense for what the `argv` does? 

It gives us access to the arguments sent to `python3` in a list format! Now let's show the real power of what we just did!

```sh
python3 hello.py "I'm learning python!"
# Should print ['hello.py', 'I'm learning python!']
```

Now we don't need to explicitly write our messages like we did in the master branch, we can just pass them in as arguments to our program.

Now let's go ahead and commit the changes to the current branch that we're working on. Note that we are on the super_cool_feature branch.

```sh
$ git status
On branch super_cool_feature
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   hello.py

no changes added to commit (use "git add" and/or "git commit -a")
```

Now we add it and commit it.

```sh
$ git add hello.py                                                                
$ git commit -m "Now parses command line arguments"                                                     
[super_cool_feature 53c3a1a] Now parses command line arguments
 1 file changed, 5 insertions(+)
```

The pattern of status, adding, and committing is extremely common. You'll find yourself doing this all the time. Now that we've committed it, let's checkout our status now. We're still in the super_cool_feature branch.

```sh
$ git status                                                                              
On branch super_cool_feature
nothing to commit, working directory clean
```

But we can also run another command to see what other branches that we have.

```sh
$ git branch                                                                              
* super_cool_feature
  master
```

We can see that we have a master branch as well as our super_cool_feature branch. Now our new feature is really great, so let's go ahead and merge it back into the master branch. This is a formalized way of integrating one branch into another one. First what we'll want to do is checkout the master branch.

```sh
$ git checkout master
Switched to branch 'master'
```

Now we're back on the master branch if we run

```sh
$ python3 hello.py
```

We'll see our unmodified version of hello.py (the one without the feature that we added). Now let's go ahead and merge the two branches.



```sh
$ git merge super_cool_feature                                                                        
Updating 4407308..53c3a1a
Fast-forward
 hello.py | 5 +++++
 1 file changed, 5 insertions(+)
```

```sh
python3 hello.py "This is my brand new feature that I just merged."
# Should print ['hello.py', 'This is my brand new feature that I just merged.']
```

*Your output may vary slightly but the general format should be the same.*

We just took a branch that we were working on completely seperately from another one and merged it into another one! This format comes up all the time on projects when large or small teams are working on lots of different features, each that has their own branch. Eventually it will come time to merge the branches into another branch.

Now that we've got some files that we're proud of, let's go ahead and commit them to a repository on Github!

*There are going to be all kinds of issues here with authentication... not sure how we'll handle this in class.*

*References:*

- [Git Website](http://git-scm.com/)
- [Git Cheatsheet](http://jonas.nitro.dk/git/quick-reference.html)
- [Better Explained](http://betterexplained.com/articles/a-visual-guide-to-version-control/)