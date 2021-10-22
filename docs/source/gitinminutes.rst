.. meta::
   :description: Git in 30 minutes - get to know the basic Git commands to perform the most essential tasks
   :keywords: Git, commands, repository, versioning, documentation

#################
Git in 30 minutes
#################

Short introduction
==================

Git is a :abbr:`VCS (Version Control System)`. Basically, a version control system allows you to trace back all the changes that you have made to your project. Git was initially introduced in the Linux community as a revision control system for kernel development. 

Unlike centralized version control systems such as Subversion and CVS, Git is a fast distributed system. With Git, you do not need a single central repository to work on your project, since you can work locally on a full clone of the remote repository. What is beautiful about Git is that you can also use it to automate your documentation process.  

Git states
==========

In a Git workflow, your files will basically go through 3 different states:

* Modified: this is when you make changes to the files in your working directory; 
* Staged: in this intermediate state, Git saves snapshots of the modified files in the staging area;
* Committed: once you commit your changes, Git will save the staged files in the Git directory. 

The Git directory is a hidden folder ``.git`` at the top level of your working tree.

Installing Git
==============

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

Git Basic commands
==================

Here are the most essential commands that will get you up and running within minutes.

If you already have a project, you can immediately navigate to the relevant folder, then initialize an empty repository with the command:

.. code-block:: console

   $ git init

To add all the available files in your directory to Git, type the command:

.. code-block:: console
   
   $ git add -A

You can achieve the same result with the following command:

.. code-block:: console

   $ git add .

Either way, the files existing in your project's folder will be added recursively to Git's index.

