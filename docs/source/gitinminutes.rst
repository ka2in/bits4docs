.. meta::
   :description: Git in 30 minutes - get to know the basic Git commands to perform the most essential tasks
   :keywords: Git, commands, repository, versioning, documentation


Git Primer for the Impatient
----------------------------

.. image:: git-tutorial.png
   :alt: Git logo
   :scale: 50%
   :align: center

Short introduction
==================

Git is a :abbr:`VCS (Version Control System)`. Basically, a version control system allows you to perform a number of essential tasks, including:

* creating a copy of the original project 
* tracking all the changes that you have made to the project
* keeping track of previous versions of the project
* marking milestones during the development cycle 

Git was initially introduced in the Linux community as a revision control system for kernel development. Unlike centralized version control systems such as Subversion and CVS, Git is a fast distributed system. 

With Git, you do not need a single central repository to work on your project, since you can work locally on a full clone of the remote repository. What is beautiful about Git is that you can also use it to automate your documentation process.  

Git states
==========

In a Git workflow, your files will basically go through 3 different states:

* Modified: This is when you make changes to the files in your working directory. 
* Staged: In this intermediate state, Git saves snapshots of the modified files in the staging area.
* Committed: Once you commit your changes, Git will save the staged files in the Git directory. 

The Git directory is a hidden folder ``.git`` at the top level of your working tree.

Installation on Linux
=====================

To install Git on Debian based distros, run the following commands:

.. code-block:: console
   
   $ sudo apt-get update
   $ sudo apt install git-all

For Red Hat based distros, use the following commands:

.. code-block:: console

   $ sudo dnf update
   $ sudo dnf install git-all

Initial configuration
=====================

Git ships with a tool called ``git config`` that allows you to set multiple configuration variables. These variables control how Git looks and behaves. 

Depending on your system, the configuration variables will be stored at different locations. For further details about the topic, check Git's official documentation: `Getting Started - First-Time Git Setup <https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup>`_.

Once you have installed Git, you should set your credentials by indicating your **user name** and **email**. To do so, type the following commands:    

.. code-block:: console

   $ git config --global user.name "Random User"
   $ git config --global user.email randomuser@test.com

To check all your personal settings, type the following command:

.. code-block:: console

   $  git config --list

Git essential commands
----------------------

Here are the most essential commands that will get you up and running within minutes.

Initializing a new repository
=============================

If you already have a project, you can immediately navigate to the relevant folder, then initialize an empty repository with the command:

.. code-block:: console

   $ git init

Cloning an existing repository
==============================

To clone an existing repository, type the command:

.. code-block:: console

   $ git clone <URL>

For instance, if we want to clone the documentation repository from the collaboration platform *Codeberg*, then we will type the following command:

.. code-block:: console

   $ git clone https://codeberg.org/Codeberg/Documentation.git


Adding files
============

Git will not begin tracking your files unless you add them. To add all the files that are available in your directory to Git, type the command:

.. code-block:: console
   
   $ git add -A

You can achieve the same result with the following command:

.. code-block:: console

   $ git add .

Either way, the files existing in your project's folder will be added recursively to Git's index.

To add a single file called 'foo', type the command:

.. code-block:: console

   $ git add foo

Committing changes
==================

To commit your changes with a message, type the command:

.. code-block:: console

   $ git commit -m "Initial commit for Git's documentation project"

.. note::

   If you do not insert a commit message at the time of committing your files, i.e. if you only type ``git commit``, Git will launch the default text editor that is set in your environment variables.

Checking the status
=================== 

If you want to check the status of the project's files, type the command:

.. code-block:: console

   $ git status

You will then get something like this:

.. code-block:: console

   On branch maindoc
   Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
   modified:   build/doctrees/environment.pickle
   modified:   build/doctrees/gitcommands.doctree
   modified:   build/doctrees/index.doctree
   modified:   build/html/_sources/gitcommands.rst.txt
   modified:   build/html/_static/pygments.css
   modified:   build/html/gitcommands.html
   modified:   build/html/index.html
   modified:   build/html/objects.inv
   modified:   build/html/searchindex.js
   modified:   source/conf.py
   modified:   source/gitcommands.rst

The command ``git status`` provides the default description. To get a verbose description, type the following command:

