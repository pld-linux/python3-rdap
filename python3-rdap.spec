%bcond_with	tests	# unit tests (require network access and test fixtures)

%define		module	rdap
Summary:	Registration Data Access Protocol tools
Name:		python3-%{module}
Version:	1.7.0
Release:	2
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/rdap/
Source0:	https://files.pythonhosted.org/packages/source/r/rdap/%{module}-%{version}.tar.gz
# Source0-md5:	92a42bc76d12fca7300b331c4f8db6a7
URL:		https://github.com/20c/rdap
BuildRequires:	python3-build
BuildRequires:	python3-hatchling
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.10
%if %{with tests}
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-googlemaps >= 4
Requires:	python3-modules >= 1:3.10
Requires:	python3-munge
Requires:	python3-phonenumbers >= 8
Requires:	python3-pydantic >= 2
Requires:	python3-requests >= 2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RDAP is a Python library and CLI tool for querying Registration Data
Access Protocol servers. It provides access to registration data for
domains, IP addresses, and autonomous systems, replacing the older
WHOIS protocol with a standardized RESTful interface.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%{__mv} $RPM_BUILD_ROOT%{_bindir}/{rdap,pyrdap}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%attr(755,root,root) %{_bindir}/pyrdap
%{py3_sitescriptdir}/rdap
%{py3_sitescriptdir}/rdap-%{version}.dist-info
