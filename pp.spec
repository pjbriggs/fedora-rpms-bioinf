%define name pp
%define version 1.6.1
%define unmangled_version 1.6.1
%define release 1

Summary: Parallel and distributed programming for Python
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: BSD-like
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Vitalii Vanovschi <support@parallelpython.com>
Url: http://www.parallelpython.com

%description

Parallel Python module (PP) provides an easy and efficient way to create parallel-enabled applications for SMP computers and clusters. PP module features cross-platform portability and dynamic load balancing. Thus application written with PP will parallelize efficiently even on heterogeneous and multi-platform clusters (including clusters running other application with variable CPU loads). Visit http://www.parallelpython.com for further information.


%prep
%setup -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
