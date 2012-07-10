%global 	debug_package %{nil}
Name:		GEM-library-bin
Version:	20100419
Release:	1%{?dist}
Summary:	"Next-generation" tool for handling sequence data using state-of-the-art algorithms and data structures

Group:		Applications/Engineering
License:	Closed source
URL:		http://sourceforge.net/apps/mediawiki/gemlibrary/
Source0:	http://sourceforge.net/projects/gemlibrary/files/gem-library/Binary%20pre-release%201/GEM-binaries-Linux-x86_64-20100419-003425.tbz2
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
%setup q -n GEM-binaries-Linux-x86_64-%{version}-003425

%build


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
install -m 0755 gem-mappability %{buildroot}%{_bindir}
install -m 0755 gem-mapper %{buildroot}%{_bindir}
install -m 0755 gem-mappability_fm_dna_32b %{buildroot}%{_bindir}
install -m 0755 gem-do-index_fm_general_32b %{buildroot}%{_bindir}
install -m 0755 gem-mapper_fm_dna_64b %{buildroot}%{_bindir}
install -m 0755 gem-do-index_fm_dna_32b %{buildroot}%{_bindir}
install -m 0755 gem-mapper_fm_general_64b %{buildroot}%{_bindir}
install -m 0755 gem-fasta2loc_cont_32b %{buildroot}%{_bindir}
install -m 0755 gem-mappability_fm_general_32b %{buildroot}%{_bindir}
install -m 0755 gem-do-index_fm_dna_64b %{buildroot}%{_bindir}
install -m 0755 gem-split-mapper_fm_general_64b %{buildroot}%{_bindir}
install -m 0755 gem-do-dna-bwt %{buildroot}%{_bindir}
install -m 0755 gem-fasta2loc_cont_64b %{buildroot}%{_bindir}
install -m 0755 gem-split-mapper %{buildroot}%{_bindir}
install -m 0755 gem-do-bwt_32b %{buildroot}%{_bindir}
install -m 0755 gem-split-mapper_fm_dna_32b %{buildroot}%{_bindir}
install -m 0755 gem-mapper_fm_general_32b %{buildroot}%{_bindir}
install -m 0755 gem-retriever %{buildroot}%{_bindir}
install -m 0755 gem-mappability_fm_general_64b %{buildroot}%{_bindir}
install -m 0755 gem-mappability-retriever %{buildroot}%{_bindir}
install -m 0755 gem-split-mapper_fm_general_32b %{buildroot}%{_bindir}
install -m 0755 gem-split-mapper_fm_dna_64b %{buildroot}%{_bindir}
install -m 0755 gem-mapper_fm_dna_32b %{buildroot}%{_bindir}
install -m 0755 gem-do-index_fm_general_64b %{buildroot}%{_bindir}
install -m 0755 gem-2-sam %{buildroot}%{_bindir}
install -m 0755 gem-mappability_fm_dna_64b %{buildroot}%{_bindir}
install -m 0755 gem-do-index %{buildroot}%{_bindir}
install -m 0755 gem-do-bwt_64b %{buildroot}%{_bindir}
install -m 0755 gem-dump-magic %{buildroot}%{_bindir}

%files
%defattr(-,root,root,-)
%{_bindir}/*


%changelog
* Tue Jul 10 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 20100419-1
- initial version


