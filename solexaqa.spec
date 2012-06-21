Name:		solexaqa
Version:	1.13
Release:	1%{?dist}
Summary:	SolexaQA: data quality statistics from Illumina sequencers

Group:		Applications/Productivity
License:	GPLv3
URL:		http://solexaqa.sourceforge.net/
Source0:	SolexaQA_v%{version}.pl.zip
Source1:	DynamicTrim_v%{version}.pl.zip
Source2:	LengthSort_v%{version}.pl.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
	
Requires:	matrix2png


%description
SolexaQA is a Perl-based software package that calculates quality statistics
and creates visual representations of data quality from FASTQ files generated
by Illumina second-generation sequencing technology (“Solexa”).

This package also contains DynamicTrim, which trims each sequence of a FASTQ
file individually to the longest contiguous read segment for which the quality
score at each base is greater than a user-supplied quality cutoff (or
alternately, the read segment returned by the BWA trimming algorithm), and
LengthSort, which sorts dynamically trimmed reads into subset files based on a
user-defined length cutoff. DynamicTrim and LengthSort should typically be
used in combination to remove poor quality bases and reads.


%prep
%setup -c
%setup -T -D -a 1
%setup -T -D -a 2


%build
# Nothing to do


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 0755 *.pl %{buildroot}%{_bindir}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
##%doc AUTHORS README NEWS COPYING ChangeLog
%{_bindir}/*.pl


%changelog
* Thu Jun 21 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 1.2.2-1
- initial version


