#
#	RPM Package Manager (RPM) spec file for fdpr_wrap
#
Summary: FDPR wrapper scripts for IBM Power Linux SDK
Name: fdpr_wrap
Version: w.x.y
Release: z
Prefix: /opt/ibm
License: Commercial, see COPYRIGHT file for details
Group: Application/Performance
URL: http://www.haifa.il.ibm.com/projects/systems/cot/fdpr/fdpr_linux.html
Vendor: IBM Corp
Packager: Genady Gurevich <genadyg@il.ibm.com>
BuildRoot: /tmp/var/fdprpro
Requires: fdprpro >= 5.6.1-4
%description
FDPR wrapper scripts are used as a glue to facilitate 
activation of FDPR from IBM Power Linux SDK

%files
%attr(644, bin, bin) /opt/ibm/fdprpro/share/doc/license_files-wrapper.zip
%attr(644, bin, bin) %doc /opt/ibm/fdprpro/share/doc/README-WRAPPER.txt
%attr(644, bin, bin) /opt/ibm/fdprpro/share/doc/COPYRIGHT-WRAPPER
%attr(755, bin, bin) /opt/ibm/fdprpro/bin/fdpr_dl.py
%attr(755, bin, bin) /opt/ibm/fdprpro/bin/fdpr_instr
%attr(755, bin, bin) /opt/ibm/fdprpro/bin/fdpr_instr_prof
%attr(755, bin, bin) /opt/ibm/fdprpro/bin/fdpr_instr_prof_opt
%attr(755, bin, bin) /opt/ibm/fdprpro/bin/fdpr_instr_prof_jour
%attr(755, bin, bin) /opt/ibm/fdprpro/bin/fdpr_prof
%attr(755, bin, bin) /opt/ibm/fdprpro/bin/fdpr_prof_opt
%attr(755, bin, bin) /opt/ibm/fdprpro/bin/fdpr_prof_jour
%attr(755, bin, bin) /opt/ibm/fdprpro/bin/fdpr_opt
%attr(755, bin, bin) /opt/ibm/fdprpro/bin/fdpr_jour

%post
echo $RPM_BUILD_DIR
find /opt/ibm/fdprpro/share/doc/ -name "COPYRIGHT" -delete

%postun
num_pkgs=$1
if [ $num_pkgs = 0 ]; then 
  # no package remain installed -- remove our files
  rm -fv /opt/ibm/fdprpro/bin/fdpr_* /opt/ibm/fdprpro/share/doc/README_fdpr_wrap.txt
fi
#EOF
