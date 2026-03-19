#
# Conditional build:
%bcond_with	tests		# build without tests

%define		pkgname	mixlib-authentication
Summary:	Simple per-request authentication
Name:		ruby-%{pkgname}
Version:	3.0.10
Release:	1
License:	Apache v2.0
Group:		Development/Languages
Source0:	https://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	2b6d753a64e6c13d75fc6e87727d27c9
URL:		http://github.com/opscode/mixlib-authentication
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-rake >= 10.4
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mixlib::Authentication provides a class-based header signing
authentication object.

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%__gem_helper spec

%check
%if %{with tests}
# need RSpec2
%{__ruby} -S rspec -Ilib spec/mixlib/authentication/
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%{ruby_vendorlibdir}/mixlib/authentication.rb
%{ruby_vendorlibdir}/mixlib/authentication
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

# FIXME, who owns the dir?
%dir %{ruby_vendorlibdir}/mixlib

%if 0
%files doc
%defattr(644,root,root,755)
%endif
