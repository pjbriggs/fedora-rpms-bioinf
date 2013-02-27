Name:		primer3v2
Version:	2.0.0
Release:	alpha1%{?dist}
Summary:	PCR primer design tool
License:	BSD and GPLv2+
URL:		http://primer3.sourceforge.net/
Source0:	https://sourceforge.net/projects/primer3/files/primer3/2.0.0-alpha/primer3-2.0.0-alpha.tar.gz

%description
Primer3 is a widely used program for designing PCR primers (PCR =
"Polymerase Chain Reaction"). PCR is an essential and ubiquitous
tool in genetics and molecular biology. Primer3 can also design
hybridization probes and sequencing primers.

PCR is used for many different goals. Consequently, primer3 has
many different input parameters that you control and that tell
primer3 exactly what characteristics make good primers for your
goals.

Note that the primer3v2 package is specifically tied to primer3
version 2.


%prep
%setup -q -n primer3-2.0.0-alpha


%build
# Compile
cd src
make


%install
rm -rf %{buildroot}
# Doesn't have a make install of its own so fudge it here
# Executables
mkdir -p %{buildroot}%{_bindir}
cd src
install -m 0755 primer3_core %{buildroot}%{_bindir}
install -m 0755 oligotm %{buildroot}%{_bindir}
install -m 0755 ntdpal %{buildroot}%{_bindir}
install -m 0755 long_seq_tm_test %{buildroot}%{_bindir}
# Docs
cd ..
mkdir -p %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 0644 COPYING.txt %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 0644 primer3_manual_2_0_0_alpha.htm %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 0644 primer3_v1_1_4_default_settings.txt %{buildroot}/%{_docdir}/%{name}-%{version}


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}/*
%{_bindir}/*


%changelog
* Tue Feb 26 2013 Peter Briggs <peter.briggs@manchester.ac.uk> - 2.0.0-alpha-1
- initial version

