Name:           stacks
Version:        0.9991
Release:        1%{?dist}
Summary:	Build loci out of a set of short-read sequenced samples

Group:		Applications/Engineering
License:	GPLv3
URL:		http://creskolab.uoregon.edu/stacks/
Source0:	http://creskolab.uoregon.edu/stacks/source/stacks-0.9991.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	libgomp
Requires:	perl-Spreadsheet-WriteExcel

%description

Stacks is a software pipeline for building loci out of a set of short-read
sequenced samples. Stacks was developed for the purpose of building genetic
maps from RAD-Tag Illumina sequence data, but can also be readily applied
to population studies, and phylogeography.

%package          user-interface
Summary:          Stacks web-base user interface
Group:            Applications/Engineering

Requires:         %{name} = %{version}
Requires:	  httpd
Requires:	  mysql,mysql-server
Requires:	  php,php-pear-MDB2,php-pear-MDB2-Driver-mysql
Requires:	  perl-DBD-MySQL

%description user-interface

Web-based user interface for Stacks.


%prep
%setup -q


%build
./configure --prefix=%{_prefix}
make


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc LICENSE README

%{_bindir}/*


%files user-interface
%defattr(-,root,root,-)

%{_prefix}/share/stacks


%changelog

* Wed May  9 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 0.9991-1
- initial version
