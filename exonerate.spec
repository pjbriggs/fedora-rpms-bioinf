Name:		exonerate
Version:	2.2.0
Release:	1%{?dist}
Summary:	exonerate is a generic tool for pairwise sequence comparison

Group:		Applications/Productivity
License:	GPLv3
URL:		http://www.ebi.ac.uk/~guy/exonerate/
Source0:	http://www.ebi.ac.uk/~guy/exonerate/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
	
BuildRequires:	glib2 glib2-devel
Requires:	glib2

%description
exonerate is a general tool for sequence comparison.

It uses the C4 dynamic programming library. It is designed to be both general and fast.
It can produce either gapped or ungapped alignments, according to a variety of different
alignment models. The C4 library allows sequence alignment using a reduced space full
dynamic programming implementation, but also allows automated generation of heuristics
from the alignment models, using bounded sparse dynamic programming, so that these
alignments may also be rapidly generated. Alignments generated using these heuristics
will represent a valid path through the alignment model, yet (unlike the exhaustive
alignments), the results are not guaranteed to be optimal. 


%prep
%setup -q


%build
./configure --prefix=%{_prefix}
make


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS README NEWS COPYING TODO ChangeLog
%{_bindir}/*
%{_datadir}/man/man1/*

%changelog
* Wed Jun 27 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 2.2.0-1
- initial version



