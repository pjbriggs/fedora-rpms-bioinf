Name:		weeder
Version:	1.4.2
Release:	1%{?dist}
Summary:	Motif (transcription factor binding sites) discovery from coregulated genes 

License:	Non-commercial/no warranty/all-rights reserved
URL:		http://159.149.109.9/modtools/
Source0:	http://159.149.109.9/modtools/downloads/weeder1.4.2.tar.gz
Patch0:		weeder-freqfiles.patch

%description
Motif (transcription factor binding sites) discovery in sequences from
coregulated genes of a single species.


%prep
%setup -q -n Weeder%{version}
# Patch the source code to look for FreqFiles dir in
# /usr/share/weeder-1.4.2
%patch0 -p1


%build
# Compile
./compileall


%install
rm -rf %{buildroot}
# Doesn't have a make install of its own so fudge it here
# Executables
mkdir -p %{buildroot}%{_bindir}
install -m 0755 *.out %{buildroot}%{_bindir}
# Data files
mkdir -p %{buildroot}/%{_datadir}/%{name}-%{version}/FreqFiles
install -m 0644 FreqFiles/* %{buildroot}/%{_datadir}/%{name}-%{version}/FreqFiles
# Docs
mkdir -p %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 0644 LICENSE.txt %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 0644 organisms.txt %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 0644 README_LARGE_SEQUENCE_SETS.txt  %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 0644 weedermanual.pdf %{buildroot}/%{_docdir}/%{name}-%{version}
# Examples
mkdir -p %{buildroot}/%{_datadir}/%{name}-%{version}/examples
install -m 0644 examples/* %{buildroot}/%{_datadir}/%{name}-%{version}/examples


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}/*
%{_datadir}/%{name}-%{version}/*
%{_bindir}/*


%changelog
* Fri Mar 16 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 1.4.2-1
- initial version

