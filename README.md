openshift-postgres-devel-cartridge
==================================

Crunchy Data Solutions - postgres developer tools cartridge


This cartridge is intended to provide a package of postgresql SQL development tools.   A developer can install the Crunchy postgresql RLS database cartridge, then install this Developer cartridge on that application and have access to a variety of postgresql development tools in a private sandbox environment hosted on OpenShift.

##Contents
pgadmin3 - graphical UI for executing SQL commands and debugging postgres procedural language
pgbadger (v 5.0) - log analyzer tool that reads a postgresql database log file, and generates HTML output
ora2pg - Oracle-to-postgres conversion tools
Oracle client libraries
Oracle SQL Plus client libraries


##Setup the OpenShift Postgresql instance


$ rhc app-create devtest -t php-5.3
$ rhc cartridge-add crunchydatasolutions-pg-1.0 --app dev
$ rhc cartridge-add crunchydatasolutions-pgdevel-1.0 --app dev


After this, you will have a postgres (v 9.3.4) deployed with the development tools installed on it.

##Using SQLPlus

The Oracle SQLPlus client has been installed and configured within the Crunchy Developer Cartridge.  The sqlplus binary is included into the PATH variable and the sqlplus libraries are included into the LD_LIBRARY_PATH variable upon installation.  To use the sqlplus command, issue a command similar to the following:

$ sqlplus system/xyz@//192.168.2.4/XE

This command syntax will connect to an Oracle host located on 192.168.2.4, to an Oracle instance named XE, and uses the ID of system and a password of xyz.

##Using pgadmin3

Unfortunately you can’t run pgadmin3 from an OpenShift application due to the way X11 Forwarding is prohibited on OpenShift.  But, the pgadmin3 client is bundled within the Crunchy Developer Cartridge for you to use if your client workstation is a RHEL or CentOS 6.5 operating system.

To use the pgadmin3, you will need to clone the Crunchy Developer Cartridge to your local RHEL 6.5 workstation using the following git command:

$ git clone git@github.com:crunchyds/openshift-postgres-devel-cartridge.git

Then you can execute pgadmin3 with this command:

$ cd openshift-postgres-devel-cartridge
$ unzip ./archives/pgadmin3-build.zip
$ export LD_LIBRARY_PATH=`pwd`/pgadmin3-build/lib
$ ./pgadmin3-build/bin/pgadmin3

In another terminal window, run the following command to start port forwarding to your postgres instance:

$ rhc port-forward -a yourpgapp

At this point, you can connect to your postgres instance, running on your OpenShift application, to your locally running pgadmin3 client.  You will need to look up the postgres user ID using the following command:

$ rhc ssh -a yourpgapp ‘echo $USER’




##Using pgbadger

pgbadger (version 5.0) is installed in the Crunchy Developer Cartridge.  To use it, you will need to issue the following command from within the OpenShift application:

$ pgbadger $OPENSHIFT_PGRLS_DIR/data/pg_log/postgres*.log -o $OPENSHIFT_REPO_DIR/php/pgbadger-report.html

This will generate a report, in this example, that will be served by the installed PHP web server.  If you build your OpenShift with another web framework (e.g. python, Java), you will need to adjust the pgbadger output file location accordingly.



##Using ora2pg

ora2pg is installed in the Crunchy Developer Cartridge.  You will need to modify the ora2pg configuration file located in $OPENSHIFT_PGDEVEL_DIR/ora2pg/etc/ora2pg/ora2pg.conf.dist and specify what Oracle system you want to connect to.  The value of ORACLE_HOME has already been set during the OpenShift cartridge installation process.

To run ora2pg, issue the following command from the OpenShift application command line:

$ ora2pg -c $OPENSHIFT_PGDEVEL_DIR/ora2pg/etc/ora2pg/ora2pg.conf.dist -b $OPENSHIFT_DATA_DIR

This command runs a default ora2pg configuration as shipped with the Crunchy Development Cartridge, it will send the output.sql file to the $OPENSHIFT_DATA_DIR directory.

##Using pldebugger

The pldebugger for pgadmin is included into the Crunchy Postgresql Cartridge as a contrib module, compiled and ready for installation.  

When the Crunchy Development Cartridge is installed, it will issue the following SQL command to enable the pldebugger extension on the postgres database:

CREATE EXTENSION pldbgapi

The Developer installer also includes the following configuration line in the postgresql.conf file:

shared_preload_libraries = '$libdir/plugin_debugger'

Lastly, the postgres instance will be restarted to pick up the debugger changes.  At this point you are ready to connect to pgadmin and use the debugger features as documented on the pldebugger and pgadmin web sites.  




