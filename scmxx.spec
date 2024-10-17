%define name 	scmxx
%define version 0.9.0
%define release 7

Name:		%{name}
Summary:	Exchange data with Siemens mobile phones
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Communications
URL:		https://www.hendrik-sattler.de/scmxx
Source:		http://prdownloads.sourceforge.net/scmxx/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
SCMxx is a console program that allows you to exchange certain types of data
with mobile phones made by Siemens. Some of the data types that can be
exchanged are logos, ring tones, vCalendars, phonebook entries, and SMS
messages. It works with the following models: S25, S35i, M35i and C35i, SL45,
S45, ME45 and C45 and probably others.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-, root, root)
%doc BUGS INSTALL README TODO AUTHORS CHANGELOG docs/*.txt contrib
%{_bindir}/*
%{_mandir}/man*/*
%lang(ru) %{_mandir}/ru/*/*
%lang(de) %{_mandir}/de/*/*
%lang(it) %{_mandir}/it/*/*


%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.9.0-6mdv2010.0
+ Revision: 433626
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.9.0-5mdv2009.0
+ Revision: 260561
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.9.0-4mdv2009.0
+ Revision: 252172
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.9.0-2mdv2008.1
+ Revision: 140776
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Mon May 07 2007 Olivier Thauvin <nanardon@mandriva.org> 0.9.0-2mdv2008.0
+ Revision: 23923
- rebuild
- Import scmxx



* Fri Mar 03 2006 Austin Acton <austin@mandriva.org> 0.9.0-1mdk
- New release 0.9.0

* Sat Nov 19 2005 Austin Acton <austin@mandriva.org> 0.8.2-1mdk
- New release 0.8.2

* Mon Oct 03 2005 Lenny Cartier <lenny@mandriva.com> 0.8.1-1mdk
- 0.8.1

* Thu Jul 14 2005 Austin Acton <austin@mandriva.org> 0.8.0-1mdk
- 0.8.0
- source URL
- configure 2.5

* Mon Feb 21 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.7.5-1mdk
- 0.7.5
- add italian manpage

* Thu Oct 14 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.7.4-1mdk
- 0.7.4

* Wed Oct 13 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.7.3-1mdk
- 0.7.3

* Wed Jul 21 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.7.2-1mdk
- 0.7.2

* Mon May 24 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.7.1-1mdk
- 0.7.1

* Wed Jan 24 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.6.4.1-1mdk
- 0.6.4.1

* Wed Sep 03 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.6.4-1mdk
- 0.6.4

* Wed Jun 04 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.6.3.8-1mdk
- 0.6.3.8

* Mon May 12 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.6.3.7-1mdk
- 0.6.3.7

* Wed Jan 01 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.6.3.5-1mdk
- 0.6.3.5
- \o/ Happy new year \o/ even for you silly rpmlint :-) 

* Mon Dec 16 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.6.3.3-1mdk
- 0.6.3.3

* Sun Nov 03 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.6.1.6-1mdk
- from Michael Reinsch <mr@uue.org> :
	- first mandrake spec file
