Summary: e-smith server and gateway - proxy module
%define name e-smith-proxy
Name: %{name}
%define version 4.13.2
%define release 05
Version: %{version}
Release: %{release}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-proxy-4.13.2-02.mitel_patch
Patch1: e-smith-proxy-4.13.2-03.mitel_patch
Patch2: e-smith-proxy-4.13.2-04.mitel_patch
Packager: e-smith developers <bugs@e-smith.com>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: e-smith-base
Requires: squid
Requires: e-smith-lib >= 1.15.1-19
Requires: iptables
BuildRequires: e-smith-devtools
Obsoletes: e-smith-transproxy
AutoReqProv: no

%description
e-smith server and gateway software - proxy module.

%changelog
* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 4.13.2-05
- Bump release number only

* Wed Nov 23 2005 Charlie Brady <charlieb@e-smith.com>
- [4.13.2-04]
- Return 'return "DIRECT";' by default if squid is disabled [SF: 1310447]

* Sat Nov  5 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.13.2-03]
- Return "DIRECT" by default if squid is disabled [SF: 1310447]

* Mon Oct 17 2005 Charlie Brady <charlieb@e-smith.com>
- [4.13.2-02]
- Allow squid to create a real pid file, so that "squid -k rotate"
  works. PID file needs to be created in a directory owned by 'squid'
  user - I've chosen /var/log/squid. [SF: 1327724]

* Fri Oct 14 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.13.2-01]
- Remove L10Ns from base packages [SF: 1309520]

* Fri Oct 14 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.13.1-01]
- New dev stream before relocating L10Ns

* Fri Sep 30 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.13.0-40]
- Added Italian L10N - Thanks Filippo Carletti [SF: 1309266]

* Tue Sep 27 2005 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-39]
- Fix squid run script so that initialization output is also
  sent to the logger. [SF: 1200402]

* Mon Sep 26 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.13.0-38]
- Added German L10N - Thanks Dietmar Berteld [SF: 1293325]

* Mon Aug 29 2005 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-37]
- Remove dependency on e-smith-hosts.

* Tue Aug  2 2005 Shad Lords <slords@email.com>
- [4.13.0-36]
- Add TCPPort and access for firewall definitions [SF: 1246986]
- Add squid{TCPProxyPort} for transparent redirects [SF: 1246986]

* Mon Jul 18 2005 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-35]
- Add French translation of panel (Merci, Didier RAMBEAU). [SF: 1234928]

* Mon Jul 18 2005 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-34]
- Update to current db access APIs, in readiness for move of dbs to private
  directory. [SF: 1216546 (Shad)]

* Thu Jul 14 2005 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-33]
- Change smtpfront-qmail{Proxy} -> smtpd{Proxy}. [Gordon Rowell, SF: 1212323]

* Thu Jul 14 2005 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-32]
- Disable DNS tests on startup, like the standard RH config. [SF: 1234007]

* Tue Jul  5 2005 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-31]
- Add extension_methods spec to squid.conf, to allow subversion
  passthrough - see http://subversion.tigris.org/faq.html#proxy.
  [SF: 1231333]

* Thu Jun  9 2005 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-30]
- Reword the initial section of the proxy panel to remove reference
  to 6040 product. [Gordon SF:1201757]
- Remove -s flag in run script, to avoid sending debug messages
  from squid via syslog. [SF: 1200402]

* Tue Mar  8 2005 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-29]
- Replace all restart-* and most reload-* actions with calls to 'adjust-services'.
  Update e-smith-lib version dependency. [MN00065576]
- Use generic_template_expand action where possible, in place
  of specific actions. Update e-smith-lib dependency. [MN00064130]

* Tue Jan 18 2005 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-28]
- Use /dev/null as pid_filename. Squid documentation lies - "none"
  doesn't work. [charlieb MN00062550]

* Wed Dec 29 2004 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-27]
- Use e-smith-service for rc7.d symlink, so that "status" is respected.
  [charlieb MN00061795]

* Wed Dec 29 2004 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-26]
- Better fix for logging problem. Log run script errors to /var/log/squid.run,
  and let squid own and manage /var/log/squid. Remove migration fragment
  which does chown/chmod. [charlieb MN00057027]
- Don't try to create a pid file - we don't have permission anyway
  [charlieb MN00062550]

* Thu Nov 11 2004 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-25]
- Have multilog run as user squid, logging to /var/log/squid
  (provided by squid package).  [charlieb MN00057027]

