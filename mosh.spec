Name:		mosh
Version:	1.2.4
Release:	1%{?dist}
Summary:	mosh (mbile shell) is a remote terminal application
Group:		Applications/Productivity

License:	GPLv3
URL:		http://mosh.mit.edu/
Source0:	http://mosh.mit.edu/mosh-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	protobuf-devel
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
BuildRequires:	openssl-devel
BuildRequires:	libutempter-devel
Requires:	protobuf
Requires:	ncurses
Requires:	zlib
Requires:	libutempter
Requires:	openssl

%description
mosh (mobile shell) is a remote terminal application that allows roaming,
supports intermittent connectivity, and provides intelligent local echo
and line editing of user keystrokes.

Mosh is a replacement for SSH. It's more robust and responsive, especially
over Wi-Fi, cellular, and long-distance links.

%prep
%setup -q


%build
%configure
make


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%files
%doc COPYING
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Wed Mar 26 2014 Peter Briggs <peter.briggs@manchester.ac.uk> - 1.2.4-1
- first version


