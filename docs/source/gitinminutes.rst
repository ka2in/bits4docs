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
------------------

Git is a :abbr:`VCS (Version Control System)`. Basically, a version control system allows you to perform a number of essential tasks, including:

* creating a copy of the original project 
* tracking all the changes that you have made to the project
* keeping track of previous versions of the project
* marking milestones during the development cycle 

Git was initially introduced in the Linux community as a revision control system for kernel development. Unlike centralized version control systems such as Subversion and CVS, Git is a fast distributed system. 

With Git, you do not need a single central repository to work on your project, since you can work locally on a full clone of the remote repository. What is beautiful about Git is that you can also use it to automate your documentation process.  

Git states
----------

In a Git workflow, your files will basically go through 3 different states:

* Modified: This is when you make changes to the files in your working directory. 
* Staged: In this intermediate state, Git saves snapshots of the modified files in the staging area.
* Committed: Once you commit your changes, Git will save the staged files in the Git directory. 

The Git directory is a hidden folder ``.git`` at the top level of your working tree.

Installation on Linux
---------------------

To install Git on Debian based distros, run the following commands:

.. code-block:: console
   
   $ sudo apt-get update
   $ sudo apt install git-all

For Red Hat based distros, use the following commands:

.. code-block:: console

   $ sudo dnf update
   $ sudo dnf install git-all

Initial configuration
---------------------

Git ships with a tool called ``git config`` that allows you to set multiple configuration variables. These variables control how Git looks and behaves. 

Depending on your system, the configuration variables will be stored at different locations. For further details about the topic, check Git's official documentation: `Getting Started - First-Time Git Setup <https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup>`_.

Once you have installed Git, you should set your credentials by indicating your **user name** and **email**. To do so, type the following commands:    

.. code-block:: console

   $ git config --global user.name "Random User"
   $ git config --global user.email randomuser@test.com

To check all your personal settings, type the following command:

.. code-block:: console

   $  git config --list

Git basic commands
==================

Here are the most essential commands that will get you up and running within minutes.

Initialize a new repository
---------------------------

If you already have a project, you can immediately navigate to the relevant folder, then initialize an empty repository with the command:

.. code-block:: console

   $ git init

Clone an existing repository
----------------------------

To clone an existing repository, type the command:

.. code-block:: console

   $ git clone <URL>

For instance, if we want to clone the documentation repository from the collaboration platform *Codeberg*, then we will type the following command:

.. code-block:: console

   $ git clone https://codeberg.org/Codeberg/Documentation.git


Add files
---------

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

Commit changes
--------------

To commit your changes with a message, type the command:

.. code-block:: console

   $ git commit -m "Initial commit for Git's documentation project"

.. note::

   If you do not insert a commit message at the time of committing your files, i.e. if you only type ``git commit``, Git will launch the defaut text editor that is set in your environment variables.

Check the status
---------------- 

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

Compare with 'diff'
-------------------

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

Manage branches
---------------

At the beginning of each project, you will have a ``master branch``, also called ``main branch`` in newer terminology.

To view all current branches, type the following command:

.. code-block::

   $ git branch -a 

If you want to create a new branch and switch to it, type the command:

.. code-block::

   $ git checkout -b <new-branch>

.. note:: 
   
   The Git command ``checkout`` allows you to switch to a different branch, which then becomes the ``HEAD`` branch. ``HEAD`` is a special pointer that points to the branch you are currently on.

Fork from a repository
----------------------

``Forking`` is the process of creating a completely new copy of a public repository. Forking allows you to work on your own copy of the project before submitting your changes back to the main repository through a ``pull request``.     

Manage remotes
--------------

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

If you want to pull a single file from the remote repo, check the current remote repo with the command:

.. code-block::

   $ git remote -v

Once you have confirmed that ``origin`` is the name of your remote, run the following commands:

.. code-block::

   $ git fetch --all
   $ git git checkout origin/main -- /path/to/your/file 

To push your local commits to the remote repo, run the following command:

.. code-block::

   $ git push <remote> <branch>


If you want to set a different repo, type the command:

.. code-block::

   $ git remote set-url origin <URL>

In order to delete references to any remote branches that no longer exist, use the command:

.. code-block::

   $ git remote prune origin

Syncing your fork with upstream
-------------------------------

If you have forked an upstream repo and started working on your local fork, you may notice after a while that your fork is out of sync with upstream. To remedy this situation and sync your fork with the upstream repo, run the following commands:

.. code-block::

   $ git fetch upstream
   $ git checkout main
   $ git merge upstream/master

.. note::

   Use the term ``main`` or ``master`` in your commands acording to the default terminology of your Git hosting platform, e.g. Codeberg or GitHub. 