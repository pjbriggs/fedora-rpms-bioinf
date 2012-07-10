%global 	debug_package %{nil}
Name:		GEM-library-parser
Version:	20090710
Release:	1%{?dist}
Summary:	Perl converters for the ouput of the GEM-library gem-mapper

Group:		Applications/Engineering
License:	GPLv3
URL:		http://sourceforge.net/apps/mediawiki/gemlibrary/
Source0:	http://sourceforge.net/projects/gemlibrary/files/gem-library/Binary%20pre-release%201/GEM-parser-20090710.tbz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	GEM-library-bin
BuildArch:	noarch

%description
Provides supported and unsupported Perl converters for output of GEM-library programs
gem-mapper and split-mapper to SAM, GFF, Bed and Wiggle formats.


%prep
%setup q -n GEM-parser-%{version}

%build


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{perl_vendorarch}
install -m 0755 gem-2-gff.pl %{buildroot}%{_bindir}
install -m 0755 gem-2-miro.pl %{buildroot}%{_bindir}
install -m 0755 gem-2-wiggle.pl %{buildroot}%{_bindir}
install -m 0755 gem-2-sam.pl %{buildroot}%{_bindir}
install -m 0755 gem-2-bed.pl %{buildroot}%{_bindir}
install -m 0755 gem-2-sequence.pl %{buildroot}%{_bindir}
install -m 0644 GemReader.pm %{buildroot}%{perl_vendorarch}
install -m 0644 GemHit.pm %{buildroot}%{perl_vendorarch}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{perl_vendorarch}/*


%changelog
* Tue Jul 10 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 20100419-1
- initial version