.. code-block:: console

   $ git status -v


If you prefer a shorter description, type the command:

.. code-block:: console

   $ git status -s

This will you give you the following result:

.. code-block:: console

   M build/doctrees/environment.pickle
   M build/doctrees/gitcommands.doctree
   M build/doctrees/index.doctree
   M build/html/_sources/gitcommands.rst.txt
   M build/html/_static/pygments.css
   M build/html/gitcommands.html
   M build/html/index.html
   M build/html/objects.inv
   M build/html/searchindex.js
   M source/conf.py
   M source/gitcommands.rst

In the example above, The letter **M** at the beginning of each line means ``Modified``.

Comparing with 'diff'
=====================

To compare your local index with the repository, type the following command:

.. code-block:: console

   $ git diff

You will then get a result similar to this:

.. code-block:: console

   diff --git a/docs/build/doctrees/environment.pickle b/docs/build/doctrees/environment.pickle
   index 76e71d8..ca8948d 100644
   Binary files a/docs/build/doctrees/environment.pickle and b/docs/build/doctrees/environment.pickle differ
   diff --git a/docs/build/doctrees/gitcommands.doctree b/docs/build/doctrees/gitcommands.doctree
   index b4e2fe0..5821717 100644
   Binary files a/docs/build/doctrees/gitcommands.doctree and b/docs/build/doctrees/gitcommands.doctree differ
   diff --git a/docs/build/doctrees/index.doctree b/docs/build/doctrees/index.doctree
   index dc2937d..d476ecb 100644
   Binary files a/docs/build/doctrees/index.doctree and b/docs/build/doctrees/index.doctree differ
   diff --git a/docs/build/html/_sources/gitcommands.rst.txt b/docs/build/html/_sources/gitcommands.rst.txt
   index 9a17fde..962687d 100644
   --- a/docs/build/html/_sources/gitcommands.rst.txt
   +++ b/docs/build/html/_sources/gitcommands.rst.txt
   @@ -24,8 +24,8 @@ In a Git workflow, your files will basically go through 3 diff


If you want the same result in a table format, add the option ``--stat`` to the initial command ``git status``:

.. code-block:: console

   $ git diff --stat

The command above will display something similar to this:

.. code-block:: console

   docs/build/doctrees/environment.pickle        | Bin 15477 -> 15570 bytes
   docs/build/doctrees/gitcommands.doctree      | Bin 14576 -> 20749 bytes
   docs/build/doctrees/index.doctree             | Bin 9193 -> 8977 bytes
   docs/build/html/_sources/gitcommands.rst.txt |  78 ++++++++++++++++++++++-
   docs/build/html/_static/pygments.css          |   6 +-
   docs/build/html/gitcommands.html             |  86 +++++++++++++++++++++-----
   docs/build/html/index.html                    |   9 ++-
   docs/build/html/objects.inv                   | Bin 402 -> 414 bytes
   docs/build/html/searchindex.js                |   2 +-
   docs/source/conf.py                           |   2 +-
   docs/source/gitcommands.rst                  |  78 ++++++++++++++++++++++-
   11 files changed, 228 insertions(+), 33 deletions(-)

Managing branches
=================

At the beginning of each project, you will have a ``master branch``, also called ``main branch`` in newer terminology.

To view all current branches, type the following command:

.. code-block::

   $ git branch -a

.. raw:: latex

    \newpage

If you want to create a new branch and switch to it, type the command:

.. code-block::

   $ git checkout -b <new-branch>

.. note:: 
   
   The Git command ``checkout`` allows you to switch to a different branch, which then becomes the ``HEAD`` branch. ``HEAD`` is a special pointer that points to the branch you are currently on.

Deleting branches
==================

Each time you want to introduce a fix or a feature, you create a new branch to separate your work from the codebase. Once you deploy your contribution, you can delete that particular branch both locally and remotely. Note that the local and the remote branch are two completely different objects in Git, i.e. deleting a branch locally does not mean that its remote counterpart will be removed, and vice versa.

Deleting branches locally
^^^^^^^^^^^^^^^^^^^^^^^^^

You can delete a local branch with the ``-d`` option. Since you cannot delete the branch you are currently on, you will first have to checkout a different branch:

.. code-block::
   
   git checkout <not-to-be-deleted branch>

   git branch -d <branch-to-delete>

.. note::

   The ``-d`` option only allows you to delete branches that have already been pushed and merged with their respective remote branches.

To force local deletion **without** prior push and merge, use the ``-D`` option:

.. code-block::

   git branch -D <branch-to-delete>

Deleting branches remotely
^^^^^^^^^^^^^^^^^^^^^^^^^^

To delete a branch on a remote repo, use the ``git push`` command in combination with the ``--delete`` option as shown below:

.. code-block::

   git push <remote> --delete <branch>

Example:

.. code-block::

   git push origin --delete feature/captcha


Forking from a repository
=========================

``Forking`` is the process of creating a completely new copy of a public repository. Forking allows you to work on your own copy of the project before submitting your changes back to the main repository through a ``pull request``.     

Managing remotes
================

Managing your remotes, i.e. remote servers, involves verifying the available remotes, setting a particular remote and removing references to remote branches, among other things.

To set a remote repository, type the command:

.. code-block::

   $ git remote add origin <URL>


.. note:: 
   
   In the context of Git hosting platforms, ``origin`` designates your own fork, while ``upstream`` refers to the original repository that you have forked.

To verify the remote repository, type the command:

.. code-block::

   $ git remote -v

You will then get a result similar to this:

.. code-block::
   
   origin   https://codeberg.org/Codeberg/Documentation.git (fetch)
   origin   https://codeberg.org/Codeberg/Documentation.git (push)

Note that the output contains 2 different terms at the end of each line, which are ``fetch`` and ``push``: ``fetch`` is the action of getting data from the remote repository, while ``push`` means sending data to the remote. 

To fetch data from your remote repository with its entire branches, run the command:

.. code-block::

   $ git fetch <remote>

If you want to fetch a specific branch from the remote repository, run the following command:

.. code-block::

   $ git fetch <remote> <branch>

.. attention:: 

   The ``fetch`` command allows you to download the data to your local repository, but it does **not** alter your local content. If you want to check out the fetched content, you will have to do it manually. Another possibility would be to use the ``git pull`` command, which allows you to fetch the content from the remote server and merge it automatically into your local branch.

.. raw:: latex

    \newpage

If you want to pull a single file from the remote repo, check the current remote repo with the command:

.. code-block::

   $ git remote -v

Once you have confirmed that ``origin`` is the name of your remote, run the following commands:

.. code-block::

   $ git fetch --all
   $ git checkout origin/main -- /path/to/your/file 

To push your local commits to the remote repo, run the following command:

.. code-block::

   $ git push <remote> <branch>

If a branch on your local fork is not synced with the latest commits from its remote counterpart, Git will not allow you to push your changes. This is to prevent you from rewriting the remote history that other contributors may be relying on. The ``--force`` option allows you to force the push in such cases and overwrite the history:

.. code-block::

   $ git push -f <remote> <branch>

You can also achieve the same result by typing the following:

.. code-block::

   git push <remote> <branch> --force

.. attention::

   Proceed with caution when using the ``--force`` option. Rewriting the commit history means that others cannot access the older commit history anymore. Here are some "safer" alternatives:

   * Avoid force pushing commits on repos with a shared history.
   
   * Use ``git revert`` to undo changes from existing commits.

   * Use the command ``git push <remote> <branch> --force-with-lease``. This command will not rewrite any changes made by other team members on the remote repo.  


If you want to set a different repo, type the command:

.. code-block::

   $ git remote set-url origin <URL>

In order to delete references to any remote branches that no longer exist, use the command:

.. code-block::

   $ git remote prune origin

Syncing your fork with upstream
===============================

If you have forked an upstream repo and started working on your local fork, you may notice after a while that your fork is out of sync with upstream. To remedy this situation and sync your fork with the upstream repo, run the following commands:

.. code-block::

   $ git fetch upstream
   $ git checkout main
   $ git merge upstream/main

.. note::

   Use the term ``main`` or ``master`` in your commands according to the default terminology of your Git hosting platform, e.g. Codeberg or GitHub.

Viewing the commit history
==========================

