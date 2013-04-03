%define		pkgname	mixlib-authentication
Summary:	Simple per-request authentication
Name:		ruby-%{pkgname}
Version:	1.3.0
Release:	1
License:	Apache v2.0
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	c2e40b5bf1d72d03ea91991c37c2a65a
URL:		http://github.com/opscode/mixlib-authentication
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
Requires:	ruby-mixlib-log
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
%check
%if %{with tests}
# need RSpec2
rspec -Ilib spec/mixlib/authentication/
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rdoc NOTICE
%{ruby_vendorlibdir}/mixlib/authentication.rb
%{ruby_vendorlibdir}/mixlib/authentication

# FIXME, who owns the dir?
%dir %{ruby_vendorlibdir}/mixlib

%if 0
%files doc
%defattr(644,root,root,755)
%endif
