%define _topdir TOPDIR
Name:		fdpr_wrap
Version:	MAJOR.MINOR
Release:	RELEASE%{?dist}
Summary:	FDPR wrapper scripts for IBM Power Linux SDK
License:	Commercial, see COPYRIGHT file for details
URL:		http://www.haifa.il.ibm.com/projects/systems/cot/fdpr/fdpr_linux.html

Prefix:		/opt/ibm
Source0:	fdpr_wrap-%{version}.tar.gz

Requires:	fdprpro >= 5.6.1-4 python

%description
FDPR wrapper scripts are used as a glue to facilitate 
activation of FDPR from IBM Power Linux SDK

%prep
%autosetup

%install
make install DESTDIR=%{buildroot}

%files
%doc %{prefix}/fdprpro/share/doc/README-WRAPPER.txt
%license %{prefix}/fdprpro/share/doc/COPYRIGHT-WRAPPER
%license %{prefix}/fdprpro/share/doc/license_files-wrapper.zip
%prefix/fdprpro/bin/*

%changelog

