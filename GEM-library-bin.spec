%global 	debug_package %{nil}
Name:		GEM-library-bin
Version:	20130406
Release:	1%{?dist}
Summary:	"Next-generation" tool for handling sequence data using state-of-the-art algorithms and data structures

Group:		Applications/Engineering
License:	Closed source
URL:		http://algorithms.cnag.cat/wiki/The_GEM_library
Source0:	http://sourceforge.net/projects/gemlibrary/files/gem-library/Binary%20pre-release%203/GEM-binaries-Linux-x86_64-core_i3-20130406-045632.tbz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	x86_64

%description
Next-generation sequencing platforms (Illumina/Solexa, ABI/SOLiD, etc.) call for powerful and
very optimized tools to index/analyze huge genomes. The GEM library strives to be a true
"next-generation" tool for handling any kind of sequence data, offering state-of-the-art
algorithms and data structures specifically tailored to this demanding task. At the moment,
efficient indexing and searching algorithms based on the Burrows-Wheeler transform (BWT) have
been implemented. The library core is written in C for maximum speed, with concise interfaces
to higher-level programming languages like OCaml and Python. Many high-performance standalone
programs (mapper, split-mapper, etc.) are also provided along with the library; in general,
new algorithms and tools can be easily implemented on the top of it.

This is a binary-only package.

%prep
%setup q -n GEM-binaries-Linux-x86_64-core_i3-%{version}-045632

%build


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}

install -m 0755 bin/gem-mapper %{buildroot}%{_bindir}
install -m 0755 bin/splits-2-junctions %{buildroot}%{_bindir}
install -m 0755 bin/compute-transcriptome %{buildroot}%{_bindir}
install -m 0755 bin/gem-info %{buildroot}%{_bindir}
install -m 0755 bin/gem-2-gem %{buildroot}%{_bindir}
install -m 0755 bin/gem-2-wig %{buildroot}%{_bindir}
install -m 0755 bin/gtf-2-junctions %{buildroot}%{_bindir}
install -m 0755 bin/gem-indexer_fasta2meta+cont %{buildroot}%{_bindir}
install -m 0755 bin/gem-2-sam %{buildroot}%{_bindir}
install -m 0755 bin/gem-retriever %{buildroot}%{_bindir}
install -m 0755 bin/gem-rna-mapper %{buildroot}%{_bindir}
install -m 0755 bin/gem-mappability-retriever %{buildroot}%{_bindir}
install -m 0755 bin/gem-indexer_generate %{buildroot}%{_bindir}
install -m 0755 bin/gem-indexer %{buildroot}%{_bindir}
install -m 0755 bin/gem-mappability %{buildroot}%{_bindir}
install -m 0755 bin/transcriptome-2-genome %{buildroot}%{_bindir}
install -m 0755 bin/gem-indexer_bwt-dna %{buildroot}%{_bindir}
install -m 0755 bin/External/gemtools %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 man/gem-mappability.man %{buildroot}/%{_mandir}/man1/gem-mappability.1
install -m 0644 man/gem-2-gem.man %{buildroot}/%{_mandir}/man1/gem-2-gem.1
install -m 0644 man/gem-2-sam.man %{buildroot}/%{_mandir}/man1/gem-2-sam.1
install -m 0644 man/gem-indexer.man %{buildroot}/%{_mandir}/man1/gem-indexer.1
install -m 0644 man/gem-mapper.man %{buildroot}/%{_mandir}/man1/gem-mapper.1

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Wed Sep 18 2013 Peter Briggs <peter.briggs@manchester.ac.uk> - 20130406-1
- new upstream release

* Tue Jul 10 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 20100419-1
- initial version


