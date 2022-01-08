.. meta::
   :description: Compression and Metadata Removal - how to compress and remove metadata from PDF and image files
   :keywords: compression, metadata, privacy, image, pdf

Compression & Metadata Removal
================================

.. figure:: Data-Mike-Haynes-mini.jpeg
   :alt: Git logo
   :scale: 50%
   :align: center

   Picture by Mike Haynes under `CC0 1.0 License <https://creativecommons.org/publicdomain/zero/1.0/>`_

Compressing from the command line
=================================

There are multiple scenarios where you would need to compress your files, whether it is for a web development project or to send some attachments by email, just to name a few examples. You do not necessarily need to rely on proprietary software products or :abbr:`GUIs (Graphical User Interfaces)` to achieve these tasks, especially if your are a Linux user. 

In fact, Linux has many command line tools that allow you to compress your PDF and image files easily. My favorite open source tools for the compression of PDF and image files are ``ps2pdf`` and ``jpegoptim``, respectively.  

PDF compression with ps2pdf
---------------------------

``ps2pdf`` is a PostScript-to-PDF converter that uses ``ghostscript`` to convert a PDF into a PostScript file before converting it back again. This process allows you to compress your initial PDF file. According to its man page, ``ps2pdf`` provides nearly all the features that you would find in Adobe's Acrobat |reg| product, Distiller |reg|.   

Installation on Linux
---------------------

To install ``ps2pdf`` with all the required dependencies, you need to install ``ghostscript``. 

On Debian based distros, run the following commands:

.. code-block:: console
   
   $ sudo apt-get update
   $ sudo apt install ghostscript

For Red Hat based distros, use the following commands:

.. code-block:: console

   $ sudo dnf update
   $ sudo dnf install ghostscript

ps2pdf commands
---------------

To compress a file without any additional options, type the following command:     

.. code-block:: console

   $ ps2pdf  [options...] {input.[e]ps|-} [output.pdf|-]

Note that ``ps2pdf`` uses the same options as ``ghostscript``. 

Depending on your work scenario, you can achieve the best results in terms of file compression and image quality by using the option ``-dPDFSETTINGS=/ebook``:

.. code-block:: console

   $ ps2pdf -dPDFSETTINGS=/ebook input.pdf output.pdf

Metadata and privacy implications
=================================

Metadata reveal more about you than you might imagine. Here is an example of the metadata that were extracted from an image file taken by a conventional smartphone: ``Image Type`` ``Width`` ``Height`` ``Exposure Time`` ``Aperture Value`` ``ISO Speed Rating`` ``Flash Fired`` ``Metering Mode`` ``Exposure Program`` ``Focal Length`` ``Software`` ``Camera Brand`` ``Camera Model`` ``Date Taken``.

With this information at hand, malicious users can easily search for the the most recent vulnerabilities associated with your device and craft a custom payload. Therefore, it is always good practice to remove metadata from your files before handing them over. 

Metadata removal with mat2
---------------------------

``mat2`` is a metadata anonymisation toolkit that runs from the command line. ``mat2`` allows you to remove metadata from a wide range of file formats, including archive, image, office, audio, video and PDF files.  

To install ``mat2`` on Debian based distros, run the following commands:

.. code-block:: console
   
   $ sudo apt-get update
   $ sudo apt install mat2

For Red Hat based distros, use the following commands:

.. code-block:: console

   $ sudo dnf update
   $ sudo dnf install mat2

mat2 does not overwrite the source file. Instead, it will generate a new output file that contains the word *cleaned* between the filename and the file extension. So, if you run the command: 

.. code-block:: console

   $ mat2 foo.pdf

Then mat2 will generate a new file called *foo.cleaned.pdf*.

PDF forensics and safety measures
---------------------------------

As a general rule of thumb, you should never, ever open PDF files in a productive environment, even if you receive such files from people you trust. The reason for this is pretty obvious, since the persons you trust may themselves not be aware of the presence of an embedded payload in the PDF file. 

For PDF files that do not contain any sensitive information, you can run a check on `VirusTotal <https://www.virustotal.com/>`_. Beware though, that hackers also run a preliminary test on VirusTotal to make sure that their malicious payloads will not be flagged.  

For an in-depth analysis, it is recommended to use forensic tools such as ``pdfid.py`` in combination with the PDF parser ``pdf-parser.py`` from `Didier Stevens <https://blog.didierstevens.com/programs/pdf-tools/>`_. 

.. note::

   Even when using your tools of choice to analyze suspicious PDF files, you should always perform your analysis on a virtual environment or in a sandbox, with no connection to any other devices or a network. Remember, never run these tests on a productive environment!


As a safety measure, check also if your PDF reader supports JavaScript by default and disable it. There are multiple open-source PDF readers that do not render JavaScript at all.




.. |reg| unicode:: U+000AE .. REGISTERED SIGN