* Tue Sep 28 2004 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-24]
- Remove duplicate local network in ACL. [charlieb MN00050804]

* Fri Sep  3 2004 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-23]
- Clean BuildRequires. [charlieb MN00043055]

* Wed Jul  7 2004 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-22]
- Added initialization of the cache to the run script. [msoulier MN00037758]

* Thu Jun 10 2004 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-21]
- Forgot to export the change_settings function. [msoulier MN00037755]
- Made the smtp proxy toggle display conditionally on the existence of the
  e-smith-email rpm. [msoulier MN00037755]
- Made proxy-restart smarter, so it stops calling stop when the service is
  down. [msoulier MN00037755]

* Thu Jun 10 2004 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-20]
- Added the initial version of the code, including a proxy-update event.
  [msoulier MN00037755]

* Thu Jun 10 2004 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-19]
- Moved perl -> perl5, typo in directory path. [msoulier MN00037755]

* Thu Jun 10 2004 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-18]
- Added stub for new web panel. [msoulier MN00037755]

* Tue Jun  8 2004 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-17]
- Forward port of squid disable in serveronly mode. [msoulier MN00037260]

* Tue May  4 2004 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-16]
- Fixed bad var reference. [msoulier dpar-27884]

* Thu Jan 22 2004 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-15]
- Moved proxy-start/stop from e-smith-ntp to this package. [msoulier 10929]

* Fri Dec 19 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-14]
- Fixed a migration fragment that was mangling the log permissions.
  [msoulier 6449]

* Fri Dec 19 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-13]
- Specified full path to logfile, as relative path did not work as expected.
  [msoulier 6449]

* Fri Dec 19 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-12]
- Changing permissions on /var/log/squid to permit smelog to use the directory
  beneath. [msoulier 6449]

* Fri Dec 19 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-11]
- Explicitly creating /var/log/squid/run with correct permissions.
  [msoulier 6449]

* Wed Dec 17 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-10]
- Added migration for supervise change. [msoulier 6449]

* Wed Dec 17 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-09]
- Changed ownership of /var/log/squid. [msoulier 6449]

* Mon Dec 15 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-08]
- Added multilog back, logging to /var/log/squid/run. [msoulier 6449]

* Thu Dec 11 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-07]
- Removed multilog, as it does not apply here. [msoulier 6449]

* Thu Dec 11 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-06]
- Changed log owner to smelog. [msoulier 6449]

* Wed Dec 10 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-05]
- Changed owner of squid process and log directory to user squid.
  [msoulier 6449]

* Wed Dec 10 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-04]
- Fixed bug in genfilelist options. [msoulier 6449]

* Wed Dec 10 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-03]
- Fixed bug in createlinks. [msoulier 6449]

* Wed Dec 10 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-02]
- Supervising squid. [msoulier 6449]

* Wed Dec 10 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-01]
- rolling to dev stream - 4.13.0

* Tue Sep  9 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.12.0-02]
- Disable safe_ports ACL by default. Create squid{SafePorts}
  default ports list and squid{EnforceSafePorts} default to no [gordonr 9488]

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [4.12.0-01]
- Changing version to stable stream number - 4.12.0

* Fri May 30 2003 Michael Soulier <msoulier@e-smith.com>
- [4.11.0-09]
- Removed dangling symlink to e-smith-proxy. [msoulier 8808]

* Tue Apr 29 2003 Tony Clayton <apc@e-smith.com>
- [4.11.0-08]
- Add default db fragments for squid [tonyc 8537]
- Remove dead proxy-startup action [tonyc 8537]

* Thu Apr 10 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.11.0-07]
- Move defaults fragment to right location [gordonr 6911]

* Tue Apr  8 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.11.0-06]
- Added port 119 (nntp) to Safe_ports, corrected high ports range [gordonr 4430]

* Mon Apr  7 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.11.0-05]
- Set default for $squid{TransparentPort} and use in proxy.pac [gordonr 6911]

* Mon Apr  7 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.11.0-04]
- Added port 81 to acl Safe_ports [gordonr 4430]
- Sorted Safe_ports to make it easier to read [gordonr 4430]

* Tue Mar 18 2003 Lijie Deng <lijied@e-smith.com>
- [4.11.0-03]
- Deleted ./etc/squid/squid.conf/template-begin [lijied 3295]

* Mon Feb 24 2003 Michael Soulier <msoulier@e-smith.com>
- [4.11.0-02]
- Removed use of LocalDomainPrefix. [msoulier 4812]

