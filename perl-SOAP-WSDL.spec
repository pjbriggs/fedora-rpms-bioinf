Name:           perl-SOAP-WSDL
Version:        2.00.10
Release:        2%{?dist}
Summary:        SOAP with WSDL support
License:        Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/SOAP-WSDL/
Source0:        http://www.cpan.org/authors/id/M/MK/MKUTTER/SOAP-WSDL-%{version}.tar.gz
Patch0:		perl-SOAP-WSDL-HeaderFault.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 1:5.8.0
BuildRequires:  perl-Class-Std-Fast >= 0.0.5
BuildRequires:  perl-TimeDate
BuildRequires:  perl-Module-Build
BuildRequires:  perl-Template-Toolkit >= 2.18
BuildRequires:  perl-TermReadKey
BuildRequires:  perl-Test-Simple
BuildRequires:  perl-XML-Parser
Requires:       perl-Class-Std-Fast >= 0.0.5
Requires:       perl-TimeDate
Requires:       perl-Template-Toolkit >= 2.18
Requires:       perl-TermReadKey
Requires:       perl-XML-Parser
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
SOAP::WSDL provides easy access to Web Services with WSDL descriptions.

%prep
%setup -q -n SOAP-WSDL-%{version}
%patch0 -p1

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes HACKING LICENSE MIGRATING README TEST_COVERAGE TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_bindir}/wsdl2perl.pl
%{_mandir}/man1/wsdl2perl.pl.1.gz

%changelog
* Thu Jul 26 2012 Peter Briggs <peter.briggs@manchester.ac.uk> - 2.00.10-2
- added patch for lib/SOAP/WSDL/SOAP/HeaderFault.pm

* Thu Jul 26 2012 Peter Briggs <peter.briggs@manchester.ac.uk> 2.00.10-1
- Edits to generated BuildRequires and Requires directives
- Specfile autogenerated by cpanspec 1.78.
