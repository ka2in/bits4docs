.. meta::
   :keywords: ftp, api, networks, protocols

FTP vs. API – differences in terms of data transmission
-------------------------------------------------------

Users can choose either to send their data to an FTP server or via an API. These two connectivity options have different implications in terms of security, access possibilities, and customer experience.

.. figure:: network-ftp.svg
   :alt: FTP vs. API
   :width: 1054.24231px
   :height: 693.25610px
   :scale: 50%
   :align: center

FTP – an old, well-established protocol
---------------------------------------

FTP (*File Transfer Protocol*) uses a client/server model to allow users to move files between a local machine (*client*) and a remote host (*server*). FTP is an easy and convenient method to download and upload large data volumes.

One particular aspect of FTP is that it relies on "two" logical TCP connections to ensure communication between the client and the server: 

* **Control connection:** This primary communication channel ensures the transmission of control traffic over port 21 and remains active during the entire FTP session. Control traffic includes FTP commands and replies. 

* **Data connection:** Whenever you need to transfer files between a client and a remote server or vice versa, FTP will initiate this TCP connection to ensure data transmission over port 20. Unlike the control connection, a data connection does not remain active during the entire FTP session and ends immediately after the file transfer.

FTP uses a simple authentication mechanism that consists in using a "user name" and a "password". The client sends the authentication data to the remote server using the FTP commands: ``USER`` and ``PASS``.

the FTP standard defines three main categories of FTP commands:

- ``Access Control Commands``
- ``Transfer Parameter Commands``
- ``FTP Service Commands`` 

The following tables provide an overview of the different commands within each category:

.. role::  raw-html(raw)
    :format: html


.. table::
   :class: tight-table

   +--------------------------------------------------------------------------------------+
   | **Access Control Commands**                                                          |
   +===========+============+====+========================================================+
   | ``USER``  | *User Name*     | User identification to access the server's file system |
   +-----------+-----------------+--------------------------------------------------------+
   | ``PASS``  | *Password*      | Command that follows the ``USER`` command immediately  |
   +-----------+-----------------+-----------------------------+--------------------------+
   | ``ACCT``  | *Account*       | For login purposes or tasks requiring specific access  |
   +-----------+-----------------+--------------------------------------------------------+
   | ``CWD``   | *Change Working*| Store or retrieve files on a different directory       |
   |           | *Directory*     | without modifying login or account information         |
   +-----------+-----------------+--------------------------------------------------------+
   | ``CDUP``  | *Change*        | Transfer directory trees between operating systems     |
   |           | *Directory Up*  | that use different syntaxes to name the parent         |
   |           |                 | directory                                              |   
   +-----------+-----------------++-------------------------------------------------------+
   | ``SMNT``  | *Structure Mount*| Mount a different file system data structure without  | 
   |           |                  | modifying the login or accounting information         |
   +-----------+------------------+-------------------------------------------------------+
   | ``REIN``  | *Reinitialize*   | Reset parameters to the default settings and flush    |
   |           |                  | account information and all Input/Output              |
   +-----------+------------------+-------------------------------------------------------+
   | ``QUIT``  | *Logout*         | Terminate USER session and close control connection   |
   +-----------+------------------+-------------------------------------------------------+

