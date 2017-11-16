# 
# Copyright (C) 2017 IBM Corporation
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


%define _topdir TOPDIR
Name:		fdpr_wrap
Version:	MAJOR.MINOR
Release:	RELEASE%{?dist}
Summary:	FDPR wrapper scripts for the IBM SDK for Linux on Power (IDE and CLI)
License:	Apache 2.0
URL:		http://www.haifa.il.ibm.com/projects/systems/cot/fdpr/fdpr_linux.html

Prefix:		/opt/ibm
Source0:	fdpr_wrap-%{version}.tar.gz

Requires:	fdprpro >= 5.6.1-4 python coreutils which

%description
FDPR wrapper scripts are used as a glue to facilitate 
activation of FDPR from IBM SDK for Linux on Power (IDE and CLI)

%prep
%autosetup

%install
make install DESTDIR=%{buildroot}

%files
%doc %{prefix}/fdprpro/README.md
%license %{prefix}/fdprpro/LICENSE
%prefix/fdprpro/bin/*

%changelog
* Mon Nov 13 2017 Rafael Peria de Sene <rpsene@br.ibm.com>
- Update the file section and the SDK name.

