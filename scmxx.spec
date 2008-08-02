%define name 	scmxx
%define version 0.9.0
%define release %mkrel 5

Name:		%{name}
Summary:	Exchange data with Siemens mobile phones
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Communications
URL:		http://www.hendrik-sattler.de/scmxx
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
