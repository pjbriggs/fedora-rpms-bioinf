Name:		weblogo
Version:	2.8.2
Release:	3%{?dist}
Summary:	Generate sequence logos of amino acid or nucleic acid multiple sequence alignments

Group:		Applications/Engineering
License:	MIT
URL:		http://weblogo.berkeley.edu/
Source0:	http://weblogo.berkeley.edu/release/weblogo.2.8.2.tar.gz
Patch0:		weblogo-path.patch
Patch1:		weblogo-conf.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch

#BuildRequires:	
Requires:	ghostscript ImageMagick

%description
WebLogo is an application designed to make the generation of sequence logos as easy and
painless as possible. Sequence logos are a graphical representation of an amino acid or
nucleic acid multiple sequence alignment developed by Tom Schneider and Mike Stephens.
Each logo consists of stacks of symbols, one stack for each position in the sequence. The
overall height of the stack indicates the sequence conservation at that position, while
the height of symbols within the stack indicates the relative frequency of each amino or
nucleic acid at that position. In general, a sequence logo provides a richer and more
precise description of, for example, a binding site, than would a consensus sequence. 


%prep
%setup -q -n weblogo

# Patch seqlogo to locate template.eps in /usr/share/weblogo
%patch0 -p1

# Create conf file for locating gs and convert
%patch1

%build


%install
rm -rf %{buildroot}

# Put seqlogo in bin
mkdir -p %{buildroot}%{_bindir}
install -m 0775 %{_builddir}/%{name}/seqlogo %{buildroot}%{_bindir}

# Put perl modules in lib
mkdir -p %{buildroot}%{perl_vendorlib}
install -m 0644 %{_builddir}/%{name}/logo.pm %{buildroot}%{perl_vendorlib}
install -m 0644 %{_builddir}/%{name}/template.pm %{buildroot}%{perl_vendorlib}

# Put data files in share
mkdir -p %{buildroot}%{_datadir}/%{name}
install -m 0644 %{_builddir}/%{name}/logo.conf %{buildroot}%{_datadir}/%{name}
install -m 0644 %{_builddir}/%{name}/template.eps %{buildroot}%{_datadir}/%{name}

# Put documents in doc
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
install -m 0644 %{_builddir}/%{name}/README %{buildroot}%{_docdir}/%{name}-%{version}
install -m 0644 %{_builddir}/%{name}/LICENSE %{buildroot}%{_docdir}/%{name}-%{version}

%files
%{_bindir}/*
%{perl_vendorlib}/*
%{_datadir}/%{name}/*
%{_docdir}/%{name}-%{version}/*


%changelog
* Mon Jan 23 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 2.8.2-3
- Use "perl_vendorlib" rather than "perl_vendorarch" macro for installing Perl modules.

* Tue Jan 17 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 2.8.2-2
- added requirements for ghostscript and ImageMagick, plus custom conf file.

* Tue Jan 17 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 2.8.2-1
- initial version (command line version only)