* Mon Feb 24 2003 Michael Soulier <msoulier@e-smith.com>
- [4.11.0-01]
- dev stream to 4.11.0

* Mon Feb 24 2003 Michael Soulier <msoulier@e-smith.com>
- [4.10.0-03]
- Backed-out changes in 4.10.0-02, as this should be in a dev stream.
  [msoulier 4812]

* Mon Feb 24 2003 Michael Soulier <msoulier@e-smith.com>
- [4.10.0-02]
- Removed use of LocalDomainPrefix. [msoulier 4812]

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [4.10.0-01]
- Roll to maintained version number to 4.10.0

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [4.10.0-01]
- Roll to maintained version number to 4.10.0

* Wed Oct  2 2002 Michael Soulier <msoulier@e-smith.com>
- [4.9.7-02]
- Removing redundant iptables rule in PREROUTING chain which forwarded
- any local network http traffic to the squid proxy, when the previous
- rule already forwarded _all_ traffic there. [msoulier 5029]

* Thu Sep 12 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.7-01]
- Move proxy.pac file to /etc/httpd/conf/proxy/proxy.pac, and add
  two URL aliases to it (/wpad.dat and /proxy.pac). Add appropriate
  access rules. [charlieb 4838]

* Wed Sep 11 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.6-02]
- Dynamically adjust transparent proxy rules in "adjust" section of masq
  script. [charlieb 4501]

* Thu Aug 22 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.6-01]
- Remove 45DenySquid template fragment - it's no longer needed since we
  are using connection tracking. [charlieb 4499]

* Wed Aug 21 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.5-01]
- Fix error in squid conf template if LocalDomainPrefix is defined.
  [charlieb 4686]

* Tue Aug 20 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.4-01]
- Add rc7.d symlink and don't set deprecated ORDER property [charlieb 4458]

* Tue Jul 30 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.3-01]
- Add additional rules in nat table to protect local HTTP accesses from
  being forced through transparent proxy. [charlieb 1268]

* Wed Jul 17 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.2-01]
- Get syntax correct for iptables form of REDIRECT target, for
  transparent proxy. [charlieb 1268]

* Wed Jul 17 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.1-01]
- Change masq script fragments to use iptables. [charlieb 1268]

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.0-01]
- Changing version to development stream number - 4.9.0

* Fri May 31 2002 Charlie Brady <charlieb@e-smith.com>
- [4.8.0-01]
- Changing version to maintained stream number to 4.8.0

* Wed May 29 2002 Charlie Brady <charlieb@e-smith.com>
- [4.7.12-01]
- Update proxy.pac to check host with isPlainHostName before doing DNS lookups.
  Go direct for any plain host names. This shouldn't be necessary, but IE
  is not going direct from WinXP with current setup. Remove redundent
  else clauses while we are at it. [charlieb 3715]

* Wed May 29 2002 Charlie Brady <charlieb@e-smith.com>
- [4.7.11-01]
- Add append_domain directive in squid.conf, so that squid can resolve
  unqualified names. (Why doesn't it use what's in resolv.conf?)
  [charlieb 3715]

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.7.10-01]
- RPM rebuild forced by cvsroot2rpm

* Fri May 17 2002 Tony Clayton <apc@e-smith.com>
- [4.7.9-01]
- Added 'use esmith::util' to 20ACL10localhost squid.conf fragment [tonyc 3253]

* Fri Apr 19 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.7.8-01]
- And really cleaning old directory this time [gordonr 3073]

* Fri Apr 19 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.7.7-01]
- Cleaned directory structure of bad pathname [gordonr 3073]

* Fri Apr 19 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.7.6-01]
- Moved start of function to template-begin in case comments are 
  a problem for some clients [gordonr 3073]

* Fri Apr 19 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.7.5-01]
- Added braces to templates to evaluate ConfigDB entries [gordonr 3073]

* Fri Apr 19 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.7.4-01]
- Added dependency on e-smith-hosts

* Fri Apr 19 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.7.3-01]
- Thanks to Damien Curtain for the wpad.dat details [gordonr 3073]

* Fri Apr 19 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.7.2-01]
- Rewrote proxy-conf using ConfigDB [gordonr 3073]
- Added support wpad.dat and proxy/pac files [gordonr 3073]

* Fri Apr 19 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.7.1-01]
- Initial CVS import

* Fri Apr 19 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.7.0-01]
- rollRPM: Rolled version number to 4.7.0-01. Includes patches up to 4.6.0-06.

* Fri Feb 01 2002 Charlie Brady <charlieb@e-smith.com>
- [4.6.0-06]
- Disable transparent proxy rule if squid is disabled.

