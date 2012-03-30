Name:		raxml
Version:	7.2.6
Release:	1%{?dist}
Summary:	Randomized Axelerated Maximum Likelihood (RAxML)

Group:		Applications/Engineering
License:	GPLv2
URL:		http://sco.h-its.org/exelixis/hands-On.html
Source0:	http://sco.h-its.org/exelixis/software/RAxML-%{version}.tar.bz2

##BuildRequires:	
##Requires:	

%description
RAxML (Randomized Axelerated Maximum Likelihood) is a program for sequential and
parallel Maximum Likelihood based inference of large phylogenetic trees.


%prep
%setup -q -n RAxML-%{version}


%build
# Build sequential version of RAxML (raxmlHPC)
make -f Makefile.gcc
# Build vectorized version (raxmlHPC-SSE3)
rm -f *.o
make -f Makefile.SSE3.gcc
# Build PTHREADS version (raxmlHPC-PTHREADS)
rm -f *.o
make -f Makefile.PTHREADS.gcc
# Build vectorized PTHREADS version (raxmlHPC-PTHREADS-SSE3)
rm -f *.o
make -f Makefile.SSE3.PTHREADS.gcc


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
install -m 0755 raxmlHPC %{buildroot}%{_bindir}
install -m 0755 raxmlHPC-SSE3 %{buildroot}%{_bindir}
install -m 0755 raxmlHPC-PTHREADS %{buildroot}%{_bindir}
install -m 0755 raxmlHPC-PTHREADS-SSE3 %{buildroot}%{_bindir}


%files
##%doc readme COPYING release
%{_bindir}/*



%changelog
* Thu Mar 29 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 7.2.6-1
- initial version

