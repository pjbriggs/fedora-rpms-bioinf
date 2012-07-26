Name:		meme
Version:	4.8.1
Release:	1%{?dist}
Summary:	MEME suite: motif-based sequence analysis tools

Group:		Applications/Engineering
License:	Noncommercial
URL:		http://meme.nbcr.net/meme/
Source0:	%{name}_%{version}.tar.gz
Patch0:		meme_%{version}.patch
Patch1:		meme-Makefiles-DESTDIR.patch
Patch2:		meme-Makefiles-perl5.patch

BuildRequires:	libxml
BuildRequires:	libxslt
Requires:	python
Requires:	perl-HTML-Parser
Requires:	perl-HTML-Template
Requires:	perl-SOAP-WSDL

Provides:	perl(MyInterfaces::RSATWebServices::RSATWSPortType)
Provides:	perl(prior_utils.pl)
Provides:	perl(mhmm_globals)


%description

The MEME Suite allows you to:

* discover motifs using MEME, DREME (DNA only) or GLAM2 on groups of related DNA or
  protein sequences,
* search sequence databases with motifs using MAST, FIMO, MCAST or GLAM2SCAN,
* compare a motif to all motifs in a database of motifs,
* associate motifs with Gene Ontology terms via their putative target genes, and
* analyse motif enrichment using SpaMo or CentriMo.


%prep
%setup -q -n %{name}_%{version}

# Official patches from the Meme website
%patch0 -p1
# Patches to fix DESTDIR targets in some Makefiles
%patch1 -p1
# Patches to use %{_libdir}/perl5 rather than %{_libdir}/perl
%patch2 -p1

%build
./configure --prefix=%{_prefix} --with-url=http://meme.nbcr.net/meme/ --sysconfdir=%{_sysconfdir}/%{name} --libdir=%{_libdir}
make


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

# Rename "tree" to "meme-tree" to avoid name clash
mv %{buildroot}%{_bindir}/tree %{buildroot}%{_bindir}/meme-tree

# Relocate docs to appropriate place
mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}%{_prefix}/doc %{buildroot}%{_docdir}/%{name}-%{version}

# Clean up unused stuff
rmdir %{buildroot}%{_prefix}/db
rm -rf %{buildroot}%{_includedir}


%files
%defattr(-,root,root,-)
%{_sysconfdir}/%{name}/*
%{_bindir}/*
%{_docdir}/%{name}-%{version}/*
%{_libdir}/perl5/*

%changelog
* Tue Mar 27 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 0.65-1
- rename "tree" to "meme-tree"
- patch to script Makefile.in's to use "%{_libdir}/perl5"
- patch to top-level Makefile.in to fix broken DESTDIR functionality
- initial version