* Tue Jan 15 2002 Charlie Brady <charlieb@e-smith.com>
- [4.6.0-05]
- Rationalise distribution of actions to events (#2507)
  - Add proxy-restart to console-save event
  - Remove proxy-startup from console-save and bootstrap-console-save events
  - Remove proxy-conf from post-upgrade event
- Move mkdir to create bootstrap-console-save event directory into prep
  section (from %build), so that it gets included in the tarball by the
  next rollRPM.

* Mon Jan 14 2002 Charlie Brady <charlieb@e-smith.com>
- [4.6.0-04]
- Fix missing newline in previous never-direct fix.

* Mon Jan 14 2002 Charlie Brady <charlieb@e-smith.com>
- [4.6.0-03]
- Add never_direct statements to parent cache case, as always_direct on 
  its own is not enough.

* Thu Jan 03 2002 Charlie Brady <charlieb@e-smith.com>
- [4.6.0-02]
- Fix runtime lookup of external IP in masq script fragment.
- Use always_direct deny statement to force squid to use an external cache
  if a parent cache is specified.

* Tue Dec 11 2001 Jason Miller <jay@e-smith.com>
- [4.6.0-01]
- rollRPM: Rolled version number to 4.6.0-01. Includes patches up to 4.5.0-03.

* Wed Nov 07 2001 Charlie Brady <charlieb@e-smith.com>
- [4.5.0-03]
- Change the default setting for transparent to "yes".

* Wed Nov 07 2001 Charlie Brady <charlieb@e-smith.com>
- [4.5.0-02]
- Add transparent proxy feature, which is disabled by default. To enable,
  set Transparent property of "squid" service to "yes".

* Wed Nov 7 2001 Charlie Brady <charlieb@e-smith.com>
- [4.5.0-01]
- Rolled version number to 4.5.0-01. Includes patches upto 4.4.0-07.

* Wed Nov 07 2001 Tony Clayton <tonyc@e-smith.com>
- [4.4.0-07]
- rebranding to Mitel Networks

* Mon Oct 22 2001 Charlie Brady <charlieb@e-smith.com>
- [4.4.0-06]
- Translate shell createlinks to perl createlinks
- Add bootstrap-console-save symlinks via changes to createlinks script

* Wed Aug 29 2001 Charlie Brady <charlieb@e-smith.com>
- [4.4.0-05]
- Add template fragment to set ftp_user used for password in anonymous ftp
- Add template fragment to set cache administrator email address in messages.

* Fri Aug 17 2001 gordonr
- [4.4.0-04]
- Autorebuild by rebuildRPM

* Wed Aug 15 2001 Charlie Brady <charlieb@e-smith.com>
- [4.4.0-03]
- Add template fragements to make sure that webdav protocols are not requested
  via an upstream cache.
- Re-add template-begin, as the default template-begin is not yet inserted.

* Mon Aug 13 2001 Charlie Brady <charlieb@e-smith.com>
- [4.4.0-02]
- Break template-begin for squid.conf into fragments.
- Change acl name of localhost into localsrc, and change all
  references to it.
- Add acl of localdst for all local destinations. In future we should point
  client browsers directly at local web servers.

* Wed Aug 8 2001 Charlie Brady <charlieb@e-smith.com>
- [4.4.0-01]
- Rolled version number to 4.4.0-01. Includes patches upto 4.3.0-03.

* Fri Jul 6 2001 Peter Samuel <peters@e-smith.com>
- [4.3.0-03]
- Changed license to GPL

* Tue May 29 2001 Tony Clayton <tonyc@e-smith.com>
- [4.3.0-02]
- untie %conf hash in before calling serviceControl in proxy-startup

* Mon Apr 30 2001 Charlie Brady <charlieb@e-smith.com>
- [4.3.0-01]
- Rolled version number to 4.3.0-01. Includes patches upto 4.2.0-04.

* Sun Mar 25 2001 Gordon Rowell <gordonr@e-smith.com>
- [4.2.0-04]
- Removed dependency on e-smith-packetfilter. There is a filter fragment
  which will will be useless without it, but it's not really a dependency

* Sat Mar 03 2001 Charlie Brady <charlieb@e-smith.com>
- [4.2.0-03]
- Add packet filter fragment to deny and log any connection attempt on
  the external interface. This filter fragment is only active if squid
  is enabled.
- Add requires e-smith-packetfilter spec.

* Thu Feb  8 2001 Adrian Chung <adrianc@e-smith.com>
- [4.2.0-02]
- Rolling release number for GPG signing.

* Thu Jan 25 2001 Peter Samuel <peters@e-smith.com>
- [4.2.0-01]
- Rolled version number to 4.2.0-01
  Includes patches upto 4.1.0-2

* Thu Dec 28 2000 Gordon Rowell <gordonr@e-smith.com>
- [4.1.0-2]
- Added manager port (980) to Safe_ports

* Wed Dec 06 2000 Peter Samuel <peters@e-smith.com>
- [4.1.0-1]
- Rolled version to 4.1.0-1. Includes patches up to 4.0.7-3

* Mon Oct 30 2000 Charlie Brady <charlieb@e-smith.com>
- Fix typo in proxy-startup which prevented squid from starting

* Mon Oct 30 2000 Charlie Brady <charlieb@e-smith.com>
- This is e-smith-proxy-4.0.7-2.
- Merge services database back into configuration db.

* Thu Oct 26 2000 Peter Samuel <peters@e-smith.com>
- Rolled version to 4.0.7. Includes patches up to 4.0.6-13

* Fri Oct 06 2000 Charlie Brady <charlieb@e-smith.com>
- Fix perl errors in proxy-conf

* Fri Oct 06 2000 Charlie Brady <charlieb@e-smith.com>
- Make sure that "squid" is enabled in the services database
- Remove %post section.
- Fixed some script errors in other action scripts.

* Thu Oct 05 2000 Adrian Chung <adrian.chung@e-smith.com>
- Changed restart action to use serviceControl
- Removed post-install event conditional.
- Changed %post set to setdefault.

* Wed Oct 04 2000 Paul Nesbit <pkn@e-smith.com>
- expand templates only if enabled in services database.
- added /sbin/e-smith/db services set proxy enabled to %post

* Tue Oct 03 2000 Charlie Brady <charlieb@e-smith.com>
- Update services database when enabling/disabling service startup

* Mon Sep 25 2000 Paul Nesbit <pkn@e-smith.com>
- updated contact, support and URL info

* Fri Aug 25 2000 Charlie Brady <charlieb@e-smith.com>
- Added build dependency on e-smith-devtools, and dependency on
  e-smith-lib. Generate file list with genfilelist.

* Thu Aug 24 2000 Gordon Rowell <gordonr@e-smith.com>
- Rewrote proxy-startup to user serviceControl()

* Wed Jul 12 2000 Joseph Morrison <jdm@e-smith.net>
- Use -1 argument to split command to handle null final values in
  configuration records

* Sat Jun 17 2000 Charlie Brady <charlieb@e-smith.net>
- Do not mark templates as config files.

* Mon Jun 12 2000 Charlie Brady <charlieb@e-smith.net>
- Use list form of backgroundCommand.

* Thu May 18 2000 Charlie Brady <charlieb@e-smith.net>
- fold long lines in spec file
- Use & substitution in sed line

* Sun May 14 2000 Charlie Brady <charlieb@e-smith.net>
- Removed transproxy patch
- Make squid.conf template a directory

* Thu May 11 2000 Charlie Brady <charlieb@e-smith.net>
- Some small fixes in conf startup script
- Add dependency on squid

* Fri Apr 21 2000 Charlie Brady <charlieb@e-smith.net>
- Add a missing script template

* Thu Apr 20 2000 Charlie Brady <charlieb@e-smith.net>
- Add transparent proxy feature. Change architecture to "noarch"
- Make templates %config files.

%prep
%setup
mkdir -p root/etc/e-smith/events/bootstrap-console-save
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
perl createlinks

mkdir -p root/var/service/squid/supervise
touch root/var/service/squid/down
mkdir -p root/var/service/squid/log/supervise
mkdir -p root/var/log/squid.run

mkdir -p root/etc/httpd/conf/proxy

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    --dir '/var/service/squid' 'attr(1755,root,root)' \
    --file '/var/service/squid/down' 'attr(0644,root,root)' \
    --file '/var/service/squid/run' 'attr(0755,root,root)' \
    --dir '/var/service/squid/supervise' 'attr(0700,root,root)' \
    --dir '/var/service/squid/log' 'attr(1755,root,root)' \
    --file '/var/service/squid/log/run' 'attr(0755,root,root)' \
    --dir '/var/service/squid/log/supervise' 'attr(0700,root,root)' \
    --dir '/var/log/squid.run' 'attr(0750,smelog,root)' \
    > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING" >> %{name}-%{version}-%{release}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
