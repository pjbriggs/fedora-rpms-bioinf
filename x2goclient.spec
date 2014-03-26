Name:		x2goclient
Version:	4.0.1.3
Release:	1%{?dist}
Summary:	Client for the x2go remote desktop service
Group:		Applications/Productivity

License:	GPLv2
URL:		http://wiki.x2go.org/doku.php/doc:installation:x2goclient
Source0:	http://code.x2go.org/releases/source/x2goclient/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	man2html
BuildRequires:	openldap-devel
BuildRequires:	libssh-devel
BuildRequires:	libXpm-devel
BuildRequires:	cups-devel
BuildRequires:	qt-devel
Requires:	libssh
Requires:	cups
Requires:	qt

%description
Client for the x2go remote desktop service.

%prep
%setup -q


%build
make


%install
rm -rf %{buildroot}
# Install to /usr rather than /usr/local
# Make sure that 'install' is not invoked with '-o root' and '-g root' options
# Only install client and manpages
make install_client DESTDIR=%{buildroot} PREFIX=%{_prefix} INSTALL_DIR="install -d -m 755" INSTALL_FILE="install -m 644" INSTALL_PROGRAM="install -m 755"
make install_man DESTDIR=%{buildroot} PREFIX=%{_prefix} INSTALL_DIR="install -d -m 755" INSTALL_FILE="install -m 644" INSTALL_PROGRAM="install -m 755"


%files
%doc LICENSE
%{_bindir}/*
%{_datadir}/*
%{_mandir}/man1/*


%changelog
* Wed Mar 26 2014 Peter Briggs <peter.briggs@manchester.ac.uk> - 4.0.1.3-1
- first version


