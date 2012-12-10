Name:		meme
Version:	4.8.1
Release:	4%{?dist}
Summary:	MEME suite: motif-based sequence analysis tools

Group:		Applications/Engineering
License:	Noncommercial
URL:		http://meme.nbcr.net/meme/
Source0:	%{name}_%{version}.tar.gz
Patch0:		meme_%{version}.patch
Patch1:		meme-Makefiles-DESTDIR.patch
Patch2:		meme-Makefiles-perl5.patch
Patch3:		meme-etc-files.patch

BuildRequires:	libxml2
BuildRequires:	libxml2-devel
BuildRequires:	libxslt
BuildRequires:	libxslt-devel
BuildRequires:	perl-XML-Simple
BuildRequires:	perl-SOAP-Lite
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-HTML-Template
BuildRequires:	perl-SOAP-WSDL
BuildRequires:	ImageMagick
BuildRequires:	ghostscript

Requires:	python
Requires:	libxml2
Requires:	libxslt
Requires:	perl-XML-Simple
Requires:	perl-SOAP-Lite
Requires:	perl-HTML-Parser
Requires:	perl-HTML-Template
Requires:	perl-SOAP-WSDL
Requires:	ImageMagick
Requires:	ghostscript

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
# Patches to use %{_prefix}/etc/meme rather than %{_prefix}/etc as default
# location for configuration and data files
%patch3 -p1


%build
./configure --prefix=%{_prefix} --with-url=http://meme.nbcr.net/meme/ --sysconfdir=%{_prefix}/etc/%{name} --libdir=%{_libdir}
make


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

# Rename "tree" to "meme-tree" to avoid name clash
mv %{buildroot}%{_bindir}/tree %{buildroot}%{_bindir}/meme-tree

# Relocate docs to appropriate place
mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}%{_prefix}/doc %{buildroot}%{_docdir}/%{name}-%{version}

# Remove database updating scripts - these are only used for web inteface
rm %{buildroot}%{_bindir}/update_db
rm %{buildroot}%{_bindir}/get_db_csv

# Clean up unused stuff
rmdir %{buildroot}%{_prefix}/db
rm -rf %{buildroot}%{_includedir}


%files
%defattr(-,root,root,-)
%{_prefix}/etc/%{name}/*
%{_bindir}/*
%{_docdir}/%{name}-%{version}/*
%{_libdir}/perl5/*


%changelog
* Mon Dec 10 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 4.8.1-4
- patch meme.csh.in and init.c to use correct default location for config and data files

* Fri Dec  7 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 4.8.1-3
- fix location of configuration files

* Thu Jul 26 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 4.8.1-2
- fix dependencies
- removed database updating Perl scripts

* Tue Jul 24 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 4.8.1-1
- rename "tree" to "meme-tree"
- patch to script Makefile.in's to use "%{_libdir}/perl5"
- patch to top-level Makefile.in to fix broken DESTDIR functionality
- initial version

