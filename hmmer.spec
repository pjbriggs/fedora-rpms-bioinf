Name:           hmmer
Version:        3.0
Release:        1%{?dist}
Summary:        Biosequence analysis using hidden Markov models

Group:		Applications/Engineering
License:	GPLv3
URL:		http://hmmer.janelia.org/
Source0:	http://selab.janelia.org/software/%{name}3/%{version}/%{name}-%{version}.tar.gz


%description

HMMER is used for searching sequence databases for homologs of protein sequences,
and for making protein sequence alignments. It implements methods using probabilistic
models called profile hidden Markov models (profile HMMs).

%prep
%setup -q


%build
%configure
make


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

# Install man pages manually
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 documentation/man/*.man %{buildroot}%{_mandir}/man1

%files
%doc README LICENSE COPYRIGHT RELEASE-NOTES
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Wed Mar 28 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 3.0-1
- Initial version


