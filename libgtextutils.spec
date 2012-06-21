%define debug_package %{nil}

Name:		libgtextutils
Version:	0.6.1
Release:	1%{?dist}
Summary:	Gordon-Text_utils-Library for FASTX-Toolkit

Group:		Applications/Productivity
License:	GNU Affero GPLv3
URL:		http://hannonlab.cshl.edu/fastx_toolkit/index.html
Source0:	http://hannonlab.cshl.edu/fastx_toolkit/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Utility library required by the fastx-toolkit programs.

%prep
%setup -q


%build
./configure --prefix=%{_prefix} --libdir=%{_libdir}
make


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
# Remove pkgconfig from lib
rm -rf %{buildroot}%{_libdir}/pkgconfig
# Remove aclocal from share
rm -rf %{buildroot}%{_datadir}/aclocal

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS README NEWS COPYING THANKS ChangeLog
%{_libdir}/*
%{_includedir}/*


%changelog
* Wed Jun 20 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 0.6.1-1
- initial version