During your project, you may want to go back to a "safe" commit if you encounter some issues at a certain point. There are other reasons why you might need access to the commit history, such as finding out *who* made *what* changes and *why*.

The ``git log`` command allows you to track your project history in a reverse chronological order, i.e. the newest commit appears at the top.

Below is a sample output of the ``git log`` command without any additional flags:

.. code-block::

   $ git log
   commit ad06d9ba80ba723b68b6600600e23bc85af7ff82 (HEAD -> easydocbranch, origin/easydocbranch)
   Author: Faycal Alami-Hassani <anon@yme.com>
   Date:   Thu Feb 17 21:43:38 2022 +0100

   Updating content about metadata

   commit 09ca7947a1935841ea4d76d3fe815ea988ad2c77
   Author: Faycal Alami-Hassani <anon@yme.com>
   Date:   Thu Feb 17 21:31:59 2022 +0100

   Proofreading the Git article

   commit b5ef042c0f907bfebb2c6917b5de1e072a3fd18a
   Author: Faycal Alami-Hassani <anon@yme.com>
   Date:   Thu Feb 17 20:29:28 2022 +0100

   Finished proofreading the article


To get a compact overview of your commit history, you can combine the ``git log`` command with the option ``--oneline``. Each single line will then display the **commit ID** and the **first line** of the commit message, e.g.:

.. code-block::

   $ git log --oneline
   
   fd9e2e4 Updating the table about HTTP verbs
   91137e4 Adding information about HTTP methods and URIs
   3b5f0e8 Adding content about FTP commands
   41f2a36 Updating the article about Git 

.. note:: To get the greatest benefit from your commit history, always follow these two rules:

   1. Keep your commits as small as possible, i.e. each commit should include the smallest possible amount of changes. This ensures a logical organization of your commits and makes it easier to revert single changes.

   2. Provide a good description in your commit message. The commit message should explain precisely what the commit does.

Squashing commits
=================

Squashing is the act of merging multiple commits into a single one. You can squash commits at any time with the *interactive rebase* feature.
For instance, to display the three latest commits, we will type the following command:

.. code-block::

   git rebase -i HEAD~3

.. note::

   In the command above, the ``n`` within ``HEAD~n`` denotes the number of commits you want to go back. In this particular case, the HEAD branch will move three positions back to a previous commit.

You should then get an output similar to this:

.. code-block::

   pick 09ca794 Proofreading the git article
   pick ad06d9b Updating content about metadata
   pick b60f293 Introducing changes to produce PDF with LaTeX and updating article

   # Rebase b5ef042..b60f293 onto b5ef042 (3 commands)
   #
   # Commands:
   # p, pick <commit> = use commit
   # r, reword <commit> = use commit, but edit the commit message
   # e, edit <commit> = use commit, but stop for amending
   # s, squash <commit> = use commit, but meld into previous commit
   # f, fixup [-C | -c] <commit> = like "squash" but keep only the previous
   #                    commit's log message, unless -C is used, in which case
   #                    keep only this commit's message; -c is same as -C but
   #                    opens the editor
   # x, exec <command> = run command (the rest of the line) using shell
   # b, break = stop here (continue rebase later with 'git rebase --continue')
   # d, drop <commit> = remove commit
   # l, label <label> = label current HEAD with a name
   # t, reset <label> = reset HEAD to a label

If you replace **pick** by **squash** in one of the lines above, the line in question will be combined with the one above, e.g.:

.. code-block::

   pick 09ca794 Proofreading the git article
   squash ad06d9b Updating content about metadata
   squash b60f293 Introducing changes to produce PDF with LaTeX and updating article

Once you edit the commit message for the new compact commit, the interactive rebase will complete successfully. You should now have a single commit instead of three.  

Submitting separate pull requests
=================================

You may want to submit a separate pull request for each commit. To do so, you first have to reset your ``main`` repo to sync it with ``upstream``:

.. code-block::

   git checkout main
   git reset --hard upstream/main

The next step consists in creating a new branch for each new commit, then "cherry-picking" the relevant commit. The ``git cherry-pick`` command allows you to re-apply the changes from a previous commit to the current active branch:

.. code-block::

   git checkout -b new-branch
   git cherry-pick 91137e4
   git push --set-upstream origin new-branch
