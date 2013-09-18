%global 	debug_package %{nil}
Name:		gma-bin
Version:	0.1.3
Release:	1%{?dist}
Summary:	Measure how well NGS reads can be mapped to reference genomes

Group:		Applications/Engineering
License:	MIT
URL:		http://sourceforge.net/apps/mediawiki/gma-bio/index.php?title=Genomic_Dark_Matter:_The_limitations_of_short_read_mapping
Source0:	http://sourceforge.net/projects/gma-bio/files/gma-0.1.3.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	x86_64
Requires:	bwa samtools

%description
The Genome Mappability Analysis (GMA) suite is used for measuring how well NGS reads
can be mapped to reference genomes, especially for discovering variations.

This package bundles the pre-compiled binaries.

%prep
%setup -q -n gma-%{version}

%build


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
install -m 0755 bin/mapper %{buildroot}%{_bindir}
install -m 0755 bin/reducer %{buildroot}%{_bindir}

%files
%defattr(-,root,root,-)
%{_bindir}/*

%changelog
* Wed Sep 18 2013 Peter Briggs <peter.briggs@manchester.ac.uk> - 20130406-1
- initial version


