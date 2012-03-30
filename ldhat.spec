Name:		ldhat
Version:	2.2
Release:	1%{?dist}
Summary:	LDhat: analysis of recombination rates from population genetic data

Group:		Applications/Engineering
License:	Public Domain
URL:		http://ldhat.sourceforge.net/
Source0:	http://sourceforge.net/projects/ldhat/files/LDhat_v%{version}.tar.gz
Source1:	%{name}-README.Fedora

%description
LDhat is a package of programs written in the C language for the analysis of
recombination from population genetic data. The key feature of the package
is the estimation of population recombination rates using the composite
likelihood method of Hudson, adapted to finite-sites models (applicable to
diverse genomes such as those of some viruses and bacteria) and to estimate
variable recombination rates. The method accommodates both phased or haplotype
and unphased or genotype data, with arbitrary levels of missing data.


%prep
%setup -q -n LDhat_v%{version}

cp -p %{SOURCE1} .

%build
make


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
# Rename convert to avoid clash with ImageMagick convert,
# rename stat to avoid clash with coreutils stat,
# rename others for consistency
install -m 0755 complete %{buildroot}%{_bindir}/ldhat-complete
install -m 0755 convert %{buildroot}%{_bindir}/ldhat-convert
install -m 0755 fin %{buildroot}%{_bindir}/ldhat-fin
install -m 0755 interval %{buildroot}%{_bindir}/ldhat-interval
install -m 0755 lkgen %{buildroot}%{_bindir}/ldhat-lkgen
install -m 0755 pairwise %{buildroot}%{_bindir}/ldhat-pairwise
install -m 0755 rhomap %{buildroot}%{_bindir}/ldhat-rhomap
install -m 0755 stat %{buildroot}%{_bindir}/ldhat-stat


%files
%doc manual.pdf ldhat-README.Fedora
%{_bindir}/*


%changelog
* Fri Mar 30 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 2.0.2-1
- initial version

