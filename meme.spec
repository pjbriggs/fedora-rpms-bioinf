Name:           meme
Version:        4.9.0
Release:        1%{?dist}
Summary:        Motif-based sequence analysis tools

License:        Noncommercial
URL:            http://meme.nbcr.net/meme/
Source0:        http://ebi.edu.au/ftp/software/MEME/4.9.0/meme_4.9.0_3.tar.gz

BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  perl-XML-Simple
BuildRequires:  perl-HTML-Parser
BuildRequires:  perl-HTML-Template
BuildRequires:  ImageMagick
BuildRequires:  ghostscript

Requires:       perl-XML-Simple
Requires:       perl-SOAP-Lite
Requires:       perl-HTML-Parser
Requires:       perl-HTML-Template
Requires:       perl-SOAP-WSDL
Requires:       ImageMagick
Requires:       ghostscript

Provides:       perl(prior_utils.pl)
Provides:       perl(mhmm_globals)
Provides:       perl(convert2html)


%description

The MEME Suite allows you to:

* discover motifs using MEME, DREME (DNA only) or GLAM2 on groups of related DNA
  or protein sequences,
* search sequence databases with motifs using MAST, FIMO, MCAST or GLAM2SCAN,
* compare a motif to all motifs in a database of motifs,
* associate motifs with Gene Ontology terms via their putative target genes, and
* analyze motif enrichment using SpaMo or CentriMo.


%prep
%setup -q -n %{name}_%{version}

# Fix Makefile.in
sed -i -e 's|mkdir -p \$(MEME_DB)|mkdir -p "$(DESTDIR)$(MEME_DB)"|' Makefile.in
sed -i -e 's|mkdir -p \$(MEME_LOGS)|mkdir -p "\$(DESTDIR)\$(MEME_LOGS)"|' Makefile.in
sed -i -e 's|chmod a+w \$(MEME_LOGS)|chmod a+w "\$(DESTDIR)\$(MEME_LOGS)"|' Makefile.in

# Fix doc Makefile.in
sed -i -e 's|MEME_DOC_DIR = \$(prefix)/doc|MEME_DOC_DIR = $(docdir)|' doc/Makefile.in

# Fix examples Makefile.in
sed -i -e 's|-C \$(other_exdir)|-C "\$(DESTDIR)\$(other_exdir)"|' doc/examples/Makefile.in

# Fix perl Makefile.in
sed -i -e "s|perlmoddir = \$(libdir)/perl|perlmoddir = \$(libdir)/perl5|" scripts/Makefile.in
sed -i -e "s|moduledir = \$(libdir)/perl|moduledir = \$(libdir)/perl5|" scripts/Makefile.in
sed -i -e "s|perlmoddir = \$(libdir)/perl|perlmoddir = \$(libdir)/perl5|" website/scripts/Makefile.in
sed -i -e "s|moduledir = \$(libdir)/perl|moduledir = \$(libdir)/perl5|" website/scripts/Makefile.in

# Fix the etc Makefile.in
sed -i -e 's|etcdir = \$(sysconfdir)|etcdir = \$(sysconfdir)/meme|' etc/Makefile.in
sed -i -e 's|set usage = \@MEMEDIR\@/etc/meme.doc|set usage = \@MEMEDIR\@/etc/meme/meme.doc|' scripts/meme.csh.in

sed -i -e 's|define ETC_DIR "$(sysconfdir)" |define ETC_DIR "$(sysconfdir)/meme" |' src/Makefile.in

%build

./configure --prefix=%{_prefix} \
            --with-url=http://meme.nbcr.net/meme/ \
            --sysconfdir=%{_sysconfdir} \
            --libdir=%{_libdir}

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

# Rename "tree" to "meme-tree" to avoid name clash
mv %{buildroot}%{_bindir}/tree %{buildroot}%{_bindir}/meme-tree

# Remove database updating scripts - these are only used for web inteface
rm %{buildroot}%{_bindir}/update_db
rm %{buildroot}%{_bindir}/get_db_csv

# Clean up unused stuff
rmdir %{buildroot}%{_prefix}/db
rm -rf %{buildroot}%{_includedir}

# Move the doc to a versioned directory
mkdir -p  %{buildroot}/%{_docdir}/%{name}-%{version}
cp -rf %{buildroot}/%{_docdir}/%{name}/* %{buildroot}/%{_docdir}/%{name}-%{version}/
# Remove previous doc folders
rm -rf %{buildroot}/%{_docdir}/%{name}/ %{buildroot}/%{_prefix}/doc

# Remove +x rights to the perl scripts
chmod -x %{buildroot}%{_libdir}/perl5/*

# Rename the application meme_<app> as they do not start with "meme", this to
# prevent conflicts such as the one with "purge".
for file in %{buildroot}/%{_bindir}/*
do
  filename=`basename $file`;
  if [[ $filename != meme* ]];
  then
    mv $file %{buildroot}/%{_bindir}/meme_$filename;
  fi
done

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_bindir}/*
%{_docdir}/%{name}-%{version}/*
%{_libdir}/perl5/*


%changelog
* Thu Jan 31 2013 Pierre-Yves Chibon <pingou@pingoured.fr> - 4.9.0-1
- Update to 4.9.0
- Move the configuration to /etc/
- Remove the patches and use sed hoping this gets stronger
- Rename all binary to meme_<bin> if they don't already start by meme

* Mon Dec 10 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 4.8.1-4
- patch meme.csh.in and init.c to use correct default location for config and data files

* Fri Dec  7 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 4.8.1-3
- fix location of configuration files

* Thu Jul 26 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 4.8.1-2
- fix dependencies
- removed database updating Perl scripts

* Tue Jul 24 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 4.8.1-1
- rename "tree" to "meme-tree"
- patch to script Makefile.in's to use "%%{_libdir}/perl5"
- patch to top-level Makefile.in to fix broken DESTDIR functionality
- initial version

