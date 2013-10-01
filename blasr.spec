Name:		blasr
# BLASR doesn't have an official version number so use the date stamp
# of the last commit
Version:	131001
Release:	1%{?dist}
Summary:	BLASR: long read aligner for PacBio data

Group:		Applications/Engineering
License:	BSD
URL:		https://github.com/PacificBiosciences/blasr
Source0:	%{name}-master.zip

BuildRequires:	hdf5
BuildRequires:	hdf5-devel
BuildRequires:	hdf5-static
BuildRequires:	glibc-static
BuildRequires:	zlib-static
%if 0%{?el6}
BuildRequires:	libstdc++-devel
%else
BuildRequires:	libstdc++-static
%endif


%description

BLASR (Basic Local Alignment with Successive Refinement) rapidly maps reads
to genomes by finding the highest scoring local alignment or set of local
alignments between the read and the genome. Optimized for PacBio's
extraordinarily long reads and taking advantage of rich quality values, BLASR
maps reads rapidly with high accuracy.

See BMC Bioinformatics 2012, 13:238 http://www.biomedcentral.com/1471-2105/13/238/abstract

%prep
%setup -q -n %{name}-master


%build
make HDF5INCLUDEDIR=%{_includedir} HDF5LIBDIR=%{_libdir}


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}

# Executables
install -m 0755 alignment/bin/blasr %{buildroot}%{_bindir}
install -m 0755 alignment/bin/buildQualityValueProfile %{buildroot}%{_bindir}
install -m 0755 alignment/bin/cmpPrintTupleCountTable %{buildroot}%{_bindir}
install -m 0755 alignment/bin/extendAlign %{buildroot}%{_bindir}
install -m 0755 alignment/bin/guidedalign %{buildroot}%{_bindir}
install -m 0755 alignment/bin/kbandMatcher %{buildroot}%{_bindir}
install -m 0755 alignment/bin/malign %{buildroot}%{_bindir}
install -m 0755 alignment/bin/pbmask %{buildroot}%{_bindir}
install -m 0755 alignment/bin/printReadWordCount %{buildroot}%{_bindir}
install -m 0755 alignment/bin/removeAdapters %{buildroot}%{_bindir}
install -m 0755 alignment/bin/sals %{buildroot}%{_bindir}
install -m 0755 alignment/bin/samatcher %{buildroot}%{_bindir}
install -m 0755 alignment/bin/samodify %{buildroot}%{_bindir}
install -m 0755 alignment/bin/saprinter %{buildroot}%{_bindir}
install -m 0755 alignment/bin/saquery %{buildroot}%{_bindir}
install -m 0755 alignment/bin/sawriter %{buildroot}%{_bindir}
install -m 0755 alignment/bin/sdpMatcher %{buildroot}%{_bindir}
install -m 0755 alignment/bin/swMatcher %{buildroot}%{_bindir}
install -m 0755 alignment/bin/tabulateAlignment %{buildroot}%{_bindir}
install -m 0755 alignment/bin/wordCounter %{buildroot}%{_bindir}

# Documents
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
mv LICENSE.txt README.txt %{buildroot}%{_docdir}/%{name}-%{version}


%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_docdir}/%{name}-%{version}/*


%changelog
* Tue Oct  1 2013 Peter Briggs <peter.briggs@manchester.ac.uk> - 131001-1
- new upstream version based on commit 78875212f1

* Thu Apr 25 2013 Peter Briggs <peter.briggs@manchester.ac.uk> - 130412-1
- initial version based on commit 0fe0a198c5


