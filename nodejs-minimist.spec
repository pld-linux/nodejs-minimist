#
# Conditional build:
%bcond_with	tests		# build with tests

%define		pkg	minimist
Summary:	Parse argument options in Node.js
Name:		nodejs-%{pkg}
Version:	0.0.8
Release:	0.1
License:	MIT
Group:		Development/Libraries
Source0:	https://registry.npmjs.org/minimist/-/minimist-%{version}.tgz
# Source0-md5:	2cf431b6650eef21fbace17b133be31e
URL:		https://github.com/substack/minimist
%if %{with tests}
BuildRequires:	nodejs-tap
BuildRequires:	nodejs-tape
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parse argument options in Node.js

This module is the guts of nodejs-optimist's argument parser without
all the fanciful decoration.

%prep
%setup -qc
mv package/* .

%build
%if %{with tests}
tap test/*.js
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr package.json index.js $RPM_BUILD_ROOT%{nodejs_libdir}/minimist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.markdown LICENSE example
%{nodejs_libdir}/%{pkg}