.. table::
   :class: tight-table

   +------------------------+------------+----------+-------------------------------+
   | **Transfer Parameter Commands**                                                |
   +===========+=================+=======+==========+===============================+
   | ``PORT``  | *Data Port*     | Specify port number to use for data connection   |
   +-----------+-----------------+--------------------------------------------------+
   | ``PASV``  | *Passive*       | Request the Server Data Transfer Process to      | 
   |           |                 | *listen* on a non-default data port              |
   +-----------+-----------------+----+---------------------------------------------+
   | ``TYPE``  | *Representation*| Inform the server about the data type of         |
   |           | *Type*          | files that are transferred by the client         |
   +-----------+-----------------+--------------------------------------------------+
   | ``STRU``  | *File Structure*| Specify the data structure for the file          |
   |           |                 | (``File``, ``Record``, or ``Page``)              |
   +-----------+-----------------+--------------------------------------------------+
   | ``MODE``  | *Transfer Mode* | Specify the transmission mode to use             |
   |           |                 | (``Stream``, ```Block``, or ``Compressed``)`     |
   +-----------+-----------------+--------------------------------------------------+
   
.. table::
   :class: tight-table

   +------------------------+------------+----------+-------------------------------+
   | **FTP Service Commands**                                                       |
   +===========+============+====+=======+==========+===============================+
   | ``RETR``  | *Retrieve*      | Transfer a file from the server to the client    |
   +-----------+-----------------+--------------------------------------------------+
   | ``STOR``  | *Store*         | Store data as a file on the server               |
   +-----------+-----------------+--------------------------------------------------+
   | ``STOU``  | *Store Unique*  | Similar to ``STOR``, but the file must have a    |
   |           |                 | unique name inside the current directory         |
   +-----------+-----------------+--------------------------------------------------+
   | ``APPE``  | *Append*        | If a file with same name already exists on the   |
   |           |                 | server, the data is appended to the existing file|
   +-----------+-----------------+--------------------------------------------------+
   | ``ALLO``  | *Allocate*      | Make sure that sufficient storage is available on|
   |           |                 | the server before data transmission              |
   +-----------+-----------------++-------------------------------------------------+
   | ``REST``  | *Restart*       | Restart file transfer at a specific server marker|
   +-----------+-----------------+--------------------------------------------------+
   | ``RNFR``  | *Rename From*   | Specify the old name of the file to be renamed.  |
   |           |                 | Must be followed by the ``RNTO`` command         |
   +-----------+-----------------+--------------------------------------------------+
   | ``RNTO``  | *Rename To*     | Specify the new name of the file to be renamed.  |
   +-----------+-----------------+--------------------------------------------------+
   | ``ABOR``  | *Abort*         | Instruct the server to abort the last FTP command| 
   |           |                 | and any associated data transfer                 |
   +-----------+-----------------+--------------------------------------------------+
   | ``DELE``  | *Delete*        | Remove the specified file from the server        |
   +-----------+-----------------+--------------------------------------------------+
   | ``RMD``   | *Remove*        | Remove the specified directory from the server   |
   |           | *Directory*     |                                                  |
   +-----------+-----------------+--------------------------------------------------+
   | ``MKD``   | *Make Directory*| Create a directory                               |
   +-----------+-----------------+--------------------------------------------------+
   | ``PWD``   | *Print Working* | Display the current working directory on the     |
   |           | *Directory*     | server                                           |
   |           |                 |                                                  |
   +-----------+-----------------+--------------------------------------------------+
   | ``LIST``  | *List*          | Instruct the server to send a list of the content|
   |           |                 | available in the current directory               |
   +-----------+-----------------+--------------------------------------------------+
   | ``NLST``  | *Name List*     | Similar to ``LIST``, but only sends a directory  |
   |           |                 | listing                                          |
   +-----------+-----------------+--------------------------------------------------+
   | ``SITE``  | *Site*          | Server-side commands to use specific functions   | 
   |           | *Parameters*    | that are required for data transfer              |
   +-----------+-----------------+--------------------------------------------------+
   | ``SYST``  | *System*        | Instruct the server to send information about its|
   |           |                 | operating system                                 |
   +-----------+-----------------+--------------------------------------------------+
   | ``STAT``  | *Status*        | Instruct the server to indicate the status of a  |
   |           |                 | file or the ongoing data transfer                |
   +-----------+-----------------+--------------------------------------------------+
   | ``HELP``  | *Help*          | Prompt the server to send help information that  |
   |           |                 | shows how to use the server                      |
   +-----------+-----------------+--------------------------------------------------+
   | ``NOOP``  | *No Operation*  | Prompt the server to send an OK reply but does   |
   |           |                 | not impact the previously entered commands       |
   +-----------+-----------------+--------------------------------------------------+

For a more detailed description, please refer to The FTP specification `RFC959 <https://www.w3.org/Protocols/rfc959/4_FileTransfer.html>`_. 

FTP and security
----------------

Data transmission with the basic FTP protocol is insecure because it is unencrypted. For a secure data transfer, you need to use FTPS (*FTP over SSL*) or SFTP (*SSH File Transfer Protocol*). Unlike FTPS, which requires opening multiple ports for data transmission, SFTP only needs a single port number to transfer the data. Therefore, SFTP is more suitable for firewall security. 

While FTP is convenient for large data transfers, its performance in terms of access possibilities and customer experience remains rather limited. For instance, FTP does not allow you to share resources in real-time between multiple systems, nor does it give you the ability to process data on remote systems.

API – more access options for a better customer experience
----------------------------------------------------------

An API (*Application Programming Interface*) is an interface that serves as a bridge between two or more applications. The server-side components encapsulate the business logic and make it available to multiple clients through the API. 

To ensure a secure data transmission, companies can use the HTTPS protocol in conjunction with different encryption methods. 
Besides providing real-time data access to the linked systems, an API integration allows clients to manage and process data by sending requests to the appropriate endpoints. 

In the context of HTTP based architectures, clients use ``URIs`` and ``HTTP verbs`` (or methods) to create, request, modify, or delete ``resources`` on a server. A URI (Unique Resource Identifier) allows clients to unequivocally identify a resource that is located on a server. A resource can be anything that is stored on a sever, e.g.:

- an employee list in CSV format
- a customer database in SQL format 
- or a presentation file in ODP format

The commonly used version of HTTP, i.e. HTTP/1.1, defines eight verbs as the table below shows:

.. list-table::
   :widths: 25 75
   :class: tight-table

   * - **HTTP Verb/Method**
     - **Purpose**
   * - GET
     - Request a resource
   * - HEAD
     - Similar to GET, but only provides the HTTP header, and not the entire resource 
   * - POST
     - Generate a resource with a unique ID that is assigned by the server
   * - PUT
     - Create or replace a resource. The client specifies the resource ID through the URI
   * - PATCH
     - Partially update a resource that is accessed through its URI
   * - DELETE
     - Remove a resource that is identified by its URI
   * - CONNECT
     - Establish an end-to-end tunnel connection through a proxy server
   * - OPTIONS
     - Retrieve information about the available communication options for a given resource

APIs offer more advantages over FTP, but they require a higher investment of time and technical expertise.