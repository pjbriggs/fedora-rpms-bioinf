%define debug_package %{nil}

Name:		ViennaRNA
Version:	2.1.1
Release:	1%{?dist}
Summary:	ViennaRNA: prediction and comparison of RNA secondary structures

Group:		Applications/Engineering
License:	Non-commercial
URL:		http://www.tbi.univie.ac.at/~ronny/RNA/index.html
Source0:	http://www.tbi.univie.ac.at/~ronny/RNA/ViennaRNA-2.1.1.tar.gz
BuildRequires:	perl-ExtUtils-MakeMaker


%description

RNA secondary structure prediction through energy minimization is the most used
function in the package. We provide three kinds of dynamic programming
algorithms for structure prediction: the minimum free energy algorithm of (Zuker
& Stiegler 1981) which yields a single optimal structure, the partition function
algorithm of (McCaskill 1990) which calculates base pair probabilities in the
thermodynamic ensemble, and the suboptimal folding algorithm of (Wuchty et.al
1999) which generates all suboptimal structures within a given energy range of
the optimal energy. For secondary structure comparison, the package contains
several measures of distance (dissimilarities) using either string alignment or
tree-editing (Shapiro & Zhang 1990). Finally, we provide an algorithm to design
sequences with a predefined structure (inverse folding). 


%prep
%setup -q

%build

# Version that tries to install Perl modules
PERLPREFIX=%{buildroot}/usr ./configure --prefix=%{_prefix} --without-forester --with-cluster

# Make the Perl modules separately so we can specify the
# installation directory explicitly
cd Perl
perl Makefile.PL PREFIX=%{_prefix}
cd ..

# Make the rest of the packages (except RNAforester)
make

# Build RNAforester
cd RNAforester
./configure --prefix=%{_prefix}
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

# Remove the share/info/dir file
rm -rf %{buildroot}/%{_infodir}/dir

# RNAforester makefile doesn't seem to support DESTDIR so do
# the install process manually here
cd RNAforester
install -m 0755 src/RNAforester %{buildroot}/%{_bindir}
install -m 0644 g2-0.70/libg2.a %{buildroot}/%{_prefix}/lib
install -m 0644 g2-0.70/include/*.h %{buildroot}/%{_includedir}
install -m 0644 man/RNAforester.1 %{buildroot}/%{_mandir}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_prefix}/lib/*
%{_includedir}/*
%{_datarootdir}/%{name}/*
%{_docdir}/%{name}/*
%{_mandir}/*
%{_infodir}/*
%{_libdir}/perl5/*

%changelog
* Thu May 23 2013 Peter Briggs <peter.briggs@manchester.ac.uk> - 2.1.1-1
- initial version





