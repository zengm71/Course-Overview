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
$ git checkout -b feature_test
Switched to a new branch 'feature_test'
```

We can see here that we've now switched to a new branch. the `-b` flag means that we want to checkout a new branch that we called feature_test. Now let's make some changes. It's important to remember that this branch is completely seperate from our other branches, any code, changes, modifications to this branch are completely isolated from the other branches. Go ahead and open up `hello_world.txt` in your favorite editor. We'll add in the text:
****

Hello Git!

Now that we've added Hello Git, we can try adding other changes to this file. Imagine that you're working on a feature or changing your machine learning model a little bit, but you're not sure if it's going to improve the system or you don't want to disrupt the code you have in place.

A branch is how you do that.

****

After reviewing your code and doing some tests, you discover that this actually works quite well. Be sure to save the file. Now let's go ahead and commit the changes to the current branch that we're working on. Note that we are on the feature_test branch.

```sh
$ git status
On branch feature_test
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   hello_world.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

Now we add it and commit it.

```sh
$ git add hello_world.txt                                                                
$ git commit -m "Great new feature"                                                     
[feature_test 53c3a1a] Great new feature
 1 file changed, 5 insertions(+)
```

The pattern of status, adding, and committing is extremely common. You'll find yourself doing this all the time. Now that we've committed it, let's checkout our status now. We're still in the feature_test branch.

```sh
$ git status                                                                              
On branch feature_test
nothing to commit, working directory clean
```

But we can also run another command to see what other branches that we have.

```sh
$ git branch                                                                              
* feature_test
  master
```

We can see that we have a master branch as well as our feature_test branch. Now our new feature is really great, so let's go ahead and merge it back into the master branch. This is a formalized way of integrating one branch into another one. First what we'll want to do is checkout the master branch.

```sh
$ git checkout master
Switched to branch 'master'
```

Now we're back on the master branch if we run

```sh
$ cat hello_world.txt
Hello Git!
```

We'll see our unmodified version of hello_world.txt (the one without the feature that we added). Now let's go ahead and merge the two branches.

```sh
$ git merge feature_test                                                                        
Updating 4407308..53c3a1a
Fast-forward
 hello_world.txt | 5 +++++
 1 file changed, 5 insertions(+)
```

Your actual insertions may vary but that's not important. What's important is that we just took a branch that we were working on completely seperately from another one and merged it into another one! This comes up all the time on projects when large or small teams are working on lots of different features, each that has their own branch. Eventually it will come time to merge the branches together and they follow this exact same process.

Now that we've got some files that we're proud of, let's go ahead and commit them to a repository on Github!

*There are going to be all kinds of issues here with authentication... not sure how we'll handle this in class.*

#Github and git Collaboration

*References:*

- [Git Website](http://git-scm.com/)
- [Git Cheatsheet](http://jonas.nitro.dk/git/quick-reference.html)
- [Better Explained](http://betterexplained.com/articles/a-visual-guide-to-version-control/)