Name:		pal_finder
Version:	0.02.04
Release:	1%{?dist}
Summary:	Find microsatellite repeats and design PCR primers to amplify them

License:	GPL3
URL:		http://sourceforge.net/projects/palfinder/
Source0:	http://sourceforge.net/projects/palfinder/files/pal_finder_v0.02.04.tar.gz
Patch0:		pal_finder-no-warnings-recursion.patch
Requires:	primer3v2 == 2.0.0
BuildArch:	noarch


%description
pal_finder finds microsatellite repeat elements directly from raw 454 or
Illumina paired-end sequencing reads, and design PCR primers to amplify
these repeat loci in an automated fashion. Exact matches to repeats or 2-,
3-, 4-, 5-, and/or 6-mers are located and primer3 is then used to generate
primer pairs to amplify regions containing microsatellite loci. The
minimum number of repeat units for each n-mer size is specified by the
user.


%prep
%setup -q -n pal_finder_v%{version}
# Patch the source code to suppress "deep recursion" warnings
%patch0 -p1


%build
# Nothing to do


%install
rm -rf %{buildroot}
# Move the pal_finder script to bindir
mkdir -p %{buildroot}%{_bindir}
install -m 0755 pal_finder_v0.02.04.pl %{buildroot}%{_bindir}
# Data files
mkdir -p %{buildroot}%{_datadir}/%{name}_v%{version}
install -m 0644 config.txt %{buildroot}%{_datadir}/%{name}_v%{version}
install -m 0644 simple.ref %{buildroot}%{_datadir}/%{name}_v%{version}
# Examples
mkdir -p %{buildroot}%{_datadir}/%{name}_v%{version}/test/data
install -m 0644 test/data/* %{buildroot}%{_datadir}/%{name}_v%{version}/test/data
# Docs
mkdir -p %{buildroot}/%{_docdir}/%{name}_v%{version}
install -m 0644 COPYING.txt %{buildroot}/%{_docdir}/%{name}_v%{version}
install -m 0644 README.txt %{buildroot}/%{_docdir}/%{name}_v%{version}


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_docdir}/%{name}_v%{version}/*
%{_datadir}/%{name}_v%{version}/*
%{_bindir}/*


%changelog
* Tue Feb 26 2013 Peter Briggs <peter.briggs@manchester.ac.uk> - 0.02.04-1
- initial version
