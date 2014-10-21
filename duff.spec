Name:		duff
Version:	0.5.2
Release:	2%{?dist}
Summary:	Command-line utility for quickly finding duplicates in a given set of files

Group:		File Tools
License:	zlib/libpng
URL:		http://duff.dreda.org/
Source0:	https://github.com/elmindreda/duff/archive/duff-%{version}.tar.gz

BuildRequires:	  autoconf
BuildRequires:	  automake
BuildRequires:	  gettext-devel

%description

Duff is a command-line utility for identifying duplicates in a given set of
files.  It attempts to be usably fast and uses the SHA family of message
digests as a part of the comparisons.


%prep
%setup -q

%build
# Append gettext version to configure.ac so that autopoint can work
# Nb this doesn't always seem to work under 'mock'?
echo "AM_GNU_GETTEXT_VERSION("$(autopoint --version | grep autopoint | cut -d' ' -f4)")" 1>> configure.ac 2>&1
# Use autopoint rather than 'gettextize --no-changelog' in RPM context
# autopoint is the non-interactive version
autopoint
# Create configure, Makefiles etc
autoreconf -i
# configure and make
./configure --prefix=%{_prefix} --mandir=%{_mandir}
make %{?_smp_mflags}


%install
mkdir -p %{buildroot}/%{_bindir}
make install DESTDIR=%{buildroot}
# Use %find_lang macro to handle locale files
# See http://fedoraproject.org/wiki/PackagingDrafts/find_lang
%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README README.SHA
%{_bindir}/*
%{_mandir}/man?/*
%{_datadir}/%{name}/*
%{_datadir}/doc/%{name}/*

%changelog
* Tue Oct 21 2014 Peter Briggs <peter.briggs@manchester.ac.uk> - 0.5.2-2
- Updated spec file with suggestions from Pierre-Yves Chibon (pypingou@github)

* Fri Oct 17 2014 Peter Briggs <peter.briggs@manchester.ac.uk> - 0.5.2-1
- initial version

