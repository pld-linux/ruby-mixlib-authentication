#
# Conditional build:
%bcond_with	tests		# build without tests

%define		pkgname	mixlib-authentication
Summary:	Simple per-request authentication
Name:		ruby-%{pkgname}
Version:	2.1.1
Release:	1
License:	Apache v2.0
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	b9fae61aaac84f71aad68791c454ac44
URL:		http://github.com/opscode/mixlib-authentication
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-rake < 11
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
%setup -q

%build
%__gem_helper spec-dump %{pkgname}.gemspec

%check
%if %{with tests}
# need RSpec2
rspec -Ilib spec/mixlib/authentication/
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
%doc README.md NOTICE
%{ruby_vendorlibdir}/mixlib/authentication.rb
%{ruby_vendorlibdir}/mixlib/authentication
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

# FIXME, who owns the dir?
%dir %{ruby_vendorlibdir}/mixlib

%if 0
%files doc
%defattr(644,root,root,755)
%endif
