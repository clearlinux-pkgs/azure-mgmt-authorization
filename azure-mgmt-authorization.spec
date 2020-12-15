#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-mgmt-authorization
Version  : 0.60.0
Release  : 8
URL      : https://files.pythonhosted.org/packages/d5/42/cb6dc4b14c39c16ea7319c12e63cfb6b67af8d5b1c6ab1ee5a6bdc2ecd8d/azure-mgmt-authorization-0.60.0.zip
Source0  : https://files.pythonhosted.org/packages/d5/42/cb6dc4b14c39c16ea7319c12e63cfb6b67af8d5b1c6ab1ee5a6bdc2ecd8d/azure-mgmt-authorization-0.60.0.zip
Summary  : Microsoft Azure Authorization Management Client Library for Python
Group    : Development/Tools
License  : MIT
Requires: azure-mgmt-authorization-python = %{version}-%{release}
Requires: azure-mgmt-authorization-python3 = %{version}-%{release}
Requires: azure-common
Requires: msrest
Requires: msrestazure
BuildRequires : azure-common
BuildRequires : buildreq-distutils3
BuildRequires : msrest
BuildRequires : msrestazure

%description
==============================
        
        This is the Microsoft Azure Authorization Management Client Library.
        
        Azure Resource Manager (ARM) is the next generation of management APIs that
        replace the old Azure Service Management (ASM).
        
        This package has been tested with Python 2.7, 3.4, 3.5, 3.6 and 3.7.
        
        For the older Azure Service Management (ASM) libraries, see

%package python
Summary: python components for the azure-mgmt-authorization package.
Group: Default
Requires: azure-mgmt-authorization-python3 = %{version}-%{release}

%description python
python components for the azure-mgmt-authorization package.


%package python3
Summary: python3 components for the azure-mgmt-authorization package.
Group: Default
Requires: python3-core
Provides: pypi(azure_mgmt_authorization)
Requires: pypi(azure_common)
Requires: pypi(msrest)
Requires: pypi(msrestazure)

%description python3
python3 components for the azure-mgmt-authorization package.


%prep
%setup -q -n azure-mgmt-authorization-0.60.0
cd %{_builddir}/azure-mgmt-authorization-0.60.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588788347
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/lib/python3.9/site-packages/azure/mgmt/__init__.py
rm -f %{buildroot}/usr/lib/python3.9/site-packages/azure/mgmt/__pycache__/__init__.cpython-38.pyc

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
