Name:		bismark
Version:	0.7.12
Release:	1%{?dist}
Summary:	Bismark: Bisulfite Mapper and Methylation Caller

Group:		Applications/Engineering
License:	GPLv2
URL:		http://www.bioinformatics.babraham.ac.uk/projects/bismark/
Source0:	http://www.bioinformatics.babraham.ac.uk/projects/bismark/bismark_v%{version}.tar.gz

BuildArch:	noarch


%description

Bismark is a set of tools for the time-efficient analysis of Bisulfite-Seq (BS-Seq)
data. Bismark performs alignments of bisulfite-treated reads to a reference genome
and cytosine methylation calls at the same time. Bismark is written in Perl and is
run from the command line. Bisulfite-treated reads are mapped using the short read
aligner Bowtie 1 (Langmead B, Trapnell C, Pop M, Salzberg SL. Ultrafast and
memory-efficient alignment of short DNA sequences to the human genome. Genome
Biol 10:R25), or alternatively Bowtie 2, and therefore it is a requirement that
Bowtie 1 (or Bowtie 2) are also installed on your machine.

%prep
%setup -q -n bismark_v%{version}

%build

%install
rm -rf %{buildroot}

# Executables
mkdir -p %{buildroot}%{_bindir}
install -m 0755 bedGraph2cytosine %{buildroot}%{_bindir}
install -m 0755 bismark %{buildroot}%{_bindir}
install -m 0755 bismark2bedGraph %{buildroot}%{_bindir}
install -m 0755 bismark_genome_preparation %{buildroot}%{_bindir}
install -m 0755 bismark_methylation_extractor %{buildroot}%{_bindir}

# Documentation
mkdir -p %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 0644 Bismark_User_Guide.pdf %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 0644 Bismark_User_Guide_v0.7.12.pdf %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 0644 license.txt %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 0644 RELEASE_NOTES.txt %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 0644 RRBS_Guide.pdf %{buildroot}/%{_docdir}/%{name}-%{version}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_docdir}/%{name}-%{version}/*


%changelog
* Wed May 29 2013 Peter Briggs <peter.briggs@manchester.ac.uk> - 0.7.12-1
- initial version

